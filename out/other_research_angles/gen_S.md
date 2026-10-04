# gen_S: SLAM, odometry and localization on low-cost open robots

Generator S. Date: 2026-10-04. Brief: `brief.md`.

**How I checked things.** I cloned and read the code (Oct 2026 heads): `SteveMacenski/slam_toolbox` (rolling head 33841d0, 2026-09-21, plus the `lyrical` branch), `ldrobotSensorTeam/ldlidar_stl_ros2`, `PRBonn/kinematic-icp` (d5b513e, 2025-07-31), `huggingface/lerobot` (8c920c4, 2026-10-03), `SIGRobotics-UIUC/LeKiwi`, `christopherdoer/rio`, `robo-friends/m-explore-ros2`, `linorobot/linorobot2` (`lyrical` branch).
- I read GitHub issue and PR pages with a page fetcher.
- arXiv, IEEE, Bonn PDFs, foxglove.dev and SMU pages were **blocked** by the sandbox. Any claim that rests only on a search-result snippet is marked **[snippet]**. Claims I verified in code are marked **[code]**, with file and line.
- I did not invent any citation. Where I recall a paper but could not open it, I mark it **[not opened]**.

---

## 0. Candidates considered and killed

| # | Candidate | Verdict | Why (evidence) |
|---|---|---|---|
| 1 | Motion deskew and driver timestamps for $100 spinning 2D lidars in slam_toolbox | **Killed** (N~4) | The limitation is real **[code]**. The LD19 ROS 2 driver stamps each scan with `node->now()` when the scan is *published*, so the stamp marks the end of the scan (`ldlidar_stl_ros2/src/demo.cpp` L155, L173). slam_toolbox never deskews (it has no deskew or time_increment code). But range-only deskew aimed at LD06 and RPLIDAR A1-class lidars already exists: arXiv 2303.07312, "Enhancing LiDAR performance: Robust de-skewing exclusively relying on range measurements" **[snippet]**. "SLAM with slow rotating range sensors" (HAL hal-01112428) is older still **[snippet]**. The fix is well known. |
| 2 | Glass and mirror detection from cheap-lidar intensity | **Killed** | PINMAP (DGIST, IEEE Access) already maps glass with low-cost 2D lidar **[snippet]**. Also Cartographer_glass (arXiv 2212.08633) and Tibebu et al., Sensors 2021 (PMC8038001) **[snippet]**. |
| 3 | 8x8 multizone ToF (VL53L5CX) SLAM on ground robots | **Killed** | "Same thing, cheaper". NanoSLAM (arXiv 2309.12008) already does 4xVL53L5CX SLAM on a 44 g drone **[snippet]**. |
| 4 | Single-chip mmWave Doppler odometry against wheel slip on lawn robots | **Killed** | Ground-speed radar is decades-old tractor practice. Recent work covers it: IWR6843AOP on ground robots (arXiv 2602.24192), Radarize, mmPhase (arXiv 2404.09691), and a TI-cited lawn-robot patent **[snippet]**. |
| 5 | Change-aware, information-preserving node retirement for slam_toolbox "true lifelong" mode | **Killed** | The limitation is real **[code]**. `src/experimental/slam_toolbox_lifelong.cpp` scores nodes by bounding-box IoU and overlap only, never by detected change. `removeFromSlamGraph` drops a node's edges, with the author's own comment: "LTS what do we do about the contraints that node had about it?Nothing?Transfer?" But the method space is done: Kurz, Holoch, Biber, "Geometry-based graph pruning for lifelong SLAM" (arXiv 2110.01286) **[snippet]**; Walcott-Bryant et al., DPG-SLAM, IROS 2012; Lázaro, Capobianco, Grisetti, "Efficient long-term mapping in dynamic environments", IROS 2018 **[snippet]**. |
| 6 | Let decentralized slam_toolbox robots start anywhere, aligned by UWB or by grid map merging | **Killed** (N~4.5) | UWB relative pose plus PCM for distributed SLAM already exists (arXiv 2207.03700, 2203.11004) **[snippet]**. `m-explore-ros2` map_merge already merges with `known_init_poses: false` **[code]**. Birk & Carpin (Proc. IEEE 2006) is canonical. |
| 7 | LeKiwi: does a drift-corrected base pose help imitation policies? | **Killed** | It now looks predictable. "Do you need proprioceptive states in visuomotor policies?" (arXiv 2509.18644) shows state-free policies generalize better **[snippet]**. Mobile UMI (arXiv 2605.20894) already realigns action chunks to the current base pose **[snippet]**. |
| 8 | F1TENTH particle-filter localization with a cheap 10 Hz lidar | **Killed** | Over budget (car plus compute). SynPF (arXiv 2401.07658) already covers robustness at racing speed **[snippet]**. |
| 9 | Rolling- vs global-shutter VIO on a Pi | **Killed** | The TUM rolling-shutter VI dataset (Schubert et al., IROS 2019) records both shutters at once **[not opened]**. |
| 10 | Conformal error bounds for AMCL | **Killed** | Conformal SE(2) localization bounds were already shown on a real MBot (arXiv 2512.10294) **[snippet]**. |
| 11 | Crosstalk between identical cheap DTOF lidars in small fleets | **Folded into S1** as a logged covariate | No documented limitation, a large risk of a null result, and D2SR (SMU) already handles mutual interference for scanning lidars **[snippet]**. |
| 12 | Lidar-detectable retroreflective markers on robots, for rendezvous merging | **Killed** | Relative localization from mutual lidar observations, and the correspondence problem it raises, are covered (Univ. of Moratuwa work; Zhou & Roumeliotis rendezvous) **[snippet]**. |
| 13 | Kinematic-ICP on skid-steer robots | **Merged into S3** | Online-calibrated LiDAR-IMU-wheel odometry for skid-steer robots exists (arXiv 2404.02515, 2407.08907) **[snippet]**. |

Survivors: **S1** (strongest), **S2**, **S3**.

---

## S1. Do decentralized slam_toolbox robots agree on the map? Cross-replica consistency under lossy Wi-Fi on ~$300 robots

### Base project and the specific limitation
- **Base:** slam_toolbox's new `decentralized_multirobot_slam_toolbox_node`. It came from PR #592 by acachathuranga, merged Oct 22, 2025, and ships on ROS 2 Lyrical and newer only. Links: https://github.com/SteveMacenski/slam_toolbox/pull/592 and `docs/decentralized_multi_robot_slam.md`. slam_toolbox is the default 2D SLAM in Nav2. Paper: Macenski & Jambrecic, JOSS 2021, https://joss.theoj.org/papers/10.21105/joss.02783.
- **Documented limitations:**
  - The PR's README lists as future work: *"Experiment on lossy WiFi networks. How would the nodes handle scan message losses between each other."* (PR #592 page, fetched.)
  - The PR author says that at larger fleet sizes *"you're likely to run into bandwidth problems before anything else"* (fetched).
  - The public demo is Gazebo with TurtleBot3 (`acachathuranga/slam_toolbox_multi_robot_demo`). The PR mentions physical Monsterborg tests but no published metrics.
- **What the code does [code]:**
  - Each robot keeps a full *replica* of everyone's pose graph. Every peer scan arrives as a `LocalizedLaserScan` carrying the producer's raw odometric pose (`publishLocalizedScan(..., range_scan->GetOdometricPose(), ...)`, L85-90). The receiver runs it through its own `Mapper::Process` (L144-156) on a per-peer sensor chain.
  - Inter-robot links come only from the receiver's own loop closures. Defaults: `loop_search_maximum_distance: 3.0`, `coarse_search_angle_offset: 0.349` (`config/mapper_params_online_multi_async.yaml`).
  - No message carries sequence numbers, retransmission, or any exchange of optimized poses. Each replica is optimized on its own, so N robots hold N different estimates of the same scan. The published covariance is identity times a scale factor.
- **Consequence nobody has measured:** robots that "share a global map" may disagree about where things are, and about where each other is. This gets worse as messages are lost and arrive out of order. Disagreement matters directly for multi-robot Nav2 (shared goals, deconfliction).

### Research question
How far do the N independently optimized replicas of a decentralized slam_toolbox fleet disagree about the same scans and the same map, how does that disagreement grow with packet loss and fleet size, and can a tiny owner-pose digest with gap-triggered retransmission bound it?

### Why the outcome is uncertain
- **Result A:** replicas agree within a few cm and about 0.5° even at 30% loss. Each replica matches the same physical walls, so they converge. That is publishable: the first quantified validation of the default ROS 2 multi-robot SLAM under real loss, with a safe operating envelope (loss rate, fleet size, CPU) for practitioners.
- **Result B:** replicas drift apart by decimeters, or close inconsistent loops (each replica's `TryCloseLoop` sees a different graph). Disagreement then rises steeply past some loss rate. Also publishable: a failure mode with a measured dose-response curve, plus a fix.
- I cannot derive which one happens. It depends on how often replica-specific loop closures differ, and on correlative-matcher basins under the odometric gaps that loss creates.

### The non-obvious insight
Consistency in a replicated-graph design can be measured **without any ground truth**: compare robot j's estimate of scan s (owned by robot k) against robot k's own estimate, in the shared frame. Disagreement is what breaks coordination, and it is cheap to log.

The fix exploits an asymmetry. The owner of a scan has the best information about its own trajectory (its full-rate odometry plus its own scans). So a ~16-byte-per-node digest of owner-optimized poses, sent at 1 Hz, can anchor all replicas. You do not need to ship graphs, factors or full maps. The digest also exposes sequence-number gaps, which trigger retransmission of only the lost scans.

### Open-source reuse

| Component | Link | License | What it saves |
|---|---|---|---|
| slam_toolbox decentralized node | github.com/SteveMacenski/slam_toolbox (`lyrical` branch has the node; verified) | LGPL-2.1 (verified) | The entire SLAM back end and the baseline system |
| Multi-robot sim demo | github.com/acachathuranga/slam_toolbox_multi_robot_demo | not checked | Gazebo multi-TB3 launch: day-1 pipeline |
| linorobot2 | github.com/linorobot/linorobot2 (`lyrical` branch; supports LD06/LD19/STL-27L, RPLIDAR) | Apache-2.0 (verified) | Robot firmware (micro-ROS), URDF, bringup, Nav2 config |
| LD19 driver | github.com/ldrobotSensorTeam/ldlidar_stl_ros2 | not checked | Lidar driver (fix its end-of-scan stamp, about 10 lines) |
| MIT Stata Center dataset | projects.csail.mit.edu/stata | academic | Multi-session PR2 2D lidar (UTM-30LX) plus odometry with ~2 cm floor-plan GT **[snippet]**. Sessions become "pseudo-robots" with real GT |
| Planetary-analogue C-SLAM dataset (arXiv 2601.21063) | via paper | unverified | Real peer-to-peer throughput and latency traces for trace-driven loss replay **[snippet]** (check that they are released) |
| evo | github.com/MichaelGrupp/evo | GPL-3 [not checked] | ATE/RPE |
| rosbags (Python) | gitlab.com/ternaris/rosbags | Apache-2.0 [not checked] | Converts ROS 1 Stata bags to ROS 2 without installing ROS 1 |
| Linux `tc netem` | kernel | GPL | Controlled loss, bursts and latency on real DDS or Zenoh traffic |

**The team builds:**
1. A lossy relay node (Gilbert–Elliott bursts, seeded) and a netem harness.
2. A replay orchestrator (N slam_toolbox containers on one laptop).
3. A disagreement logger (dumps every replica's pose graph by node ID, then computes metrics).
4. The fix: sequence numbers, a 1 Hz owner digest, gap-triggered re-request, and soft priors from digest poses on peer nodes. The soft priors are C++ in slam_toolbox. If that is too hard, the fallback is retransmission only, in Python.
5. Two real robots, plus a third "push-cart" agent (laptop, LD19, rf2o laser odometry).

### Closest prior work, and exactly what is new
1. **Swarm-SLAM** (Lajoie & Beltrame, RA-L 2024; arXiv 2301.06230 [snippet]). Sparse decentralized C-SLAM with budgeted inter-robot loop closures. It shares descriptors and factors, not replicated scan graphs, and does not measure replica disagreement.
2. **"Multi-robot decentralized collaborative SLAM in planetary analogue environments"** (arXiv 2601.21063, Jan 2026 [snippet]). Studies limited and intermittent comms with 3 robots on Swarm-SLAM outdoors. Closest in spirit. It covers a different architecture, 3D, and no replica-consistency metric. **We reuse its link traces.**
3. **DDF-SAM 2.0** (Cunningham, Indelman, Dellaert, ICRA 2013 [not opened]). Consistency (no double counting) in distributed smoothing. It is theory and system for factor-sharing; we do an empirical audit of a scan-sharing replica design.
4. **Chang, Chen, Mehta, "Resilient and consistent multirobot cooperative localization with covariance intersection"** (T-RO 2022, arXiv 2108.08789 [snippet]; UCLA LEMUR). Consistency under sparse or blocked comms. Evaluated on simulated data and the UTIAS benchmark, not on a deployed ROS 2 SLAM. Its CI-weighted fusion is a candidate variant for our digest prior.
5. **DOOR-SLAM** (Lajoie et al., RA-L 2020 [not opened]). Outlier-resilient distributed SLAM with PCM. About loop-closure outliers, not replica divergence.
6. **Zhivkov et al., "Measuring the effects of communication quality on multi-robot team performance"** (TAROS 2017 [snippet]). Nonlinear performance drop with packet loss for team tasks, not SLAM consistency.
7. **"Deep compressed communication… multi-robot 2D-lidar SLAM: an intelligent Huffman algorithm"** (Sensors 2024, PMC11124910 [snippet]). Compresses 2D maps (99% fewer bytes). Our digest is orthogonal: poses, not maps.
8. **Birk & Carpin**, "Merging occupancy grid maps from multiple robots" (Proc. IEEE 2006) [not opened]. Map-level merging. We study pose-graph replicas.

**New:** (i) the first measurement of cross-replica disagreement, and of its loss and fleet-size dose-response, for the replicated-graph 2D design that the most-used ROS 2 SLAM now ships. (ii) A GT-free consistency metric any fleet can log. (iii) A sub-1 kB/s owner digest with gap retransmission, measured against the original PR's own configuration. (iv) A test of the PR author's claim that bandwidth is the first bottleneck. My estimate: an LD19 scan is ~450 beams x 8 B ≈ 3.6 KB and is shared about 2 times per second (0.5 m / 0.5 rad thresholds). That is ~7 KB/s per robot, so replicated compute on a Pi or DDS overhead may bind first. This is untested.

### Experiment design (the baseline is the original team's own configuration)
- **Baseline:** stock `decentralized_multirobot_slam_toolbox_node` with the shipped `mapper_params_online_multi_async.yaml`, on Fast DDS (the Lyrical default **[snippet]**).
- **Variants:** V1 retransmission only; V2 digest priors only; V3 both. Secondary arm: rmw_zenoh vs Fast DDS, on real Wi-Fi only.
- **Phase 1, replay (bulk of data, free compute):**
  - Scenario sets: (a) Stata sessions split into 2/4/6 concurrent pseudo-robots, using GT start poses as the required shared frame. (b) The team's own building bags from 2 robots plus the cart.
  - Lidar realism: Stata UTM-30LX scans are also degraded to LD19-like (10 Hz, 12 m, ~0.8°, Gaussian noise fitted to our LD19 data).
  - Loss: {0, 10, 30, 50}% Gilbert–Elliott bursts, plus 1 recorded trace.
  - Each cell is seeded and paired: the same scenario and seed is run under stock and V1–V3.
- **Phase 2, live (validation):** 2 robots plus the cart in a school building, on real Wi-Fi.
  - Conditions: (near AP, far from AP, +20% netem) x stock/V3 x 5 runs = 30 runs of about 10 min.
  - Twelve floor checkpoints are surveyed with a laser distance meter (trilateration from walls). Robots pause on them.
  - Also logged: lidar-crosstalk events (spurious short returns when robots face each other), as a covariate.
- **Sample size:** the unit is a seeded replay run.
  - Primary contrast: stock vs V3 on log median disagreement.
  - Assumptions: SD of paired log-differences ≈ 0.5 (no pilot yet; replaced by the Nov pilot). Target effect: a 25% reduction (Δlog = 0.29). α = 0.05, power 0.8. Then n = ((1.96+0.84)·0.5/0.29)² ≈ 23 → **30 seeds per cell**.
  - Grid: 4 loss levels x 4 variants x 30 seeds x 3 scenario sets = 1,440 replays. That is ~5 min each at 2x real time, about 120 laptop-hours, spread over 6 weeks.
  - If the pilot SD is larger, drop to 2 variants (stock, V3) first.
  - Live runs (n = 15 per arm) only confirm the replay direction. Power ≈ 0.8 for a paired effect size dz ≈ 0.75.

### Measurements and analysis
- **Primary: cross-replica disagreement.** For every scan s with owner k and replica j ≠ k: D_xy = ‖p_j(s) − p_k(s)‖ and D_θ, logged over time. Report the median and 95th percentile at end of run, and the time-to-agreement.
- **Secondary:**
  - Occupancy-grid disagreement between replicas: the fraction of known cells that differ.
  - ATE/RPE per replica against Stata GT, and checkpoint error on real runs.
  - Missed or wrong inter-robot loop closures.
  - Bytes/s on the wire, Pi 5 CPU, RAM, and scan-to-map latency per replica as N grows. This tests the bandwidth claim.
- **Analysis:**
  - Mixed model: log D ~ loss x variant + fleet size + (1 | scenario/seed).
  - Dose-response curves with bootstrap 95% CIs.
  - Paired Wilcoxon per loss level, Holm-corrected.
- **Pre-registered decision:** "consistent" means D_95 < 10 cm and < 1°, the slam_toolbox map resolution being 5 cm.

### Build list (≤ $1,000; free compute)

| Item | Qty | Unit | Total | Status |
|---|---|---|---|---|
| Raspberry Pi 5 4GB | 2 | $110 | $220 | Price after the Apr-2026 increase **[snippet: gigazine/pcworld]**. Recheck; a Pi 5 2GB or a used Pi 4 cuts this |
| LD19 DTOF lidar | 3 | ~$100 | $300 | **Estimated**. DFRobot kit lists $141.25 at RobotShop **[snippet]**; LDROBOT-direct and Amazon are usually lower |
| linorobot2-style 2WD base: 2 encoder gear motors, driver, Pico/ESP32, 3S pack or 18650 pack and charger, 5 V/5 A buck, caster, 3D-printed deck | 2 | ~$95 | $190 | Estimated |
| microSD 64 GB | 2 | $12 | $24 | Estimated |
| Travel router (controlled Wi-Fi) | 1 | $40 | $40 | Estimated |
| Laser distance meter | 1 | $35 | $35 | Estimated |
| Push-cart agent (existing laptop and cart, USB-UART for LD19) | 1 | $15 | $15 | Estimated |
| Spares (fuses, cables, tape, floor markers) | | | $60 | Estimated |
| **Total** | | | **≈ $884** | All replay compute runs on the team laptop |

### Timeline (Oct 12, 2026 – Feb 26, 2027)
- **Wk 1 (Oct 12):** Install Lyrical (Docker on laptop). Run the multi-TB3 Gazebo demo. Order parts.
- **Wk 2 (Oct 19):** Download and convert 4 Stata sessions with rosbags. Run single-robot slam_toolbox and check against GT.
- **Wk 3 (Oct 26):** Split Stata into 2 pseudo-robots and replay through the decentralized node. Write the disagreement logger (graph dump by node ID).
- **Wk 4 (Nov 2):** Lossy relay plus seeding. **First pilot numbers (stock, 0/30% loss)** feed the power analysis. Email Carpin and LEMUR with the plot.
- **Wk 5 (Nov 9):** Parts arrive. HW student builds robot 1 (linorobot2 firmware, encoders, LD19 with fixed stamps).
- **Wk 6 (Nov 16):** Build robot 2 and the cart. SW student finishes the replay orchestrator and runs the Stata 4- and 6-robot sets.
- **Wk 7 (Nov 23):** Survey the school checkpoints. First live 2-robot plus cart mapping. Record bags.
- **Wk 8 (Nov 30):** Full replay grid for stock. Implement V1 (sequence numbers, retransmission).
- **Wk 9 (Dec 7):** Implement V2 (digest priors; fallback: digest-based re-seeding only).
- **Wk 10 (Dec 14):** Grid for V1–V3 on Stata. **Data checkpoint Dec 20:** stock dose-response plus a V1 comparison in hand.
- **Wk 11–12 (Dec 21 – Jan 3):** Break, with long unattended replays running.
- **Wk 13 (Jan 4):** Live runs, batch 1 (near/far AP).
- **Wk 14 (Jan 11):** **Go/no-go Jan 15:** is there a clear stock-vs-V3 signal or a clear "consistent" result? Either way the paper proceeds. If V2 is broken, ship V1 only.
- **Wk 15–16 (Jan 18 – 31):** Live batch 2 (netem, Zenoh arm). CPU and bandwidth scaling runs.
- **Wk 17 (Feb 1):** Analysis and figures.
- **Wk 18 (Feb 8):** **Data freeze Feb 14.** Draft.
- **Wk 19–20 (Feb 15 – 26):** Lab feedback, revise, submit. Open-source the PR and logger upstream.

### Roles
- **Hardware student:** builds 2 robots and the cart (wiring, encoders, power, 3D-printed lidar mounts at a common height). Surveys the checkpoints. Runs the live trials and the Wi-Fi placement plan. Builds a simple LED/Buzzer "pause at checkpoint" button tied to a ROS topic. Logs crosstalk geometry.
- **Software student:** Docker/Lyrical setup, Stata conversion, lossy relay, orchestrator, disagreement logger, V1 (Python), V2 (C++ with mentor help), statistics.

### Main risk and fallback
- **Risk:** the V2 C++ change in the Karto/Ceres graph is beyond the team.
  - **Fallback:** V1 (retransmission) plus "digest re-seeding", which only replaces the odometric guess for peer chains. Both are pure ROS 2 Python or relay-level. The core measurement (disagreement vs loss) needs no code changes to slam_toolbox at all.
- **Second risk:** Stata download size (full set 2.3 TB).
  - **Fallback:** take only the laser and odometry topics of a few sessions, or the derivative text logs. As a last resort, own bags only, with checkpoint GT.

### Best venue
IEEE CASE 2027 main track, or IROS 2027. Workshop fallback: an ICRA 2027 multi-robot/communication workshop. ROSCon 2027 talk for adoption.

### Lab appeal
- **Best fit: UC Merced Robotics Lab (Carpin).**
  - Their work: multi-robot systems and ROS 2 navigation, e.g., Sani, Sgorbissa, Carpin, ICRA 2024 (Nav2 for agriculture), and "Environmental map learning with multiple robots", ICRA 2025 (labs.md). Also the canonical multi-robot map merging (Birk & Carpin 2006).
  - What they gain: a measured envelope for the off-the-shelf ROS 2 decentralized mapper they could drop into multi-robot field work, plus a consistency logger.
- **Second: UCLA LEMUR (Mehta).** Chang, Chen, Mehta T-RO 2022 is about exactly this kind of consistency under sparse comms, and a CI-weighted digest would be a deployment of their idea on real ROS 2 robots.
- **Also:** SCU Kitts (multi-robot rovers), SJSU Wu (multi-robot sensing).

### Honest self-score
- **Novelty 6:** the replica-disagreement measurement and the digest fix for this widely used design are new. But distributed-SLAM consistency and comms-loss studies are an established area, and a reviewer may call it "a benchmark of one package plus a patch".
- **Feasibility 6.5:** replay on public data removes the hardware dependency, and the measurement needs no code changes. The risks are the Lyrical/Pi setup, the Stata conversion and the C++ fix.
- **Impact 6.5:** directly useful to the large Nav2/slam_toolbox community, and it answers the PR's stated future work. More likely a solid CASE paper or strong workshop paper than a widely cited main-track result.
- **Overall ≈ 6.33.**

---

## S2. Geometry, wheels or intensity? Using the free intensity channel of $100 DTOF lidars to break 2D corridor degeneracy in slam_toolbox

### Base project and the specific limitation
- **Base:** slam_toolbox (Karto correlative matcher) on low-cost Nav2 robots, e.g., linorobot2 with LD19.
- **Documented limitation:** long corridors are degenerate along their axis.
  - Issue #769, "SLAM Toolbox Fails in Symmetric Environments Like Corridors": ~1.8 m drift vs 3D-lidar SLAM, no maintainer fix (fetched). https://github.com/SteveMacenski/slam_toolbox/issues/769
  - Issue #631, "Robot Jumps in Multiple Narrow Corridor"; #134, "map overlapping in corridor".
  - The community's current remedy is PR #877 (Aug 2026), a **manual** runtime switch, "runtime_disable_scan_matching", meant "to prevent SLAM from causing false pose updates in ambiguous corridors" (fetched).
- **[code]:** slam_toolbox never uses `intensities`. They appear only in `src/laser_utils.cpp` L62-74, where they are copied when a scan is inverted. LD19 and STL-27L publish per-point intensity (`demo.cpp` fills `output.intensities`).
- **Second baseline, Kinematic-ICP** (PRBonn, ICRA 2025; 2D mode via `use_2d_lidar`, `online_node.cpp` L44-54). It handles degeneracy with adaptive wheel-odometry regularization. Its open issue #31 reports 2D timestamp-handling crashes (fetched).
  - Side finding to fix first: the LD19 driver stamps scans at the end of the revolution (`demo.cpp` L155/L173). `laser_geometry`'s per-point times in Kinematic-ICP's 2D mode are therefore shifted by one scan period.

### Research question
Does the 8-bit intensity return of a ~$100 DTOF 2D lidar carry enough repeatable along-corridor structure to cut along-axis drift beyond what wheel-odometry fallback already achieves? The fallback here means an automated version of PR #877, plus Kinematic-ICP.

### Why the outcome is uncertain
- **A:** wall intensity (door frames, kick plates, posters, extinguisher boxes, paint patches) forms a repeatable 1-D "barcode". Matching it cuts end-of-corridor along-axis error by ≥40% beyond wheel fallback, with zero new hardware.
- **B:** cheap-lidar intensity is too quantized, too range- and incidence-dependent, or too saturated at grazing angles to repeat across passes. Wheel fallback is the right answer, and that is quantified.
- Both outcomes give practitioners a clear decision. The answer depends on unknown radiometric behavior of $100 sensors, which no paper reports to my knowledge.

### The non-obvious insight
You do not need intensity SLAM. In a corridor, geometry already fixes heading and lateral offset; only one direction is unobservable. That direction can be read off the correlative matcher's response covariance (or the ICP Hessian). So intensity is needed only as a **1-D correlation along that eigenvector**, between the current wall-intensity profile and the map's. This is cheap enough for a Pi, and it is used only when degeneracy is detected.

### Open-source reuse

| Component | Link | License | Saves |
|---|---|---|---|
| slam_toolbox | github.com/SteveMacenski/slam_toolbox | LGPL-2.1 | Baseline SLAM; the team adds a degeneracy hook |
| Kinematic-ICP | github.com/PRBonn/kinematic-icp | MIT (verified) | Wheel-regularized lidar odometry baseline, 2D mode |
| linorobot2 | github.com/linorobot/linorobot2 | Apache-2.0 | Robot stack |
| ldlidar_stl_ros2 | github.com/ldrobotSensorTeam/ldlidar_stl_ros2 | not checked | Driver; publishes intensities |
| apriltag_ros | github.com/christianrauch/apriltag_ros [not checked] | BSD [not checked] | Floor-tag checkpoint GT |
| evo, rosbags | as in S1 | | Evaluation, bag handling |

**The team builds:**
1. An intensity calibration rig and a normalization model I(r, α, surface).
2. Degeneracy detection, turning PR #877 into an automatic switch.
3. A 1-D intensity correlator and its fusion as an along-axis pose correction.
4. A floor-tag checkpoint logger (down-facing Pi camera).

### Closest prior work, and what is new
1. **COIN-LIO** (Pfreundschuh et al., ICRA 2024) [not opened]. Intensity images from 3D lidar fix degeneracy in tunnels. 3D, high-end sensors.
2. **"An intensity-enhanced LiDAR SLAM for unstructured environments"** (2023) [snippet]. Adds intensity constraints only when degradation is detected; reports 55% better accuracy. Same trigger logic, but 3D.
3. **"When geometry is not enough: using reflector markers in lidar SLAM"** (arXiv 2211.03484) [snippet]. Uses retroreflectors added to the environment; we use natural surfaces.
4. **X-ICP** (Tuna et al., T-RO 2023) and **Zhang, Kaess, Singh, "On degeneracy of optimization-based state estimation problems"** (ICRA 2016) [not opened]. Degeneracy detection; we reuse the concept.
5. **Kinematic-ICP** (arXiv 2410.10277) [code read]. Wheel-prior answer to degeneracy; it is our strongest baseline.
6. **2DLIW-SLAM** (arXiv 2404.07644) [snippet]. 2D lidar-IMU-wheel fusion for degenerate scenes. Uses extra sensors, not intensity.
7. **Kashani et al., "A review of LIDAR radiometric processing"** (Sensors 2015) [not opened]. Intensity calibration theory, applied here to $100 DTOF units.
8. **Tibebu et al. 2021** (PMC8038001) [snippet]. 2D intensity for glass, not for localization.

**New:** a radiometric characterization of $100 DTOF 2D lidars (LD19, plus an STL-27L if the budget allows). The first test of natural-surface intensity as the along-corridor observation in 2D SLAM. A measured head-to-head against the wheel-odometry fallback the community is actually adopting (PR #877, Kinematic-ICP).

### Experiment design (baseline: stock slam_toolbox as configured by linorobot2)
- **Pilot (Oct, decides go/no-go by Nov 15):** drive one corridor 10 times. Compute the cross-pass correlation of the normalized wall-intensity profile. Proceed with the intensity arm only if the median r > 0.6. Otherwise pivot to a "wheels vs geometry" paper on the same data.
- **Main:** 5 corridors (school, library, community center) x 8 passes (4 per direction) x 2 speeds (0.2, 0.4 m/s) = 80 bags of ~40–70 m each.
- **Pipelines:** all run *offline on the same bags*, so the comparison is fully paired.
  - P0 stock slam_toolbox.
  - P1 P0 with automatic degeneracy switch (scan matching off along the degenerate axis).
  - P2 Kinematic-ICP (fixed stamps) feeding slam_toolbox odometry.
  - P3 P1 + intensity.
  - P4 P2 + intensity.
- **GT:** AprilTag floor tags every 5 m, with positions measured by laser distance meter. A down-facing camera timestamps each crossing, which gives along-axis truth at every tag.
- **Sample size:** the unit is a pass.
  - Assumptions: SD of paired differences in end-of-corridor along-axis error ≈ 0.3 m (a guess; replaced by the pilot). Target effect: 0.15 m. Then n ≈ (2.8·0.3/0.15)² ≈ 31 passes.
  - 80 passes leave margin for a corridor random effect. Weakness: 5 corridors limits corridor-level generalization.

### Measurements and analysis
- **Primary:** along-axis error at tags (cm) and corridor-length scale error (%).
- **Secondary:** lateral and heading error, loop-closure success, map-length error vs taped length, and Pi 5 CPU.
- **Calibration:** intensity vs range (0.5–8 m) x incidence (0–80°) x 8 surfaces, with the repeatability coefficient.
- **Analysis:** mixed model error ~ pipeline + speed + (1 | corridor/pass), and paired contrasts P3−P1 and P4−P2 with bootstrap CIs.

### Build list

| Item | Cost | Status |
|---|---|---|
| 1 linorobot2-style robot (Pi 5 4GB $110, LD19 ~$100, base ~$95, SD $12) | ~$317 | Pi price [snippet], rest estimated |
| STL-27L (second DTOF model) | ~$160 | Estimated, not verified |
| Pi Camera Module 3 (floor tags) | ~$25 | Estimated |
| Calibration rig: NEMA17 + driver, printed turntable, 8 surface samples | ~$45 | Estimated |
| Laser distance meter | ~$35 | Estimated |
| Tag printing, tape, spares | ~$40 | Estimated |
| **Total** | **≈ $622** | |

### Timeline
- **Wk 1–2 (Oct 12–25):** Order parts. SW student runs slam_toolbox and Kinematic-ICP on the Stata corridors (check whether those bags contain intensities; if not, use own data only).
- **Wk 3–4 (Oct 26 – Nov 8):** LD19 on a laptop cart: **intensity pilot** of 10 passes. Fix driver stamps.
- **Wk 5 (Nov 9):** Robot build. Calibration rig printed.
- **Wk 6 (Nov 16):** Go/no-go on intensity repeatability. Calibration sweeps.
- **Wk 7–9 (Nov 23 – Dec 13):** Collect 80 passes (3 sessions per week). Build the floor-tag logger.
- **Dec 20:** all bags plus P0–P2 results.
- **Wk 11–12:** Break. Implement the 1-D correlator.
- **Wk 13–15 (Jan 4–24):** P3/P4. Go/no-go Jan 15 on whether the intensity gain shows.
- **Wk 16–17:** Analysis.
- **Data freeze Feb 14. Submit Feb 26.**

### Roles
- **Hardware student:** robot, calibration turntable rig, surface samples, floor-tag camera mount, corridor surveys and data runs.
- **Software student:** driver stamp fix, degeneracy detector, correlator, pipeline batch runs, statistics.

### Main risk and fallback
- **Risk:** cheap-lidar intensity is not repeatable (result B).
  - **Fallback:** the paper becomes "an automated degeneracy switch vs Kinematic-ICP vs stock on cheap robots, with a radiometric characterization of $100 lidars". It is less novel but finishable on the same data.

### Best venue
IROS 2027 or CASE 2027. Fallback: IEEE Sensors Letters or an ICRA 2027 workshop.

### Lab appeal
- **Best fit: UCSC ASL (Elkaim).**
  - Their work: Pi + ROS 2 + Nav2 differential-drive robots (SIP 2026 CSE-11), the SIP 2025 "Graph-Based SLAM Simulation" project, and the lab's stated aim of cutting autonomy cost (labs.md).
  - What they gain: a zero-hardware fix for the corridor failures their robots will hit.
- **Second: UCLA LEMUR** (Direct LiDAR Odometry, Chen et al., RA-L 2022).

### Honest self-score
- **Novelty 5:** intensity-aided, degeneracy-triggered registration exists in 3D. The new parts are the 2D cheap-sensor setting and the head-to-head against the community fix.
- **Feasibility 7:** one robot, offline paired pipelines, and a pilot that decides early.
- **Impact 5:** useful to Nav2 users in buildings, but narrow, and result B is a modest paper.
- **Overall ≈ 5.67.**

---

## S3. Kinematic-ICP cannot correct sideways error: lidar odometry for $250 omni-wheel bases (LeKiwi)

### Base project and the specific limitation
- **Base 1: Kinematic-ICP** (Guadagnino, Mersch, Vizzo, …, Stachniss; ICRA 2025; arXiv 2410.10277), MIT license, https://github.com/PRBonn/kinematic-icp. The README requires "Planar Movement" and an existing wheel odometry.
- **[code]:** the ICP update has only **2 DOF**:
  - Forward displacement and yaw: `J.col(0) = R·UnitX`, yaw column (Registration.cpp L90-91).
  - The motion model is a unicycle arc (`motion_model` lambda, L156-163).
  - The odometry regularizer acts on forward translation only: `Omega = diag(beta, 0)` (L121), with an adaptive `beta = 1/mean residual` (L58).
  - The initial guess uses the full wheel-odometry delta (L151). So any **lateral** wheel-odometry error passes through uncorrected, because ICP has no lateral degree of freedom to fix it. For holonomic bases (omni or mecanum), and for skid-steer robots that slip sideways, the core assumption is violated.
- **Base 2: LeKiwi** (SIGRobotics-UIUC + Hugging Face LeRobot), Apache-2.0, https://github.com/SIGRobotics-UIUC/LeKiwi.
  - A three-omni-wheel base. The BOM lists base-only 12V at $251.5, with the Pi priced at the old $60 (verified BOM).
  - **[code]:** the LeRobot driver reports only body velocities (`x.vel, y.vel, theta.vel`, from wheel `Present_Velocity`; `lekiwi.py` L341-354). There is no pose, odometry or localization at all.
  - The community is bolting on lidars ad hoc (Foxglove blog "Upgrading the LeKiwi into a LiDAR-equipped explorer" [snippet; page blocked]).

### Research question
On a slipping omni-wheel base, which motion prior gives the lowest-drift 2D lidar odometry, and does any wheel prior still help once the kinematic constraint is gone? The priors compared are: none (constant velocity, KISS-ICP-style); Kinematic-ICP as-is; a 3-DOF extension with Kinematic-ICP's adaptive weighting generalized to a direction-dependent 3x3 weight; a commanded-velocity prior; and IMU yaw.

### Why the outcome is uncertain
- **A:** a direction-weighted 3-DOF wheel prior still beats prior-free ICP, mainly in degenerate scenes, so Kinematic-ICP's idea generalizes.
- **B:** omni-roller slip makes every wheel prior harmful, and prior-free ICP plus IMU yaw wins. Then Kinematic-ICP's benefit is specific to non-slipping drives.
- Kinematic-ICP as-is is *predicted* to show lateral drift equal to the wheel odometry's. That part is derivable. The ranking among the fixes is not.

### The non-obvious insight
Kinematic-ICP's adaptive β already measures, frame by frame, how wrong the odometry was (the mean residual of the odometry-predicted alignment, L48-58). Splitting that residual by direction (forward, lateral, yaw) gives a self-tuning *anisotropic* trust in the wheels. That fits omni bases, where rollers slip mainly in one direction, with no slip model or calibration step.

### Open-source reuse

| Component | Link | License | Saves |
|---|---|---|---|
| Kinematic-ICP | github.com/PRBonn/kinematic-icp | MIT | Whole odometry pipeline; the team edits ~60 lines in Registration.cpp |
| KISS-ICP | github.com/PRBonn/kiss-icp | MIT [not checked] | Prior-free baseline |
| LeKiwi hardware and LeRobot driver | github.com/SIGRobotics-UIUC/LeKiwi, github.com/huggingface/lerobot | Apache-2.0 | Base CAD, BOM, motor driver, teleop |
| ldlidar driver, rosbags, evo | as above | | Sensor and evaluation |
| slam_toolbox | as above | LGPL-2.1 | Downstream mapping check |

**The team builds:**
1. A ROS 2 bridge publishing LeKiwi wheel odometry (`/odom` + TF) from `Present_Velocity`.
2. LD19 and BNO085 mounts.
3. The 3-DOF anisotropic variant.
4. An overhead ArUco GT camera.

### Closest prior work, and what is new
1. **Kinematic-ICP** (arXiv 2410.10277) [code read]. Unicycle-only by construction.
2. **KISS-ICP** (Vizzo et al., RA-L 2023) [not opened]. Prior-free; used as a baseline.
3. **Okawara et al., LiDAR-IMU-wheel odometry with online kinematic calibration for skid-steer** (arXiv 2404.02515), and **neural kinematic model learning** (arXiv 2407.08907) [snippet]. Skid-steer, 3D LIO. Not omni, not 2D cheap lidar.
4. **Censi, Franchi, Marchionni, Oriolo, "Simultaneous calibration of odometry and sensor parameters"** (T-RO 2013) [not opened]. Calibration, not slip-adaptive weighting.
5. **Rabiee & Biswas, friction-based skid-steer kinematic model** (ICRA 2019) [snippet]. A model-based alternative.
6. **TidyBot++** (arXiv 2412.10447) [snippet]. Holonomic learning platform with powered casters (low slip). Shows why holonomic bases matter for learning.

**New:** the first lidar-odometry evaluation on a slipping omni base. A measured test of whether Kinematic-ICP's benefit survives without a kinematic constraint. An anisotropic adaptive weight, measured against Kinematic-ICP's own released code and defaults.

### Experiment design (baseline: Kinematic-ICP release defaults)
- **Arena:** 4x5 m, with an overhead 1080p webcam tracking an ArUco board on the robot (expected ~1 cm; validated against a tape grid). Plus a 30 m corridor with floor tags for degenerate scenes.
- **Grid:** 3 motion profiles (diff-like, strafe-heavy, mixed spin+translate) x 2 floors (tile, carpet) x 8 runs of 3 min = 48 runs.
- **Pipelines:** all run offline on the same bags (paired). A day of diff-drive data (the S2 robot, if built, or a borrowed TurtleBot) checks that Kinematic-ICP wins where its assumption holds.
- **Sample size:**
  - Assumptions: SD of paired drift difference ≈ 1.0 % of distance (a guess). Target effect: 0.6 %. Then n ≈ (2.8·1.0/0.6)² ≈ 22 → 48 runs gives margin for per-profile analysis.

### Measurements and analysis
- **Metrics:** RPE (%/m), lateral vs forward drift split, ATE in the arena, along-axis error in the corridor, and Pi 5 CPU.
- **Analysis:** mixed model drift ~ pipeline x profile + floor + (1 | run), with paired bootstrap contrasts.

### Build list

| Item | Cost | Status |
|---|---|---|
| LeKiwi base-only 12V kit (BOM $251.5, Pi listed at $60) plus the Pi price increase (+$50) | ~$300 | BOM verified; Pi increase [snippet] |
| LD19 | ~$100 | Estimated |
| BNO085 IMU breakout | ~$25 | Estimated |
| Overhead 1080p webcam and mount | ~$40 | Estimated |
| ArUco and tag printing, tape, spares | ~$35 | Estimated |
| **Total** | **≈ $500** | |

### Timeline
- **Wk 1–2:** Order the LeKiwi kit and print parts. SW student builds Kinematic-ICP and KISS-ICP 2D on Stata bags.
- **Wk 3–5:** Assemble LeKiwi. Write the odometry bridge. Calibrate the overhead camera.
- **Wk 6–8:** Collect 48 runs and corridor runs. **Data by Dec 20.**
- **Wk 11–13:** 3-DOF anisotropic variant.
- **Jan 15:** Go/no-go.
- **Wk 14–17:** Analysis.
- **Freeze Feb 14. Submit Feb 26.**

### Roles
- **Hardware student:** LeKiwi assembly, sensor mounts, GT camera rig, arena and corridor runs.
- **Software student:** ROS 2 bridge, pipelines, the Registration.cpp change, statistics.

### Main risk and fallback
- **Risk:** the overhead-camera GT is not accurate enough for strafe drift.
  - **Fallback:** use checkpoint returns (closed-loop start=end error) and floor tags.
- **Risk:** the C++ change is hard.
  - **Fallback:** run KISS-ICP 2D with an external EKF that fuses wheel odometry and IMU (robot_localization) as the "3-DOF prior" arm.

### Best venue
An ICRA 2027 workshop (low-cost robot learning or open hardware), or IROS 2027 with a short-paper framing. The LeRobot community release is the main impact path.

### Lab appeal
- **Best fit: UCLA LEMUR (Mehta).** Kenny Chen's Direct LiDAR Odometry (RA-L 2022), plus the lab's cheap and printable robots ("Towards One-Dollar Robots", Robotica 2020; labs.md). They gain a lidar-odometry result on the cheapest holonomic learning platform.
- **Second: UCSC ASL (Elkaim),** for the Pi/ROS 2 embedded fit.

### Honest self-score
- **Novelty 4.5:** a code-verified limitation, but extending a 2-DOF ICP to 3-DOF with odometry weighting is close to standard fusion, and reviewers may call it incremental.
- **Feasibility 7.5:** cheap kit, one robot, offline paired analysis.
- **Impact 5:** gives LeKiwi/LeRobot users odometry they lack, but the audience is narrow for IROS/CASE.
- **Overall ≈ 5.67.**

---

## Ranking and cross-cutting notes
1. **S1 (6.33)** is the strongest. It answers future work the original team stated themselves, it has a GT-free primary metric, and it can produce most of its data from public datasets before any robot exists.
2. **S2 (5.67)** has an early, cheap pilot that decides between two papers.
3. **S3 (5.67)** is the safest build but has the thinnest novelty.

S1 and S2 share the same robot design (linorobot2 + LD19), so the team could build once and pursue S1 with S2's pilot as a side check.

None of the three clears 7.5 on my own harsh reading. Novelty in low-cost 2D SLAM is crowded. S1's best route upward is a mentor (Carpin or LEMUR) who sees the November pilot plot and suggests the consistency formulation reviewers expect (for example, CI-weighted digests).
