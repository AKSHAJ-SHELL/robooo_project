# Round 3, generator F: "Something other researchers will reuse"

Date: 2026-10-04. Strategy: the main contribution is a test, a measurement method or a validated number that other labs would adopt, and it must include at least one empirical result that could come out either way.

**How links were checked.** Direct page fetches (WebFetch and curl to arXiv, NCBI, OpenAlex and Semantic Scholar) are blocked by this sandbox's egress proxy. Every prior-work item below was found and read through web-search retrieval (extended mode, which reads the page), not opened in a browser. Titles, authors and venues come from those retrieved pages. I list nothing I did not retrieve. Before citing, a reviewer or mentor should click each link once.

---

## Candidates considered and killed (8 of 11)

| # | Candidate | Why it was killed |
|---|---|---|
| K1 | Magnetometer heading error over rebar driveways vs. sensor height | Predictable: dipole field decay settles the height trend on paper. Overlaps round-2 P5 (Hall sensors on rebar). Low adoption. |
| K2 | Robot-measured ADA curb-ramp audit vs. manual and Street View audits | Close prior work: mobile-lidar ADA assessment ([Ai & Tsai, TRR 2016](https://aichengbo.com/wp-content/uploads/2016/12/J_TRR_2016_LiDARSidewalk_Manuscript.pdf)), the Caltrans point-cloud ramp project ([task 4568](https://dot.ca.gov/-/media/dot-media/programs/research-innovation-system-information/documents/research-notes/task4568-rns-05-26-a11y.pdf)), the commercial ULIP profiler, and Project Sidewalk vs. government data ([Askari et al. 2025](https://makeabilitylab.cs.washington.edu/media/publications/Askari_ValidatingPedestrianInfrastructureDataHowWellDoStreetViewImageryAuditsCompareToGovernmentFieldData_UrbanSci2025.pdf)). A robot viewpoint would only make it a "cheaper" version. |
| K3 | Sunlight-degradation model for $70–120 2D lidars and ToF sensors | [A comparative study of multiple 2D laser scanners outdoors](https://www.researchgate.net/publication/370315322_A_Comparative_Study_of_Multiple_2D_Laser_Scanners_for_Outdoor_Measurements) already exists. The SNR-vs-ambient-light physics is predictable, and the headline would be "cheap sensors". |
| K4 | Consumer RTK (F9P) as ground truth: wrong-fix audit with a rotating-baseline rig | Rotating-arm GNSS test rigs already exist ([PolyU trajectory-constrained rig](https://research.polyu.edu.hk/en/publications/development-of-a-trajectory-constrained-rotating-arm-rig-for-test/); the Czech [Measurement Robotic Arm](https://dspace.emu.ee/items/bf2e0dca-4fcd-4654-8f7b-eac08b32a55c)). Overlaps the explored "RTK on driveway" ideas. |
| K5 | Field validation of the Cornell Robotability Score in California suburbs | Close to the original paper, which already did physical deployments ([CHI 2025](https://robotability.cornell.edu/)). Pedestrian-adjacent data on public sidewalks raises human-subjects and safety problems. |
| K6 | Standard object set for pushing wheeled carts | The area is active (e.g. [Combining Planning and Diffusion for Mobility with Unknown Dynamics](https://arxiv.org/html/2410.06911)), but the work needs a mobile manipulator, and it is unclear any lab would adopt the set. |
| K7 | Dew and condensation on robot sensors at 20–40 cm height | A heat-balance model mostly predicts whether a heater works. Narrow audience. Automotive sensor-soiling work covers the mitigation side. |
| K8 | Camera height/pitch sensitivity of navigation foundation models | Just done: [CanonNav (2026)](https://arxiv.org/html/2608.30242) and [Can Vision Foundation Models Navigate? (2026)](https://arxiv.org/html/2603.25937v2). |
| (K9) | Residential driveway and apron geometry survey plus a 3DEP DEM predictor | DEM road-grade accuracy is already known (Georgia Tech reports about 0.5% RMSE on local roads), so the predictor result is foreseeable. The bin-specific impact ceiling matches what earlier reviewers penalized. |

**Survivors (written up below):** F1, outdoor-trial variance components; F2, a turf slope-traction test; F3, sim-to-real calibration of falsification.

---

## F1. How much of an outdoor navigation result is the day it was run? Variance components and rank stability of field navigation trials

**Research question.** In outdoor ground-robot navigation trials, what fraction of the variance in standard metrics comes from the session (day and time), the site, the robot unit and the individual trial? How often does a single-session comparison of two navigation stacks pick the wrong winner?

**Who benefits and how much.** Anyone who reports outdoor navigation results with n = 5–30 trials from one or two outings. All of the following would have used a measured session-level intraclass correlation (ICC) and design effect to size and report their experiments:
- [Sani, Sgorbissa & Carpin, "Improving the ROS 2 navigation stack with real-time local costmap updates for agricultural applications", ICRA 2024](https://sites.ucmerced.edu/files/scarpin/files/documents/carpincvonline.pdf) (Nav2 outdoors; CV link)
- ViNT and NoMaD field deployments ([ViNT, CoRL 2023](https://arxiv.org/pdf/2306.14846v2))
- [Can Vision Foundation Models Navigate? Zero-Shot Real-World Evaluation (2026)](https://arxiv.org/html/2603.25937v2), which evaluates GNM, ViNT, NoMaD, NaviBridger and CrossFormer on two robots
- [One year in a forest (2026)](https://arxiv.org/pdf/2608.27628) and [Kilometer-scale navigation in subarctic forests](https://arxiv.org/pdf/2111.13981), long-term field campaigns where the session effect is the confound
- The manipulation-evaluation community already wants this number for navigation: [Kress-Gazit et al., "Robot Learning as an Empirical Science" (2024)](https://arxiv.org/pdf/2409.09491) and [PhAIL (2026)](https://arxiv.org/pdf/2605.29710). PhAIL reports that the modal real-robot VLA paper uses 10–20 trials per condition with no confidence intervals.

**Why the outcome is uncertain.**
- **Result A: the session ICC is small (< 0.05).** Same-day trials are then nearly independent, current practice is defensible, and the paper gives evidence-based trial counts. That is publishable as a reassuring calibration number.
- **Result B: the session ICC is large (> 0.2), and stack rankings flip between sessions.** With m = 20 trials in one session and ICC = 0.2, the design effect 1 + (m − 1)·ICC = 4.8, so 20 trials carry the information of about 4. Most single-outing comparisons would then be pseudo-replicated. That result is publishable and uncomfortable.
- **A second uncertain question:** whether logged covariates (sun elevation, irradiance, wind, surface moisture, temperature) explain the session effect. If they do, labs can control for conditions instead of repeating days. If not, labs have to repeat days.
- **No theory gives the ICC.** It depends on the stack, the metric and the site. Nobody has measured it for outdoor navigation; the search found no such study.

**Non-obvious insight.** Two things are unmeasured and both matter:
1. **The robot unit is a random effect too.** Labs compare stacks on one physical robot and generalize to "the method". Building **two nominally identical units** puts a number on build-to-build variance (tire wear, IMU mounting, motor-controller differences). Nobody reports it.
2. **The same ICC sets the cost of better statistics.** STEP-style sequential tests and PhAIL-style distributional metrics both assume independent trials. Clustering by session breaks that assumption. We test whether these tools keep their nominal error rate when sessions are clustered.

**Closest prior work and what is new.**
1. [Kress-Gazit et al. 2024, Robot Learning as an Empirical Science](https://arxiv.org/pdf/2409.09491): best practices for manipulation-policy evaluation; no variance decomposition by day or site.
2. [PhAIL 2026](https://arxiv.org/pdf/2605.29710): distributional time-to-success metrics on a fixed Franka cell; indoor and single-fixture, with no session or site factor.
3. STEP sequential testing, as described in the search summary of [Kress-Gazit et al.](https://arxiv.org/html/2409.09491v1) ("20–30 real-world trials are insufficient"): assumes i.i.d. trials.
4. [MIRRER (2024)](https://arxiv.org/html/2408.04736): a conceptual framework for iterated, reproduced and replicated robot experiments (NSF and NIST funded), with no outdoor field data.
5. [Lynnerup et al., Survey on reproducibility of deep RL on real robots](https://arxiv.org/pdf/1909.03772): run-to-run variance on robot arms, not field sessions.
6. [Rethink Repeatable Measures of Robot Performance with Statistical Query (2025)](https://arxiv.org/html/2505.08216v1): repeatability measures for robot performance; not outdoor sessions.
7. Long-term visual teach-and-repeat studies (e.g. [Krajník et al. 2017, image features for VT&R](https://robotica.dc.uba.ar/public/papers/krajnik2017image.pdf)): show that appearance change hurts, but report per-condition success, not variance components or the risk of a ranking flip.

**New here:**
- The first measured session, site and unit variance components and ICCs for outdoor navigation metrics.
- The probability that a single-session comparison flips the ranking.
- A check of whether sequential and distributional tests stay valid under clustering.
- A literature audit of how many sessions published outdoor-navigation papers use.
- An open protocol plus a cheap, validated checkpoint ground-truth method.

**Validation design.**
- **Course.** At each site, a 50–70 m route on park paths, a school blacktop edge or lawn (no roads). Four checkpoint gates.
- **Ground truth: checkpoint mats.** A laminated AprilTag grid mat is fixed at each gate, and a downward global-shutter camera on the robot reads lateral and heading offset as it passes. The mats are validated in the lab against a steel rule and calipers, with a target below 5 mm and 0.5°. Final stop error is also measured from a mat.
- **Subjects (three stacks).**
  - S1: Nav2 + AMCL on a prebuilt 2D lidar map.
  - S2: Nav2 + SLAM Toolbox localization mode. This is a close competitor to S1, chosen on purpose because close pairs are where ranking flips matter.
  - S3: NoMaD or ViNT topological navigation from the released visualnav-transformer code, run on the team's laptop on board. It is camera-based, so it should be the most lighting-sensitive.
- **Design.**
  - Two main sites × 14 sessions each, spread over morning, noon and late afternoon, sun and overcast, Nov–Feb.
  - Each session: 2 units × 3 stacks × 4 trials = 24 trials in randomized interleaved order, about 75 min.
  - One held-out third site × 4 sessions tests whether the covariate model transfers.
  - Total: about 32 sessions and about 770 trials.
- **Power.** For a one-way ICC with k = 28 sessions and m = 8 trials per stack per session, Fisher's large-sample SE at ρ = 0.2 is about 0.07, so the 95% CI is about ±0.14. That separates "negligible" (< 0.05) from "large" (> 0.25). The primary metrics are continuous (gate deviation in mm, time to goal), so power does not depend on rare failures. A ranking flip is estimated by bootstrapping over sessions. The rank-flip probability is reported for the S1–S2 pair, whose pooled effect should be small, and for S1–S3.
- **Literature audit** (software student, about 15 h). Code 60 outdoor-navigation papers (ICRA, IROS and RA-L, 2023–2026) for number of sessions and days, trials per condition, CIs and test type.

**Strongest fair baseline.** Current best practice: one session of 20–30 trials analyzed with a CI or with the STEP sequential test, as recommended by Kress-Gazit et al. We do exactly that on every session and report how often it agrees with the pooled multi-session answer. The comparison is to the recommended practice, not a straw man.

**Measurements and analysis.**
- **Metrics.** Gate lateral error, heading error, final stop error, time to goal, interventions and success.
- **Model.** A linear mixed model: stack as a fixed effect; session, site, unit and the session × stack interaction as random effects. Logistic GLMM for success.
- **Covariates.** Sun elevation (computed), lux (BH1750), wind, a soil- or surface-moisture probe and temperature, added as fixed effects to measure how much of the session variance they explain.
- **Key outputs.**
  - Variance components with bootstrap CIs.
  - The design effect.
  - The rank-flip probability.
  - The empirical type-I error of STEP and PhAIL-style tests under clustering, by resampling the real data with no true difference (S1 vs. S1).
  - The recommended number of sessions × trials for a given minimum detectable effect.

**Build list (target ≤ $1,000).** Prices are estimates unless marked verified.

| Item | Qty | Unit cost | Total |
|---|---|---|---|
| Used hoverboard base (reflash with EFeru FOC; check mainboard support) | 2 | ~$60 (est., used) | $120 |
| ST-Link programmer | 1 | ~$10 (est.) | $10 |
| Raspberry Pi 5 8 GB | 2 | ~$95 (est.; check current price) | $190 |
| LD19-class 2D lidar | 2 | ~$80–99 (est.) | $180 |
| Pi Global Shutter camera + 6 mm lens (checkpoint reader) | 2 | ~$75 (est.) | $150 |
| Pi Camera Module 3 (for S3) | 1 | ~$25 (est.) | $25 |
| BNO085 IMU | 2 | ~$25 (est.) | $50 |
| Frames, fasteners, wiring, fuses | 2 | ~$40 (est.) | $80 |
| Laminated AprilTag mats (4 gates + stop) | 5 | ~$12 (est.) | $60 |
| Weather logging (BH1750, cheap anemometer, moisture probe) | 1 | ~$50 (est.) | $50 |
| **Total** | | | **~$915** |

Compute is the team's laptop (S3 inference) plus free Colab for analysis. **Saving lever:** if the bin-robot base already exists, it becomes unit 1, which saves about $250.

**Timeline (Oct 12, 2026 – Feb 26, 2027).**
- **Oct 12–25:**
  - Mechanical: buy parts, flash the hoverboard FOC firmware.
  - Software: Nav2 bring-up in simulation, start the literature audit protocol.
  - Choose sites and get permission.
- **Oct 26 – Nov 15:** both units built and driving. Checkpoint mat plus camera reader working, with lab validation (≥ 30 passes over a calipered offset table).
- **Nov 16–29:**
  - Maps for sites 1–2. S1 and S2 tuned once, then frozen.
  - S3 topomaps recorded.
  - Pilot session: check the time per trial and that reset takes under 1 min.
- **Nov 30 – Dec 20:** sessions 1–8, at both sites, 2–3 per week.
- **By Dec 20:** about 190 trials, a first ICC estimate with a wide CI, a validated ground-truth error budget, and the literature audit half coded.
- **Dec 21 – Jan 14:** winter break, sessions 9–20 (morning, noon, overcast, post-rain). Interim mixed-model analysis.
- **Jan 15 go/no-go:**
  - **Go:** the session SE is on track below 0.1.
  - **Fallback:** drop S3 to raise the number of sessions.
- **Jan 15 – Feb 8:** sessions 21–28. Held-out site 3 × 4 sessions. Literature audit finished.
- **Feb 9–14:** data freeze. Resampling studies (STEP and PhAIL validity under clustering).
- **Feb 15–26:** write-up, release of the dataset, protocol, mat generator and analysis notebook.

**Main risk and fallback.**
- **Risk 1: winter rain and short days cut sessions.**
  - Rain itself is a session condition worth logging.
  - The design works with as few as about 20 sessions (SE about 0.08).
- **Risk 2: S3 is too fragile and success near 0% gives a degenerate ICC.** Fall back to two Nav2 stacks, and add a lidar-odometry-only Nav2 variant.

**Best venue.** IROS 2027 main track, as a methods and evaluation paper with an open dataset. RA-L is the backup. An ICRA 2027 workshop on evaluation or reproducibility is the fallback.

**Lab appeal.**
- **UC Merced, Carpin.** His [ICRA 2024 Nav2 agricultural costmap paper](https://sites.ucmerced.edu/files/scarpin/files/documents/carpincvonline.pdf) evaluates Nav2 outdoors. The lab gains a measured trial-count rule for its own outdoor experiments and a co-authored CASE/IROS methods paper. Cost to the lab: about two advising calls on mixed models.
- **UCSC Autonomous Systems Lab, Elkaim.** His [SIP 2026 CSE-11 project, "Embedded AI and Navigation on a Differential-Drive Robot using Raspberry Pi, ROS 2, and Docker"](https://sip.ucsc.edu/2026-research-projects/) uses the same Pi + ROS 2 + Nav2 stack. The lab gains a ready evaluation protocol and checkpoint-mat tool for future SIP cohorts.
- **Optional third: UCSC, Fremont.** His statistical-testing view of autonomy fits too.

**Link to the bin robot.** The units are bin-robot bases. The garage-to-curb route can serve as a third site (driveway only). The protocol becomes the bin robot's own evaluation method.

**Honest self-score.**
- **Novelty 7:** a new measured quantity (the outdoor-navigation session ICC and rank-flip risk) in an active evaluation-methods debate. The statistics are standard, so the novelty is the data and the finding.
- **Feasibility 6.5:** two robots plus about 32 outdoor sessions is a lot for two part-time students in winter. The fallback design keeps it publishable.
- **Impact 7:** if the ICC is large, every outdoor-navigation paper's trial design is affected and the paper will be cited. If it is small, it is still a reference number, but cited less.
- **Overall about 6.8.**

---

## F2. Does flat-ground pull predict slope capability on living turf? A portable traction test and field-validated slope predictor for small outdoor robots

**Research question.** Across real lawns, does a 2-minute flat-ground drawbar test with the robot's own wheels predict the maximum turf slope a small wheeled robot can climb? How much do wheel type and leaf wetness shift that slope?

**Who benefits and how much.**
- **Robot-mower makers.** Slope ratings are manufacturer-claimed (e.g. Segway Navimow and Lymow pages). Per retailer guidance, they come from "controlled testing on dry, healthy turf" ([Lymow](https://www.lymow.com/blogs/mower-world/robot-mowers-on-hills-slope-ratings-stuck-prevention); [robotmowerspecs](https://robotmowerspecs.com/articles/best-robot-mowers-steep-slopes)). There is no standardized traction-capability test: [IEC 60335-2-107 / ANSI/OPEI 60335-2-107](https://webstore.ansi.org/standards/opei/ansiopei603351072020) is a safety standard.
- **Self-supervised traversability learners** that use traction proxies, e.g. ["How Does It Feel? Self-Supervised Costmap Learning for Off-Road Vehicle Traversability" (Castro et al.)](https://arxiv.org/pdf/2209.10788). They would get a physical ground-truth slope/traction label set.
- **Small-UGV designers choosing wheels** for parks, vineyards and campuses, e.g. Kitts's [modular multi-drive-unit rover, IMECE 2023](https://asmedigitalcollection.asme.org/IMECE/proceedings/IMECE2023/87592/V002T02A002/1195567) and Carpin's outdoor agricultural robots.
- **Kobayashi's** [SIP 2026 ECE-08 terrain traversability (slip, slope) project](https://sip.ucsc.edu/2026-research-projects/).

**Why the outcome is uncertain.**
- **Coulomb theory predicts tan θ_max = DP/W.** DP/W is the peak net traction ratio measured on flat ground. If it holds on turf, a 2-minute flat pull is a slope rating.
- **Turf may break the prediction**, for several reasons:
  - The root mat shears in a way that depends on normal-load direction.
  - Uphill slip lifts the wheel onto grass blades with a wet-leaf lubricating layer.
  - Downhill load transfer unloads the front wheels.
  - Slip-sinkage grows with time on a slope.
- **Result A:** the prediction holds within ±3° across held-out sites. A simple standard test is validated for industry and labs.
- **Result B:** a systematic, wetness-dependent overestimate, e.g. "the flat test says 22°, the robot fails at 15° on dewy turf". This explains the gap between manufacturer ratings and reality. A handheld probe (shear vane plus moisture) may then predict the correction.
- **Both results are publishable, and no model settles this on turf.** Small-wheel terramechanics is validated on sand and soil bins, not living grass.

**Non-obvious insight.** The robot can be its own dynamometer: run the FOC current ramp against a stake and a load cell, with slip from wheel encoders against the taut tether. That makes a field test that needs no single-wheel rig and runs the actual wheel/robot combination at the actual site in 2 minutes. That is what makes many sites, wet and dry, affordable. The open question is whether the flat measurement carries over to slopes.

**Closest prior work and what is new.**
1. [Meirion-Griffith & Spenko, modified pressure–sinkage model for small rigid wheels, J. Terramechanics 2011](https://www.sciencedirect.com/science/article/abs/pii/S0022489811000024), and the follow-up 120-test dilative-soil model ([ISTVS note](https://www.istvs.org/publication-news/2014/1/15/development-and-experimental-validation-of-an-improved-pressure-sinkage-model-for-small-wheeled-vehicles-on-dilative-deformable-terrain)). These cover small wheels on sand and soil only.
2. "A new field single wheel tester", [J. Terramechanics 1996](https://www.sciencedirect.com/science/article/abs/pii/S0022489896000146), and the UC Davis mobile single-wheel tester: tractor-mounted, agricultural tires, not living turf with small robot wheels.
3. [Testbed for slip, sinkage and torque of small rover wheels on granular terrain (Measurement, 2026)](https://www.sciencedirect.com/science/article/pii/S0263224126016453): a lab bench on granular media.
4. Sports-turf traction testing with a studded-disc torque apparatus, including automated testers ([USQ automated turf testing](https://research.usq.edu.au/item/9z518/development-of-automated-turf-testing-equipment-for-playing-surfaces); [Loughborough, Webb 2014](https://dspace.lboro.ac.uk/2134/17262)). This measures shoe-stud rotational traction, not rolling wheels or slope capability.
5. [Experimental comparison of locomotion system performance of ground mobile robots in agricultural drawbar works (2022)](https://www.sciencedirect.com/science/article/pii/S277237552200096X): drawbar on farm soil, no slope prediction on turf.
6. [Nagatani et al., accurate estimation of drawbar pull of wheeled mobile robots (IROS 2009)](https://k-nagatani.org/pdf/2009-IROS-AYA-online.pdf): estimation on loose soil.

**New here:**
- The first test of the flat-to-slope traction prediction on living turf.
- Across held-out sites, wet vs. dry, and several wheel types.
- A portable test protocol a mower lab or manufacturer can copy.
- An open dataset of slip-curve and slope-limit pairs.

**Validation design.**
- **Test robot.** One small differential-drive robot (the bin-robot base or an F1 unit) with ballast set to 15 or 25 kg.
- **Wheels (3 types):** stock solid hoverboard tire, 8" pneumatic turf tire, and a TPU-printed lugged tread designed by the mechanical student.
- **Sites.** 12 lawns with natural slopes of 10–40% in parks and school fields, with permission and no roads. Each site is visited twice: dry (afternoon) and wet (early-morning dew or after irrigation). That gives 24 site-conditions.
- **Per site-condition and wheel:**
  - 3 flat-ground pulls: current ramp against a stake with an S-type load cell and string-pot slip, giving the peak DP/W.
  - 3 straight uphill attempts on the site's slope gradient, measuring the slope at stall. Stall is defined as ground progress below 10% of commanded. The slope at the stall point is measured with a digital inclinometer on a 1 m board, cross-checked with the robot IMU.
  - Probe readings: shear vane, capacitive moisture, a leaf-wetness proxy (paper-towel blot weight) and grass height.
- **About 1.5 h per visit, 24 visits.** Stall attempts are low-speed and tethered from below, so there is no runaway.
- **Power.**
  - **Primary test:** the paired difference θ_measured − θ_predicted per site-condition and wheel. To detect a 3° mean bias with SD 4°, α = 0.05 and power 0.8, a paired test needs n ≈ (1.96 + 0.84)² × 16/9 ≈ 14 units. We have 24 per wheel and 72 total, clustered by site, analyzed with a mixed model and site as a random effect.
  - **Predictive test:** leave-one-site-out RMSE (degrees) of (a) Coulomb from the flat pull, (b) flat pull + wetness, (c) probe-only. A difference in RMSE is judged with a paired bootstrap over sites.

**Strongest fair baseline.**
1. The physics baseline: Coulomb, tan θ = DP/W from the same robot on the same day.
2. The current industry practice, emulated: the slope rating obtained on a dry, artificial-turf-covered plywood ramp (a standard surface any lab can build). It shows how far a lab-ramp rating sits from field reality.

**Measurements and analysis.**
- **Raw data:** slip-traction curves (DP/W vs. slip), stall slope, rolling resistance on flat ground, and the probe covariates.
- **Analysis:**
  - Mixed models with wheel and wetness as fixed effects and site as random.
  - LOSO prediction.
  - A Bland–Altman plot of predicted vs. measured slope.
  - The fraction of site-conditions where the ramp-lab rating overstates field capability by more than 5°.
- **Release:** the test protocol (one page), dataset and STL files for the tread.

**Build list (~$560 on top of an existing base; ~$810 with a used base).** Estimates unless marked verified.

| Item | Cost |
|---|---|
| Load cell + HX711 (SparkFun 200 kg kit, price verified in round 1 final.md) | $101.90 |
| String potentiometer or a 10-turn pot with spool (slip) | ~$35 (est.) |
| Ground stakes, strap, carabiners | ~$25 (est.) |
| 8" pneumatic turf wheels (pair) + hub adapters | ~$60 (est.) |
| TPU filament (treads) | ~$30 (est.) |
| Digital inclinometer + 1 m aluminum board | ~$35 (est.) |
| Turf shear vane (Turf-Tec-type) | ~$150 (est.; check price) |
| Capacitive moisture meter, scale for blot test | ~$35 (est.) |
| Ballast (sandbags) | ~$30 (est.) |
| Plywood ramp + artificial turf (baseline) | ~$60 (est.) |
| **Subtotal** | **~$560** |
| Used hoverboard base, if no bin robot | ~$250 incl. Pi/ESP32 (est.) |

No compute beyond a laptop.

**Timeline.**
- **Oct 12 – Nov 8:**
  - Mechanical: tether and load-cell fixture, wheel adapters, first TPU tread.
  - Software: FOC current-ramp script, logging, slip estimation.
  - Get site permissions (city parks, school).
- **Nov 9–22:** lab validation of the drawbar fixture against hanging weights (≤ 2% error). Ramp baseline built.
- **Nov 23 – Dec 20:** first 6 site visits (3 sites × dry/wet).
- **By Dec 20:** 18 site-condition × wheel cells, a first look at predicted vs. measured slope, and the ramp baseline done.
- **Dec 21 – Jan 14:** 10 more visits over break. Winter dew is reliable in coastal CA mornings.
- **Jan 15 go/no-go:**
  - **Go:** stall measurements repeat within ±2°.
  - **No-go fallback:** switch the slope measure to a tethered constant-slope incline mat placed on the lawn.
- **Jan 15 – Feb 10:** remaining 8 visits, including 2 held-out sites visited last.
- **Feb 11–14:** data freeze.
- **Feb 15–26:** write-up, protocol and data release.

**Main risk and fallback.**
- **Risk 1: hoverboard motors hit the current or thermal limit before the wheels slip** (flagged for B2 in round 1).
  - Bench stall test in October.
  - If the motors are current-limited, add ballast or use a lower gear ratio.
  - On flat ground, pull against the stake until slip with the current limit raised briefly. The EFeru firmware limit is configurable.
- **Risk 2: suitable natural slopes are uneven.** Measure local slope at the stall point (already in the protocol), and treat slope as continuous.

**Best venue.** IEEE CASE 2027 main track (design rule + test method). IROS 2027 if Result B is striking. Journal follow-up: *Journal of Terramechanics* or *J. Field Robotics*.

**Lab appeal.**
- **UCSC, Kobayashi.** His SIP 2026 ECE-08 project, ["Unmanned Autonomous Ground Vehicle Terrain Traversability for Unstructured Environments" (slip, slope, SLAM uncertainty)](https://sip.ucsc.edu/2026-research-projects/), is the same question in a different setting. The lab gains a ground-truth slip/slope dataset and a portable test for future SIP cohorts, at nearly zero cost.
- **Santa Clara RSL, Kitts.** The [modular multi-drive-unit rover (IMECE 2023)](https://asmedigitalcollection.asme.org/IMECE/proceedings/IMECE2023/87592/V002T02A002/1195567) and the RSL agricultural robots need wheel and slope sizing. RSL gains a wheel-selection rule and a test its undergraduates can run.

**Link to the bin robot.** Lawn-edge and sloped-driveway traction is the bin robot's hard case. The same test, run on concrete, asphalt and wet surfaces, gives the robot's own sizing rule.

**Honest self-score.**
- **Novelty 7:** the first held-out-site test of flat-to-slope traction prediction on living turf. The physics framing is classical, but the answer on turf is unknown.
- **Feasibility 7:** a simple rig, one robot, 24 visits. The current-limit risk is known and has a fix.
- **Impact 6.5:** a test method industry and traversability labs can adopt. The audience is narrower than F1's (outdoor small robots and mowers).
- **Overall about 6.8.**

---

## F3. Do simulated counterexamples happen in the real world? Calibrating Scenic/VerifAI falsification of a Nav2 robot against ~300 physical trials

**Research question.** For a ROS 2 Nav2 ground robot, does the robustness value that simulation-based falsification (Scenic + VerifAI) assigns to a scenario predict that scenario's real-world failure probability? Which scenario features break that relationship?

**Who benefits and how much.**
- **Labs that use simulation-based falsification to pick physical tests.** Their whole premise is that sim robustness ranks real risk. That premise has been checked only on a few track tests with a full-size AV ([Fremont et al., ITSC 2020](https://arxiv.org/abs/2003.07739)) and for DNN lane-keeping on a 1:16 Donkey Car ([Stocco, Pulfer & Tonella, "Mind the Gap!", IEEE TSE 2023](https://arxiv.org/pdf/2112.11255)).
- **Users of scenario-based ROS 2 testing tools**, e.g. [Scenario Execution for Robotics (2024)](https://arxiv.org/pdf/2409.07080), which demonstrates Nav2 on TurtleBot4s.
- **Researchers calibrating sim-to-real for low-cost UGVs**, e.g. [Real-to-Sim Calibration and Cross-Domain Trajectory Validation of a Low-Cost Multi-Sensor UGV Digital Twin (Sensors 2026)](https://doi.org/10.3390/s26185729) and [Sim-to-Real Transfer for Mobile Robots with RL: Isaac Sim to Gazebo and Real ROS 2 Robots (2025)](https://arxiv.org/pdf/2501.02902).

All of these would have used a measured calibration curve (sim ρ → P(real failure)).

**Why the outcome is uncertain.**
- **Result A: sim robustness is well calibrated** (AUC ≥ 0.85, monotone). That validates falsification-driven test selection for modular, map-based stacks. It gives a calibration curve and a rule for how many physical tests to run per sim counterexample.
- **Result B: calibration is poor in structured ways.** Possible causes:
  - Real failures come from things the simulator does not model: lidar misses on dark, low or thin obstacles; wheel slip in turns; localization jumps on glossy surfaces.
  - Sim-only failures come from overly pessimistic sensor noise.
  - We then test whether a 1-day real-to-sim calibration (friction, lidar dropout model, odometry noise fitted from logs) restores calibration. Either answer tells labs what simulator fidelity is worth buying.
- **"Mind the Gap" found transfer problems for an end-to-end DNN on a toy track.** Whether a modular lidar-plus-planner stack, the most common real-robot configuration, behaves better or worse is not known.

**Non-obvious insight.** For a modular stack, the gap may be concentrated in a few physical mechanisms rather than spread evenly. If so, the robustness signal can be "repaired" by modeling those mechanisms. The paper's reusable result would be a ranked list of which sim components move calibration most, measured by ablating them one at a time in simulation against fixed real outcomes. Real trials are expensive and sim runs are cheap, so the same 300 real trials can score many simulator variants. That asymmetry is what makes the study affordable.

**Closest prior work and what is new.**
1. [Fremont et al., Formal Scenario-Based Testing of AVs: From Simulation to the Real World, ITSC 2020](https://arxiv.org/abs/2003.07739). This is the same pipeline (Scenic → VerifAI → track) on a full-size AV, with a small number of track test cases. New here: a calibration curve with ~60 scenarios × 5 repeats, and a modular Nav2 stack.
2. [Stocco, Pulfer & Tonella, Mind the Gap!, IEEE TSE 2023](https://arxiv.org/pdf/2112.11255): virtual vs. physical failure exposure for DNN lane-keeping on Donkey Car. New here: a modular lidar/planner stack, falsification-based test selection, robustness → probability calibration, and fidelity ablations.
3. [Scenario Execution for Robotics (2024)](https://arxiv.org/pdf/2409.07080): runs reproducible scenarios in sim and on real Nav2 robots, without measuring sim–real agreement of failure probability.
4. [Seshia, "Bridging Simulation and the Real World with VerifAI and Scenic" (talk)](https://people.eecs.berkeley.edu/~sseshia/talks/Seshia_Sim_Real_VerifAI_Scenic.pdf): poses the sim-to-real question for falsification. Our study is a direct quantitative answer for a small UGV.
5. [Real-to-Sim calibration of a low-cost UGV digital twin (Sensors 2026)](https://doi.org/10.3390/s26185729): trajectory-level validation, not failure-probability calibration.
6. [Sim-to-Real Transfer for Mobile Robots with RL (2025)](https://arxiv.org/pdf/2501.02902): policy transfer, not test-selection validity.

**Validation design.**
- **Course.** A school blacktop or private paved lot, fenced and with no road access. The course is 15 × 10 m with a grid painted in chalk.
- **Robot and stack.** Nav2 with AMCL on an LD19 map, DWB or MPPI controller, parameters frozen.
- **Scenario space** (in Scenic):
  - Goal pose.
  - 1–3 static obstacles (boxes, cones, a refuse cart, a low 8 cm curb-stop block) at sampled poses.
  - One dynamic obstacle: a wheeled cart pulled across the path by an ESP32-timed winch, with sampled crossing time and speed.
- **Safety specification** (STL): minimum clearance > 0.15 m and goal reached within T.
- **Simulator.** Scenic has a Webots interface, and webots_ros2 ships a Nav2 demo. This avoids writing a new Gazebo interface; confirm in week 1. The robot model uses measured mass, wheel radius, lidar model and the same Nav2 config.
- **Falsification.** VerifAI cross-entropy and Halton samplers, about 5,000 sim runs on a laptop or free Colab.
- **Physical test set.** 60 scenarios stratified by sim ρ: 20 counterexamples, 20 near-boundary, 20 clearly safe. Each is run 5× physically, so 300 trials at about 2 min each, or about 10 h of robot time.
- **Mechanical role (core):**
  - A reproducible placement system: a chalk grid plus laser-cut or printed corner templates, targeting ±1 cm and ±2°, with placement checked by an overhead phone photo and AprilTags.
  - The repeatable dynamic-obstacle winch trolley, with timing repeatability measured at ≤ 0.1 s.
  - Measuring the robot's physical parameters for the model.
- **Software role (core):** Scenic programs, the VerifAI pipeline, STL monitors, a log-to-sim replay, real-to-sim calibration and the analysis.
- **Power.**
  - With 60 scenarios and about 30% real-failure prevalence, the Hanley–McNeil SE of AUC ≈ 0.065 at AUC = 0.75. That separates "useful" (≥ 0.85) from "weak" (≤ 0.65).
  - For the continuous metric (sim vs. real minimum clearance across 60 scenarios), r = 0.4 is detectable at power 0.9 (n ≈ 61).
  - The 5 repeats per scenario give per-scenario failure probabilities and an estimate of real-world repeat noise. That noise is the ceiling on any achievable calibration.

**Strongest fair baseline.**
1. The originating pipeline's own setting: Fremont et al.'s Scenic + VerifAI test selection, with default simulator fidelity.
2. Uniform random scenario sampling with no falsification, to check whether falsification actually finds more real failures per physical trial.
3. A calibrated simulator (one day of real-to-sim fitting) as the "best effort" arm.

**Measurements and analysis.**
- **Real-world outcomes:** min clearance, collision or contact (bumper switch), time, goal reached.
- **Calibration:** logistic GLMM of real failure on sim ρ with a scenario random effect; AUC, Brier score and a reliability diagram.
- **Yield:** real failures found per physical trial, falsification vs. random.
- **Fidelity ablation:** re-score all 60 scenarios under sim variants (lidar dropout on dark materials on/off, wheel-slip model, odometry noise, controller latency) against the fixed real outcomes. Rank components by AUC gain.
- **Release:** Scenic world files, robot model, placement templates, real outcomes.

**Build list (~$640 standalone; ~$250 if reusing the bin-robot or F1 base).** Estimates unless marked verified.

| Item | Cost |
|---|---|
| Robot base (used hoverboard + Pi 5 + LD19 + IMU + frame) | ~$390 (est.; see F1 line items) |
| Front bumper with microswitches (contact ground truth) | ~$20 (est.) |
| Dynamic-obstacle winch: geared DC motor, ESP32 Feather V2 ($19.95, price verified in round 1), driver, spool, rope, light cart | ~$90 (est.) |
| Obstacles: cones, boxes, foam blocks (borrowed refuse cart) | ~$40 (est.) |
| Placement templates (plywood/laser-cut at school or library maker space), chalk | ~$40 (est.) |
| AprilTags + phone tripod for overhead placement check | ~$30 (est.) |
| Spare battery / charger | ~$30 (est.) |
| **Total** | **~$640** |

Compute: the laptop and free Colab run Webots headless; Webots is free and open source.

**Timeline.**
- **Oct 12–25:** install Scenic, VerifAI, Webots and webots_ros2 Nav2. Confirm the Scenic–Webots interface works with a differential-drive robot. Mechanical: order parts, design the templates.
- **Oct 26 – Nov 22:** build the robot and bumper. Measure model parameters. Nav2 frozen on the course map. First Scenic world with static obstacles. Winch built.
- **Nov 23 – Dec 20:** falsification campaign in sim (static plus dynamic). Pick the first 30 scenarios. Physical runs of 30 × 5 = 150 trials.
- **By Dec 20:** half the physical dataset and a first AUC estimate.
- **Dec 21 – Jan 14:** remaining 30 scenarios × 5. Collect the logs for real-to-sim calibration.
- **Jan 15 go/no-go:**
  - **Go:** placement repeatability is within spec and the real repeat noise is not dominant.
  - **Fallback:** drop the dynamic obstacle and raise the static-scenario count.
- **Jan 15 – Feb 10:** calibrated-sim arm, fidelity ablations, random-sampling yield comparison (20 extra scenarios × 3 runs).
- **Feb 11–14:** data freeze.
- **Feb 15–26:** write-up and release.

**Main risk and fallback.**
- **Risk 1: the Scenic–Webots–Nav2 integration takes weeks.** De-risk in October. If it stalls, use Scenic for sampling only: export the parameters, then run them through Scenario Execution for Robotics on Gazebo and compute ρ offline from the logs.
- **Risk 2: real-world repeat noise is so large that per-scenario failure probability is poorly estimated.** That is itself a finding (the calibration ceiling). Raise to 8 repeats on the 30 most informative scenarios.

**Best venue.** IROS 2027 main track (sim-to-real evaluation). CASE 2027 is the alternative. Software-testing venues (ICST/ISSTA workshops) are a secondary audience.

**Lab appeal.**
- **UCSC, Fremont.** He is co-creator of Scenic and VerifAI and first author of [the ITSC 2020 sim-to-real track-testing paper](https://arxiv.org/abs/2003.07739); he hosted [SIP 2026 CSE-04 on robustness of autonomous agents](https://sip.ucsc.edu/2026-research-projects/). His lab gains a large-n real-world calibration of its own tools on a new robot class, at the cost of advising on Scenic and STL specs.
- **UCSC ASL, Elkaim.** The Pi + ROS 2 + Nav2 differential-drive robot, plus the [SIP 2025 SLAM/Gazebo projects](https://sip.ucsc.edu/2025-research-projects/), gives a matching platform. ASL gains a reproducible sim–real test bench for future SIP cohorts. The two UCSC labs could co-advise through SIP.

**Link to the bin robot.** The refuse cart is one of the scenario obstacles, and the course resembles a driveway. A calibrated sim then lets the team safety-test the bin robot's Nav2 stack mostly in simulation.

**Honest self-score.**
- **Novelty 6.5:** sim–real transfer of failures has been studied (Fremont 2020; Stocco 2023). The calibration curve for a modular Nav2 stack and the real-outcome-fixed fidelity ablation are new but incremental to those.
- **Feasibility 6.5:** the toolchain integration is the main risk. The physical trials (about 10 h of robot time) are modest.
- **Impact 7:** it answers a question every sim-based testing lab relies on, with a reusable artifact, and has the strongest lab-appeal hook (Fremont's own tools).
- **Overall about 6.7.**

---

## Summary

| Idea | N / F / I | Overall | Best lab fit |
|---|---|---|---|
| F1. Session/site/unit variance components and rank stability of outdoor navigation trials | 7 / 6.5 / 7 | 6.8 | Carpin (UC Merced); Elkaim (UCSC ASL) |
| F2. Flat-ground pull vs. slope capability on living turf: portable traction test + held-out-site predictor | 7 / 7 / 6.5 | 6.8 | Kobayashi (UCSC); Kitts (SCU RSL) |
| F3. Calibrating Scenic/VerifAI falsification of a Nav2 robot against ~300 physical trials | 6.5 / 6.5 / 7 | 6.7 | Fremont (UCSC); Elkaim (UCSC ASL) |

Note on shared hardware: F1, F2 and F3 can all run on the same bin-robot base. F1 needs a second unit.
