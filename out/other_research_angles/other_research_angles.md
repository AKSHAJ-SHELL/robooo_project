# Other research angles: build on an existing low-cost project and fix its limitation

Date: 2026-10-04. Inputs: [brief.md](brief.md), [gen_M.md](gen_M.md) (robot learning models), [gen_S.md](gen_S.md) (SLAM), [gen_H.md](gen_H.md) (custom hardware/PCBs), [reviews/](reviews/).

## Bottom line

- **No idea reached 7.5.** The best in this run is **S1 (multi-robot slam_toolbox over lossy Wi-Fi), median 6.00**. Scores are reported unadjusted.
- The best idea overall is still **E1.v2 from round 3** (phone-scanned sidewalk copies vs. the real sidewalk, median 6.33; see [../round3/final_round3.md](../round3/final_round3.md)).
- Process: 3 generators, one per area you named, started from 25+ candidates, killed the weak ones with evidence, and wrote up 9. The top 5 got 3 blind reviewers each: prior work, methods and feasibility (including whether the open-source reuse is real), and impact and lab fit.
- **The open-source reuse is real and big.** Reviewers confirmed in the code that most ideas need little from-scratch work (toolkit table below). The ideas lost points on novelty, not feasibility. Fixing another team's limitation often turned out to be already done, or the limitation turned out smaller than claimed.

## Scoreboard

| Idea | Area | Reviews | **Median** | Median N / F / I |
|---|---|---|---|---|
| **S1** Do decentralized slam_toolbox robots agree on the map under lossy Wi-Fi? | SLAM | 6.17, 6.00, 5.67 | **6.00** | 5.5 / 6 / 6 |
| **H1** Making open magnetic skins (eFlesh/AnySkin) work on steel with one-sided (Halbach) magnet layouts | Hardware/PCB | 6.33, 5.83, 5.50 | **5.83** | 6 / 6.5 / 5.5 |
| M1 Goal-pose sensing (RTK + heading) for GPS-conditioned navigation models (LogoNav) on an EarthRover | Learning | 6.17, 5.83, 5.67 | 5.83 | 5.5 / 6.5 / 5.5 |
| M2 How fragile are LeRobot ACT/SmolVLA policies to a routine SO-101 recalibration? | Learning | 6.17, 5.83, 5.67 | 5.83 | 5 / 7 / 5.5 |
| M3 Does the SO-101 leader arm's feel hurt demos? Magnetic-encoder leader PCB | Learning + PCB | 5.67, 5.67, 5.17 | 5.67 | 5.5 / 6 / 5 |

Not reviewed (self-scores): H2 kHz Hall readout board for slip sensing (6.0), H3 pump-pulsation suction-cup sensing (5.7), S2 lidar intensity against corridor drift (5.67), S3 omni-wheel lidar odometry for LeKiwi (5.67).

## What the reviewers found, idea by idea

**S1, multi-robot SLAM (6.00).** slam_toolbox's new decentralized mode (merged Oct 2025) lists lossy-Wi-Fi testing as future work, which is a real, maintainer-acknowledged gap with a large user base.
- Main problem: the node already uses reliable DDS delivery, which retransmits lost messages, and each message carries an absolute pose. So the stock system may barely suffer from the loss the study simulates.
- Fixes: replay what real Fast DDS and Zenoh actually deliver under `tc netem`, and add a best-effort arm; measure the no-loss noise floor first (processing order is asynchronous); use more environments rather than more seeds; report disagreement raw and after alignment; drop the C++ solver changes. Cite the Kimera-Multi datasets paper and arXiv 2508.11366 on DDS over lossy Wi-Fi.
- If the honest answer is "reliable DDS already handles it, and here is where it stops", that is still a useful result for every ROS 2 multi-robot user.

**H1, magnetic skins on steel (5.83).** The physics checks out: a reviewer's own magnet simulation found a correctly oriented Halbach layout cuts the steel "phantom" signal about 30x versus eFlesh's aligned magnets.
- Main problems: the gain over eFlesh's own alternating layout is only about 1.5–5x. The strong side as drawn would saturate the MLX90393 chips (70–200 mT against a ~50 mT linear range). Hand-placing ~64 tiny magnets is risky. One print per variant can't separate layout from print-to-print variation.
- Fixes: flip or space the layout to stay in the chip's range; compare against the alternating layout as the real baseline; make 3+ prints per variant; cite XELA uSkin's 2026 ferromagnetic compensation and Halbach use in position encoders.
- The best fit for your hardware student. The released Gerbers, BOM and pick-and-place files go straight to JLC assembly.

**M1, navigation-model goal sensing (5.83).** The code claims hold up: the released rover script never sets the goal inside 30 m.
- But a 2026 paper (IntentReact) already measured how a waypoint policy tolerates goal-direction bias, and the rover may already support RTK by default (~50 cm). The authors also used a different FrodoBots model.

**M2, recalibration fragility (5.83).** The easiest to do (feasibility 7–7.5), because LeRobot already contains the fix (`RelativeActionsProcessorStep`). That is also why novelty is low.

**M3, leader-arm feel (5.67).** The "detents" premise couldn't be confirmed. Both arms use 12-bit magnetic encoders on the output shaft, so the resolution contrast isn't real. An SO-100 leader with its gears removed is a cleaner control than a new PCB.

## Open-source toolkit: what you can reuse instead of building

Licenses were checked by the generators where marked; recheck before publishing.

| Area | Reuse | Link | What it saves |
|---|---|---|---|
| Robot base + ROS 2 | linorobot2 (Apache-2.0) | github.com/linorobot/linorobot2 | Firmware (micro-ROS), URDF, bringup, Nav2 config; supports LD06/LD19/STL-27L lidars |
| SLAM | slam_toolbox, incl. decentralized node on the `lyrical`/`ros2` branch (LGPL-2.1) | github.com/SteveMacenski/slam_toolbox | Whole SLAM back end |
| SLAM sim | slam_toolbox multi-robot demo | github.com/acachathuranga/slam_toolbox_multi_robot_demo | Gazebo multi-TurtleBot3 launch on day 1 |
| Lidar odometry | KISS-ICP, Kinematic-ICP (MIT) | github.com/PRBonn/kiss-icp, github.com/PRBonn/kinematic-icp | Lidar odometry baselines |
| Lidar driver | ldlidar_stl_ros2 | github.com/ldrobotSensorTeam/ldlidar_stl_ros2 | LD19 driver with intensities |
| Datasets | MIT Stata Center (2D lidar + odometry; per-frame ground truth for 17 bags) | projects.csail.mit.edu/stata | Evaluation before any robot exists |
| Evaluation | evo, rosbags | github.com/MichaelGrupp/evo, gitlab.com/ternaris/rosbags | Trajectory error; ROS 1 to ROS 2 bag conversion |
| Network tests | Linux `tc netem` | kernel | Controlled packet loss and latency |
| Arms + learning | LeRobot (Apache-2.0): ACT, Diffusion Policy, SmolVLA, record/train/eval | github.com/huggingface/lerobot | All learning code and teleop |
| Arm hardware | SO-100/SO-101 arm CAD + BOM (Apache-2.0) | github.com/TheRobotStudio/SO-ARM100 | Whole arm design |
| Mobile manipulator | LeKiwi | github.com/SIGRobotics-UIUC/LeKiwi | Omni-wheel base CAD and BOM |
| VLA weights | SmolVLA base | huggingface.co/lerobot/smolvla_base | Pretrained policy |
| Community data | LeRobot datasets on the HF Hub | huggingface.co/datasets?other=LeRobot | Data without robot time |
| Navigation models | LogoNav/MBRA weights + scripts (MIT), OmniVLA (MIT) | github.com/NHirose/Learning-to-Drive-Anywhere-with-MBRA, github.com/NHirose/OmniVLA | Pretrained outdoor navigation policies |
| Rover | EarthRover SDK and hardware repo (check license) | github.com/frodobots-org/earth-rovers-sdk, github.com/frodobots-org/earth-rover-mini | Robot I/O, firmware, schematics |
| GNSS | RTKLIB `str2str`; free California CRTN/SOPAC corrections | github.com/tomojitakasu/RTKLIB | cm-level reference without buying a base station |
| Tactile skins | eFlesh (MIT; lattice generator, firmware, slip code + data) | github.com/notvenky/eFlesh | Whole sensor body and slip baseline |
| Tactile skins | AnySkin library + firmware (MIT) | github.com/raunaqbhirangi/anyskin | Streaming, visualizer |
| Tactile PCB | ReSkin 5X magnetometer board, Gerbers + BOM (MIT) | github.com/raunaqbhirangi/reskin_sensor | A known-good board to order in week 1 |
| Magnet simulation | Magpylib | github.com/magpylib/magpylib | Simulate magnet layouts before building |
| Teleop reference | GELLO (MIT) | github.com/wuphilipp/gello_software | Passive leader-arm design pattern |
| Encoders | AS5600 library (MIT) | github.com/RobTillaart/AS5600 | Magnetic encoder driver |
| PCB | KiCad + JLCPCB assembly | kicad.org | Board design and fab (~1–2 weeks) |

## Recommendation

1. **Strongest overall: E1.v2 (round 3, 6.33).** It already reuses open code (CityWalker, LogoNav, Wanderland, Gaussian-splat tooling) and has the best lab fit.
2. **If you want something from this run:**
   - **S1 (6.00)** for a software-led project with a big user base. It's ROS 2 + slam_toolbox + linorobot2 + a public dataset, and the gap is acknowledged by the slam_toolbox maintainers. Reframe it around what real DDS/Zenoh delivers, so it can't be dismissed as "reliable delivery already fixes it". Lab fit: Carpin (UC Merced, multi-robot), Mehta (UCLA, multi-robot localization), Elkaim (UCSC, ROS 2 ground robots).
   - **H1 (5.83)** if the hardware student should lead with PCBs and sensor building. Fix the saturation and baseline problems first; simulate the layouts in Magpylib before ordering magnets.
3. **Safest fallback: M2.** Highest feasibility. Fine as a workshop paper or a first project to learn LeRobot, but low novelty.
