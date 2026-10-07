# Generator M: robot-learning models on low-cost open robots

**Date:** 2026-10-04. **Area:** learned policies (navigation foundation models, ACT/SmolVLA) on cheap open robots (FrodoBots EarthRover, SO-101/LeRobot).

**How I checked things.** I cloned and read the released code for every base project: `huggingface/lerobot` (HEAD of 3 Oct 2026), `NHirose/Learning-to-Drive-Anywhere-with-MBRA`, `NHirose/OmniVLA`, `frodobots-org/earth-rovers-sdk` and `frodobots-org/earth-rover-mini`. Statements tagged **[code]** are things I read in those repositories. arXiv, Semantic Scholar, Hugging Face and the vendor shop pages are blocked from this sandbox. Statements tagged **[snippet]** come from search-result text only; I did not open the paper. GitHub issue titles and summaries were read through github.com pages. Prices are tagged **verified** (a seller or listing snippet gives the number) or **estimated**.

---

## 0. Candidate funnel (9 ideas → 3)

| # | Candidate | Verdict | Why (evidence) |
|---|---|---|---|
| 1 | **The goal-pose sensing gap in GPS-conditioned navigation foundation models (LogoNav/OmniVLA) on a ~$300 EarthRover; switching on the rover's unused RTK receiver** | **KEEP (#1)** | The authors' README says they replaced the robot's GPS for evaluation. I found no study that measures how goal-pose error passes through a learned navigation policy. The labs in the brief are a strong fit. |
| 2 | **Recalibration frame shift on SO-101: how much does a routine LeRobot recalibration break ACT/SmolVLA policies, and which existing fix works?** | **KEEP (#2)** | [code] In LeRobot, a joint's zero is defined by how far the person sweeps it during calibration. Issue #1360: users must recalibrate after power cycles (closed "not planned"). Fixes exist in other settings but have never been compared under this perturbation. |
| 3 | **Leader-arm fidelity: do SO-101 leader detents/friction change what ACT learns? (open encoder-leader PCB)** | **KEEP (#3)** | Issue #2074 (snapping into ~29 positions per revolution, closed "not planned"). I found no study of within-device leader fidelity versus policy quality. It gives the hardware student a real PCB to build. |
| 4 | Servo current / tracking error as a free force signal for ACT on SO-101 | KILL | Already done: "Beyond Implicit Force" (arXiv 2607.14578) [snippet] studies exactly the leader-follower tracking-error cue plus current proxies in ACT. Also FACTR 2 (2606.12406) and NeuralActuator (2607.11734) [snippet] cover SO-101 load registers, and TA-VLA (2509.07962) covers torque in VLAs. LeRobot already ships a `Present_Current` observation processor [code: `src/lerobot/rl/joint_observations_processor.py`]. |
| 5 | Force-feedback (bilateral) SO-101 leader | KILL | Done on low-cost hardware: 2507.06174 and 2509.08226 [snippet]. |
| 6 | Camera-latency alignment for LeRobot datasets | KILL | The limitation is real: [code] OpenCV frames are timestamped on host receipt (`capture_time = time.perf_counter()` after decode), and `read_latest` accepts frames up to 500 ms old. But the method is UMI's latency matching, and "Mind the Gap" (2602.08776) plus a latency-aware visuomotor framework (2602.14255) [snippet] already cover the I/O and latency gap. That makes it incremental. |
| 7 | STS3215 thermal drift degrading policies over long sessions | KILL | The size of the effect can be worked out on paper (about +16% copper resistance from 25 to 65 °C, so a little more gravity sag under P=16). I found no community complaints, the audience is narrow, and the result would be predictable (lesson 1). |
| 8 | SmolVLA chunk-boundary jitter / async inference | KILL | LeRobot already includes Real-Time Chunking (`src/lerobot/policies/rtc`) [code]. |
| 9 | Porting OK-Robot to LeKiwi; NoMaD rate study | KILL | Already tried in earlier rounds (`ideas_v2_log.md`): the fix existed in stretch_ai, and the NoMaD outcome was foreseeable. |

---

## IDEA M1: Is the bottleneck the policy or the compass? Goal-pose sensing for GPS-conditioned navigation foundation models on a $300 rover

### Base project and the specific limitation
- **Base:** *Learning to Drive Anywhere with Model-Based Reannotation* (MBRA), which trains the **LogoNav** GPS-waypoint-conditioned policy (Hirose, Ignatova, Stachowicz, Glossop, Levine, Shah; arXiv 2505.05592). Code (MIT): https://github.com/NHirose/Learning-to-Drive-Anywhere-with-MBRA . Its successor, **OmniVLA** (ICRA 2026, MIT), accepts the same 2D-pose goals: https://github.com/NHirose/OmniVLA . Both were trained on FrodoBots-2k data from cheap teleoperated sidewalk rovers.
- **Limitation 1 (stated by the authors).** The MBRA README says, in the FrodoBots inference section: *"Note that we use our own GPS instead of the mounted GPS on Frodobot to conduct more reliable evaluation with accurate localization."* So the published numbers were not obtained with the robot's own sensors, and the gap is never quantified. [code: README.md]
- **Limitation 2 (visible in released code).** `deployment/LogoNav_frodobot.py` builds the goal vector each tick, at 3 Hz, from one raw SDK GPS fix and the raw SDK `orientation` (magnetometer heading). It does no filtering. The goal is clipped to 30 m, so a heading error θ shifts the commanded goal sideways by 30·sin θ m (about 10 m at 20°). [code, lines 86–121]
- **Limitation 3 (vendor docs).** The SDK README for the Mini+ says the IMU telemetry *"reports every 2 s with 100 accelerometer samples, 1 gyroscope sample and 1 magnetometer sample per report."* It also lists *"accurate GPS positioning"* as a feature of the older ZERO model but not the Mini+. [code: earth-rovers-sdk/README.md]
- **Limitation 4 (related work).** CityWalker (arXiv 2411.17820) [snippet] says its method *"is sensitive to large GPS errors"* and lists robustness to location noise as future work. The Earth Rover Challenge uses a ~15 m checkpoint tolerance to absorb consumer-GPS noise [snippet, earth-rover-challenge.github.io].
- **The unused fix.** The open-hardware wiki says the Mini+ GNSS is a **Quectel LC29HDA**: dual-band, RTK-capable, *"centimetre-level in open sky"* (wiki/docs/zh/06-3). Quectel's material [snippet] says it is an RTK rover that needs RTCM corrections on its UART. I found no RTCM or NTRIP handling anywhere in the released rover software (my inference: the stock firmware runs it without RTK). The wiki also documents root access over the rover's WiFi AP (`adb connect 192.168.11.1`) and replacing `/usr/bin/frodobot.bin` with your own program.
- **Released-code bug (must be fixed for a fair baseline).** In `LogoNav_frodobot.py`, `goal_pose` is only assigned inside `if distance_goal > thres_dist:` (30 m). The final approach therefore never sets a goal: the variable is unbound or stale, and the 5 m waypoint switch is unreachable. `LogoNav_ros.py` has the correct `else:` branch. We will use the ROS-script logic as "the authors' intended baseline" and report the bug to the authors.

### Research question
How much of a GPS-conditioned navigation foundation model's goal-reaching error on a stock $300 rover comes from goal-pose sensing (position versus heading), and can zero-cost onboard fixes (unlocking RTK, gyro/course-over-ground heading fusion) match the authors' external-GPS setup?

### Why the outcome is uncertain
- **Result A: the policy absorbs noise.** LogoNav re-plans at 3 Hz from 6 context images. Its visual prior (stay on the sidewalk, avoid obstacles) and the 30 m clip may average out zero-mean noise, and dual-band standalone GNSS may already be good enough in open sky. Then the stock rover matches the external-GPS setup and the README's GPS swap was unnecessary. That is useful to the many groups buying these rovers for the Earth Rover Challenge.
- **Result B: sensing dominates.** Magnetometer errors from motor hard-iron, rebar and parked cars are *biased and slowly varying*, not zero-mean, so the policy cannot average them away. Paths curve systematically and final errors exceed the challenge tolerance. Cheap fixes then recover most of the gap.
- **Mixed and most interesting.** Heading dominates path efficiency during the traverse, while position dominates the final approach. If so, the cheapest fix that matters depends on the metric.

Both A and B are publishable. A is a reproducibility result ("the stock sensors are enough"). B is a diagnosis plus a fix.

### The non-obvious insight
Treat the learned policy as a **block in a control loop with a measurable goal-error transfer gain**. Feed logged images with deliberately perturbed goal vectors and measure how much the predicted waypoint direction rotates per degree of goal error. A gain near 1 means the policy follows the goal blindly and sensing is everything. A gain well below 1 means the visual prior attenuates goal noise. This one number, measured offline from logs, predicts the closed-loop sensitivity. It tells anyone deploying LogoNav, OmniVLA or CityWalker how good their GPS and compass need to be. I could not find this measurement for any navigation foundation model.

### Open-source reuse
| Component | Link | License | What it saves |
|---|---|---|---|
| LogoNav weights + deployment script | github.com/NHirose/Learning-to-Drive-Anywhere-with-MBRA (weights on HF `NHirose/MBRA_project_models`) | MIT | The whole policy: no training needed |
| OmniVLA-edge (2D-pose goal mode), optional second policy | github.com/NHirose/OmniVLA | MIT | A second policy for generality |
| EarthRover SDK (HTTP: `/v2/front`, `/data`, `/control`) | github.com/frodobots-org/earth-rovers-sdk | no LICENSE file found (check) | Robot I/O and the telemetry logger |
| Rover hardware, firmware, schematics, wiki (LC29HDA serial commands, root access) | github.com/frodobots-org/earth-rover-mini | check repo | Path to feeding RTCM to the onboard GNSS |
| LeRobot EarthRover driver | lerobot `src/lerobot/robots/earthrover_mini_plus` | Apache-2.0 | Dataset recording of runs |
| RTKLIB / `str2str` NTRIP client | github.com/tomojitakasu/RTKLIB | BSD-2 | NTRIP→serial relay for RTCM |
| Free RTK corrections (CRTN / SOPAC, California) | listed by ardusimple.com and support.raptordynamic.com [snippet] | free, registration | cm-level reference without buying a base station |
| robot_localization-style EKF (or a 100-line numpy EKF) | github.com/cra-ros-pkg/robot_localization | BSD | Heading fusion |

**What the team builds:** (1) a logger that records SDK frames, telemetry and RTK fixes with timestamps; (2) an RTCM relay into the onboard LC29HDA through the rover's root shell, or, as a fallback, an external LC29H(DA) board plus ESP32; (3) a gyro + course-over-ground + magnetometer heading filter; (4) a goal-perturbation harness (offline replay and online injection); (5) a printed GNSS antenna mast and a ground-truth survey of route endpoints; (6) the bug-fixed baseline script.

### Closest prior work and what is new
1. **MBRA/LogoNav** (2505.05592; code above): the base. It evaluates with external GPS and does not quantify the stock-sensor gap.
2. **OmniVLA** (Hirose et al., ICRA 2026; github.com/NHirose/OmniVLA): accepts 2D-pose goals. No sensing-noise analysis that I could find.
3. **CityWalker** (arXiv 2411.17820) [snippet]: states sensitivity to GPS error as a limitation and does not measure it.
4. **ViKiNG** (Shah & Levine, RSS 2022, arXiv 2202.11271): treats GPS and maps as unreliable heuristics by design. It is a different architecture (planner plus heuristic) and has no transfer-gain measurement.
5. **GeNIE** (arXiv 2506.17960) [snippet]: won ERC at ICRA 2025 with SAM2 traversability plus path fusion toward the GPS goal. It is a modular system, not an analysis of how noise passes through a learned policy.
6. **Learning to Navigate Sidewalks in Outdoor Environments** (arXiv 2109.05603) [snippet]: reports that GPS delays and noise broke waypoint switching. Classical stack.
7. **Earth Rover Challenge** (earth-rover-challenge.github.io) [snippet]: its 15 m tolerance is a workaround, not a measurement.
8. **SidewalkBench** (arXiv 2606.16953) [snippet]: benchmarks 9 navigation models in simulation, with no sensing-noise axis that I could see.

**New:** (a) the first measured position-versus-heading decomposition of goal-sensing error for a learned GPS-conditioned policy, on the authors' own platform; (b) the offline goal-error transfer gain and a check that it predicts closed-loop error; (c) evidence that the rover's onboard receiver, given RTK corrections, can replace the external GPS the authors used, at no hardware cost.

### Experiment design (baseline = authors' released policy and logic on the authors' robot family)
- **Platform:** EarthRover Mini+ with LogoNav (released weights, MAX_v 0.3 m/s, 3 Hz, 30 m clip, bug-fixed). Policy runs on the laptop.
- **Routes:** 6 fixed sidewalk routes of 60–150 m on a school or park campus. 4 have open sky; 2 run beside buildings or near cars, where the magnetometer and multipath are bad. Endpoints are surveyed with RTK, each route has 1–3 waypoints, and the rover always starts from the same marked pose.
- **Part 1, a 2×2 within-route factorial.** Position source {stock SDK GPS, RTK} × heading source {stock SDK orientation, fused gyro+COG+mag}. RTK + fused stands in for the authors' external GPS. Six routes × 3 repetitions × 4 conditions gives **72 runs**, with condition order randomized within each route block.
- **Part 2, dose-response (closed loop).** Starting from RTK + fused, inject a constant heading bias b ∈ {0°, 10°, 20°, 35°} plus a matched-variance random-walk position error, with magnitudes taken from logged stock-versus-RTK statistics. 2 routes × 4 repetitions × 4 levels gives **32 runs**.
- **Part 3, offline transfer gain.** Replay about 20k logged frames from the runs through LogoNav with goal vectors rotated by −40°…+40° and scaled by 0.5…1.5. Measure the rotation of the predicted waypoint heading. Free, and many samples.
- **Sample size.** The primary outcome is continuous: final distance to the goal (m), with path-length ratio as co-primary. I assume a pilot SD of about 4 m. The paired within-block design with 18 runs per cell detects d ≈ 0.7 (about a 2.8 m difference) at α = 0.05 with 80% power (paired t, n = 18). The analysis is a linear mixed model with route as a random effect, which has more power than the paired t. For Part 2, regressing error on |b| with 32 runs detects a slope of 0.1 m/° with power above 0.9 if residual SD is ≤ 3 m (estimate). Field time is about 104 runs × ~4 min ≈ 7 h plus resets, spread over 4–5 weekend sessions.

### Measurements and analysis
Logged at 3 Hz: SDK fix, RTK fix and fix-quality flag, SDK heading, fused heading, RTK course-over-ground (ground-truth heading while moving above 0.15 m/s), commanded v/ω, predicted waypoints, interventions, collisions. Metrics: final goal error; path-length ratio against the RTK straight-line or waypoint path; mean absolute cross-track error; interventions per 100 m; success at 3 m and 15 m (the ERC tolerance) with Wilson CIs. Analysis: mixed-model ANOVA for the 2×2 (main effects and interaction); dose-response slope; transfer gain from Part 3 compared with the closed-loop slope from Part 2. Also an error budget: the share of the stock-versus-RTK+fused gap explained by the heading factor and by the position factor.

### Build list (≤ $1,000; free compute)
| Item | Cost | Status |
|---|---|---|
| EarthRover Mini+ | $199–299 | listing snippet says "$199 (retail $299)" (verify at checkout) |
| Any FrodoBots SDK/data access fee | $0–?/mo | **unknown, ask the vendor before ordering**; fallback is the documented local WiFi/adb control |
| Waveshare LC29H(DA) GNSS board (external RTK fallback) | ~$45–60 | estimated |
| ESP32 dev board + LiPo + cables | ~$25 | estimated |
| Spare 18650 cells + charger | ~$35 | estimated |
| PETG for antenna mast / mounts | ~$25 | estimated |
| Cones, chalk, 30 m tape | ~$30 | estimated |
| Phone hotspot data (NTRIP, about 1 MB/min) | $0 (existing phone) | estimated |
| CRTN NTRIP corrections | $0 | free with registration [snippet] |
| Contingency | ~$100 | — |
| **Total** | **~$490–610** | |

Compute: LogoNav is a small EfficientNet-B0 + transformer/diffusion head at 96×96 input and runs on a laptop CPU or GPU at 3 Hz (my estimate; to check in week 1). No training needed.

### Timeline (Oct 2026 – Feb 26 2027)
| Week | Hardware student | Software student |
|---|---|---|
| Oct 12–18 | Confirm the vendor's SDK and data terms; order rover + GNSS board | Run LogoNav offline on the sample frames; fix the `goal_pose` bug |
| Oct 19–25 | Register for CRTN; survey candidate routes | Telemetry and frame logger via the SDK; check the policy runs at 3 Hz |
| Oct 26–Nov 1 | (rover arrives) assembly, antenna mast print | First tele-op drives; log the stock GPS/heading rate and quantization |
| Nov 2–8 | adb into the rover; read LC29HDA NMEA through the wiki commands | Heading EKF (gyro + COG + mag) offline on logs |
| Nov 9–15 | RTCM relay into the onboard LC29HDA (`str2str`) **or** build the external LC29H+ESP32 fallback | Goal-perturbation harness, offline replay |
| Nov 16–22 | Survey route endpoints with RTK; mark start poses | Stock LogoNav pilot runs (n ≈ 6) → SD for the power check |
| Nov 23–29 | Field logistics, battery swaps | Part 3 offline transfer gain on pilot logs |
| Nov 30–Dec 6 | Part 1 runs, routes 1–3 | Online fused-heading condition integrated |
| Dec 7–13 | Part 1 runs, routes 4–6 | Data QA, first mixed model |
| **Dec 14–20** | Part 1 complete (72 runs) | **First data: 2×2 result** |
| Dec 21–Jan 3 | Break / buffer re-runs | Error budget figures |
| Jan 4–10 | Part 2 dose-response runs | Injection code online |
| **Jan 11–15** | **Go/no-go:** is the Part 1 effect size known? Is Part 2 half done? | Same |
| Jan 16–31 | Part 2 complete; optional OmniVLA-edge replication on 2 routes | Transfer gain versus closed-loop comparison |
| Feb 1–14 | Re-runs of failed or invalid trials; **data freeze Feb 14** | Stats, figures |
| Feb 15–26 | Photos, hardware appendix | Write paper; submit ~Feb 26 |

### Roles
- **Hardware:** GNSS integration (onboard RTCM path or external board), antenna mast, wiring and power, route survey, all field operation and safety, magnetometer-disturbance mapping of routes.
- **Software:** logger, bug-fixed baseline, EKF, perturbation harness, offline replay, mixed-model statistics, figures.

### Main risk and fallback
- **Risk 1: vendor dependence.** The SDK needs a FrodoBots token and the rover uses 4G. Fallback: the documented local WiFi AP plus adb root and the open UART protocol, with frames taken from the onboard sample code. **Check this before ordering.**
- **Risk 2: RTCM injection into the onboard module fails**, because the host binary is closed. Fallback: the external LC29H(DA) board is the "RTK" condition. It is the same chip, so the comparison stays clean.
- **Risk 3: LogoNav behaves badly on the Mini+** (it was trained mostly on ERZ-type data, and the camera sits lower). A degenerate stock baseline is itself a finding. Fallback: OmniVLA-edge.
- **Risk 4: rainy December.** Spread runs across weekends and bank Part 3 offline data early.

### Best venue
IEEE CASE 2027 or IROS 2027 (both due Mar 1). The fallback is an ICRA 2027 workshop on navigation foundation models or field robotics.

### Lab appeal
- **Best fit: UCSC Autonomous Systems Lab (Gabriel Elkaim).** GNC and sensor fusion on low-cost ground robots, with a stated goal of reducing autonomy cost through open source (https://asl.soe.ucsc.edu/research). Their SIP 2024 project was a GNC framework for ground vehicles, and SIP 2026 ran Pi + ROS 2 + Nav2 (https://sip.ucsc.edu/2026-research-projects/). What they gain: a heading/GNSS fusion problem in front of a learned policy, a $300 open platform for future SIP interns, and an easy co-advised project.
- **Second: UC Merced (Carpin).** Outdoor ROS 2 navigation (ICRA 2024 costmap paper). They gain evidence on how much localization quality matters for learned outdoor navigators.
- **Third: Kobayashi (UCSC SIP 2026 UGV traversability).**

### Honest self-score
- **Novelty 6.5:** The transfer-gain framing and the position/heading decomposition on the authors' own platform look new. But "better GPS → better navigation" sounds obvious, and reviewers may see it as a careful ablation rather than a new method.
- **Feasibility 7:** No training. Cheap hardware. Data needs only weekend field runs. The real risks are vendor access and RTCM injection, both with fallbacks, plus winter weather.
- **Impact 6.5:** Directly useful to Earth Rover Challenge teams and to anyone deploying LogoNav, OmniVLA or CityWalker. A strong workshop or solid CASE paper, probably not one that gets cited widely.
- **Overall ≈ 6.67.**

---

## IDEA M2: Recalibration is a distribution shift. How fragile are LeRobot policies to a routine SO-101 recalibration, and which known fix holds up?

### Base project and the specific limitation
- **Base:** Hugging Face LeRobot with the SO-101 arm (TheRobotStudio/SO-ARM100, Apache-2.0; `huggingface/lerobot`, Apache-2.0) and its default ACT and SmolVLA policies.
- **Limitation (code-verified).** In `so_follower.py`, calibration asks the user to *"Move … to the middle of its range of motion"*, then to sweep each joint through its range. In `motors_bus.py`, DEGREES mode normalizes a reading as `(val − mid)·360/max_res` with `mid = (range_min + range_max)/2`. **The joint's zero angle is therefore the midpoint of however far that person swept the joint.** A different sweep, a different person or a different arm gives a shifted joint frame. Policies take absolute `observation.state` as input and output absolute joint targets by default. [code]
- **Recalibration happens often.** LeRobot issue #1360, "Homing offset not taken into account during calibration": users must recalibrate SO-100 arms after each power disconnect (closed "not planned") (https://github.com/huggingface/lerobot/issues/1360). Community datasets pooled for SmolVLA pretraining come from many independently calibrated arms. SmolVLA's own write-ups note dataset heterogeneity [snippet].
- **Folk claims, not measurements.** A practitioner guide says policies can fail "completely" on another unit because of "robot joint calibration differences between units" [snippet, roboticscenter.ai]. The SO-101 VLA benchmark (arXiv 2606.08881) lists "imperfect calibration" among stochastic perturbations [snippet] but, as far as I can tell, does not isolate it.

### Research question
How large are real SO-101 recalibration frame shifts, how much do they degrade ACT (and SmolVLA) placement accuracy, and which existing representation fix restores performance without losing precision: relative actions, episode-relative state, state-free input, or frame-shift augmentation?

### Why the outcome is uncertain
- **Result A: robust.** With a wrist camera, ACT closes the loop visually, and a 2–5° frame shift is corrected. Then "recalibrate freely" becomes a measured fact, and pooling community datasets without calibration harmonization is safe.
- **Result B: fragile.** Policies overfit proprioception (the "state shortcut" of arXiv 2509.18644 [snippet]), so a few degrees of frame shift moves the gripper by centimetres. Here the fixes compete: state-free input generalizes but loses precision (as that paper's own trade-offs suggest); relative actions still see an absolute state; episode-relative frames (arXiv 2605.13067 [snippet]) cancel constant offsets exactly but may hurt tasks that depend on absolute pose.

Which fix wins is not derivable on paper.

### The non-obvious insight
A recalibration offset is a **constant shift of the joint frame that is visible in the image but not in the state**. It is the cleanest real-world probe of how much a policy trusts proprioception over vision. It can be injected *exactly* by editing the calibration file, with no confounds from lighting or object placement. One more point: of the fixes, only **episode-relative encoding** is mathematically invariant to a constant offset (subtracting s₀ removes δ). Relative actions are not invariant, because the state input still carries δ. We test whether that theoretical invariance survives joint limits, gravity sag under the soft P=16 gain [code: `position_p_coefficient: int = 16`] and gripper normalization (RANGE_0_100 scales with the swept range).

### Open-source reuse
| Component | Link | License | Saves |
|---|---|---|---|
| SO-101 arm (CAD, BOM) | github.com/TheRobotStudio/SO-ARM100 | Apache-2.0 | Whole robot design |
| LeRobot record/train/eval, ACT, SmolVLA | github.com/huggingface/lerobot | Apache-2.0 | All learning code |
| `RelativeActionsProcessorStep` (already in LeRobot) | lerobot `src/lerobot/processor/relative_action_processor.py` | Apache-2.0 | Fix R1 for free |
| SmolVLA base weights | HF `lerobot/smolvla_base` | Apache-2.0 | VLA arm of the study |
| Community SO-100/101 datasets on HF Hub | huggingface.co/datasets?other=LeRobot | per dataset | Heterogeneity audit, no robot time |
| OpenCV ArUco | opencv.org | Apache-2.0 | Placement-error measurement |

**Team builds:** (1) a calibration-offset injector (edits `MotorCalibration` ranges by ±δ); (2) an episode-relative processor step (subtract s₀; about 40 lines, modelled on the existing relative-action step); (3) frame-shift augmentation, adding a random constant δ to state and action jointly during training; (4) a printed fixture, overhead ArUco rig and target board for millimetre placement error; (5) a Hub-audit script (first-frame joint distributions across about 200 SO-100/101 datasets).

### Closest prior work and what is new
1. **"Do You Need Proprioceptive States in Visuomotor Policies?"** (arXiv 2509.18644) [snippet]: state-free policies generalize spatially better. Its perturbation is object and scene position, not calibration frames.
2. **"When Absolute State Fails: Evaluating Proprioceptive Encodings for Robust Manipulation"** (Alvarez et al., ICRA 2026 WS, arXiv 2605.13067) [snippet]: proposes episode-wise relative frames for *mobile carriages and rails*. It is the closest prior work. It did not test calibration shifts, low-cost servo arms or VLAs.
3. **GeoProp** (arXiv 2607.07101) [snippet]: grounds the state in image features. It targets fusion quality, not robustness to frame shift.
4. **UMI** (Chi et al., RSS 2024): relative trajectory actions. A different embodiment.
5. **SO-101 VLA benchmark, failure and recovery** (arXiv 2606.08881) [snippet]: names imperfect calibration as one perturbation among many but does not isolate it.
6. **LeRobot relative actions** (code above): a fix that exists, apparently without a published evaluation.

**New:** (a) the first measured distribution of real recalibration shifts (people × repeats × units) for the most widely used low-cost learning arm, plus a Hub-wide audit; (b) a dose-response for policy accuracy under exact frame-shift injection; (c) a head-to-head of four existing fixes plus frame-shift augmentation under this perturbation, checking theoretical invariance against servo realities.

### Experiment design
- **Baseline (the original team's setup):** LeRobot default ACT (absolute joints, front + wrist camera, 50 demos, default hyperparameters) on an SO-101 calibrated per the official guide.
- **Step 1, real shift distribution (weeks 3–4).** 5 people × 3 calibrations × 2 follower arms = 30 calibrations. For each, command a fixed set of 5 joint configurations and measure gripper-tip position with the overhead ArUco rig, then solve for per-joint offsets. Output: p50 and p95 of |δ| per joint. Hub audit in parallel.
- **Step 2, training.** One precision pick-and-place task (cube to a 3 cm target), 60 demos. Train 4 ACT variants: R0 absolute (baseline), R1 relative actions, R2 episode-relative state + action, R3 frame-shift augmentation. Add R4 state-free if Kaggle time allows. SmolVLA fine-tune (R0 vs R2 only) as a secondary.
- **Step 3, evaluation.** Offset level ∈ {0, p95, 2×p95}, each with a random joint-direction vector from a fixed seed. 4 variants × 3 levels × 15 trials = **180 trials** at about 1.5 min each, about 5 h. Then a cross-unit check: the baseline and the best fix run on arm #2 with its own real calibration (2 × 20 trials).
- **Sample size.** The primary outcome is continuous placement error (mm). Assuming SD ≈ 12 mm, 15 trials per cell detects a 13 mm between-cell difference (d ≈ 1.1, two-sample, α = .05, power .8). Factor effects are pooled across cells in a two-way model (variant × level, 45 trials per marginal level), which detects d ≈ 0.6 marginally. Success rates are reported with Wilson CIs only, never as the inferential claim.

### Measurements and analysis
Placement error (mm), success (≤ 15 mm and grasp held), time to completion, max-jerk proxy, fraction of trials hitting joint limits. Two-way ANOVA / mixed model (variant × offset level, interaction = robustness). Slope of error against |δ| per variant. Precision cost of each fix at δ = 0. Cross-unit transfer gap.

### Build list
| Item | Cost | Status |
|---|---|---|
| SO-ARM101 Pro kit (leader + follower servos, boards) | ~$220–247 | verified [snippet: cnx-software / slickdeals listings] |
| Second follower: 6 × STS3215 + bus board | ~$110–130 | estimated |
| PLA/PETG for 2 arms + fixtures | ~$50 | estimated |
| 3 USB cameras (front, wrist ×2) | ~$75 | estimated |
| 12 V supplies, clamps, cables | ~$40 | estimated |
| ArUco board print, target mats, test objects | ~$25 | estimated |
| Contingency | ~$100 | — |
| **Total** | **~$620–670** | |

Compute: ACT trains on free Kaggle (2×T4, 30 h/week) in about 2–4 h per variant (estimate); SmolVLA fine-tuning about 6–10 h on Kaggle (estimate, the main compute risk).

### Timeline
| Week | Hardware | Software |
|---|---|---|
| Oct 12–25 | Order kit and servos; print parts | Install LeRobot; read the calibration code; write the injector |
| Oct 26–Nov 8 | Assemble 2 followers + leader; camera mounts | ArUco rig software; Hub audit script |
| Nov 9–22 | Calibration study (30 calibrations) | Solve offsets; p50/p95 |
| Nov 23–Dec 6 | Record 60 demos | Episode-relative step and augmentation; train R0–R3 |
| **Dec 7–20** | Eval at offset 0 and p95 (R0, R2) | **First data: baseline dose-response** |
| Dec 21–Jan 3 | buffer | Train SmolVLA R0/R2 on Kaggle |
| Jan 4–15 | Complete 180-trial grid | Analysis; **go/no-go Jan 15** |
| Jan 16–Feb 7 | Cross-unit trials on arm #2; SmolVLA eval | Stats, figures |
| Feb 8–14 | Re-runs; **freeze** | Freeze |
| Feb 15–26 | Figures, CAD appendix | Write; submit |

### Roles
- **Hardware:** builds both arms, the calibration-study protocol and fixtures, the ArUco rig, the target board; runs all trials.
- **Software:** injector, processors, training on Kaggle, Hub audit, statistics.

### Main risk and fallback
- **Risk: Result A with a tiny effect.** If ACT is robust at real p95 shifts, the paper turns into the measured shift distribution plus the Hub audit plus the 2×p95 stress test plus the precision cost of each fix. That is a smaller, still useful workshop result.
- **Risk: SmolVLA does not fit free compute.** Drop it to "future work."

### Best venue
ICRA 2027 workshop (low-cost / open-source manipulation, data for robot learning) is realistic. CASE 2027 main track is a stretch.

### Lab appeal
- **Best fit: UCLA LEMUR (Ankur Mehta).** Cheap printable robots ("Towards One-Dollar Robots," Robotica 2020, https://uclalemur.com/publications). Calibration robustness is the practical barrier for their kind of cheap hardware. What they gain: a measured robustness recipe for learning on imprecise cheap arms.
- **Second: Sanfelice (UCSC SIP 2026 manipulator obstacle avoidance)**, through SIP.
- Honest note: none of the reachable labs is a manipulation-learning group, so engagement will be lighter than for M1.

### Honest self-score
- **Novelty 5.5:** The perturbation and the measured shift distribution are new, but every fix is prior work. The closest paper (2605.13067) already argues for episode-relative frames, which makes this a careful evaluation in a new setting.
- **Feasibility 8:** One cheap arm, exact software injection, mostly continuous metrics, standard LeRobot pipeline. Data by Dec 20 is realistic.
- **Impact 6:** Thousands of SO-100/101 users and pooled community datasets make it practically relevant, but the audience is mostly LeRobot practitioners.
- **Overall ≈ 6.5.**

---

## IDEA M3: Does the leader arm teach bad habits? Detents, friction and resolution of the SO-101 leader versus an open magnetic-encoder leader PCB

### Base project and the specific limitation
- **Base:** the SO-101 leader arm (TheRobotStudio/SO-ARM100, Apache-2.0), which uses STS3215 servos with lower gear ratios as joint encoders, and LeRobot's leader–follower recording.
- **Limitation:** LeRobot issue #2074, "SO-101 leader precision". When back-driving the leader, joints *"lock into approximately 29 distinct positions per revolution,"* snapping into detents even when unpowered. The user notes programmatic control is "much higher precision." Closed as **not planned** (https://github.com/huggingface/lerobot/issues/2074; summary read via github.com). Related: issue #1333, wrist_roll instability during teleop (title only). **Caveat:** this rests on one report. Week 1 must confirm it on our own leader by logging a slow constant-speed sweep and histogramming joint positions. If there is no clustering, the idea becomes a general friction and resolution study (see Risk).

### Research question
Does the leader's mechanical fidelity (detents, friction, resolution) measurably change demonstration quality and the precision and smoothness of the ACT policy trained on it, compared with a detent-free magnetic-encoder leader of identical kinematics?

### Why the outcome is uncertain
- **Result A: fidelity matters.** Detents quantize and stick-slip the action labels, ACT learns jerky, biased targets, and placement precision suffers. The fix is a ~$40 PCB.
- **Result B: it does not, or the opposite.** Friction and detents act as *damping and virtual fixtures*. They suppress operator tremor, and the smoother-feeling encoder leader yields *noisier* demos. ACT's chunking and CVAE also smooth label noise, so policy precision is unchanged.

Both are publishable. B would be counter-intuitive and tells the community not to over-engineer leaders.

### The non-obvious insight
The leader is part of the *data-generating process*, and its mechanics shape the action distribution the policy imitates. Friction is not simply a defect: in human motor control, damping reduces tremor. The study separates **label quantization** (resolution and detents) from **operator damping** (friction) by giving the encoder leader an adjustable friction collar. That 2×2 is what turns a hardware swap into a finding.

### Open-source reuse
| Component | Link | License | Saves |
|---|---|---|---|
| SO-101 leader CAD (kinematics copied exactly) | github.com/TheRobotStudio/SO-ARM100 | Apache-2.0 | Linkage design |
| LeRobot teleop/record/ACT | github.com/huggingface/lerobot | Apache-2.0 | All learning code. A new `Teleoperator` subclass is small (pattern of `so_leader`) |
| AS5600 Arduino/RP2040 libraries | e.g. github.com/RobTillaart/AS5600 | MIT | Encoder driver |
| GELLO (design pattern for passive leaders) | github.com/wuphilipp/gello_software | MIT | Reference for passive-leader design |
| KiCad + JLCPCB | kicad.org | GPL | Board design and fab |

**Team builds:** a small KiCad carrier board (RP2040 + I²C mux + 6 × AS5600 breakouts, USB), a printed leader with bearings and diametric magnets on each joint, an adjustable friction collar, a LeRobot `Teleoperator` driver that emits the same joint-name dictionary as `so_leader`, and the demo-quality metrics.

### Closest prior work and what is new
1. **"How to Train Your Robots?"** (arXiv 2503.07017) [snippet]: compares kinesthetic, VR and SpaceMouse demonstrations and their downstream learning. That is *between* modalities, not leader mechanical fidelity.
2. **"Static Is Not Enough: VR vs SpaceMouse"** (arXiv 2601.13042) [snippet]: interface comparison, again across modalities.
3. **GELLO** (Wu et al., 2023; github.com/wuphilipp/gello_software): low-cost passive leaders. Not evaluated for fidelity effects on policies.
4. **Data quality in imitation learning** (Belkhale et al., NeurIPS 2023, "Data Quality in Imitation Learning"): defines action divergence and state diversity metrics, which we reuse. Not about teleoperation hardware.
5. **Low-cost bilateral force feedback** (arXiv 2507.06174, 2509.08226) [snippet]: changes the leader by adding force. Orthogonal.
6. **ALOHA 2** (Aldaco et al., 2024): reports improved leader ergonomics (my recollection; not re-verified in this sandbox). No controlled fidelity ablation that I know of.

**New:** a controlled 2×2 (quantization × friction) on identical kinematics, with downstream ACT precision as the outcome, plus an open encoder-leader PCB for the most common low-cost arm.

### Experiment design
- **Baseline:** stock SO-101 leader, LeRobot default ACT.
- **Conditions:** stock leader (detents + friction) | encoder leader, low friction | encoder leader + friction collar tuned to match the stock leader's measured breakaway torque (spring-scale measurement). Optional fourth cell: encoder output software-quantized to 29 positions per revolution, which isolates quantization.
- **Operators:** 2 (the two students), counterbalanced (ABCCBA) to cancel learning effects. 40 demos per operator per condition gives 3 × 80 = **240 demos**, about 6 h.
- **Policies:** one ACT per condition (pooling both operators), 3–4 policies on Kaggle.
- **Evaluation:** a precision placement task (peg onto a 6 mm-clearance post, or cube onto a 2 cm target). 25 trials per policy, about 100 trials.
- **Sample size.** Demo-level metrics have n = 80 per condition and detect d ≈ 0.45. Policy placement error with 25 trials per arm detects d ≈ 0.8 (α = .05, power .8). Within-condition seed variance is checked by training 2 seeds of the baseline.

### Measurements and analysis
Demonstration: label resolution (unique values per joint), spectral power of action labels from 4–12 Hz (tremor band), mean squared jerk, demo duration, leader-to-follower tracking error. Policy: placement error (mm), success, action jerk at rollout, time to completion. Analysis: one-way ANOVA across conditions with planned contrasts (quantization contrast; friction contrast); mediation-style check of whether demo jerk predicts policy error.

### Build list
| Item | Cost | Status |
|---|---|---|
| SO-ARM101 kit (shared with any SO-101 work) | ~$220–247 | verified [snippet] |
| 6 × AS5600 breakouts + diametric magnets | ~$25 | estimated |
| RP2040 board (or bare RP2040 on own PCB) | ~$6–10 | estimated |
| PCB fab + assembly parts (JLCPCB, 5 boards) | ~$30–60 | estimated |
| Bearings (6–12 × 6800/608) | ~$20 | estimated |
| Filament | ~$30 | estimated |
| Spring scale / luggage scale (breakaway torque) | ~$15 | estimated |
| Cameras (2) | ~$50 | estimated |
| Contingency | ~$80 | — |
| **Total** | **~$480–590** | |

### Timeline
| Week | Hardware | Software |
|---|---|---|
| Oct 12–18 | Order kit and encoders | LeRobot install; **detent test on stock leader** (position histogram) |
| Oct 19–Nov 8 | Assemble SO-101; CAD encoder leader (same DH); KiCad board | Teleoperator driver skeleton; demo-metric scripts |
| Nov 9–15 | **PCB order by Nov 15**; print leader | Test driver with breakout boards |
| Nov 16–29 | Assemble encoder leader + friction collar; measure breakaway torque | Integrate with `lerobot-record` |
| Nov 30–Dec 20 | Demo collection (240) | Train ACT ×3–4; **first demo-quality data by Dec 20** |
| Dec 21–Jan 15 | Policy evals (100 trials) | Analysis; **go/no-go Jan 15** |
| Jan 16–Feb 14 | Re-runs, seed check; **freeze** | Stats, figures |
| Feb 15–26 | PCB/CAD release | Write; submit |

### Roles
- **Hardware:** detent and breakaway characterization, encoder leader CAD, KiCad board, friction collar, assembly, demo collection.
- **Software:** firmware (RP2040 USB serial), LeRobot driver, metrics, training, statistics.

### Main risk and fallback
- **Risk: the detent claim does not reproduce on our leader.** The study still runs as friction × resolution (the stock STS3215 leader reads 4096 counts per revolution through gears with backlash, against direct-drive AS5600 with no backlash). The headline weakens.
- **Risk: operator learning confounds conditions.** Mitigated by counterbalancing and practice demos before recording.
- **Risk: the PCB slips.** Breakout boards on perfboard work for the study, and the PCB becomes the release artifact.

### Best venue
ICRA 2027 workshop (low-cost robot learning / data collection). CASE 2027 is unlikely.

### Lab appeal
- **Best fit: SJSU Winncy Du (sensors and mechatronics).** A sensor-design study with a human-in-the-loop outcome (lab overview in ../labs.md). Gains: a student mechatronics project with a clear evaluation protocol.
- **Second: UCLA LEMUR (Mehta).** Cheap printable electromechanical design.
- Honest note: neither lab works on imitation learning.

### Honest self-score
- **Novelty 5.5:** A within-modality fidelity ablation looks unstudied, but "better teleop hardware gives better data" is an intuitive hypothesis. The damping twist is the only non-obvious part.
- **Feasibility 7:** Simple hardware, but 240 demos plus a PCB plus operator counterbalancing is real work. The base evidence is a single issue report.
- **Impact 5.5:** Useful to SO-101 users and an open hardware artifact, but narrow. Workshop level.
- **Overall ≈ 6.0.**

---

## Ranking summary
1. **M1: Goal-pose sensing for LogoNav/OmniVLA on EarthRover (RTK unlock + heading fusion).** N 6.5 / F 7 / I 6.5 → 6.67.
2. **M2: SO-101 recalibration frame shift versus proprioceptive encodings.** N 5.5 / F 8 / I 6 → 6.5.
3. **M3: Leader-arm fidelity (detents/friction) versus an encoder-leader PCB.** N 5.5 / F 7 / I 5.5 → 6.0.

**Searches I could not do:** a direct "cited-by" listing for MBRA and CityWalker on Semantic Scholar or Scholar (blocked). The follow-ups I found by keyword (OmniVLA, GeNIE, S2E 2507.22028, "Data Scaling for Navigation in Unknown Environments" 2601.09444, SidewalkBench) do not address goal-sensing noise as far as their snippets show. Before writing, the team should run Scholar "cited by" on 2505.05592 and 2411.17820.
