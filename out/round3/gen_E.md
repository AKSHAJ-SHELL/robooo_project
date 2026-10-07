# Generator E: "Test an assumption the field relies on"

Date: 2026-10-04. Strategy: find an assumption that mobile and field robotics relies on, test it in the real world, and pick questions where a 20–40 cm robot is the right test platform rather than a compromise. Each idea below has a **Lab appeal** section, per the coordinator's update.

## How the search was done (read this first, it limits what I can claim)

- **The sandbox blocked direct access to arXiv, Google Scholar, IEEE Xplore, Semantic Scholar, OpenAlex, Hugging Face and project pages (HTTP 403 from the egress proxy).** I could not open PDFs. Every paper below was checked through a web search engine's result (title, abstract and text extracts), marked **[S]**. I list only items that came up in my own searches. Nothing is cited from memory.
- **GitHub was reachable through `git clone`, so I read the released code** of S2E/NavBench-GS, VisNavKit, CityWalker, MBRA/LogoNav, NavDP, urban-sim and visualnav-transformer. These are marked **[G]**. The code findings that the ideas depend on are quoted with file names.
- The reviewers should still repeat the Scholar and IEEE searches. Search coverage is wide (about 45 queries), but I could only read abstracts.

## Candidates considered and killed

| # | Candidate | Verdict | Why |
|---|---|---|---|
| K1 | Camera-height sweep of navigation foundation models (does a model trained at human height fail at 20 cm?) | **Killed** | Already treated as a known problem with published fixes: CanonNav (normalises camera height, [arXiv 2608.30242](https://arxiv.org/abs/2608.30242) [S]), CeRLP (height-adaptive pseudo-scans, [2603.19602](https://arxiv.org/pdf/2603.19602) [S]), VIL / V²-VLNCE (camera height and pitch varied in simulation, [2507.08831](https://arxiv.org/pdf/2507.08831) [S]), ExAug. A measurement study would read as incremental. Height survives only as a factor inside Ideas 1 and 3. |
| K2 | Zero-shot metric monocular depth at low viewpoints | **Killed** | GenDepth ([2312.06021](https://arxiv.org/html/2312.06021v1) [S]) and GVDepth (ICCV 2025, [paper](https://openaccess.thecvf.com/content/ICCV2025/papers/Koledic_GVDepth_Zero-Shot_Monocular_Depth_Estimation_for_Ground_Vehicles_based_on_ICCV_2025_paper.pdf) [S]) already study camera-height and perspective bias. CeRLP adds offline scale correction. |
| K3 | Are sidewalk navigation rankings stable across sessions and sun angles (how many trials are needed)? | **Killed** | Evaluation-methodology papers cover this: Kress-Gazit et al. ([2409.09491](https://arxiv.org/pdf/2409.09491) [S]), "Is Your Imitation Learning Policy Better than Mine?" ([2503.10966](https://arxiv.org/html/2503.10966v1) [S]), AutoEval ([2503.24278](https://arxiv.org/html/2503.24278v1) [S]), Active factor-based real-world evaluation ([2607.14439](https://arxiv.org/html/2607.14439v1) [S]). Moving it to sidewalks is "known method, new setting" (novelty about 5.5). |
| K4 | Does synthetic corruption robustness (sun flare, blur) predict real lighting robustness? | **Killed** | The outcome is predictable from the classification literature (synthetic robustness does not transfer to natural shifts). The "Can Vision Foundation Models Navigate?" study already uses synthetic sun flare ([2603.25937](https://arxiv.org/pdf/2603.25937) [S]). |
| K5 | Do open-loop metrics (ADE/ATE) predict closed-loop navigation, as a standalone study? | **Folded into Idea 1** | Driving has already shown poor correlation: "Do Open-Loop Metrics Predict Closed-Loop Driving?" ([2605.00066](https://arxiv.org/html/2605.00066) [S]), Scalable Offline Metrics ([2510.08571](https://www.arxiv.org/pdf/2510.08571) [S]). Kept as one of the proxies that Idea 1 compares. |
| K6 | "Nav2 with default parameters" is a straw-man baseline | **Killed** | Known from BARN-challenge and APPLR-style tuning results. Predictable. |
| K7 | Depth-derived pseudo-scan vs a real 2D lidar slice on sidewalks | **Killed** | Too close to CeRLP. It also looks like the "camera vs sensor" ideas that already failed. |

The three survivors share one robot and software stack, so they can also be combined into one larger paper.

---

## Idea 1: Phone-scan digital twins vs the real sidewalk: does Gaussian-splat evaluation predict how navigation foundation models behave at 30 cm?

**Research question.** Do 3D Gaussian-splat "digital twins" of a sidewalk predict, episode by episode, how sidewalk navigation foundation models behave on a 30 cm-camera robot in the same place? Does the answer depend on whether the scene was captured at human height (current practice) or at robot height?

**Who benefits and how much.**
- Several groups now rank navigation models mainly in simulation:
  - NavBench-GS (S2E, ICLR 2026) builds its scenes with Vid2Sim from human-height video.
  - SidewalkBench evaluates 9 models in Isaac Sim.
  - NavArena turns more than 2,000 splat reconstructions into benchmarks.
  - EmbodiedSplat fine-tunes and evaluates in iPhone scans.
- If the twins predict real behaviour, these labs get the first outdoor, low-viewpoint validation they can cite. If they do not, we give a concrete fix (capture height, or a fidelity check in the policy's output space) before large benchmarks get built on a biased proxy.
- Either way, the released set of paired real and twin episodes becomes a reusable calibration set for every future splat benchmark.

**The assumption tested and who relies on it.** "A photoreal reconstruction captured from human-viewpoint video is a faithful closed-loop evaluator for a low robot."
- S2E/NavBench-GS ([2507.22028](https://arxiv.org/pdf/2507.22028) [S]; code [G]). The README says the scenes come from `vid2sim_raw` captures. Its robots are the COCO delivery robot and a Unitree Go2.
- Vid2Sim ([CVPR 2025](https://openaccess.thecvf.com/content/CVPR2025/papers/Xie_Vid2Sim_Realistic_and_Interactive_Simulation_from_Video_for_Urban_Navigation_CVPR_2025_paper.pdf) [S]). Monocular hand-held video. It adds "screen-space covariance culling" because rendering breaks "when the agent's camera trajectory deviates substantially from the training views". The authors acknowledge the problem but do not measure what it does to policy behaviour.
- NavArena ([2609.04602](https://arxiv.org/html/2609.04602) [S]): more than 2,000 frozen splats used as closed-loop benchmarks.
- EmbodiedSplat ([ICCV 2025](https://openaccess.thecvf.com/content/ICCV2025/papers/Chhablani_EmbodiedSplat_Personalized_Real-to-Sim-to-Real_Navigation_with_Gaussian_Splats_from_a_Mobile_ICCV_2025_paper.pdf) [S]). It reports a sim-vs-real correlation of 0.87–0.97, but indoors, with a Stretch camera at 1.31 m, about the same height as the iPhone used for capture. So it never tested a height gap.
- The Neverwhere benchmark ([2609.16443](https://arxiv.org/pdf/2609.16443) [S]): more than 60 splat scenes used as closed-loop locomotion evaluators.

**Why the outcome is uncertain.**
- **Result A: the twins predict well** (episode-level r ≥ 0.7 even for human-height captures). This validates NavBench-GS and Vid2Sim-style evaluation for low sidewalk robots, which is good news for a fast-growing practice and gives it a citable bound.
- **Result B: human-height twins mispredict, but robot-height or mixed captures fix it.** Near-ground rendering artefacts (floaters, smeared curbs, missing low obstacles) would change policy outputs. That would give a design rule: capture at the deployment height, or check fidelity in the policy's output space.
- **Result C: no capture fixes it.** That is the strongest warning to the benchmark community.
- Theory cannot settle this. Policies with frozen DINOv2/v3 encoders (CityWalker, S2E) may ignore rendering artefacts that PSNR penalises. Small CNN policies (LogoNav at 96×96) may also be insensitive. Or both may react to near-field artefacts. Nobody has measured it.

**Non-obvious insight.** Twin fidelity should be measured **in the policy's output space, not in pixels**.
- We render the twin at the exact poses the real robot drove through. We feed real and rendered frame sequences to each frozen policy and compare the predicted waypoints. This "counterfactual open-loop divergence" costs no extra robot time and has thousands of samples.
- Our hypothesis: it predicts closed-loop disagreement much better than PSNR/SSIM/LPIPS. If true, anyone can check a twin's validity for a given policy from a single teleoperated drive.
- A second, smaller point: in a capture at about 1.5 m, the ground 0.5–3 m ahead of a 30 cm camera is seen only at grazing angles. That is exactly where sidewalk policies make their collision-relevant decisions.

**Closest prior work and exactly what is new.**
1. EmbodiedSplat ([CVF](https://openaccess.thecvf.com/content/ICCV2025/papers/Chhablani_EmbodiedSplat_Personalized_Real-to-Sim-to-Real_Navigation_with_Gaussian_Splats_from_a_Mobile_ICCV_2025_paper.pdf) [S]): indoor ImageNav, policy-level sim-real correlation, no height gap, no foundation models outdoors.
2. Real-to-Sim Robot Policy Evaluation with Gaussian Splatting ([2511.04665](https://arxiv.org/html/2511.04665v1) [S]): manipulation; r > 0.897 between simulated and real success.
3. PolaRiS, real-to-sim evaluation for generalist policies ([2512.16881](https://arxiv.org/pdf/2512.16881) [S]): manipulation.
4. NavBench-GS / S2E ([2507.22028](https://arxiv.org/pdf/2507.22028) [S]; [GitHub](https://github.com/VAIL-UCLA/S2E) [G]): publishes rankings (S2E > MBRA ≈ CityWalker > GNM/ViNT/NoMaD). The S2E paper's real-robot tests use only S2E variants. In the repository, `NavbenchGS/navbench_gs/{envs,metrics,scenarios}` hold only empty `__init__.py` files, and the README marks "Benchmark detail settings" as not released.
5. Vid2Sim ([CVPR 2025](https://openaccess.thecvf.com/content/CVPR2025/papers/Xie_Vid2Sim_Realistic_and_Interactive_Simulation_from_Video_for_Urban_Navigation_CVPR_2025_paper.pdf) [S]).
6. R2S-EGO ([2608.06827](https://arxiv.org/pdf/2608.06827) [S]). It states that "sparse human capture can leave behaviour-scoped robot views under-supported" and proposes a view-synthesis fix (Replica scenes, Unitree G1). It does not test whether evaluation remains valid.
7. Fremont et al., "Formal Scenario-Based Testing of AVs: From Simulation to the Real World", ITSC 2020 ([arXiv 2003.07739](https://arxiv.org/abs/2003.07739) [S]): sim-to-track transfer of test cases for a full-size AV.
8. SidewalkBench ([2606.16953](https://arxiv.org/abs/2606.16953) [S]): Isaac Sim, 9 models, no reported real-world rank validation in the abstract.

**What is new:**
- The first **outdoor, low-viewpoint, episode-level** test of splat-twin validity for **navigation foundation models**.
- The first controlled manipulation of **capture height**.
- The first comparison of three cheap proxies (splat twin, open-loop ADE, a published sim leaderboard) against the same real episodes.
- A tested fidelity metric in policy-output space.

**Experiment design.**
- **Policies.** These are the point-goal models with released weights, run through their upstream inference code. We do not use the model-zoo wrappers. VisNavKit's audit ([docs/models.md](https://github.com/DhlinV/visnavkit) [G]) reports that the zoo's CityWalker wrapper "ignores `goal_xy`, randomizes the last coordinate row", and that the S2E wrapper's comments disagree with its scaling. We run parity checks against upstream examples.
  - CityWalker (official checkpoint).
  - LogoNav/MBRA GPS-goal.
  - S2E web-pretrained behaviour-cloning model (the RL weights are unreleased; we say so).
  - NoMaD in goal-masked exploration mode. It has no goal, so we score only its collision behaviour.
- **Sites.** 8 sidewalk routes of 25–40 m at 3–4 sites, with static obstacles placed: cardboard boxes, planters, and refuse carts on collection day.
- **Runs.** Early-morning runs. If a pedestrian approaches, the episode is paused and annotated. No human-subjects data is collected, and faces are blurred before release.
- **Starts.** 3 start conditions per route: nominal, lateral offset, heading offset.
- **Real episodes.** 4 policies × 8 routes × 3 starts = **96 real episodes**.
- **Twins.** Each route is captured three ways within about 1 hour of the runs, giving 24 splats trained with gsplat or nerfstudio splatfacto:
  - (T_H) human-height phone walk at about 1.4 m, the Vid2Sim/EmbodiedSplat practice;
  - (T_R) phone on a pole at 0.3 m along the robot path;
  - (T_HR) both captures combined.
- **Twin rollouts.** Each real episode is replayed from the same start pose in each twin. The twin uses unicycle kinematics matching the robot's measured velocity limits and logged latency, and a collision footprint against a Gaussian-density occupancy grid (the NavArena-style costmap). The grid is checked against the robot's lidar map.
- **Two more proxies on the same episodes.**
  - (O) Open-loop ADE of each policy on our own teleoperated drives of the same routes, using VisNavKit's open-loop benchmark protocol.
  - (P) The published NavBench-GS ranking. This is policy-level only.
- **Power.** I simulated 4,000 draws with the Meng–Rosenthal–Rubin test for dependent correlations, assuming the two twin predictors correlate at 0.6 with each other:
  - n = 96 gives 0.84 power to tell apart r = 0.70 (T_R vs real) from r = 0.50 (T_H vs real);
  - n = 96 gives more than 0.99 power for 0.75 vs 0.45.
  - Episodes are clustered by route. With a design effect of about 1.5 (n_eff ≈ 64), power stays above 0.9 for the 0.75 vs 0.45 contrast.
  - A 95% CI half-width of about ±0.12 on a single r ≈ 0.7 needs n ≈ 72.
  - The counterfactual divergence analysis uses about 30,000 frame-level samples, so its power is not the limiting factor.
- **Stretch: failure transfer, in Fremont-style scenario testing.** In the T_R twin, search start poses and obstacle placements for collisions. Then run 20 twin-flagged and 20 random conditions per policy on the real robot, for 2 policies (80 episodes). Fisher's exact test detects 45% vs 15% real collision rates with about 0.8 power.

**Strongest fair baseline.**
- The capture practice the benchmark authors use themselves: human-height monocular video, as in Vid2Sim and NavBench-GS, and an EmbodiedSplat-style phone capture.
- The published NavBench-GS ranking, taken as reported.
- Each policy run with its authors' own deployment parameters. For example, LogoNav uses `metric_waypoint_spacing=0.25` and goal clipping at 30 m, as in `deployment/LogoNav_ros.py` [G]. CityWalker uses its `target_fps: 1` cadence from `config/finetune.yaml` [G].

**Measurements and analysis.**
- **Per episode:**
  - route completion, as a fraction of geodesic progress (primary, continuous);
  - success within 2 m of the goal;
  - bumper-switch collisions;
  - minimum clearance from the lidar;
  - cross-track deviation from the sidewalk centreline;
  - interventions.
- **Statistics:**
  - Pearson and Spearman correlations between twin and real for each twin type, with a route-cluster bootstrap;
  - Cohen's kappa for collision agreement;
  - dependent-correlation tests (T_H vs T_R vs T_HR, and twin vs open-loop ADE);
  - policy-level Kendall τ against NavBench-GS, descriptive only because there are 4 policies;
  - a mixed model of the twin-minus-real gap with fixed effects for policy × capture height and a random effect for route;
  - a fidelity-metric shoot-out: does policy-output divergence predict closed-loop disagreement better than PSNR, SSIM or LPIPS? Compared by AUC and R².
- **Release:** all episodes, splats, poses and code.

**Build list (costs are estimates unless marked).**

| Item | Cost |
|---|---|
| Hoverboard base (reuse bin-robot base if built) | ~$139 est. |
| Jetson Orin Nano Super dev kit (CityWalker's DINOv2-B runs at its native 1 Hz) | ~$249 est. |
| 2× wide-angle Pi/USB cameras | ~$70 est. |
| LD19-class 2D lidar (ground truth for clearance and twin alignment only; never a policy input) | ~$99 est. |
| ESP32 + hall-sensor odometry wiring | ~$15 est. |
| Foam bumper + microswitches | ~$25 est. |
| Battery + DC-DC | ~$60 est. |
| Frame and mounts | ~$80 est. |
| Phone pole mount for robot-height capture | ~$25 est. |
| Obstacles (boxes, pool noodles; carts borrowed) | ~$30 est. |
| **Total** | **≈ $790** |

Compute is free: Colab T4 or Kaggle for splat training (each 25–40 m outdoor scene should fit a free GPU session, to be confirmed in the pilot) and for twin rollouts. All weights are public. NavDP is left out: it needs RGB-D and has a CC-BY-NC-SA licence.

**Week-by-week timeline.**

| Dates | Work |
|---|---|
| Oct 12–25 | Install policies from upstream code; parity checks; first phone splat of a home sidewalk on Colab; e-mail labs. |
| Oct 26–Nov 8 | Twin-rollout code (gsplat render → policy → unicycle → occupancy collision); finalise the parts order. |
| Nov 9–22 | Parts arrive (order by Nov 15); build robot; ROS 2 bridge; teleoperated logging. |
| Nov 23–Dec 6 | Robot-height capture tool; first T_H/T_R pair; counterfactual-divergence pipeline. |
| Dec 7–20 | **Pilot: 2 routes × 4 policies × 3 starts = 24 real episodes, 6 splats, open-loop logs.** Re-estimate effect sizes and redo the power analysis. |
| Dec 21–Jan 10 (break) | Routes 3–5 (36 episodes) plus captures. |
| **Jan 15 go/no-go** | If real route completion has a floor effect (below 10% for all policies), shorten routes and make clearance the primary metric. If twins cannot be trained reliably, fall back to the counterfactual-divergence study only. |
| Jan 16–Feb 7 | Routes 6–8 (36 episodes); failure-transfer stretch if ahead of schedule. |
| Feb 8–14 | Re-runs; **data freeze Feb 14**. |
| Feb 15–26 | Analysis; paper; release. |

**Data by Dec 20:** 24 paired real and twin episodes, 6 splats, open-loop logs, and a first correlation estimate.

**Main risk and fallback.**
- **Risk:** the policies perform so badly on our robot that every outcome is near zero, which makes correlations meaningless. Or the outdoor splats are too poor to train because lighting changes or the scene moves.
- **Fallback:** the counterfactual open-loop divergence study needs only teleoperated drives plus splats, works even if closed-loop success is zero, and is still a publishable "fidelity in policy-output space vs PSNR" result.

**Best venue.** IROS 2027 main track (fits the sim-to-real and benchmark theme). CASE 2027 is the alternative. Fallback: an ICRA 2027 workshop on evaluation or real-to-sim.

**Lab appeal.**
- **Daniel Fremont (UCSC; SIP 2026 advisor):** his ITSC 2020 paper "Formal Scenario-Based Testing of Autonomous Vehicles: From Simulation to the Real World" ([arXiv 2003.07739](https://arxiv.org/abs/2003.07739) [S]) asked the same question for a full-size AV on a test track: do simulated test cases transfer? This project carries his sim-to-real testing line over to learned sidewalk policies and photoreal twins at almost no cost to his group. The stretch failure-transfer experiment is his methodology. **He gains:** a real-world dataset of paired twin and real learned-policy episodes and a low-cost outdoor testbed for scenario-based falsification, a natural SIP 2027 project.
- **Gabriel Elkaim (UCSC ASL):** the SIP 2026 project CSE-11 (Pi + ROS 2 + Nav2 differential-drive robot, [sip.ucsc.edu/2026-research-projects](https://sip.ucsc.edu/2026-research-projects/)) needs a cheap way to evaluate before field days. **ASL gains:** a phone-scan twin pipeline that has been validated for its own robots.
- Not on the reachable list but an obvious external beneficiary: UCLA VAIL (the S2E, NavBench-GS and MIMIC authors), whose benchmark this validates.

**Link to the bin robot.** Refuse carts are the placed obstacles. A twin of the team's own driveway lets the bin robot's navigation be tested before every software change.

**Honest self-score.**
- **Novelty 7.5:** splat-twin validity has been shown indoors and for manipulation, but outdoors, at low viewpoint, with foundation models, a capture-height manipulation and a policy-output fidelity metric, it is clearly new. Reviewers may still call it "EmbodiedSplat outdoors" if the capture-height result is null.
- **Feasibility 6.5:** four upstream policies, splat training and a closed-loop rig in 12 part-time weeks is a lot. The pilot by Dec 20 and the divergence-only fallback reduce the risk.
- **Impact 7.5:** several benchmarks released in 2025–26 depend on this assumption, so either answer gets cited, and the dataset is reusable.
- **Overall ≈ 7.2.**

---

## Idea 2: How good must the goal be? GNSS and compass error tolerance of point-goal sidewalk navigation models, measured at 20 cm

**Research question.** How large a GNSS position error and compass heading error, of the kind measured on a 20 cm-tall sidewalk robot, can today's point-goal navigation foundation models absorb before they fail? Is the binding constraint position or heading?

**Who benefits and how much.**
- The Earth Rover Challenge (IROS 2026; 14 sites, 10+ cities; ERC 2025 used GPS checkpoints with a 15 m arrival radius, [ICRA 2025 page](https://shop.frodobots.com/blogs/news/the-earthrover-challenge-2025) [S]) and its teams.
- Anyone deploying CityWalker, LogoNav or S2E-type models on a GNSS-only robot.
- Sidewalk and agricultural robot builders deciding whether a $20 GNSS receiver is enough, or whether they need RTK or visual localization.
- The deliverable is an error-tolerance curve per model plus a measured low-antenna error budget: a spec sheet, not an anecdote.

**The assumption tested and who relies on it.** "Point-goal navigation models can be driven by goals computed from consumer GNSS and compass."
- **CityWalker** ([CVPR 2025](https://www.researchgate.net/publication/394595874_CityWalker_Learning_Embodied_Urban_Navigation_from_Web-Scale_Videos) [S]; code [G]). The paper lists sensitivity to location noise as a limitation and leaves it to future work. In the released code, the synthetic noise (`input_noise: 0.1`, in step-normalised units) is added **only to past positions** (`data/citywalk_dataset.py`, line 181). The target point is never perturbed in web-video pretraining, and the teleop fine-tuning dataset feeds raw GPS without added noise (`data/teleop_dataset.py`). How it tolerates goal noise is therefore untested.
- **MBRA/LogoNav** ([GitHub](https://github.com/NHirose/Learning-to-Drive-Anywhere-with-MBRA) [G]). The README says the authors "use our own GPS instead of the mounted GPS on Frodobot to conduct more reliable" experiments. The goal is a vector plus a goal heading built from GPS and compass, clipped to 30 m (`deployment/LogoNav_ros.py`). We also noticed that the released `LogoNav_frodobot.py` assigns `goal_pose` only inside the `distance_goal > 30 m` branch. We will use the ROS script's goal logic, which handles both cases, and confirm with the authors. We do not claim this affected any published result.
- **S2E** (point goal encoded as clipped distance/200, cos, sin, per the VisNavKit wrapper audit [G]).
- **ERC teams and GeNIE**, the ERC 2025 winner ([2506.17960](https://arxiv.org/html/2506.17960v2) [S]).
- **FrodoBots-2K**, whose action and pose labels come from onboard GPS on 20 cm robots.

**Why the outcome is uncertain.**
- **Result A, the sidewalk prior dominates.** These models mostly follow the sidewalk and treat the goal as a coarse direction. Lateral goal errors of 5–10 m barely matter until a junction. Consumer GNSS is then "good enough", which contradicts CityWalker's own stated limitation.
- **Result B, they follow the goal.** The models steer toward a wrong goal into hedges, driveways or lawns. They oscillate as the goal jitters every 1 Hz GNSS update, and "arrive" at the wrong place. The tolerance then has a specific size.
- The answer can differ by model (CityWalker was trained on clean targets; LogoNav on raw FrodoBots GPS). Both outcomes change what deployers buy.

**Non-obvious insight.**
- **Heading error is multiplied by goal distance, and compasses near hub motors at 20 cm are bad.** LogoNav clips goals to 30 m, so a 20° compass error moves the clipped goal sideways by about 10 m, bigger than typical open-sky GNSS position error.
- We predict that the tolerance budget for low robots is set by **heading, not position**. This flips the usual "buy better GNSS" advice and points instead to magnetometer placement, or to heading from GNSS course over ground.
- A second insight: a continuous "goal gain" (the robot's lateral path offset per metre of lateral goal offset, between 0 and 1) summarises how much each model follows the goal versus its scene prior, and can be compared across models.

**Closest prior work and exactly what is new.**
1. CityWalker (limitation statement, [arXiv HTML](https://arxiv.org/html/2411.17820v2) [S]; code [G]).
2. MBRA/LogoNav ([2505.05592](https://arxiv.org/abs/2505.05592) [S], [G]).
3. "Integrating Egocentric Localization for More Realistic Point-Goal Navigation Agents" ([2009.03231](https://arxiv.org/pdf/2009.03231) [S]): noisy localization for PointGoal agents in Habitat simulation.
4. GeNIE ([2506.17960](https://arxiv.org/html/2506.17960v2) [S]): an ERC system with engineered localization.
5. "Can Vision Foundation Models Navigate?" ([2603.25937](https://arxiv.org/pdf/2603.25937) [S]): 5 models, real robots, image perturbations, no goal-error study.
6. Earth Rover Challenge ([ICRA 2025 announcement](https://lists.robocup.org/archives/list/robocup-worldwide@lists.robocup.org/thread/4HPGV7YWJR2ZVTBKEPFCDHIVVJC5TLDF/) [S]).

**What is new:**
- The first **closed-loop, real-world dose–response curves** of navigation foundation models against controlled goal-position and goal-heading error.
- A **measured** GNSS and compass error budget at 0.2 m vs 1.5 m antenna height on sidewalks.
- A validated prediction of real success that combines the two.

(The brief's "phone GNSS+VIO" idea was about building a localizer. This idea measures what the learned policies tolerate.)

**Experiment design.**
- **Phase A: error budget, robot-light, most of it done by Dec 20.**
  - 12 sidewalk sites (open sky, tree canopy, near buildings, near parked cars).
  - Sensors: a u-blox M10 receiver and a phone, with antennas at 0.2 m and 1.5 m on one pole, compared against a ZED-F9P RTK reference using a free NTRIP caster (California CRTN or RTK2go, to be confirmed).
  - At each site: 10 min static plus 3 walked passes. A BNO085 compass is logged at 0.2 m beside the running hub motors and on a 1 m mast.
  - Outputs: position-error and heading-error distributions by site type and height.
- **Phase B: tolerance curves (closed loop, RTK ground truth).**
  - Goals are computed from RTK truth plus injected error:
    - lateral position bias of {0, 3, 6, 10} m;
    - heading bias of {0, 15, 30}°;
    - one replayed real M10 error trace.
  - 3 models (CityWalker, LogoNav-GPS, S2E behaviour-cloning) × 8 error conditions × 6 routes (30 m segments; 3 contain a junction or driveway branch) = **144 episodes** of about 1 min each.
  - For safety, goals are displaced only toward lawns or walls, never toward the roadway.
- **Phase C: validation.** Predict each episode's outcome from (the Phase A error distribution × the Phase B curve). Then run 20 episodes per model on 3 held-out routes using the real M10 and compass (60 episodes).
- **Power.**
  - Primary outcome: lateral path offset at the segment end (continuous).
  - Assuming a residual SD of 0.4 m, 48 episodes per model and an SD of 3.7 m for the bias levels, the standard error of each model's goal gain is about 0.016.
  - So differences of 0.07 in goal gain between models are detectable at α = 0.05 with power above 0.8.
  - Success (binary) is secondary. The 60 validation episodes give a ±0.12 CI on calibration slope.

**Strongest fair baseline.** Each model's authors' own goal pipeline and parameters (LogoNav: 30 m clip and 2 m update threshold, ROS script; CityWalker: 1 Hz targets and its arrival head), fed RTK-quality goals, which is the "good localization" setting MBRA chose. A classical baseline (Nav2 with GNSS waypoints and the 2D lidar) shows how a hand-built stack degrades for comparison.

**Measurements and analysis.**
- **Per episode:** lateral offset, route completion, sidewalk departure (wheel on lawn or driveway), collisions, time, oscillation (heading-rate variance) and false arrival.
- **Statistics:** mixed models (fixed: model × error type × level; random: route); goal-gain slopes with bootstrap CIs; a decomposition of the error budget (share of failures explained by heading vs position); calibration of the predicted vs observed validation outcomes.

**Build list.**

| Item | Cost |
|---|---|
| Robot from Idea 1 (base, Orin Nano, camera, ESP32, battery, frame) | ≈ $570 est. |
| ZED-F9P RTK board | ~$220–275 est. (ask ASL to lend) |
| Multiband antenna | ~$70 est. |
| u-blox M10 breakout | ~$45 est. |
| BNO085 | ~$25 est. |
| Mast and pole | ~$20 est. |
| **Total** | **≈ $950–1,000** (≈ $680 if the RTK board is borrowed) |

The lidar is optional here. Compute is a laptop.

**Week-by-week timeline.**

| Dates | Work |
|---|---|
| Oct 12–Nov 8 | Code reading and goal adapters for the 3 models; NTRIP access; order GNSS parts first (they arrive fast). |
| Nov 9–Dec 6 | Phase A at 8 sites on foot with the pole (no robot needed); build robot. |
| Dec 7–20 | Phase A finished (12 sites); **pilot Phase B: 1 model × 8 conditions × 2 routes**. |
| Dec 21–Jan 10 | Phase B, models 1–2. |
| **Jan 15 go/no-go** | If a model cannot complete the 0-error condition (≥ 70% route completion), drop it and add NoMaD-explore as a contrast. |
| Jan 16–Feb 7 | Phase B, model 3; Phase C validation. |
| **Feb 14** | Data freeze. |
| Feb 15–26 | Analysis and writing. |

**Data by Dec 20:** a complete GNSS and compass error budget across 12 sites and 2 heights, plus 16 pilot tolerance episodes.

**Main risk and fallback.**
- **Risk:** RTK fixes under trees are unreliable, so ground truth degrades.
- **Fallback:** run Phase B on open-sky segments, where truth is clean. Error injection makes the injected error independent of site, so tolerance curves do not need bad-sky sites. Phase A then reports fix availability honestly.

**Best venue.** IROS 2027, or CASE 2027 for the deployment-spec angle. ICRA 2027 workshop fallback. Results could also be shared with the ERC organisers.

**Lab appeal.**
- **Stefano Carpin (UC Merced):** his ICRA 2024 paper "Improving the ROS 2 navigation stack with real-time local costmap updates for agricultural applications" (CV: [carpincvonline.pdf](https://sites.ucmerced.edu/files/scarpin/files/documents/carpincvonline.pdf)) is outdoor GNSS-waypoint Nav2. **His group gains:** a measured low-antenna GNSS and compass error budget and a protocol for testing whether learned local policies can replace or augment Nav2's local planner under GNSS goals. The result fits CASE, his venue.
- **Gabriel Elkaim (UCSC ASL):** GNC for ground vehicles (SIP 2024 project ELE-05 "Unified GNC framework for autonomous ground vehicle navigation", [sip.ucsc.edu/2024-research-projects](https://sip.ucsc.edu/2024-research-projects/)). Lending an RTK receiver costs ASL nothing. **ASL gains:** a SIP-ready experiment and data on cheap GNSS behaviour.

**Link to the bin robot.** The bin robot's garage-to-curb leg is a short GNSS-goal problem next to a house wall (bad multipath at low height). Phase A directly measures its error budget.

**Honest self-score.**
- **Novelty 6.5:** "noisy goals hurt" sounds predictable. The heading-dominance hypothesis, the goal-gain metric and the real closed-loop dose–response on foundation models are new, but a reviewer could still call it a sensitivity analysis.
- **Feasibility 7.5:** simple hardware, continuous metrics, and Phase A data needs no robot.
- **Impact 6.5:** directly useful to ERC teams and deployers as a spec, but the audience is narrower than Idea 1's.
- **Overall ≈ 6.8.**

---

## Idea 3: "Map with your phone, drive with your robot?" A synchronized multi-height test of place recognition and topological navigation from 0.2 m to 1.5 m

**Research question.** When the map images come from a person (about 1.5 m) and the queries come from a low robot (0.2–0.4 m), how much do state-of-the-art visual place recognition (VPR) and topological navigation models lose? Can the loss be predicted from scene depth structure on sites not used to fit the model?

**Who benefits and how much.**
- **Pipelines that build maps from human-carried cameras for robots:** EmbodiedSplat (iPhone), Vid2Sim and NavBench-GS (human video), PlaceNav (VPR trained on non-robot data), CityWalker (human videos), and the Instance-ImageNav idea of goal photos taken by users.
- **The VPR community:** it would get the first dataset where **height is the only variable**, because all cameras sit on one rig and record at the same instant.
- **Teams like ours:** a direct answer to whether to map with a phone or with the robot.

**The assumption tested and who relies on it.** "Viewpoint-robust foundation features (DINOv2-based VPR) make human-height maps usable by low robots."
- AnyLoc claims "universal" VPR across viewpoints ([2308.00688](https://arxiv.org/pdf/2308.00688) [S]).
- PlaceNav argues VPR "enables leveraging large-scale datasets from non-robotics sources" ([2309.17260](https://arxiv.org/pdf/2309.17260) [S]).
- InstanceImageNav defines goal images "taken with camera parameters independent of the agent", tested only in simulation ([Krantz et al.](https://openaccess.thecvf.com/content/ICCV2023/papers/Krantz_Navigating_to_Objects_Specified_by_Images_ICCV_2023_paper.pdf) [S]).
- EmbodiedSplat and Vid2Sim capture at human height (above).
- In NoMaD/ViNT deployment, by contrast, the topomap is built from the **robot's own camera topic** (`deployment/src/create_topomap.py`, `IMAGE_TOPIC="/usb_cam/image_raw"` [G]), and localization uses the learned temporal-distance head over nearby nodes (`navigate.py` lines 141–152 [G]). Using a phone-built map is therefore an untested deployment variant, not a documented capability.

**Why the outcome is uncertain.**
- **Result A: little loss.** DINOv2 aggregators (SALAD, BoQ, MegaLoc, AnyLoc) lose less than 5 Recall@1 points across a 1.2 m height gap, because distant structure dominates their descriptors. Phone mapping is then validated, and teams can stop driving robots just to build maps.
- **Result B: a large loss that depends on the site.** Narrow sidewalks with hedges and parked cars produce big losses (near-field parallax and ground dominance at 0.2 m). Open lots produce small ones. A simple predictor, such as median scene depth or ground-pixel fraction, explains the difference. That gives a rule: map at robot height where the near field dominates.
- Whether the topological navigation models (whose distance head was trained on same-camera pairs) degrade more or less than VPR is also unknown.

**Non-obvious insight.**
- The effect of height should scale with **near-field depth structure, not with height difference alone**. A 1.2 m height change is a large angular viewpoint change for a hedge 1.5 m away and a negligible one for a building 30 m away.
- So the loss should be **predictable per site** from a monocular depth histogram. That turns a benchmark into a held-out-validated predictive model, the lever the brief says reviewers reward.
- The synchronized rig also lets us separate height from appearance change exactly: same instant, different height; vs same height, different day.

**Closest prior work and exactly what is new.**
1. FusionPortableV2 ([2404.08563](https://arxiv.org/pdf/2404.08563) [S]): the same sensor payload on handheld, legged, wheeled and vehicle platforms, but on separate runs, so height is confounded with path and time.
2. AnyLoc ([2308.00688](https://arxiv.org/pdf/2308.00688) [S]): viewpoint shifts including aerial; no controlled ground-level height study.
3. VPR-Bench ([2005.08135](https://arxiv.org/pdf/2005.08135) [S]): quantified viewpoint and appearance change. It has a 4 m-rod drone-imitation dataset but no low-robot heights.
4. "Are SOTA VPR techniques any good for aerial robotics?" ([1904.07967](https://arxiv.org/pdf/1904.07967) [S]): the high-altitude side.
5. V²-VLNCE / VIL ([2507.08831](https://arxiv.org/pdf/2507.08831) [S]) and CanonNav ([2608.30242](https://arxiv.org/abs/2608.30242) [S]): height variation in simulation, or height normalisation in training. Neither tests real place recognition or maps.
6. The RoboSense Challenge ([2601.05014](https://arxiv.org/html/2601.05014v1) [S]): cross-platform and sensor-placement tracks for detection and driving, not VPR across heights.
7. PlaceNav ([2309.17260](https://arxiv.org/pdf/2309.17260) [S]).

**What is new:**
- The first **synchronized multi-height** (4 heights, same instant) outdoor VPR dataset.
- A predictive model of the height-gap loss validated on held-out sites.
- A closed-loop check of phone-built topomaps with NoMaD/ViNT.

**Experiment design.**
- **Rig.** A push-cart with a pole holding 4 cameras at 0.2, 0.4, 0.8 and 1.5 m (4 identical wide USB cameras on one laptop, software timestamps under 30 ms apart; or two Pi 5s with 2 CSI cameras each). Wheel encoder plus phone GNSS for position.
- **Data.** 15 routes of 300–600 m (sidewalks, parks, parking lots, driveways, a campus). Each is traversed 3 times on different days and at different times of day. About 30 rig-hours. No robot is needed.
- **Models.** NetVLAD, CosPlace, EigenPlaces, MixVPR, AnyLoc, SALAD, BoQ and MegaLoc (public weights), run on Colab.
- **Ground truth.**
  - Cross-height queries in the same traverse: identical frame index, which is exact.
  - Cross-traverse queries: sequence alignment of odometry and GNSS with a 10 m threshold (standard), plus a 5 m along-track check.
- **Predictor.** Per-site median depth and ground-pixel fraction from a monocular depth model. Fit on 10 sites, test on 5 held-out sites.
- **Closed-loop check (robot, from Jan).** NoMaD/ViNT topological navigation on 3 routes of about 40 m. The topomap is built from:
  - (a) the robot camera (authors' setting);
  - (b) a phone at 1.5 m;
  - (c) a phone at 0.3 m.
  - 3 maps × 3 routes × 8 runs = 72 runs.
- **Power.**
  - The unit is the site (n = 15) for height-gap effects. If the Recall@1 drop has a between-site SD of about 10 points, a paired test detects an 8-point mean drop with power above 0.9.
  - The held-out prediction is judged by R² and rank correlation over 5 sites. This part is weaker, so it is reported as a pilot-level prediction.
  - Closed loop: 24 runs per map condition detect 80% vs 40% success (power about 0.85). Route progress (continuous) is the primary outcome.

**Strongest fair baseline.**
- Same-height retrieval (the standard VPR protocol) for every model.
- For navigation, NoMaD/ViNT with a robot-built topomap and the authors' default `radius` and `close_threshold` settings from `navigate.py`.

**Measurements and analysis.**
- Recall@1/5 in a full height × height matrix, separated by within-traverse vs cross-day.
- A mixed logistic model (fixed: |Δh|, log height ratio, near-field depth and their interactions; random: site, model).
- Held-out-site prediction error.
- Closed loop: success, progress, localization jumps (node-index discontinuities) and interventions.
- **Release:** the dataset (faces blurred) and the evaluation scripts.

**Build list.**

| Item | Cost |
|---|---|
| 4× wide USB cameras | ~$140 est. |
| Pole + clamps | ~$40 est. |
| Push-cart (or reuse robot base) | ~$40 est. |
| ESP32 + wheel encoder | ~$25 est. |
| USB hub + battery | ~$50 est. |
| **Subtotal** | **≈ $295** |
| Robot from Idea 1 for the closed-loop check | ≈ $570 est. |
| **Total** | **≈ $865** |

Compute is free on Colab.

**Week-by-week timeline.**

| Dates | Work |
|---|---|
| Oct 12–Nov 8 | Set up the VPR evaluation (8 models) on public data; design the rig; order cameras. |
| Nov 9–22 | Build the rig; synchronization test. |
| Nov 23–Dec 20 | **Collect 10 routes × 3 traverses; first height × height matrices.** |
| Dec 21–Jan 10 | Remaining 5 routes; depth predictor; build the robot. |
| **Jan 15 go/no-go** | If all models lose less than 2 points at every height gap, frame the paper as "result A: phone mapping is safe", run the closed-loop check with more runs, and add goal-image transfer. |
| Jan 16–Feb 10 | Closed-loop topomap runs. |
| **Feb 14** | Data freeze. |
| Feb 15–26 | Writing and dataset release. |

**Data by Dec 20:** about 20 rig-hours across 10 routes, with complete VPR matrices for 8 models.

**Main risk and fallback.**
- **Risk:** the effect is uniformly tiny (result A), which some reviewers find less exciting. Or GNSS-based cross-day ground truth is noisy.
- **Fallback:** a null result on a synchronized, well-powered dataset is still a citable bound. Cross-height evaluation uses exact frame-index ground truth and does not depend on GNSS.

**Best venue.** IROS 2027, or RA-L with IROS presentation, as a dataset plus analysis. Fallback: an ICRA 2027 workshop on long-term or field localization.

**Lab appeal.**
- **Ankur Mehta (UCLA LEMUR):** "Resilient and Consistent Multirobot Cooperative Localization With Covariance Intersection" (T-RO 2022) and printable low-cost robots. Teams of different-sized robots, plus humans, sharing place recognition across heights is exactly this question. **LEMUR gains:** a dataset and a measured height-gap loss model for mixed robot teams.
- **Wencen Wu (SJSU):** the NSF RINGS cooperative-perception project (agents with different viewpoints sharing perception) and her small autonomous-parking vehicle (CACRE 2021). **Her group gains:** a controlled viewpoint-height dataset for cross-agent matching, with an HS team doing the collection.
- Secondary: Elkaim ASL's SIP 2025 graph-SLAM project (loop closures from heterogeneous cameras).

**Link to the bin robot.** Map the driveway once with a phone and let the robot (camera at about 0.3 m) localize against it. The closed-loop check uses that exact case.

**Honest self-score.**
- **Novelty 6:** viewpoint robustness in VPR is well studied. Isolating height with a synchronized rig and a validated depth-based predictor is new, but a reviewer could still call it "a new dataset axis".
- **Feasibility 8:** robot-free core data, cheap rig, all models public, data well before Dec 20.
- **Impact 6:** a useful dataset and design rule for the VPR and nav-mapping community, but probably RA-L or workshop level unless the closed-loop result is striking.
- **Overall ≈ 6.7.**

---

## Summary

| Idea | N / F / I | Overall | Best labs |
|---|---|---|---|
| 1. Phone-scan twins vs the real sidewalk (splat-evaluation validity at 30 cm, capture-height factor) | 7.5 / 6.5 / 7.5 | ≈ 7.2 | Fremont (UCSC), Elkaim (UCSC ASL) |
| 2. GNSS and compass goal-error tolerance of point-goal navigation models at 20 cm | 6.5 / 7.5 / 6.5 | ≈ 6.8 | Carpin (UC Merced), Elkaim |
| 3. Map with your phone, drive with your robot (synchronized multi-height VPR and topomaps) | 6 / 8 / 6 | ≈ 6.7 | Mehta (UCLA LEMUR), Wu (SJSU) |

All three can share one robot and software stack (Ideas 1 and 2 use the same policies; Ideas 1 and 3 both test whether human-height capture works for a low robot). If the team wants one paper, Idea 1 with Idea 3's synchronized height rig as its capture tool is the strongest combination.
