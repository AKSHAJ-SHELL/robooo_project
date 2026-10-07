# Final project: Does a phone-scanned sidewalk fool a 30 cm robot?

**One line.** Test whether the 3D "digital twins" that labs build from phone videos give the same answers as the real world when a small sidewalk robot, with its camera at 30 cm, is driven by a navigation AI model. Also test whether scanning at robot height instead of human height fixes it.

Chosen from about 60 ideas across 4 rounds of blind review. Best median score: 6.33/10. Prior work was checked against the three closest papers: Wanderland, the Kaedim reconstruction study and NavDP. Details: [round3/E1.v2.md](round3/E1.v2.md) (research plan), [system_design_E1.md](system_design_E1.md) (hardware and software), [round3/prior_work_check.md](round3/prior_work_check.md).

---

## The problem

- Testing robot navigation models in the real world is slow and hard to repeat. So labs now test them inside photoreal 3D copies of real places (Gaussian splats), built from someone walking around with a phone or scanner.
- Those scans are made at **human height (~1.1–1.4 m)**. Delivery and sidewalk robots see the world from **~30 cm**, a viewpoint the scan never saw.
- **Nobody has checked this against a real robot.** Wanderland (CVPR 2026) compares simulators only to each other, never to reality. The Kaedim study does check against a real robot, but for robot arms indoors, and it changes everything at once.

## Research questions

1. **H1 (main):** Is the gap between a model's decisions on real camera frames and on rendered frames bigger when the twin was scanned at **1.4 m** than at **0.3 m**?
2. **H2 (co-main):** Do the image-quality scores everyone reports (PSNR, SSIM, LPIPS, DINOv2 distance) predict how much the model's decisions change? (Wanderland's own numbers disagree with each other here, and its claim about DINO features was never tested.)
3. **Confirmation:** When the robot drives itself, do outcomes in the twin match outcomes on the real sidewalk (SRCC), compared with how well two real runs match each other?

Every outcome is publishable:
- **Height matters:** a cheap capture rule ("scan at robot height").
- **Height doesn't matter:** a measured bound that tells benchmark builders human-height scans are fine.
- **Both twins are far off:** independent real-robot evidence for Wanderland's argument.

## The key measurement

Drive the robot by hand along a route and record every camera frame and its exact position. Render the twin from those same positions. Give the **real** frame and the **rendered** frame to the same frozen navigation model and measure how far apart its predicted waypoints are (in metres). Compare that with the gap between **two real drives** of the same route, the noise floor. This gives thousands of paired frames per route without needing the model to drive well.

## Study design

- **Models:** CityWalker (NYU) and LogoNav/MBRA (Berkeley), both open source and run with their authors' own settings.
- **Twins per route:** T_H (phone at 1.4 m), T_R (phone at 0.3 m), T_RB (the robot's own camera frames). Scan order is alternated between routes.
- **Scale:** 16 routes at 8 sites (2 per site, 15–25 m each; book 9–10 sites as spares). Per route: 2 teleoperated drives + 2 models × 2 autonomous runs = **64 real episodes**, 32+ splats.
- **Stats (pre-registered on OSF by Dec 1):** site-level permutation test for H1 (simulated power 0.82 for a 22% effect); route-cluster bootstrap for H2; SRCC with a test-retest correction for the confirmation.
- **Extra:** move a refuse cart on 4 routes after scanning (placement sampled with the Scenic tool) to test stale twins.

## Hardware (~$790)

Hoverboard drive base (or reuse the bin robot's) · Jetson Orin Nano Super · wide-angle camera at exactly 0.30 m · LD19 2D lidar (map, scale and collisions only, never model input) · foam bumper + microswitches · physical e-stop · one 36 V battery with DC-DC converters · phone mount at 0.30 m · AprilTag stakes for checking distances.

## Open-source building blocks

| Part | Code |
|---|---|
| Motor firmware | EFeru/hoverboard-firmware-hack-FOC |
| Robot ROS 2 stack | linorobot2 (template), slam_toolbox, ldlidar_stl_ros2, image_pipeline, apriltag_ros, twist_mux, rosbag2 |
| Navigation models | ai4ce/CityWalker (via the fixed port in ai4ce/wanderland-lab), NHirose/Learning-to-Drive-Anywhere-with-MBRA |
| Waypoint controller | robodhruv/visualnav-transformer |
| 3D reconstruction | COLMAP / GLOMAP → nerfstudio-project/gsplat |
| Metrics | LPIPS, torchmetrics (PSNR/SSIM), facebookresearch/dinov2, evo |
| Obstacle placement | BerkeleyLearnVerify/Scenic |

What you write yourselves: a ~150-line base driver, model wrapper nodes, the render-and-compare scripts, a ~300-line replay loop, and the statistics notebook.

## Team roles

- **Hardware student:** chassis and 0.30 m mast, firmware and wiring, safety, phone rig, calibration, field sessions.
- **Software student:** October model check, ROS 2 bringup, model wrappers, the reconstruction and rendering pipeline, metrics, statistics, data release.

## Timeline

| When | What |
|---|---|
| **Oct 7–18** | **Free check:** film 3 sidewalk segments with a phone at 0.3 m and 1.4 m; run both models on Colab; confirm the 0.3 m footage reconstructs in COLMAP |
| Oct 19–25 | Email Fremont and Elkaim (UCSC) with the check's plot; draft the pre-registration |
| Oct 26–Nov 8 | Full pipeline working on phone data; **order parts by Nov 8** |
| Nov 9–Dec 6 | Build the robot; pre-register by Dec 1 |
| Dec 7–20 | Pilot: 2 sites, 4 routes |
| Dec 21–Feb 7 | Remaining sites (go/no-go Jan 15) |
| Feb 14 | Data freeze |
| **by Mar 1, 2027** | Submit to **IROS 2027** (or CASE 2027); fallback: an ICRA 2027 workshop |

## Labs to approach

- **Daniel Fremont (UCSC):** his work asks whether simulated tests transfer to the real world; you give him a Scenic program and a real-world counterpart dataset.
- **Gabriel Elkaim (UCSC Autonomous Systems Lab):** the robot runs his kind of stack (ROS 2, small ground robot); you can apply to SIP 2027.
- **Outside contacts, with pilot data in January:** NYU AI4CE (Wanderland, CityWalker) and VAIL-UCLA (Vid2Sim/S2E). You're testing their tools.

## Main risks and fallbacks

- **Models drive badly at 30 cm** (Wanderland shows ~21% outdoor success). The main result doesn't need them to drive well, and the October check catches this before you spend money.
- **0.3 m scans won't register.** This is tested in October; AprilTag stakes give a fallback alignment.
- **Rain or losing a site.** Sessions are short (75 min, dry mornings), and spare sites are booked.
- **Guaranteed minimum:** H1 + H2 on ≥ 8 routes is a complete workshop paper even without autonomous runs.

## First thing to do this week

Film 3 short sidewalk stretches with a phone, once held at 30 cm and once at 1.4 m. Run CityWalker and LogoNav on the footage in Colab, and check that their predicted paths make sense at 30 cm. No purchases are needed, and the plot is your opener for the lab emails.
