# System design: E1.v2, "Does a phone-scan twin see what a 30 cm robot sees?"

Date: 2026-10-04. This is the best-scoring idea across all runs (median 6.33/10; see [round3/final_round3.md](round3/final_round3.md)). The research plan is [round3/E1.v2.md](round3/E1.v2.md). This file is the engineering design: hardware, software, which open-source code goes where, and the data pipeline. It already includes the fixes from the last round of reviews (section 9).

All repository links below were checked to exist on 2026-10-04. Check each license before you publish code or data.

---

## 1. What the system has to do

1. **Capture.** Scan each sidewalk route twice with a phone, at 1.4 m (human height) and at 0.3 m (robot height).
2. **Drive.** Drive a small robot with its camera at 0.30 m over the same route: teleoperated passes, then autonomous runs where a navigation model drives.
3. **Build twins.** Turn each phone scan into a Gaussian-splat 3D model in the same metric coordinate frame as the robot.
4. **Compare.** At every robot pose, render the twin's view, feed both the real frame and the rendered frame to the same navigation model, and measure how far the model's predicted waypoints differ (D). Also compute image-quality scores (PSNR, SSIM, LPIPS, DINOv2 distance).
5. **Replay.** Replay each real autonomous run inside the twins and compare the outcomes (SRCC).
6. **Analyze** with the pre-registered statistics.

Two halves: an **onboard system** on the robot (record and drive), and an **offline pipeline** on a laptop plus free Colab/Kaggle (reconstruct, render, evaluate).

---

## 2. Architecture

```
                         ┌────────────────────────── ROBOT (onboard) ──────────────────────────┐
  Phone video ──┐        │                                                                      │
  (1.4 m, 0.3 m)│        │  Wide-angle camera ──► camera driver ─┐                              │
                │        │  LD19 2D lidar ──────► ldlidar driver ─┼─► slam_toolbox (map + pose) │
                │        │  Hoverboard (FOC fw) ◄─► base driver ──┘        │                     │
                │        │      ▲ cmd_vel   │ wheel odometry               ▼                     │
                │        │      │           └──────────────► goal converter ──► policy node    │
                │        │  teleop (gamepad) / policy node ──► twist_mux ─► base driver         │
                │        │  Bumper + e-stop ─► safety stop                  (CityWalker/LogoNav) │
                │        │                    rosbag2 records everything                        │
                │        └──────────────────────────────┬───────────────────────────────────────┘
                │                                       │ bags (USB SSD)
                ▼                                       ▼
        ┌───────────────────────────── OFFLINE PIPELINE (laptop + Colab) ───────────────────────┐
        │ 1 extract frames ─► 2 COLMAP/GLOMAP joint model (phone + robot frames) ─► 3 Sim(3)   │
        │   to slam_toolbox frame (AprilTag check) ─► 4 gsplat: T_H, T_R, T_RB twins ─►        │
        │ 5 render at robot poses ─► 6 run policies on real + rendered ─► 7 D + image metrics  │
        │ ─► 8 closed-loop twin replay (render→policy→unicycle, lidar map for collisions)      │
        │ ─► 9 statistics (site permutation, SRCC, bootstrap) ─► figures + release package     │
        └───────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Hardware

### 3.1 Bill of materials (≈ $790)

| # | Part | Choice | Est. cost | Why |
|---|---|---|---|---|
| 1 | Drive base | Used/new hoverboard with an STM32F103 or GD32F103 mainboard (check the chip before buying; the firmware supports only these) | ~$139 (reuse the bin-robot base if built) | Two hub motors, hall sensors and a 36 V pack in one cheap unit |
| 2 | Compute | NVIDIA Jetson Orin Nano Super dev kit (8 GB) | ~$249 | Runs CityWalker (DINOv2-B, 1 Hz) and LogoNav onboard; a Pi 5 is too slow for DINOv2-B |
| 3 | Storage | 256 GB NVMe or USB SSD | ~$30 | Bags: ~1–2 GB per route session |
| 4 | Camera | Global-shutter or fast rolling-shutter USB/CSI wide-angle camera, ~120° FOV, 30 fps (e.g. an IMX-series CSI module), plus a spare | ~$45 | Policy input; must be calibrated. Lock exposure and white balance |
| 5 | 2D lidar | LD19-class DToF lidar (or STL-27L) | ~$99 | Map, metric scale and collision geometry only. Never a policy input |
| 6 | Base interface | USB-to-UART adapter (3.3 V) to the hoverboard's sensor-board cable | ~$8 | Jetson talks to the FOC firmware directly |
| 7 | Safety MCU (optional) | ESP32 dev board | ~$10 | Bumper, hardware e-stop relay, battery voltage. Can be skipped by using Jetson GPIO |
| 8 | Bumper | Foam strip + 3–4 microswitches | ~$25 | Collision ground truth + stop |
| 9 | E-stop | Mushroom e-stop switch in series with the motor supply, plus a wireless kill (gamepad deadman) | ~$15 | Safety |
| 10 | Power | Hoverboard 36 V pack → 36 V-to-12 V DC-DC (≥ 5 A) for the Jetson, 5 V buck for the lidar | ~$45 | Single battery for everything |
| 11 | Frame | Aluminum extrusion or plywood deck, caster, camera mast at exactly 0.30 m lens height, lidar mount | ~$80 | Mechanical student |
| 12 | Gamepad | Any USB/Bluetooth gamepad | ~$20 | Teleop + deadman |
| 13 | Phone capture rig | Skateboard or wagon mount holding the phone lens at 0.30 m; a hand grip for 1.4 m | ~$25 | Uses a phone you already have |
| 14 | Ground truth | 4 laminated AprilTag boards on stakes per route, tape measure | ~$20 | Metric scale check (< 5 cm RMSE) |
| 15 | Obstacles | Cardboard boxes, pool noodles; borrowed refuse carts | ~$30 | Static scene objects |
| | **Total** | | **≈ $790** | About $210 left as reserve (spare camera, second lidar, a wet-weather cover) |

### 3.2 Mechanical design (hardware student)

- **Chassis.** Take the hoverboard's two hub motors and mainboard. Mount them on a flat deck with a rear caster: a differential drive about 50 × 40 cm.
- **Camera mast.** The lens center sits at **0.30 m ± 5 mm** above flat pavement, facing forward and level (0° pitch). This height is the experiment's main variable, so make the mount rigid and measure it.
- **Lidar.** Mount it on top of the mast or the front of the deck with a clear 360° view where possible. Record its exact offset from the camera (the extrinsic) with calipers, then refine it with the calibration step in 4.3.
- **Bumper.** A full-width foam bumper in front with microswitches behind it.
- **Electronics.** Jetson in a vented box; cable strain relief; e-stop reachable from behind.
- **Phone rig.** The phone's lens height at 0.30 m must match the robot camera. Use a phone clamp on a skateboard or wagon so the walk is smooth.

### 3.3 Electrical

```
36 V hoverboard pack ──► E-stop switch ──► hoverboard mainboard (FOC firmware) ── hub motors
        │                                        │ UART (3.3 V) via USB-UART
        ├──► DC-DC 36→12 V ──► Jetson Orin Nano ◄┘
        │                        │ USB: camera, lidar (via its UART adapter), SSD, gamepad dongle
        └──► buck 36→5 V ──► LD19 lidar
Jetson GPIO (or ESP32) ◄── bumper microswitches; ESP32 can also cut the motor relay
```

- **Power budget.** Jetson ~15–25 W, lidar ~1 W, motors ~50–150 W while driving. A stock 4.4 Ah pack (~160 Wh) gives well over an hour of testing per session.
- **Safety.** The physical e-stop cuts motor power and doesn't depend on software. The gamepad deadman stops the robot when released. Top speed is limited to 0.6 m/s in firmware.

---

## 4. Software: what runs where, and which open-source code it comes from

### 4.1 Onboard (ROS 2 Humble or Jazzy on the Jetson)

| Function | Open-source code | Where it's used | What you write |
|---|---|---|---|
| Motor control + wheel odometry | **hoverboard-firmware-hack-FOC** — github.com/EFeru/hoverboard-firmware-hack-FOC | Flashed onto the hoverboard mainboard (ST-Link, ~$5). Set USART control mode, speed/torque limits | Nothing in firmware beyond config |
| ROS 2 ↔ hoverboard | Protocol reference: **hoverboard-driver** — github.com/hoverboard-robotics/hoverboard-driver (ROS 1, ros_control) | Read it for the serial frame format | A small ROS 2 node (~150 lines Python): `cmd_vel` → serial speed commands; feedback → `odom` + TF |
| Lidar | **ldlidar_stl_ros2** — github.com/ldrobotSensorTeam/ldlidar_stl_ros2 | Publishes `/scan` | Launch file only |
| Mapping + pose | **slam_toolbox** — github.com/SteveMacenski/slam_toolbox | One 2D map per site; localization mode for the runs. Its poses are the metric "truth frame" | Config YAML |
| Robot description / bringup reference | **linorobot2** — github.com/linorobot/linorobot2 | Copy its URDF/launch layout and Nav2-style config patterns | Adapt to your base |
| Camera driver + calibration | **image_pipeline** (`camera_calibration`) — github.com/ros-perception/image_pipeline; plus `v4l2_camera` or a GStreamer/CSI driver | Intrinsics with a checkerboard; publish `/image_raw` | Launch + calibration file |
| AprilTag detection (QA) | **apriltag_ros** — github.com/christianrauch/apriltag_ros | Detect stake tags in robot frames for the scale check | Launch file |
| Policy 1 | **CityWalker** — github.com/ai4ce/CityWalker; use the fixed port in **wanderland-lab** — github.com/ai4ce/wanderland-lab (HF `ai4ce/citywalker`, goal row on, `target_horizon_m: 5.0`, per `configs/benchmark/policy/citywalker.yaml`) | Policy node: image + local goal → waypoints at 1 Hz | Wrapper node (load model, preprocess, publish waypoints) |
| Policy 2 | **LogoNav / MBRA** — github.com/NHirose/Learning-to-Drive-Anywhere-with-MBRA (weights on HF `NHirose/MBRA_project_models`; ROS script `deployment/LogoNav_ros.py`) | Policy node: image context + goal → waypoints | Wrapper reusing their ROS script logic (use the ROS version; the rover script has the <30 m goal bug) |
| Policy 3 (optional) | **S2E** — github.com/vail-ucla/S2E | Only if it passes the October gates | Wrapper |
| Waypoint → velocity | Shared controller pattern from **visualnav-transformer** — github.com/robodhruv/visualnav-transformer (`deployment/`) | PD/pure-pursuit from predicted waypoints to `cmd_vel` | Small node, identical in real and twin replay |
| Command arbitration | `twist_mux` (ROS 2 package) | Teleop overrides policy; deadman | Config |
| Recording | `rosbag2` (MCAP storage) | Records image, scan, odom, TF, waypoints, cmd_vel, bumper | Launch file with topic list |

**Goal handling.** Goals are points in the slam_toolbox map frame. A goal-converter node turns them into each policy's local goal from odometry. The twin replay uses exactly the same code, so real and twin conditions get identical goals.

### 4.2 Offline pipeline (laptop + free Colab/Kaggle T4)

| Step | Open-source code | What it does here | What you write |
|---|---|---|---|
| 1. Extract frames | `rosbags` (Python, gitlab.com/ternaris/rosbags) + OpenCV; `ffmpeg` for phone video | Robot frames with timestamps and poses; phone frames at ~2–3 fps | Extraction script |
| 2. Structure from motion | **COLMAP** — github.com/colmap/colmap, or **GLOMAP** — github.com/colmap/glomap (faster global SfM) | **One joint model per route** containing the T_H phone frames, T_R phone frames and robot frames, so everything shares one frame | Script that runs feature extraction → matching → mapping, with fixed robot-camera intrinsics |
| 3. Metric alignment | Umeyama Sim(3) (a few lines of NumPy) + **evo** — github.com/MichaelGrupp/evo for trajectory alignment and error | Align COLMAP's robot-camera centers to slam_toolbox poses via the camera extrinsic. Check against the AprilTag stakes; accept if RMSE < 5 cm | Alignment + QA script |
| 4. Train twins | **gsplat** — github.com/nerfstudio-project/gsplat (Apache-2.0); optionally via **nerfstudio** — github.com/nerfstudio-project/nerfstudio (`splatfacto`) | Train **T_H** on 1.4 m frames only, **T_R** on 0.3 m frames only, and **T_RB** on robot frames from teleop drive 1 only. Appearance embeddings off | Colab notebook. Avoid graphdeco-inria/gaussian-splatting for release (non-commercial license) |
| 5. Render at pose | gsplat rasterizer | Render each twin at every robot frame pose with the calibrated robot intrinsics; undistort real frames to match | Render script |
| 6. Run policies | Same wrappers as onboard (step 4.1), run in batch | Policy outputs on real frames and on each twin's renders | Batch runner |
| 7. Metrics | **LPIPS** — github.com/richzhang/PerceptualSimilarity; PSNR/SSIM from **torchmetrics** — github.com/Lightning-AI/torchmetrics; **DINOv2** — github.com/facebookresearch/dinov2 for feature cosine distance | Per-frame D (waypoint L2 distance, metres) and the four image metrics; real-vs-real floor between drive 1 and drive 2 | Metrics script |
| 8. Closed-loop twin replay | gsplat renderer + policy wrapper + a unicycle model (your velocity limits and measured latency) + the slam_toolbox occupancy map for collisions | Replay every real episode in T_H, T_R (and T_RB) from the same start; log trajectory, progress, clearance, collisions | Replay loop (~300 lines). Do **not** run wanderland-lab's simulator; it needs Isaac Sim and a 24 GB GPU |
| 9. Scene-change sampling | **Scenic** — github.com/BerkeleyLearnVerify/Scenic | A Scenic program samples where a refuse cart is moved (sidewalk edge, ≥ 0.9 m passable gap) | One `.scenic` file |
| 10. Statistics | NumPy/SciPy/statsmodels; the power code already in `round3/sim/e1v2_power.py` | Site-level permutation test (H1), mixed model, Spearman/route-cluster bootstrap (S1), SRCC in Kadian form with attenuation correction (C1) | Analysis notebook, written and run on pilot data before the freeze |
| 11. Release format | wanderland-lab's `episodes.json` schema | Starts/goals so others can rerun your routes | Export script |

### 4.3 Calibration (one time, then re-check weekly)

1. **Camera intrinsics:** `camera_calibration` with a printed checkerboard; save the YAML.
2. **Camera–lidar extrinsic:** measure with calipers, then refine by driving past a flat board or wall and aligning the lidar line with the board seen in the image. Alternatively, tune it so the COLMAP-vs-slam_toolbox alignment residual is smallest.
3. **Phone intrinsics:** let COLMAP estimate them per phone, or calibrate the phone once with the same checkerboard.
4. **Latency:** timestamp a flashing LED in the camera stream against the command to get camera-to-command delay, which the replay model needs.

---

## 5. Data layout

```
data/
  site_01/
    map/                     slam_toolbox map (.pgm/.yaml, serialized posegraph)
    route_01/
      phone_H/  phone_R/     raw phone videos (order counterbalanced, see 9.2)
      bags/                  drive_1/, drive_2/, ep_citywalker_r1/, ep_citywalker_r2/, ep_logonav_r1/, ep_logonav_r2/
      colmap/                joint sparse model
      align/                 sim3.json, apriltag_check.csv (RMSE)
      twins/                 T_H/, T_R/, T_RB/ (gsplat checkpoints)
      renders/               per-twin renders at every robot frame pose
      outputs/               policy outputs (real + each twin), metrics.parquet
      replay/                closed-loop twin replays
analysis/                    preregistered notebooks, figures
release/                     episodes.json, anonymized frames (faces blurred), code
```

---

## 6. Field session procedure (per route, about 75 min, dry pavement, early morning)

1. Place 4 AprilTag stakes; note the obstacle layout and photograph it.
2. **Phone scans**, order alternated between routes (H first on odd routes, R first on even): walk the robot path at 1.4 m and at 0.3 m, same phone, locked exposure, similar number of frames and path length.
3. Localize the robot in the site map (slam_toolbox localization mode).
4. **Teleop drive 1** (centerline) and **teleop drive 2** (±0.5 m weave), both recorded.
5. **Autonomous runs:** 2 policies × 2 repeats from the same start = 4 episodes. Spotter present; pause and annotate if a pedestrian approaches.
6. Pack up. Back up the bags to two drives the same day.

---

## 7. Who builds what

| Hardware/mechanical student | Software/perception student |
|---|---|
| Chassis, mast at 0.30 m, lidar and bumper mounts | October policy check on phone video (Colab) |
| Flash FOC firmware; wiring, power, e-stop | ROS 2 bringup: base driver node, lidar, camera, slam_toolbox, twist_mux, rosbag2 |
| Phone capture rig; AprilTag stakes | Policy wrapper nodes (CityWalker, LogoNav) + waypoint controller |
| Camera and extrinsic calibration fixtures | COLMAP → Sim(3) → gsplat → render pipeline on Colab |
| Runs field sessions (shared), maintains the robot | D/metrics code, twin replay loop, statistics notebook |
| Scenic program for cart placement (shared) | Pre-registration on OSF, data release |

---

## 8. Build order and milestones

| Dates | Milestone | Done when |
|---|---|---|
| Oct 5–18 | **October check, no purchases.** Film 3 home-street segments at 0.3 m and 1.4 m with a phone; run CityWalker (wanderland-lab port) and LogoNav open-loop on Colab | Both policies beat a "go straight" baseline at 0.3 m; the 0.3 m frames register in COLMAP together with the 1.4 m frames |
| Oct 19–25 | Choose 2 or 3 policies; email Fremont and Elkaim with the check's plot; draft the pre-registration | Email sent with a figure |
| Oct 26–Nov 8 | Offline pipeline end-to-end on phone data (0.3 m walk standing in for the robot). **Order parts by Nov 8** | Renders + D + image metrics computed on phone data |
| Nov 9–Dec 6 | Build the robot; ROS 2 bringup; calibration; teleop; recording; replay loop. **Pre-register on OSF by Dec 1** | A full teleop route recorded with aligned poses |
| Dec 7–20 | **Pilot: 2 sites, 4 routes** | Variances re-estimated; pilot rule applied |
| Dec 21–Jan 10 | Sites 3–5 | 10 routes total |
| **Jan 15** | Go/no-go | Open-loop D on ≥ 8 routes and alignment RMSE < 5 cm |
| Jan 16–Feb 7 | Sites 6–8; scene-change drives on 4 routes | 16 routes |
| Feb 8–14 | Re-runs; **data freeze Feb 14** | |
| Feb 15–26 | Analysis, paper, release | Submit to IROS 2027 or CASE 2027 by Mar 1; ICRA 2027 workshop as fallback |

---

## 9. Design changes from the final reviews (E1.v2 median 6.33)

The last three reviewers each raised different issues. These are built into the design above:

1. **Two main questions, not one.** "Human-height twins mislead more than robot-height twins" (H1) is close to predictable. So the image-metric question becomes **co-primary**: do PSNR/SSIM/LPIPS/DINOv2 scores track how much the policy is fooled? That answer can go either way.
2. **Counterbalanced capture order** (section 6, step 2) and matched frame count and path length between the 1.4 m and 0.3 m scans. Morning light changes fast, so always scanning H first would bias the result.
3. **A third twin, T_RB, trained on the robot's own camera frames** from teleop drive 1 and tested on drive 2's poses. It separates "phone vs robot camera" from "height", and costs no extra field time.
4. **Tighter real-vs-real floor.** Drives are pose-matched within 10 cm and 3°, but twins render at exact poses. To be fair, also render twins at the matched drive-1 poses when comparing to the floor.
5. **Site-count rule.** Losing 2 of 8 sites drops power from 0.82 to 0.55. Book 9–10 candidate sites in October so a lost site can be replaced, and widen the power grid in the pre-registration.
6. **Closed loop is conditional.** Twin replay is only reported in full if it works by Jan 15; otherwise the paper is open-loop plus real episodes.
7. **Distribution check for CityWalker.** It was trained on human-height video, so 0.3 m frames are out of distribution for it. The October check measures this directly, and the paper reports it.

## 10. Verify before you commit

- **Done (see [round3/prior_work_check.md](round3/prior_work_check.md)):** the Kaedim reconstruction-fidelity paper (very likely arXiv 2610.00731) and NavDP v3 were read in full. Neither covers capture height, policy-output divergence or a real-vs-real floor, so E1's claims stay open. Reframe E1 as the single-factor, low-viewpoint navigation counterpart to the Kaedim study, and do not cite NavDP for real-to-sim consistency (that sentence isn't in v3).
- **Done:** Wanderland (arXiv 2511.20620 v2) read in full. It has **no real-robot runs**; its evaluation-reliability claim is simulator-vs-simulator only, and it never varies capture height. E1's core gap is confirmed. Repeat a Scholar search for newer papers just before submission.
- Check licenses: CityWalker, LogoNav and S2E code and weights, gsplat (Apache-2.0), slam_toolbox (LGPL-2.1).
- Confirm the hoverboard's mainboard chip (STM32F103 / GD32F103) before buying.
- Confirm the Jetson runs CityWalker at ≥ 1 Hz (test on Colab first, then on the device).
- Borrow from the Kaedim paper: its agreement measures and paired-on-cell bootstrap for the closed-loop analysis, and a configuration gate that rejects any run whose camera height or settings drifted.
