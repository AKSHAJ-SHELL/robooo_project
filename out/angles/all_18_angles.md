# All 18 generated angles (round 0)


Generators: A = perception & localization, B = mechanism & physical interaction, C = systems, cost & evaluation.


## A1.v1: A1. Is RTK worth it on a driveway? A zone-by-zone cost ladder for garage-to-curb localization

**Research question:** On real residential driveways, how do cart-placement error and run success change as the robot's absolute-position source is upgraded: (0) wheel encoders + IMU only, (1) plus 2-3 printed AprilTags fixed in the environment, (2) plus a ~$264 u-blox ZED-F9P RTK rover, (3) plus daylight single-camera teach-and-repeat? And in which driveway zone (inside garage, garage mouth/eaves, open driveway, curb apron) does each source fail?

**Hypothesis:** Encoders + IMU + 2-3 environment AprilTags will place the cart within 15 cm and 10 deg of the taught spot in >=90% of runs. That is statistically indistinguishable from the RTK configuration (overlapping 95% Wilson CIs) at <15% of RTK's sensor cost. RTK will have a carrier-fix rate <50% inside the garage and within 2 m of the garage door, so RTK alone cannot start runs from inside the garage. Falsified if (a) the AprilTag configuration's success rate is >10 points below RTK's with non-overlapping CIs, or (b) the measured RTK fix rate at the garage mouth is >=95% with no false fixes.

**Measurements:** PRIMARY: final cart placement error, i.e. the 2D position (cm) of the cart's axle midpoint and its heading (deg) relative to the taught spot. It is measured by tape trilateration from two fixed reference nails (about +/-1 cm). SECONDARY: (1) Checkpoint error at 3-4 taped crosses per driveway: the robot stops and the team measures the offset of a down-pointing laser dot (+/-1 cm). (2) Per-zone RTK metrics from receiver logs: fix rate (% of epochs with a carrier fix), time-to-fix after leaving the garage (s), HRMS, and false-fix rate (fixed epochs more than 10 cm from the surveyed checkpoint position). (3) AprilTag detection rate and pose error vs. distance and viewing angle. CONDITIONS: 2-3 driveways (own plus 1-2 relatives or friends, with permission); empty vs. ballasted cart; day and dusk (night is angle A2); slope logged. TRIALS: (a) A static RTK zone survey before the robot exists: a receiver on a tripod or hand cart, 10 min per point, 5 zones x 3+ driveways. (b) Closed-loop runs: 4 configurations x 25 runs x 2 driveways = 200 one-way runs. Every sensor is logged on every run, so each configuration can also be scored offline on all 200 runs (open-loop replay). ANALYSIS: Wilson 95% CIs on success; Fisher exact tests between configurations; error CDFs and P95 error; per-zone fix and false-fix maps; a cost-performance Pareto front of localization-sensor $ vs. P95 placement error; 'successful placements per $100 of localization hardware' (cost-normalized, in the spirit of Collin & Teran Espinoza).

**Baseline:** (1) An expensive configuration the team builds and tests: ZED-F9P RTK (ArduSimple simpleRTK2B kit, $263.75 rover plus a second kit as base) fused with encoders and IMU. This is the sensing class used by consumer RTK mowers such as the $1,000 Segway Navimow i105N and by OpenMower. (2) Published reference numbers: Blesing et al. report 0.073 m RMSE at 1.1 m/s for a ZED-F9P robot in open space; Janos & Kuras got a fix in only 4 of 8 urban-canyon series; Tavasci et al. saw silent ~2 m false fixes near facades. (3) Earlier bin-robot localization: SPARC used GPS plus a colored curb stake (~$809, no results); Hamzeh & Prasetyo used IR boundary following (20% day success).

**Novelty vs prior work:** Low-cost RTK has been characterized at static points (Janos & Kuras), on drones (Tavasci), in an open motion-capture area (Blesing) and on cars (Sanna). It has not been measured on a moving robot crossing the garage-interior to open-sky transition, which is where a bin robot starts. Autonomous-snowplow competition robots (ION ASC) localized on open simulated-driveway fields with lidar landmarks or RTK, but reported no cost-vs-accuracy comparison and no house or garage multipath. A 2025 feasibility study compares UWB with LiDAR and RTK for lawn mowers on cost, but on lawns rather than the garage-to-curb route, and it does not tie a BOM to task placement success. The only bin robot found with trial statistics (Hamzeh & Prasetyo 2026) used IR line following on a toy platform with a 35 L bin. New here: a per-zone RTK fix and false-fix map at the garage mouth, plus a measured cost ladder scored on the real task metric (cart placement error at the curb).

**Prior work cited:**
- [Evaluation of Low-Cost GNSS Receiver under Demanding Conditions in RTK Network Mode (Janos & Kuras, Sensors 2021)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8401267/): Static points only. A ZED-F9P with a patch antenna got a fix in only 4 of 8 urban-canyon series. No moving robot, no garage or driveway geometry, no comparison with fiducials or odometry.
- [Reliability of RTK Positioning for Low-Cost Drones' Navigation across GNSS Critical Environments (Tavasci et al., Sensors 2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11435761/): Drones near facades showed meter-level false fixes and 9-13 s recovery. We measure the false-fix rate for a ground robot leaving a garage.
- [Accuracy evaluation of a Low-Cost Differential Global Positioning System for mobile robotics (Blesing et al., IEEE Sensors 2023)](https://arxiv.org/abs/2306.12826): 0.073 m RMSE at 1.1 m/s, but in an open 60 m^2 motion-capture area with no buildings, no cost ladder and no task metric.
- [Ultra-Wideband Localization Modules for Autonomous Lawn Mowers: A Cost-Effective Feasibility Study (Sharma et al., ICCICA 2025; DOI 10.1109/iccica67008.2025.11337516)](https://ieeexplore.ieee.org/abstract/document/11337516/): Per the Scholar snippet, compares UWB with LiDAR and RTK-GPS on cost-effectiveness for mowers. Lawn setting, not garage-to-curb. No per-zone fix or false-fix data and no cart placement metric (abstract not readable, so details are UNVERIFIED).
- [Localization, Mapping, and Navigation using only a single 2D LiDAR (Stiehm et al., ION GNSS+ 2018; ION Autonomous Snowplow Competition)](https://www.ion.org/publications/abstract.cfm?articleID=16120): A snowplow robot localizes with lidar landmarks on a competition field. No accuracy or cost figures in the abstract, no house or garage multipath, no cost ladder.
- [Automated Mobile Platform for transporting a Residential Garbage Bin to the Collection Point (Hamzeh & Prasetyo, JASAE 2026)](https://jasae.org/index.php/JASAE/article/view/92): The closest bin-robot study with trial counts: 80 trials, 20% day and 65% night success with IR boundary following on a toy car with a 35 L bin. No absolute localization, no placement error, no cost comparison.
- [One year in a forest: Analyzing the challenges of autonomous navigation in subarctic environments (Boxan et al., 2026)](https://arxiv.org/abs/2608.27628): Found complex SLAM gave 'limited accuracy gains over a proprioceptive baseline'. That was in a forest with research sensors and no cost axis. We test the same idea (proprioception plus one cheap fix) on a driveway with prices attached.

**What the team builds:** SHARED PLATFORM (mechanical student): hoverboard-hub differential drive with the cart hitch (from the mechanism workstream); a sensor mast with the RTK antenna at >=0.5 m on a ground plane, the camera and the IMU; weatherproof laminated AprilTags on the garage wall and on a removable stake or the mailbox post near the curb; a down-pointing laser-dot jig for checkpoint ground truth. SOFTWARE (perception student): ROS 2 on a Raspberry Pi 5; EKF (robot_localization) with switchable inputs (encoders from the FOC hoverboard firmware, BNO085 IMU, AprilTag poses, ZED-F9P NMEA/UBX with fix-quality gating at HRMS <5 cm as Tavasci et al. recommend); a teach-and-repeat waypoint recorder with a pure-pursuit follower; rosbag logging of all sensors on every run; Python analysis scripts for Wilson CIs, error CDFs and the Pareto plot.

**Cost estimate (USD):** 992

**Cost breakdown:** VERIFIED prices: Raspberry Pi 5 4GB $110 (PiShop US, Apr 2026, per Raspberry Pi forum price summary; Pi prices rose sharply in 2026); BNO085 IMU $29.50 (Adafruit 4754); Pi Camera Module 3 'from $25' (raspberrypi.com); ArduSimple simpleRTK2B Basic Starter Kit (ZED-F9P + ANN-MB antenna) $263.75 x2 for rover + base = $527.50 (prior_art.md). ESTIMATES (not verified): shared platform ~$230 (used hoverboard ~$50, frame/fasteners ~$80, hitch ~$60, ESP32/wiring/e-stop ~$40); microSD/buck converter/cables ~$25; printed and laminated tags plus stake ~$15; tape measures, chalk, laser pointer, nails ~$30. TOTAL ~$992, close to the ~$1,000 flag. It drops to ~$728 if a free NTRIP correction stream is usable instead of buying a base (availability near the team is UNVERIFIED). The sensor-only cost of each rung, which is the number the paper reports: rung 0 ~$30, rung 1 ~$70, rung 2 ~$300-560, rung 3 +$0.

**Timeline:** Oct 2026: recruit 2-3 driveways; set reference nails; fix the protocol and success thresholds; order RTK kits by mid-Oct (they ship from Spain) plus the IMU and camera. Nov: static RTK zone survey on 3+ driveways with a tripod (first real data before the robot exists); AprilTag detection-range tests with a hand-held Pi; outreach e-mails with the zone fix map. Dec 1-20: platform drives under teleop; encoder+IMU EKF. Dec 21-Jan 10: closed-loop waypoint following; freeze the protocol. Jan 11-Feb 14: 200 closed-loop runs, about 4 weekends plus weekday afternoons (each run about 3 min including reset). Feb 14: data freeze. Feb 15-26: write-up, Pareto figure, video. Submit IROS by Fri Feb 26 (hard stop Mar 1, 23:59 PT).

**Target venue:** IEEE/RSJ IROS 2027 (paper deadline Mon Mar 1, 2027, 23:59 PT per RAS calendar/mldeadlines; 8 pages incl. refs). Why: a field robot-perception study with real-hardware trials and a quantitative cost axis fits IROS's service-robot and perception topics and its 2027 sustainability theme. Backup: CASE 2027 (same Mar 1 deadline; the cost-effectiveness framing suits automation reviewers). Companion: an ICRA 2027 field-robotics workshop. Labs to show it to: Carpin (UC Merced; outdoor ROS 2 Nav2, CASE/ICRA) and Elkaim (UCSC ASL; Pi + Nav2 robots). Show them the per-zone RTK fix and false-fix map and the cost-vs-P95-error Pareto plot.

**Main risk:** The result could be site-specific (only 2-3 driveways) or simply 'RTK is fine' on an open driveway, and hand-measured ground truth is labor-intensive. Fallbacks: the static RTK zone survey extends cheaply to 5+ driveways without the robot, so the fix/false-fix-by-zone result stands on its own. A null result ('$70 of tags matches $560 of RTK') is still the paper's cost claim. If closed-loop time runs short, run 2 configurations closed-loop and score the others by offline replay of the same logs.


## A2.v1: A2. Pre-dawn route following on a hobby budget: what is the cheapest way to make teach-and-repeat work in the dark?

**Research question:** For a cart-towing robot repeating a daylight-taught garage-to-curb route, which sensing keeps success and path accuracy in pre-dawn darkness (<1 lux) closest to daytime levels: (a) a passive $25 RGB camera, (b) a NoIR camera with an onboard 850 nm illuminator (~$65), (c) (b) plus a few retroreflective markers in the environment (~$15), or (d) a ~$70-120 2D dToF lidar? And what does each cost per point of night success?

**Hypothesis:** Passive-RGB teach-and-repeat success will fall from >=90% in daylight (>1,000 lux) to <=50% below 5 lux. NoIR + 850 nm illumination, with or without retroreflective markers, will keep success >=90% and lateral checkpoint error within 1.5x its daytime value below 1 lux. That matches the lidar configuration within 5 points at about 2/3 of its sensor cost. Falsified if the NoIR+IR success rate below 1 lux is more than 10 points under its own daytime rate or under the lidar configuration's (non-overlapping 95% CIs).

**Measurements:** Per run: success (cart reaches the taught curb spot within 20 cm and 10 deg); lateral path error at 3 taped checkpoints (laser-dot method, +/-1 cm); number of tracking-loss events; manual interventions. Illuminance is logged at 1 Hz by an onboard VEML7700 lux sensor (0-120 klux), along with time relative to civil twilight. Lighting bins: daylight >1,000 lux; dusk 10-1,000; streetlight 1-10; dark <1. Extra conditions logged when they occur: wet pavement after rain, headlight glare from passing cars, a parked car moved from the teach run. Cross-condition design: teach once in daylight, then repeat in every bin; secondary analysis re-teaches at night. Trials: 4 configurations x 4 lighting bins x 15 runs = 240 runs. Both cameras and the lidar are logged on every run, so each configuration also gets offline replay on all runs. Analysis: logistic regression of success on log10(lux) per configuration; Wilson CIs per bin; error-vs-lux curves; a chart of sensor cost vs. dark-condition success.

**Baseline:** (1) Within-subject: each configuration's own daytime performance. (2) The active-sensor configuration the team also tests: a ~$70-120 LD19/STL-19P-class 2D dToF lidar doing scan-matching repeat. (3) Published: ROVER (DROID-SLAM ATE 0.32 m by day vs 5.62 m at night in gardens); Gridseth & Barfoot (learned features let research platforms with a GPU repeat day-taught routes in darkness over 35.5 km); Liu, Rozsypalek & Krajnik (IR+RGB fusion for VT&R at night, ECMR 2023); MacTavish et al. (headlight visual odometry, CRV 2017). None of these prices the night fix at hobby scale.

**Novelty vs prior work:** Night robustness for teach-and-repeat has been tackled with learned features (Gridseth & Barfoot), IR+RGB fusion (Liu et al. 2023), headlights (MacTavish et al. 2017) and color-constant images (Paton et al. 2015). All of these used research platforms and GPUs, and none reported cost. The bin task makes darkness the normal case, not an edge case. Recology instructs residents to put carts at the curb 'by 6 AM', and on the San Jose winter days checked (Dec 21 and Jan 15) civil twilight begins about 6:49-6:52 AM (sunrise-sunset.org; Inference: the whole Dec-Feb window is dark at 6 AM). The only bin robot with day/night trials (Hamzeh & Prasetyo 2026) found its IR sensors failed in daylight (20% vs 65%). New here: a lux-indexed, cost-indexed comparison of night-capable sensing on the exact residential route, using a $25-35 camera, IR LEDs and retroreflective markers against a lidar.

**Prior work cited:**
- [ROVER: A Multi-Season Dataset for Visual SLAM (Schmidt et al., IEEE T-RO 2025)](https://arxiv.org/abs/2412.02506): Shows camera SLAM collapsing at night in gardens (0.32 m to 5.62 m ATE). It is a dataset benchmark with no towed load, no active illumination and no cost comparison.
- [Keeping an Eye on Things: Deep Learned Features for Long-Term Visual Localization (Gridseth & Barfoot)](https://arxiv.org/abs/2109.04041): Day-taught, night-repeated VT&R with learned features on research robots and a GPU. We ask what the cheapest hardware fix is, with no GPU.
- [Self-Supervised Learning for Fusion of IR and RGB Images in Visual Teach and Repeat Navigation (Liu, Rozsypalek, Krajnik, ECMR 2023)](https://ieeexplore.ieee.org/document/10256333/): Uses IR imagery to make VT&R work at night (per the Scholar snippet; IR camera type and cost not verified). No cost analysis, no residential route, no cart.
- [Night Rider: Visual Odometry Using Headlights (MacTavish, Paton, Barfoot, CRV 2017)](https://ieeexplore.ieee.org/document/8287710/): Active lighting for visual odometry on a research vehicle. We compare hobby IR illumination against a lidar and against passive retroreflectors, with prices.
- [Navigation without localisation: reliable teach and repeat based on the convergence theorem (Krajnik et al., IROS 2018)](https://arxiv.org/abs/1711.05348): A cheap, uncalibrated-camera teach-and-repeat method that we adopt as the software baseline. It was not evaluated in residential pre-dawn darkness or with a towed cart.
- [Automated Mobile Platform for transporting a Residential Garbage Bin to the Collection Point (Hamzeh & Prasetyo, JASAE 2026)](https://jasae.org/index.php/JASAE/article/view/92): Bin robot whose IR sensors failed in daylight (20% day vs 65% night success over 80 trials). It used boundary IR sensors, not camera or lidar route following, and had no lux measurement or cost comparison.
- [Recology cart-placement instructions ('Your Three Carts')](https://www.recology.com/recology-san-mateo-county/your-three-carts/): Not research. It is the requirement that sets the operating condition: carts at the curb by 6 AM, wheels against the curb, arrows toward the street, about 3 ft apart.

**What the team builds:** SOFTWARE (perception student): re-implement BearNav's heading-correction teach-and-repeat (open-source ROS reference code exists) in Python/ROS 2 on a Pi 5. Both CSI ports are used: one RGB Camera Module 3 and one NoIR. Add a lidar scan-matching repeat mode (ICP against taught keyframe scans), lux logging, and run bookkeeping. MECHANICAL: camera and lidar mast with a rain shield; an 850 nm IR LED illuminator with heatsink and PWM control from the ESP32; retroreflective markers on 2-3 stakes or existing posts (environment only, never on the bin); checkpoint laser-dot jig. SAFETY: night trials are always supervised with an e-stop, at <=0.5 m/s, and the robot stops at the curb line and never enters the roadway.

**Cost estimate (USD):** 603

**Cost breakdown:** VERIFIED: Raspberry Pi 5 4GB $110 (PiShop US, Apr 2026 via RPi forum); Camera Module 3 RGB 'from $25' (raspberrypi.com); VEML7700 lux sensor $4.95 (Adafruit 4162); BNO085 IMU $29.50 (Adafruit 4754); 2D dToF lidar class $69-$119 (LD06/LD19/STL-19P listings returned by search: Sensorlidar $69, Hiwonder $89.99, Innomaker $99, DFRobot $119); budget $99. ESTIMATES (UNVERIFIED): Camera Module 3 NoIR Wide ~$35; 850 nm IR illuminator ~$30; retroreflective tape plus stakes ~$15; Pi accessories ~$25; shared platform ~$230 (used hoverboard, frame, hitch, ESP32, e-stop). TOTAL ~$603. Night-sensing add-on costs reported in the paper: (b) ~$65, (c) ~$80, (d) ~$99.

**Timeline:** Oct: order cameras, IR LEDs and lidar; get T&R running on a hand-pushed cart carrying the Pi and cameras at robot height. Nov: record pilot teach and repeat sequences at dusk and night on the driveway (evenings after school; San Jose sunset is about 5 PM in Dec-Jan) to tune IR power and exposure; outreach. Dec: integrate on the robot. Dec 21-Jan 10: closed-loop T&R in daylight; freeze the protocol. Jan 11-Feb 14: 240 runs. Dark and streetlight bins run 6-9 PM on weekdays, so no pre-dawn sessions are required; a few 5:30-6:30 AM sessions validate the real pickup condition. Dusk runs about 5:00-5:45 PM; daylight runs on weekends. Feb 14 data freeze; submit by Feb 26 (deadline Mar 1).

**Target venue:** IEEE/RSJ IROS 2027 (deadline Mar 1, 2027, 23:59 PT; 8 pages incl. refs): a robot-perception robustness study with real trials fits IROS. Companion: an ICRA 2027 workshop on field or long-term autonomy (deadlines estimated mid-Mar to late Apr). Labs: Elkaim (UCSC ASL; embedded Pi navigation; the SIP 2027 portal opens Jan 15) and Qin or Ghose (SFSU; perception on cheap hardware). Show them the success-vs-log(lux) curves per sensor with the cost overlay.

**Main risk:** An 850 nm illuminator lights only about 3-5 m, so an open driveway may have too few features at night. Images taught in daylight on a NoIR camera may also not match night images lit by the robot, so the cheap fix may fail outright. Fallbacks: (1) teach at night as well (multi-experience: one daytime and one nighttime teach run) and report both; (2) the retroreflective-marker configuration makes features cheap to add; (3) a clear negative result ('$65 of IR does not rescue camera T&R; a $99 lidar does') still answers the cost question.


## A3.v1: A3. Tag-free pose estimation of unmodified 64/96-gal carts for docking: accuracy per dollar, plus the first low-viewpoint cart dataset

**Research question:** From 0.3-3 m, how accurately can a robot estimate the 2D pose (x, y, yaw) and handle side of an unmodified 64/96-gal cart using (a) a $25 monocular camera with a learned keypoint model and PnP on the cart's known geometry, (b) a ~$100 2D dToF lidar with geometric model fitting, or (c) a $20 8x8-zone ToF sensor for the final approach? How do these compare with a $269-399 stereo depth camera, and is the cheapest coarse-to-fine combination accurate enough to stay inside the hitch's capture envelope?

**Hypothesis:** Lidar model fitting will give <=3 cm and <=3 deg error at <=1.5 m, comparable to the depth camera. The monocular keypoint model will give <=10 cm and <=8 deg at 1-3 m, enough for the coarse approach. The coarse-to-fine combination of a $25 camera and a $20 ToF will reach <=3 cm and <=3 deg over the final 0.5 m, producing a docking-ready estimate in >=90% of approaches at <20% of the depth camera's cost. Falsified if the cheapest combination's final-approach P95 error is more than 2x the depth camera's, or larger than the measured hitch capture envelope.

**Measurements:** STATIC BENCHMARK (all sensors capture each pose simultaneously): the cart is placed on a chalk/printed floor grid with a yaw-protractor template (ground truth +/-1 cm, +/-1 deg). Ranges are 0.3, 0.5, 1, 1.5, 2 and 3 m; relative bearings run -45 to +45 deg; cart yaw spans 0-330 deg in 30-deg steps (sampled, ~300 poses). Carts: 64 and 96 gal from 2-3 brands, borrowed from neighbors with permission. Lid states: closed and overfilled lid. Lighting: day, shade, dusk, and night with IR. Clutter: a second cart or a recycling bin adjacent. Metrics: position error (cm) and yaw error (deg) vs. range (median, P95); handle-side classification accuracy; detection rate and false positives on non-cart objects; inference time on the Pi 5 (ms). CLOSED-LOOP: 60 docking approaches from random start poses (1-3 m, +/-45 deg), scored as success when the estimate at the hitch point falls inside the hitch capture envelope measured by the mechanism workstream (or a +/-5 cm/+/-10 deg placeholder); Wilson CIs. DATASET: ~2,000 low-viewpoint images (camera at 20-40 cm) with box, 6-8 keypoints (wheel hubs, handle ends, lid hinge and front corners) and yaw, released CC-BY. Analysis: error-vs-range curves per sensor; a cost-accuracy Pareto front; docking success rates.

**Baseline:** (1) An expensive configuration the team also tests: Luxonis OAK-D Lite stereo depth ($269) with point-cloud plane/box fitting, or RealSense D435i ($399). (2) Published: Xiao et al. (ICRA 2022) docked to airport trolleys with five range/vision sensors, reaching 0.17 m/0.11 rad (camera, long range) and 0.03 m/0.02 rad (lidar, close range). Sivakanthan et al. reached 0.09 +/- 0.10 m with a D455 approaching a curb, a comparable low-speed docking-style approach. Taghibakhshi et al. report cm-level camera-only docking of a mower to a fixed station.

**Novelty vs prior work:** Existing cart-perception datasets are truck-viewpoint detection or fill-level sets: StreetView-Waste uses European container classes, and Agnew et al. 2023 is a proprietary side-loader set. Neither has a low ground-robot viewpoint or yaw/keypoint labels. Industry uses MobileNet-SSD detection from the truck (McNeilus US11527072B2) and sonar for the final approach (Con-Tech). The bin-relocation patent US20200023524A1 describes camera-guided handle hooking but gives no data. Trolley docking (Xiao et al.) is indoors with ~5 expensive sensors. Searches of arXiv and Google Scholar (2026-10-03) found no paper that estimates the pose of a wheeled refuse cart from a ground robot. New here: a measured cost-accuracy curve for tag-free cart pose estimation from robot height, a keypoint definition based on standard ANSI cart geometry (Toter/Cascade spec sheets), and a released dataset.

**Prior work cited:**
- [Robotic Autonomous Trolley Collection with Progressive Perception and Nonlinear Model Predictive Control (Xiao et al., ICRA 2022)](https://arxiv.org/abs/2110.06648): Docking-accuracy reference using 3D lidar, two 2D lidars, a solid-state lidar and RGB-D on indoor 4-wheel trolleys. We use one hobby sensor at a time on outdoor 2-wheel refuse carts and add a cost axis.
- [StreetView-Waste: A Multi-Task Dataset for Urban Waste Management (WACV 2026)](https://arxiv.org/abs/2511.16440): 36k fisheye truck-side images of European container classes with no pose or yaw labels. Our dataset covers US carts from 20-40 cm height with keypoints and yaw.
- [Detecting the overfilled status of domestic and commercial bins using computer vision (Agnew et al., 2023)](https://doi.org/10.1016/j.iswa.2023.200229): Detection and segmentation of side-loader bins from truck video (mAP >= 0.8) for fill status. No pose, no robot docking.
- [US20200023524A1: Trash and recycle bin relocation robot](https://patents.google.com/patent/US20200023524A1): Claims a camera-guided robot that hooks an unmodified cart's handle, but gives no prototype data. We measure how accurately cheap sensors can actually locate the handle and cart.
- [US11527072B2: Detecting waste receptacles using convolutional neural networks (McNeilus)](https://patents.google.com/patent/US11527072B2/en): A truck-mounted MobileNet-SSD detects carts for arm grabs. Truck viewpoint, no published accuracy, no ground-robot pose estimate.
- [Bin Buddy: an Autonomous Waste Cart - Design Specification (Simon Fraser Univ. capstone, 2021)](https://summit.sfu.ca/_flysystem/fedora/2022-08/input_data/21520_1/company2_129057_15528172_2desi.pdf): A device attached to the city cart that follows lines with a Pi camera and detects docking stations, with HC-SR04 obstacle sensing. It is a design spec with no results, and it is fixed to the cart rather than docking to it.
- [Toter Two-Wheel Cart Specifications (TOT047-092018)](https://www.toter.com/sites/default/files/2021-05/Two-Wheel_CART_SPECIFICATIONS_092018_DIGITAL.pdf): Source of the standard cart geometry, used as the 3D model for PnP and lidar fitting. Not a perception work.

**What the team builds:** SOFTWARE (perception student): collect images with a Pi camera at 20-40 cm on a hand cart, starting in Oct before the robot exists. Label boxes, keypoints and yaw (free labeling tools; ~10-15 h shared). Fine-tune a small YOLO-pose model (Ultralytics) on a laptop or free cloud GPU (free-tier availability UNVERIFIED) and run it on the Pi 5. Compute PnP against the cart geometry from spec sheets, checked with a tape measure. Lidar: cluster the cart, fit an L-shape/rectangle and the wheel-axle line, and resolve handle side from the wheel-side asymmetry. ToF: plane fit of the cart face from the 8x8 depth grid for the final 0.5 m. Fusion and a coarse-to-fine docking controller. MECHANICAL: a sensor head with fixed, calibrated extrinsics; the floor-grid and yaw-protractor ground-truth jig; integration with the hitch and its capture-envelope test rig (from the mechanism workstream).

**Cost estimate (USD):** 823

**Cost breakdown:** VERIFIED: Raspberry Pi 5 4GB $110 (PiShop US, Apr 2026); Camera Module 3 from $25 (raspberrypi.com); VL53L5CX 8x8 ToF carrier $19.95 x2 = $39.90 (Pololu 3417); 2D dToF lidar budget $99 (LD19/STL-19P-class listings $69-$119); OAK-D Lite $269 (Luxonis shop) as the expensive baseline (RealSense D435i is $399 at the RealSense store, which would make the total ~$953). ESTIMATES (UNVERIFIED): Pi accessories ~$25; floor-grid/protractor printing and chalk ~$25; extra cart brands borrowed from neighbors with permission at $0 (a used cart ~$50 if needed); shared platform ~$230. TOTAL ~$823. Cheapest sensing option reported in the paper: ~$45 (camera + ToF).

**Timeline:** Oct: image collection rig; collect ~1,000 images of own and neighbors' carts (with permission) at robot height across yaw and lighting. Nov: label, train v1 keypoint model, PnP; order lidar, ToF and OAK-D Lite; outreach with the first error-vs-range plot. Dec: lidar fitting and ToF final approach; mount on the robot. Dec 21-Jan 10: static benchmark sessions (~300 poses, all sensors at once; about 3 sessions). Jan 11-Feb 10: closed-loop docking trials (60), extra night and IR captures, labeling to ~2,000 images. Feb 14: data freeze; prepare the dataset release (anonymized: no faces, house numbers or license plates). Submit by Feb 26 (deadline Mar 1).

**Target venue:** IEEE/RSJ IROS 2027 (Mar 1, 2027, 23:59 PT; 8 pages): a perception benchmark plus dataset with real docking trials. The robot-perception topic and 2027 recycling/sustainability theme fit. Backup: CASE 2027 (Mar 1). Labs: Wencen Wu (SJSU; small-scale autonomous parking, closest to pose-based docking), Mehta (UCLA LEMUR; 'one-dollar robots' cost thesis), Ghose (SFSU; computer vision). Show them the cost-accuracy Pareto, sample keypoint detections and the dataset card.

**Main risk:** The monocular keypoint model may be unreliable with a small dataset: cart symmetry can flip yaw by 180 deg, and darkness and overfilled lids cause misses. Labeling also takes time from two students. Fallbacks: lidar fitting resolves pose and the camera only classifies handle side (a much easier task); restrict claims to the brands and conditions tested; release whatever dataset size is reached (even ~1,000 labeled images is new for this viewpoint).


## A4.v1: A4. Stopping at the curb: a same-curb sensor price sweep for head-on curb and road-edge detection from 25 cm height

**Research question:** When a 20-40 cm tall robot approaches a residential curb edge from the driveway or sidewalk side to place a cart, how do $5 ultrasonic rangers, a $20 8x8-zone ToF sensor, a $25 camera (geometric plus learned segmentation) and a ~$100 2D dToF lidar compare with a $269 stereo depth camera? The comparison covers edge detection rate, false stops and stop-distance error across curb types (vertical drop, rolled/mountable curb, curb-cut lip and gutter), lighting (sun, shade, dusk, night) and wet vs. dry pavement.

**Hypothesis:** A downward-tilted 8x8 ToF ($20) plus one ultrasonic ranger ($5) will detect >=95% of vertical-drop edges and >=85% of rolled/curb-cut edges, with stop-distance error <=5 cm in every lighting condition. That is within 5 points of the depth camera at <10% of its cost. The monocular camera alone will fall below 80% detection at night or on wet pavement, and the lidar's useful range will shrink in direct sun. Falsified if the ToF+ultrasonic combination is more than 10 points worse than the depth camera on any curb type in daylight.

**Measurements:** Commanded behavior: approach at 0.3 m/s and stop 30 cm before the detected edge. Metrics per sensor (all sensors logged simultaneously on every approach): detection rate (Wilson 95% CI); first-detection range (m); stop-distance error (cm, tape-measured from the robot reference point to the edge); edge heading error (deg) at approach angles 0, +/-20 and +/-40 deg; false stops per 10 m on expansion joints, shadows, leaves and wet patches; overruns, recorded as a failure (a spotter and e-stop prevent any actual drop). Conditions: >=10 distinct curb segments (own street, school lot, park, sidewalk-to-street edges; public curbs, with the robot never entering the roadway) x 3 curb types x 5 approach angles x lighting (sun/shade/dusk/night) x dry/wet (wet via rain days or a hose on the team's own apron). About 300 approaches; one approach yields data for every sensor. Ground-truth sanity check: a slow hand-pushed rig at robot height for the first 100 approaches. Analysis: detection and false-alarm rates per sensor x condition; RMSE and P95 stop error; cost-vs-performance chart; mixed-effects logistic regression on curb type, light and wetness.

**Baseline:** (1) An expensive configuration the team also tests: an OAK-D Lite stereo depth camera ($269) with ground-plane fitting, the same class as the RealSense D455 used by Sivakanthan et al. (2) Published numbers: Rhee & Seo 2019, 3-4 side-facing ultrasonics at $15 each on a car parallel to the curb, 12-13.5 cm RMSE and 92-96% availability; Sivakanthan et al. 2021, D455 on a wheelchair at an indoor mock curb, 0.09 +/- 0.10 m and 14/15 positions; WalkOCC 2026, learned monocular curb IoU only 14.59 on sidewalk robots.

**Novelty vs prior work:** Every published curb number comes from a different platform and geometry: a car driving parallel to the curb (Rhee & Seo; Panev et al.), a wheelchair at an indoor mock curb (Sivakanthan), sidewalk robots with 3D lidar (WalkOCC/Coco), car-scale LiDAR (CurbNet) or 4D radar. Single-chip radar was tested on curb and driveway scenes but only qualitatively (Southcott et al.). Google Scholar and arXiv searches on 2026-10-03 found no same-curb, same-robot comparison of hobby sensors approaching head-on from 20-40 cm height, outdoors, across lighting and wetness, with sensor price on the x-axis. US rolled curbs and curb cuts, which are the hard case for a bin robot, are also absent from these studies.

**Prior work cited:**
- [Low-Cost Curb Detection and Localization System Using Multiple Ultrasonic Sensors (Rhee & Seo, Sensors 2019)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6470551/): Best accuracy-per-dollar point found (~12 cm for ~$50), but on a car moving parallel to the curb at road speed. We approach head-on at low height and compare against other sensors on the same curbs.
- [Automated Curb Recognition and Negotiation for Robotic Wheelchairs (Sivakanthan et al., Sensors 2021)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8659845/): Robot-scale curb approach (0.09 m error) with one D455, indoors at a mock curb, straight curbs only. No cheaper sensors, no sun or night.
- [WalkOCC: Monocular 3D Occupancy Perception for Robots on Sidewalks via Hybrid 2D-3D Learning (2026)](https://arxiv.org/abs/2606.19122): Learned monocular curb occupancy on Coco robots reached only 14.59 curb IoU. No cost comparison and no cheap active sensors.
- [Road Curb Detection and Localization with Monocular Forward-view Vehicle Camera (Panev et al.)](https://arxiv.org/abs/2002.12492): Geometric fisheye curb detection from a car (>90% distance accuracy). Car viewpoint, not 20-40 cm and head-on, and not tested on US rolled curbs.
- [Millimeter Wave Radar-Based Road Segmentation (Southcott, Zhang, Liu; Clarkson)](https://par.nsf.gov/servlets/purl/10493760): Single-chip radar on curb and driveway scenes, qualitative only. Not included in our sweep because no radar price was verified; cited as a future rung.
- [CurbScan: Curb Detection and Tracking Using Multi-Sensor Fusion (Baek et al., ITSC 2020)](https://arxiv.org/abs/2010.04837): Fuses sparse 3D LiDAR, camera and ultrasonics on a vehicle, with no ablation that removes the LiDAR. We measure each cheap sensor alone and in a cheap pair.

**What the team builds:** MECHANICAL: an adjustable sensor bar at 20-40 cm with two downward-tilted VL53L5CX sensors, forward and corner ultrasonics (one waterproof unit), the camera, the lidar tilted a few degrees down and the OAK-D Lite, all with fixed, measured extrinsics. A hand-pushed rig carrying the same bar collects data before the robot is ready. SOFTWARE: per-sensor edge detectors. Ultrasonic: range-drop and step detection. ToF: per-zone ground-plane fit and drop/step detection. Lidar: line and drop extraction. Camera: geometric line/gradient detection plus a small fine-tuned segmentation model (YOLOv8-seg class, as in Ruan et al.). Depth: RANSAC ground plane plus edge extraction. A common 'stop at 30 cm' controller, synchronized logging, and analysis scripts. SAFETY: spotter, e-stop, 0.3 m/s, never in the roadway.

**Cost estimate (USD):** 877

**Cost breakdown:** VERIFIED: HC-SR04 $5.25 x2 = $10.50 (SparkFun); VL53L5CX $19.95 x2 = $39.90 (Pololu 3417); Camera Module 3 from $25; 2D dToF lidar ~$99 (listings $69-$119); OAK-D Lite $269 (Luxonis) baseline; VEML7700 lux sensor $4.95 (Adafruit); Raspberry Pi 5 4GB $110 (PiShop US, Apr 2026). ESTIMATES (UNVERIFIED): waterproof JSN-SR04T-type ultrasonic ~$12 x2 = $24; Pi accessories ~$25; hand-pushed rig and mounts ~$40; shared platform ~$230 (it is needed only for the closed-loop stop trials; the hand-rig data are robot-independent). TOTAL ~$877. Sensor subsets compared in the paper: $10, $20, $25, $45, $99, $269.

**Timeline:** Oct: list >=10 curb segments and get school or park permission where needed; order sensors. Nov: build the hand-pushed sensor rig and collect ~100 approaches (robot-independent, de-risking); outreach. Dec: detectors per sensor; mount the bar on the robot. Dec 21-Jan 10: closed-loop stop controller; freeze the protocol. Jan 11-Feb 14: ~200 robot approaches across lighting and wetness (wet runs on rain days, which are common in Jan-Feb in California, or by hose on the team's own apron). Feb 14 data freeze; submit by Feb 26 (deadline Mar 1).

**Target venue:** IEEE CASE 2027 (regular papers due Mar 1, 2027; 6 pages + 2 paid): a sensor-selection and cost-effectiveness engineering study fits automation reviewers. The WIP track (Apr 1, 4 pages) is the fallback. Alternative: IROS 2027 (Mar 1) if framed as robot perception. Labs: Kitts (SCU Robotic Systems Lab; field rovers, low-cost devices), Winncy Du (SJSU sensors and mechatronics; a natural contact for the mechanical student), Wu (SJSU). Show them the detection-rate-by-curb-type table vs. sensor price.

**Main risk:** Rolled curbs and curb-cut lips (1-3 cm) give very weak geometric signal, ultrasonic beams hit the ground, and the ToF's maximum range drops in sunlight (the vendor says ambient light affects max range). The cheapest sensors could fail the hard curb types, and outdoor ground truth is labor-intensive. Fallbacks: report results per curb type honestly (a 'cheap sensors handle vertical curbs but not rolled curbs' result is still the first such measurement); add the camera-based gutter-line cue; shrink to 6 curb segments if access is limited.


## A5.v1: A5. The return trip: re-finding, identifying and re-docking a household's own displaced cart after the truck empties it

**Research question:** After an automated truck empties the carts, how reliably can a cheap robot re-detect its household's own unmodified cart, confirm identity among look-alike carts, and estimate its pose for re-hitching? Reliability is measured as a function of displacement (0-3 m), rotation (0-180 deg) and number of same-model distractor carts (0-4), comparing (a) a position prior from where the robot left the cart, (b) camera detection plus appearance re-identification from naturally occurring features, and (c) reading the cart's existing city-installed UHF RFID tag with a $310 reader.

**Hypothesis:** The position prior alone will succeed in >=95% of cases with no look-alike cart nearby, but drop below 70% top-1 identity when a same-color, same-model cart is within 1.5 m. Adding camera appearance re-ID (enrollment images of the household's carts; no tags or markings added) will restore >=90% identity accuracy with a wrong-cart rate <=2%. Reading the existing RFID tag will reach >=98%, but at ~12x the sensor cost of the camera. Falsified if camera re-ID does not beat the position prior by >=15 points in the distractor conditions, or if the wrong-cart rate exceeds 5%.

**Measurements:** (1) REAL DISPLACEMENT DATA: on every pickup day Dec-Feb, tape-measure each of the household's carts before pickup and again after the truck returns it (position offset in cm, rotation in deg): ~11 weeks x 2-3 carts = ~25-30 events (descriptive distribution, bootstrap CIs). (2) STAGED TRIALS reproducing that distribution plus harder cases: displacement {0, 0.5, 1, 2, 3 m} x rotation {0, 45, 90, 180 deg} x distractors {0, 1, 2, 4} (borrowed same-model carts, with owners' permission), ~150 trials, day and dusk. METRICS: re-detection rate; top-1 identity accuracy; wrong-cart rate (the critical metric, since taking a neighbor's cart is the worst failure); pose error at re-acquisition (cm, deg; ground truth from the floor-grid method); time to re-acquire (s); re-hitch success when the hitch is available. Each trial logs camera, RFID reads (EPC and RSSI) and odometry, so all three methods are scored on the same trials. ANALYSIS: Wilson CIs per condition; logistic regression of identity success on displacement and distractor count; cost vs. wrong-cart-rate table.

**Baseline:** (1) An expensive configuration the team also tests: a SparkFun Simultaneous RFID Reader M7E Hecto ($309.95; EPC Gen2 UHF, up to ~16 ft with an external antenna) reading the RFID tag already embedded in the city cart. Toter embeds tags in the handle; San Diego's carts carry RFID chips assigned to an address; Framingham states that each cart has an embedded RFID tag. This is the same identity signal refuse trucks use to log pickups. (2) The position-prior-only behavior a taught-route robot would use (the SmartCan-style approach that strands when carts are moved). (3) Published: CartSeeker's claimed 96% truck-side cart recognition; Deyle et al.'s RFID+vision fusion for mobile manipulation of tagged objects.

**Novelty vs prior work:** The prior-art sweep found no bin robot that addresses the return trip. SmartCan reportedly cannot return if workers misplace the can, FSU's design assumes workers reload the robot, and no study has measured post-pickup cart displacement. RFID-guided robot manipulation (Deyle et al., IROS 2009) tags the objects itself. Using a municipal cart's existing, city-installed RFID tag as a zero-modification identity source for a robot appears unstudied, and so does camera re-identification of near-identical carts for docking. The paper's first contribution, the real post-pickup displacement distribution, is a new measurement in its own right.

**Prior work cited:**
- [SmartCan (Rezzi) coverage: cannot return if the can is misplaced (Interesting Engineering)](https://interestingengineering.com/smartcan-new-automated-trash-can-drive-itself-to-the-curb-on-trash-day): The best-known commercial attempt fails exactly at return-trip re-acquisition. No measurement of displacement or re-acquisition success.
- [RF vision: RFID receive signal strength indicator (RSSI) images for sensor fusion and mobile manipulation (Deyle, Nguyen, Reynolds, Kemp, IROS 2009)](https://doi.org/10.1109/iros.2009.5354047): Fuses RFID and vision to find and manipulate objects the researchers tagged themselves. We read a tag the city already installed and compare it, by cost, with tag-free camera re-ID.
- [Toter RFID Cart Management](https://www.toter.com/services/rfid-cart-management): Manufacturer confirms an RFID tag embedded in the handle with a matching serial number. This is a fleet-tracking product, not robot perception.
- [New Fee Means San Diego's Trash Bins Are About to Get Smarter, Too (Voice of San Diego, Apr 14, 2025)](https://www.voiceofsandiego.org/2025/04/14/new-fee-means-san-diegos-trash-bins-are-about-to-get-smarter-too/): California evidence that city carts carry RFID chips assigned to an address and read by trucks. It establishes that the identity signal exists on unmodified carts. Not robotics.
- [CartSeeker cart recognition (Government Fleet, Jun 2021)](https://www.government-fleet.com/10144799/mcneilus-to-debut-zero-radius-automated-side-loader): Truck-side AI camera + LiDAR cart recognition claiming 96% success and handling 'proximity to other carts'. A vendor claim from the truck viewpoint with no published method; it does not re-identify a specific household's cart.
- [Wheelie Drive (NZ high-school bin robot, 2019 PM's Future Scientist Prize)](https://pmscienceprizes.org.nz/2019-future-scientist-media-release/): Moves an unmodified wheelie bin to the kerb. Navigation errors are reported, but there is no return-trip re-acquisition or metric.

**What the team builds:** SOFTWARE (perception student): a cart detector (shared with angle A3 or fine-tuned YOLO); an enrollment gallery of the household's carts (~50 images each); appearance re-ID with local-feature matching (ORB/SIFT on the cart body) and/or a small pretrained embedding, scored on the laptop if the Pi is too slow; RFID reader integration (SparkFun library) logging EPC and RSSI; a search behavior that spirals out from the last known pose; logging and analysis. MECHANICAL: a UHF antenna mount at handle height (~0.9-1 m) with a cable run; camera mount; integration with the hitch for re-hitch trials; the floor-grid ground-truth kit for staged trials. ETHICS: read only the team's own carts' EPCs, use neighbors' carts only with permission, publish no house numbers or faces. No human-subjects data are collected.

**Cost estimate (USD):** 814

**Cost breakdown:** VERIFIED: SparkFun Simultaneous RFID Reader M7E Hecto $309.95 (SparkFun); Raspberry Pi 5 4GB $110 (PiShop US, Apr 2026); Camera Module 3 from $25; BNO085 IMU $29.50 (Adafruit). ESTIMATES (UNVERIFIED): external UHF antenna ~$50 plus cable ~$15; Pi accessories ~$25; tape, chalk and floor grid ~$20; distractor carts borrowed at $0; shared platform ~$230. TOTAL ~$814 (+$99 if a lidar is added for re-acquisition pose; the camera pose from A3 is assumed instead). Identity-sensing costs reported in the paper: position prior $0, camera re-ID ~$25, RFID ~$375.

**Timeline:** Oct: CHECK FIRST whether the household's carts carry a readable UHF tag (the city or hauler may know; otherwise a short read test after the reader arrives). If no tag, drop baseline (c) and use a lid-color plus position prior instead. Order the reader in Oct. Begin weekly pre/post-pickup displacement measurements immediately; this needs no robot, so Oct-Feb gives ~20 weeks and ~40-60 events. Nov: enrollment images and re-ID prototype on a laptop; outreach. Dec: integrate with the robot and detector. Jan 11-Feb 14: ~150 staged trials (weekends, with borrowed carts) plus re-hitch trials once the hitch works. Feb 14 data freeze; submit by Feb 26 (deadline Mar 1).

**Target venue:** IEEE CASE 2027 (Mar 1, 2027; 6 + 2 pages). RFID identification, logistics and cost-effectiveness automation are core CASE material. Fallback: the CASE WIP track (Apr 1). Alternative: a return-trip section inside an IROS systems paper. Labs: Carpin (UC Merced; publishes at CASE), Wu (SJSU; estimation for docking/parking). Show them the real displacement histogram and the wrong-cart-rate vs. cost table.

**Main risk:** Three dependencies: (1) the household's carts may have no RFID tag, or tags may not read at the reader's range; (2) same-model carts may be too similar for cheap camera re-ID; (3) the real-pickup data are few (~25-60 events) and re-hitch trials need a working hitch. Fallbacks: drop RFID and compare position prior with camera; report the re-ID failure honestly (carts are near-identical, so identity needs RFID or a position prior), which is still useful; publish the displacement distribution plus staged perception-only trials if the hitch slips.


## A6.v1: A6. Odometry under a towed cart: how much does a 4x-varying load break cheap dead reckoning, and does a $30 add-on fix it?

**Research question:** How much does towing an unmodified cart whose mass varies week to week from ~13 kg (empty 64-gal) to ~65 kg increase the endpoint drift and heading error of a hoverboard-motor robot's wheel-encoder odometry on a sloped residential driveway? Can a $30 IMU, a ground-facing optical-flow sensor (PAA5100JE, 15-35 mm working distance) and free motor-current slip detection from FOC firmware keep drift low enough to reach the curb within 30 cm with no absolute sensor, or with only one environment fiducial at the end?

**Hypothesis:** Encoder-only drift will grow from ~1-2% of distance traveled with no cart to >=5% when towing a ~65 kg cart down a >=5% grade, dominated by heading error from asymmetric slip. IMU-aided heading will cut endpoint error by >=50%. Adding the optical-flow sensor will hold drift <=2% at all loads, so a 15-25 m driveway ends within 30 cm and a single curb-side fiducial can remove the rest. Falsified if optical flow adds <20% improvement over IMU-aided odometry under the heaviest load, or if load has no significant effect on drift (regression slope CI includes 0).

**Measurements:** Endpoint and checkpoint position error (cm) and heading error (deg), with ground truth from the laser-dot checkpoints and tape trilateration (+/-1 cm). Derived: drift as % of distance; slip ratio (encoder distance / ground-truth distance); FOC motor current and slip-detector flags. FACTORS: cart load {empty ~13-17 kg, +25 kg, +50 kg} using sandbags or water jugs weighed on a bathroom scale (within the 224/336 lb rated loads; empty masses 28 and 37.25 lb from spec sheets); cart size 64 vs 96 gal; direction (loaded downhill out, empty uphill back); surface (dry concrete, wet, painted garage floor, leaf litter); grade measured with a phone inclinometer. TRIALS: 3 loads x 2 sizes x 2 directions x 10 runs = 120 runs on the main driveway plus 40 on a second driveway. All proprioceptive sensors are logged on every run, so four estimators (encoders; +IMU; +IMU+flow; +IMU+flow+current-based slip rejection) are compared on identical runs. ANALYSIS: drift-vs-load regression with CIs; paired Wilcoxon tests between estimators; cost vs. P95 endpoint error.

**Baseline:** (1) Encoder-only odometry: the default hobby stack (the SPARC bin robot had no encoders at all). (2) A reference absolute fix on the same runs: the RTK or AprilTag configuration from angle A1 if built; otherwise checkpoint ground truth only. (3) Published: Rezende et al. 2024 (wheel odometry 'viable and cost-effective' for simple tasks); Kreinar & Quinn 2014 (odometry error estimation for a snowplow robot whose plowing load, like a cart, perturbs traction); Ross et al. 2012 (refocused optical mouse sensors for outdoor optical-flow odometry); Boxan et al. 2026 (proprioceptive baseline nearly as accurate as complex SLAM).

**Novelty vs prior work:** Optical-flow and optical-mouse odometry for slip are established (Bonarini & Matteucci 2005; Ross et al. 2012; Nagai et al. 2010), and snowplow robots have studied odometry error under plowing loads on open competition fields (Kreinar & Quinn 2014). The prior-art sweep and a Scholar search for teach-and-repeat with towing found no measurement of how a towed two-wheeled refuse cart changes a low-cost robot's dead-reckoning budget. The cart is a load that changes by about 4x every week and shifts weight onto the hitch. Nor has any study asked whether a ~$30 add-on removes the need for RTK on a short driveway. New here: load-indexed drift data for cart towing, and a cost-indexed answer to 'how little absolute sensing does a driveway need?'

**Prior work cited:**
- [Odometry error estimation for a differential drive robot snowplow (Kreinar & Quinn, IEEE/ION PLANS 2014)](https://doi.org/10.1109/plans.2014.6851482): Studies odometry error on a snowplow robot (RTK reference, per the Scholar listing). A plowing load on a competition field, not a towed refuse cart on a driveway, and no cost-indexed sensor add-ons.
- [Toward Refocused Optical Mouse Sensors for Outdoor Optical Flow Odometry (Ross, Devlin, Wang, IEEE Sensors J. 2012)](https://doi.org/10.1109/jsen.2011.2180525): Establishes outdoor optical-flow odometry that is independent of wheel slip. It does not test a towed load or price the add-on against RTK for a task.
- [Comparison of Wheel Odometry and Visual Odometry for Low-Cost Vehicle Navigation (Rezende et al., SBR 2024)](https://sol.sbc.org.br/index.php/sbrlars/article/view/34065): Finds wheel odometry viable for simple tasks, but with no load or slope. We vary towed load and grade.
- [One year in a forest (Boxan et al., 2026)](https://arxiv.org/abs/2608.27628): A proprioceptive baseline was nearly as good as complex SLAM. Forest setting, research sensors, no towed load.
- [Navigation without localisation: reliable teach and repeat based on the convergence theorem (Krajnik et al., IROS 2018)](https://arxiv.org/abs/1711.05348): Shows T&R tolerates imperfect odometry, but was never tested with a heavy towed cart, which the prior-art sweep flags as a gap.
- [ROMR: A ROS-based open-source mobile robot (HardwareX 2023)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10197097): Hoverboard-motor base with a 90 kg payload claim, tested indoors only, with no towing odometry data.

**What the team builds:** SOFTWARE (perception student): flash the EFeru hoverboard FOC firmware and read speed and current telemetry over UART; drivers for the BNO085 and PAA5100JE (the vendor Python library); an EKF (robot_localization) with switchable inputs; a current-plus-flow slip detector (flag when encoder speed exceeds flow speed by more than a threshold or current spikes); synchronized logging; analysis notebooks. MECHANICAL: a spring-loaded or skid-mounted holder that keeps the optical-flow sensor 15-35 mm off rough pavement, tested on concrete, paint and leaves; adjustable cart ballast (sandbags/water jugs) secured inside the cart, removable so the cart stays unmodified; the checkpoint laser-dot jig.

**Cost estimate (USD):** 530

**Cost breakdown:** VERIFIED: BNO085 IMU $29.50 (Adafruit 4754); Raspberry Pi 5 4GB $110 (PiShop US, Apr 2026). ESTIMATES (UNVERIFIED): PAA5100JE optical-flow breakout ~$25 x2 = $50 (Pimoroni lists the product and its 15-35 mm working distance, but no price was displayed); Pi accessories ~$25; sandbags and water jugs ~$30; bathroom scale ~$25; checkpoint tools ~$30; shared platform ~$230 (used hoverboard, frame, hitch, ESP32, e-stop). Encoders and motor current come free from the hoverboard FOC firmware. TOTAL ~$530. Add-on costs reported in the paper: IMU $29.50, flow ~$25-50, slip detection $0.

**Timeline:** Oct: order sensors; flash FOC firmware on a bench hoverboard; design the flow-sensor skid. Nov: bench and hand-pushed tests of flow-sensor tracking on concrete, wet concrete, paint and leaves (de-risking before the build); outreach. Dec: platform drives and tows the cart; EKF. Dec 21-Jan 10: pilot runs with each load; freeze the protocol. Jan 11-Feb 14: 160 runs (each about 2-3 min including re-ballasting; about 4 weekends). Feb 14 data freeze; submit by Feb 26 (deadline Mar 1).

**Target venue:** IEEE CASE 2027 (Mar 1, 2027; 6 + 2 pages): a cost-effective localization engineering result. Alternative: IROS 2027 (Mar 1) if combined with angle A1 as the 'proprioceptive rung' of a larger localization study, which is the most natural home. Labs: Nobby Kobayashi (UCSC; UGV traversability, slip and slope; a SIP 2026 host) and Carpin (UC Merced). Show them drift-vs-load curves and the cost of each fix.

**Main risk:** Two things could sink the add-on result. The optical-flow sensor may lose tracking on rough, wet or leaf-covered pavement, or its 15-35 mm working distance may change with chassis pitch under hitch load. The load effect may also be small on a typical gentle driveway, which would make the headline result 'load doesn't matter'. Fallbacks: the encoder vs. IMU-aided drift-under-load data are still the first towed-cart measurements; find a steeper driveway for the second site; if the flow sensor fails, report it as a measured negative result and keep IMU plus current-based slip detection as the low-cost fix.


## B1.v1: Mechanism instead of perception: capture envelopes of a passive self-centering hitch for unmodified 64/96-gal carts

**Research question:** A low-cost robot engages an unmodified two-wheeled refuse cart by its molded handle. How large is the region of approach error (lateral offset, yaw, approach speed) inside which a passive self-centering hitch engages with at least 90% probability, compared with a rigid U-hook of the kind in US20200023524A1? The passive hitch is 3D-printed converging V-guides, a spring-centered yaw pivot and a gravity latch, about $20 of parts. How much docking accuracy, and therefore how much sensing cost, does the difference make unnecessary?

**Hypothesis:** Across 3 cart brands, both sizes and fills of 0-90 kg, the passive hitch's 90%-capture region is at least 3x wider laterally than the rigid hook's (half-width >=10 cm vs <=3 cm) and at least 2x wider in yaw (>=15 deg vs <=7 deg). A robot whose measured terminal docking error is 5-8 cm (1 sigma) will then reach >=95% end-to-end engagement only with the passive hitch; the rigid hook needs <=2 cm error, which means LiDAR-class final approach. The hypothesis is falsified if the envelope-area ratio is <2x, if cart brand explains more variance than hitch type, or if end-to-end success with the cheapest sensing stays <90%.

**Measurements:** (1) Offset-grid engagement trials. The robot makes a blind, open-loop straight approach from a plywood start jig. Grid: lateral offset -15 to +15 cm in 2.5 cm steps x yaw 0/+-10/+-20/+-30 deg x speed 0.10/0.25 m/s. Screen with 5 reps per cell, then run 10 reps per cell in the boundary band. That is about 700 trials per hitch and about 1,400 in total (about 30 s each, about 12 h of testing). (2) Outcomes per trial: latched (limit switch plus visual check); centered within +-3 cm and +-5 deg after latching (chalk grid, overhead phone photo); cart shoved more than 10 cm (tape); peak engagement force (200-kg load cell in the hitch link); time to latch. (3) Factors: Toter, Cascade and Rehrig carts (own plus borrowed with permission); 64 vs 96 gal; added fill 0/45/90 kg of sandbags; dry concrete. Subsets: cart against a garage wall, and cart parked on a 5% slope. (4) Analysis: logistic regression of P(success) on lateral offset, yaw, speed, brand, size and fill gives 90% capture contours, with bootstrap 95% CIs and an envelope-area ratio. (5) Cost link. Measure the terminal docking-error distribution of three approach configurations, 30 approaches each: wheel/hall odometry from a taught start pose; odometry plus a hobby ultrasonic for final alignment; odometry plus an LD19-class 2D lidar (~$96-99 per prior_art.md). Convolve each distribution with each hitch's envelope to predict success. Then validate with 50 autonomous end-to-end engagements per hitch using the cheapest configuration. Report the sensing dollars needed for 95% engagement per hitch, with Wilson CIs.

**Baseline:** (1) A rigid U-hook at the same height on the same robot, modeled on the abandoned US20200023524A1 design. The team builds it, and it is the main head-to-head comparison. (2) Published precision docking that buys accuracy with expensive perception, as the 'pay for sensing instead' alternative: Xiao et al. (ICRA 2022) reach 0.03 m / 0.02 rad at close range using LiDAR on a five-sensor robot; Lei et al. (2024) reach under 5 mm with two TF40 rangefinders plus QR markers. (3) The $64.99 Garbage Commander hook (verified price), where a human does all the alignment, as the zero-autonomy cost floor.

**Novelty vs prior work:** Industry already uses passive self-alignment: MiR's pivoting gripper with two contact switches ([US12403591B2](https://patents.google.com/patent/US12403591B2/en)), Aethon's converging-funnel receiver ([US12515342B2](https://patents.google.com/patent/US12515342B2/en)) and Tractonomy's tapered guide ([US11919155B2](https://patents.google.com/patent/US11919155B2/en)). All three are indoor designs that clamp steel bars or retrofitted hitches on four-wheel carts, and none publishes a capture envelope. The residential precedents publish no data at all: the [US20200023524A1](https://patents.google.com/patent/US20200023524A1/en) handle hook, the [US10046910B2](https://patents.google.com/patent/US10046910) handle latch and [Wheelie Drive](https://pmscienceprizes.org.nz/2019-future-scientist-media-release/). The only bin-to-curb robot found that reports trial counts, [Hamzeh & Prasetyo 2026](https://jasae.org/index.php/JASAE/article/view/92), carries a 35-L bin and has no hitch. This also updates the prior_art.md gap map, which said no bin robot reports trial counts. [Whitney 1982](https://doi.org/10.1115/1.3149634) gives compliant-insertion theory, but not for a mobile robot engaging a plastic cart. This would be the first measured engagement envelope on unmodified ANSI refuse carts across brands, sizes and fills, and the first to state a hitch's tolerance as sensing dollars saved. Novelty check, 2026-10-03: OpenAlex and Crossref keyword searches found nothing equivalent. Google Scholar and IEEE Xplore keyword search could not be run because the web-search budget was exhausted.

**Prior work cited:**
- [US12403591B2: Gripping system for an autonomous guided vehicle (MiR)](https://patents.google.com/patent/US12403591B2/en): A passive pivot plus contact switches self-align the gripper on indoor four-wheel carts with a steel frame. It reports no capture-envelope numbers and does not cover plastic refuse carts.
- [US12515342B2: Adaptive mobile robot behavior based on payload (Aethon)](https://patents.google.com/patent/US12515342B2/en): Converging side members self-center the end effector, but every cart is retrofitted with a universal hitch and an ID tag. The cart is modified, and there is no tolerance data.
- [US20200023524A1: Trash and recycle bin relocation robot (abandoned)](https://patents.google.com/patent/US20200023524A1/en): Same concept: a U-hook on a linear actuator lifts the handle of an unmodified cart. It is paper only, with no docking tolerance, success rate or prototype data. It serves as the rigid-hook baseline.
- [Robotic Autonomous Trolley Collection with Progressive Perception and Nonlinear MPC (Xiao et al., ICRA 2022)](https://arxiv.org/abs/2110.06648): Reaches 0.03 m / 0.02 rad docking accuracy with five LiDAR/vision sensors, indoors. It buys precision with perception rather than mechanical tolerance, and its gripper's error tolerance is untested.
- [High-precision docking of wheelchair/beds through LIDAR and visual information (Lei et al. 2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11408198/): Two cheap rangefinders give under 5 mm docking, but the design relies on QR markers on the bed (a modification) and works indoors only. It reports no mechanical capture envelope.
- [Automated Mobile Platform for transporting a Residential Garbage Bin to the Collection Point (Hamzeh & Prasetyo, JASAE, Aug 2026)](https://jasae.org/index.php/JASAE/article/view/92): The only bin robot found with trial counts: 80 trials, 20% day / 65% night full-journey success. It carries a 35-L bin on a toy-car platform with IR boundary sensing, has no hitch, and does not use unmodified 64/96-gal carts.
- [Quasi-Static Assembly of Compliantly Supported Rigid Parts (Whitney 1982)](https://doi.org/10.1115/1.3149634): The classic theory of compliance and chamfers absorbing misalignment in insertion. It does not address a mobile robot engaging a deformable plastic cart.

**What the team builds:** Mechanical student: a hoverboard-motor differential base (Gotrax hoverboard, or a used one) with a plywood/aluminum frame and a rear caster. A mast reaches handle height, about 0.9-1.0 m; the exact height comes from measuring the carts first. Two interchangeable hitch heads: (a) a rigid U-hook; (b) PETG V-guides at 30/45/60 deg convergence, a yaw pivot on a bearing with two centering springs, and a gravity latch with a limit switch. A 200-kg load cell sits in the hitch link. A plywood start jig with angle marks and a chalk grid set up each trial. After latching, the robot tilts the cart by its own motion, so there is no lift actuator. Software student: ESP32 firmware for repeatable straight approaches at a set speed using hall-sensor odometry, plus latch and load-cell (HX711) logging. Approach scripts for the three sensing configurations. Python analysis: logistic regression, bootstrap, and Monte-Carlo convolution of the error distributions with the envelopes.

**Cost estimate (USD):** 620

**Cost breakdown:** Base robot ~$260: Gotrax hoverboard $139 (regular price on gotrax.com 2026-10-03, verified; Drift model on sale from $99); Adafruit ESP32 Feather V2 $19.95 (verified); frame, caster and fasteners ~$70 (estimate); e-stop, fuse and wiring ~$30 (estimate). Hitch heads ~$85 (estimate): PETG filament ~$20, bearings, springs and fasteners ~$30, aluminum angle ~$30, limit switches ~$5. SparkFun 200 kg S-type load cell $96.95 plus HX711 $4.95 (verified; the load cell is on backorder, and generic 200 kg cells are cheaper but UNVERIFIED). Sandbags, 4 x 50 lb, ~$30 (estimate). Jig plywood, chalk and tape ~$40 (estimate). Hobby ultrasonic ~$5 (estimate). LD19-class lidar for the expensive-sensing baseline ~$99 (Omobot BOM, per prior_art.md; the Waveshare $95.99 listing is marked discontinued). Total ~$620. Carts are borrowed, not bought.

**Timeline:** Oct 2026: measure handle height, width and profile on 3 brands x 2 sizes (borrow neighbors' carts); CAD the hitch heads; email labs (Kitts at SCU RSL for low-cost rovers; Winncy Du at SJSU for mechanism and sensors). Nov: order the hoverboard (check that its mainboard MCU is supported by the EFeru firmware), load cell and filament; print v1 guides. Dec 1-20: base drives straight under ESP32 control; build both hitch heads; run 100 pilot trials. Dec 21-Jan 10 (winter break): full offset grid on own carts, about 1,000 trials; freeze the protocol. Jan 15: go/no-go and venue checkpoint. Jan 11-Feb 7: brand, size, fill, wall and slope subsets; error distributions for the 3 sensing configurations; 100 autonomous end-to-end engagements. Feb 8-20: refill boundary cells; data freeze. Feb 15-25: write. Submit Fri Feb 26; hard deadline Mon Mar 1, 23:59 PT.

**Target venue:** IEEE/RSJ IROS 2027 (deadline Mon Mar 1, 2027, 23:59 PT; 8 pages including references). A mechanism-design paper with a quantified mechanism-vs-perception cost trade-off fits IROS's robot design and service-robot topics and the 2027 sustainability/recycling theme. Fallback: IEEE CASE 2027, same day, 6+2 pages, if the pilot results look like a narrower engineering study. A shortened version can go to an ICRA 2027 workshop as a companion.

**Main risk:** Cart geometry (handle profile, rear-wall shape) may vary more across brands than expected, or light empty carts (28-37 lb empty, per spec sheets) may get shoved away instead of being centered. Either would make the envelope small or brand-specific. Fallback: report per-brand envelopes, which is itself evidence against 'works on my bin' claims; add a cart-agnostic two-point guide; approach slower. If only one brand is available, scope the paper to two sizes plus fill levels. Note: US10046910B2 (motion-actuated handle latch) is active until about 2036. Using it in a research prototype is fine, but a commercial version needs a design-around (not legal advice).


## B2.v1: Borrowed weight: how hitch height turns a full cart's own load into traction for a sub-$300 towing robot

**Research question:** A light (about 12-15 kg) hoverboard-motor robot tows an unmodified 64/96-gal cart by its handle. Hitch height sets how far the cart tilts, and so whether the cart's weight lifts the robot or presses down on it. How does hitch height determine the vertical load transferred to the drive wheels, the drawbar pull available before the wheels slip, and success when starting uphill? Which hitch height maximizes traction margin on dry and wet driveways without adding ballast?

**Hypothesis:** (1) Transferred load follows a two-parameter static model (cart mass x CG offset, plus hitch geometry) to within +-15% or +-5 kg. It is negative (the cart lifts the robot) above the cart's balance-angle height and rises to roughly 25-40% of cart weight at low hook heights. (2) Drawbar pull at slip is about mu x (robot weight + transferred load), with a single mu per surface. (3) At the best hook height, a 12-15 kg robot with no ballast starts a cart with 135 kg of added load up a 10% grade on wet concrete in >=9 of 10 attempts. A high, non-transferring hitch needs >=40 kg of ballast to match that. (4) Traction margin peaks at an intermediate height, because at very low heights the robot's own rolling resistance and the load on the hitch mast rise faster than traction. Falsified if model error exceeds 25%, if no hook height lets the ballast-free robot start the loaded cart, or if margin is monotonic in height.

**Measurements:** (1) Static transfer. 6 hook heights spanning each cart's balance height x 64/96 gal x added fill 0/45/90/135 kg (sandbags placed low), plus one high-CG fill. Read robot axle load from two bathroom scales, cross-checked with the load cell; 3 reps, about 150 readings. Fit the model and report R^2 and RMSE. (2) Drawbar pull to slip. Hitch the robot to the cart, chock the cart's wheels and tether them to a ground anchor through the 200-kg load cell, then ramp the FOC torque command until the wheels slip. Detect slip from hall odometry and confirm on video. Surfaces: dry broom-finish concrete, wet concrete (hose), asphalt. 6 heights x 3 surfaces x 3 fills x 3 reps, about 160 pulls. (3) Uphill starts on a plywood ramp at 0/5/10/15% with grip tape, plus 2-3 real driveways whose grade is measured with an inclinometer. Start from rest; success means 2 m of travel without stalling or slip above 10%. N=10 per selected condition, about 150 trials. (4) Ballast baseline: a high, near-horizontal hitch plus sandbag ballast on the robot in 10 kg steps until success matches. (5) Secondary: Wh per 20 m trip from logged pack voltage and current. Analysis: mu per surface with 95% CI; model validation; a traction-margin map against hook height; logistic success vs grade; robot mass and motor current needed for 95% success at each geometry.

**Baseline:** (1) The same robot with a high, near-horizontal hitch (no weight transfer) plus sand ballast until it matches. This prices the mass, energy and motor-sizing penalty of ballast, and the team measures it directly. (2) The carry architecture: FAMU-FSU's platform carries 100% of the load (designed for 250 lb up a 5 deg incline; $1,980.85 BOM, including a $299 drive). (3) Human pull-force references for the same object class: IFA 4161 (32-357 N on asphalt with gradients and obstacles), Schibye 2001 (25/50 kg two-wheeled containers) and Sun 2011 (20-40 kg two-wheeled carts on 5/10 deg ramps). (4) The Garbage Commander's stated ~30% of can weight on its hook, as an external check on the model.

**Novelty vs prior work:** Weight-transfer hitches are an old agricultural idea ([Persson & Johansson 1967](https://doi.org/10.13031/2013.39801)). The effect also shows up in two refuse-cart devices: the [Garbage Commander](https://gemplers.com/products/single-can-garbage-can-hauling-hook-for-lawn-tractor-or-atv) rests about 30% of the can's weight on its hook, and the [US10046910B2](https://patents.google.com/patent/US10046910) tug tips onto the bin so its own castor lifts. Neither measures traction. No robot paper reports drawbar pull, slip or slope limits for a small robot towing a refuse cart. [ROMR](https://pmc.ncbi.nlm.nih.gov/articles/PMC10197097) claims a 90 kg payload but was tested indoors only. The [Cornell hoverboard base](https://irl.tech.cornell.edu/mobile_hoverboard_robot_base) moved a bin on a dolly under teleoperation. Human studies ([IFA 4161](https://www.dguv.de/ifa/forschung/projektverzeichnis/ifa_4161-2.jsp), [Sun 2011](https://doi.org/10.33915/etd.4801)) give forces, not robot traction. The contribution is a validated model plus measurements of how much of a cart's own weight a robot can safely borrow, and the hitch height that minimizes robot mass and cost. Novelty check: OpenAlex and Crossref keyword searches only. Google Scholar and IEEE Xplore were not searched (web-search budget exhausted).

**Prior work cited:**
- [A Weight-Transfer Hitch for Pull-Type Implements (Persson & Johansson, Trans. ASAE 10(6):847-849, 1967)](https://doi.org/10.13031/2013.39801): Establishes the weight-transfer-hitch concept for tractors pulling farm implements. It does not cover small robots, tilting two-wheeled containers, or hitch height as a cost-minimizing design variable.
- [Garbage Commander UBL-MT handle hook (Gempler's listing)](https://gemplers.com/products/single-can-garbage-can-hauling-hook-for-lawn-tractor-or-atv): Passive hook for 64/96-gal carts: raises operating height 8 in, about 30% of can weight on the arm, 75 lb operating weight, $64.99. It is towed by a human-driven tractor or ATV, and no traction or slope data are given.
- [US10046910B2: Semi-autonomous tug apparatus](https://patents.google.com/patent/US10046910): Latching makes the tug tip so its castor lifts, which is implicit weight transfer. The tug is teleoperated, and the patent gives no measured traction, slope capability, or design rule for hitch geometry.
- [ROMR: A ROS-based open-source mobile robot (HardwareX 2023)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10197097): Hoverboard-motor base costing under $1,500 with a 90 kg payload claim, tested indoors on flat floors. It has no towing, traction or slope tests.
- [IFA 4161: forces when pushing/pulling large refuse bins](https://www.dguv.de/ifa/forschung/projektverzeichnis/ifa_4161-2.jsp): Human hand forces of 32-357 N on an outdoor asphalt course with gradients and obstacles. Human operators only, with no robot-side traction.
- [Effects of Load and Gradient on Musculoskeletal Loading During Dynamic Two-Wheeled Cart Pushing and Pulling (Sun, WVU PhD, 2011)](https://doi.org/10.33915/etd.4801): 12 participants pushed and pulled two-wheeled carts with 20/30/40 kg on 5 and 10 deg ramps. It reports joint loads in humans, not robot traction or hitch geometry.
- [FAMU-FSU Robotic Trash Cart (Team 311, 2019)](https://eng-web1.eng.famu.fsu.edu/me/senior_design/2019/team311/): Carry-platform design (100% of load on the robot) for 250 lb up 5 deg with a $1,980.85 BOM. It is teleoperated, does not tow, and reports no measured traction.

**What the team builds:** A hoverboard base flashed with the EFeru FOC firmware for TORQUE mode and current telemetry (the firmware supports STM32F103/GD32F103 mainboards, so check the board before buying). An adjustable aluminum mast with a pin-hole ladder for 6 hook heights, and a handle hook. A 200-kg load cell inline. A ground anchor (an eye bolt in the slab, or a heavy fixed post), with ratchet strap and wheel chocks. A plywood ramp adjustable to 0-15% with grip tape, plus sandbags, two bathroom scales and a hose for wet tests. The software student writes the torque-ramp test script, slip detection (hall odometry vs commanded torque), logging and the Python model fitting. The mechanical student builds the mast, ramp and anchor and runs the static transfer tests.

**Cost estimate (USD):** 790

**Cost breakdown:** Base robot ~$260 (Gotrax hoverboard $139 and ESP32 Feather V2 $19.95, both verified; frame, caster and wiring ~$100, estimate). Adjustable mast and hook ~$90 (estimate). SparkFun 200 kg load cell $96.95 plus HX711 $4.95 (verified). Plywood ramp (2 sheets, lumber, grip tape) ~$180 (estimate). Sandbags, 8 x 50 lb, ~$55 (estimate). Two bathroom scales ~$40 (estimate). Anchor, strap and chocks ~$30 (estimate). Miscellaneous ~$30. Total ~$790, under the ~$1,000 flag. Ballast for the baseline uses the same sandbags, so it costs nothing extra.

**Timeline:** Oct 2026: measure cart geometry and estimate balance angles by hand; derive the transfer model in a spreadsheet; outreach (Winncy Du at SJSU for mechatronics; Kitts at SCU). Nov: order parts; build the ramp and anchor. Dec 1-20: base running TORQUE-mode firmware; adjustable mast; static transfer readings (indoors, fast). Dec 21-Jan 10: drawbar pulls on dry, wet and asphalt surfaces. Jan 11-31: ramp and real-driveway uphill starts; ballast baseline. Jan 15: checkpoint. Feb 1-20: fill gaps, then data freeze. Feb 15-25: write. Submit Feb 26 (deadline Mar 1, 23:59 PT).

**Target venue:** IEEE CASE 2027 (deadline Mar 1, 2027, confirmed on the official key-dates page; 6 pages plus 2 paid). A validated design rule with a cost-effectiveness claim (a ballast-free, sub-$300 drive tows a near-rated cart) suits automation-engineering reviewers. The CASE 2026 program lists several 'low-cost' and 'affordable' system papers. Fallback: IROS 2027, same day.

**Main risk:** The hoverboard drive may hit its current limit or overheat before the wheels slip at high transferred loads, so traction limits cannot be observed. (The EFeru config defaults I_MOT_MAX to 15 A per motor; verified in config.h.) Or a new hoverboard's mainboard may not be supported by the firmware. Fallback: report motor-limited vs traction-limited regimes, since both inform sizing; measure slip at reduced fill or on wet surfaces where mu is lower; or use a used hoverboard with a supported board, or generic BLDC controllers.


## B3.v1: Fix the driveway or the robot? Measured lip- and gutter-crossing forces for towed refuse carts, and the cheapest mitigation

**Research question:** Real residential routes have small vertical lips: garage thresholds, slab joints, heaved panels and the driveway-apron/gutter lip. What peak pull does a small robot need to get a loaded, unmodified 64/96-gal cart, and itself, over them? How well does the quasi-static wheel-on-step model predict that pull? Which mitigation gives the most crossing success per dollar: approach speed (momentum), an oblique approach (one cart wheel at a time), a compliant hitch link, or a small printed or rubber threshold ramp placed at the worst lips? How do those compare with upgrading the drive train?

**Hypothesis:** (1) Surveyed residential lips often exceed the ADA 1/4-in vertical limit; specifically, the median apron/gutter lip is >= 1/2 in. (2) The quasi-static model F/N = sqrt(2rh - h^2)/(r - h), with 10-in cart wheels, predicts peak pull within +-20% at 0.1 m/s but overpredicts it by >=30% at 0.4-0.5 m/s, because the cart's kinetic energy carries the wheels over lips of 13 mm or less. (3) A 30-45 deg oblique approach cuts peak pull by about 40%. (4) Threshold ramps costing <=$30 in total, placed at the 1-3 worst lips, let the stock hoverboard drive cross every surveyed lip type with >=95% success at 135 kg added load. Matching that by upgrading the drive alone costs more. Falsified if model error at low speed is >20%, if speed gives no reduction, or if the ramps do not reach 95%.

**Measurements:** (1) Lip survey, starting in Oct with no build needed. Measure vertical lip heights with a caliper at >=40 driveway aprons, gutter transitions and sidewalk joints along the public right-of-way, plus garage thresholds at the team's and consenting neighbors' houses. Report the distribution against the ADA 1/4-in and 1/2-in thresholds. Only objects are measured, never people. (2) Lab matrix: lip strips of 6/13/19/25 mm fixed to a plywood base plate. Added fill 0/45/90/135 kg in a 96-gal cart (64-gal subset); speed 0.1/0.3/0.5 m/s; approach angle 0/30/45 deg; rigid vs spring-compliant hitch link. A fractional factorial with 5 reps gives about 350 crossings. Per crossing: success (both cart wheels and the robot cross without stall, slip or rollback); peak and impulse of drawbar force from the load cell, with FOC phase-current telemetry at >=100 Hz as the fast proxy; wheel slip (hall odometry vs 240-fps video); cart pitch disturbance (video); energy. (3) Mitigations on the 19 and 25 mm lips: a printed PETG wedge and a commercial rubber threshold ramp. (4) Field validation: 10 crossings at each of 5 real lips on the team's route. Analysis: model vs measured (RMSE, Bland-Altman); a logistic success model in lip height, mass, speed and angle; cost of each mitigation against the success it adds; and the cheapest configuration that reaches >=95% across the surveyed lip distribution.

**Baseline:** (1) Quasi-static model predictions. prior_art.md sweep 2 estimates that a 1/2-in lip needs about 0.44-0.57 x wheel load, against 0.01-0.08 for rolling. (2) A drive upgrade: the same robot with a raised current limit or a second or larger motor pair, priced from vendor listings, as the 'fix the robot' option. (3) Published obstacle data from other vehicles: Frank & Abel 1989 measured the force to push small wheelchair castors over steps, indoors; Ikeda et al. 2018 had a two-armed robot push a specially equipped hand cart up a step. (4) Human forces on refuse bins over obstacles: IFA 4161, up to 357 N.

**Novelty vs prior work:** prior_art.md flags lip crossing as the likely motor-sizing bottleneck, yet no robot-side measurement exists for a towed refuse cart. [IFA 4161](https://www.dguv.de/ifa/forschung/projektverzeichnis/ifa_4161-2.jsp) and [Schibye 2001](https://doi.org/10.1016/s0268-0033(01)00039-0) measured humans. [Frank & Abel 1989](https://doi.org/10.1016/0141-5425(89)90040-X) measured wheelchair castors up to 200 mm diameter, indoors. [Ikeda et al. 2018](https://doi.org/10.3390/app8112114) needed a hand cart with a brake and an extendable wheel mechanism, pushed by a two-armed robot, for steps. Bin-robot builds report no terrain data ([SPARC](https://www.ece.ucf.edu/seniordesign/sp2018su2018/g12), [FSU](https://eng-web1.eng.famu.fsu.edu/me/senior_design/2019/team311/), [Hamzeh & Prasetyo 2026](https://jasae.org/index.php/JASAE/article/view/92)). The [ADA standards](https://www.access-board.gov/ada/) set code limits, but no published survey of residential driveway or gutter lips was found. New contributions: the first force vs lip height vs fill vs speed data for refuse carts, a validated sizing rule, and the first cost comparison of fixing the environment versus upgrading the robot. Novelty check: OpenAlex and Crossref only; Google Scholar and IEEE Xplore not searched (budget exhausted).

**Prior work cited:**
- [Measurement of the turning, rolling and obstacle resistance of wheelchair castor wheels (Frank & Abel, J. Biomed. Eng. 11(6), 1989)](https://doi.org/10.1016/0141-5425(89)90040-X): Measured the horizontal force needed to push wheelchair castors up to 200 mm diameter over small steps, against step height, load and wheel compressibility, on indoor surfaces. It does not cover refuse carts, towing by a robot, or outdoor lips.
- [Step-Climbing Tactics Using a Mobile Robot Pushing a Hand Cart (Ikeda et al., Applied Sciences 8(11):2114, 2018)](https://doi.org/10.3390/app8112114): A two-armed wheeled robot climbs a step with a hand cart that has a brake and an extendable wheel mechanism, so the cart is modified. The steps are stair-scale, control is over an intranet connection, and the paper analyzes mass and CG requirements. It does not measure small lips, unmodified carts or cost.
- [IFA 4161: forces when pushing/pulling large refuse bins (DGUV)](https://www.dguv.de/ifa/forschung/projektverzeichnis/ifa_4161-2.jsp): Human hand forces of up to 357 N on an asphalt course with obstacles. Human operators only, and no lip-height or speed dependence is reported in the summary.
- [2010 ADA Standards for Accessible Design, sections 303.2-303.4 (U.S. Access Board)](https://www.access-board.gov/ada/): Sets code limits (1/4 in vertical; 1/4-1/2 in beveled; more than 1/2 in must be ramped). Residential driveways are not necessarily governed by it, and it contains no measured residential lip distribution.
- [SPARC: Self-Powered Autonomous Refuse Cart (UCF Senior Design 2018)](https://www.ece.ucf.edu/seniordesign/sp2018su2018/g12): Bin carrier designed for a 50 lb load, against 224-336 lb cart ratings. It has no terrain or obstacle measurements.
- [Automated Mobile Platform for transporting a Residential Garbage Bin (Hamzeh & Prasetyo 2026)](https://jasae.org/index.php/JASAE/article/view/92): Reports trial success rates for a 35-L bin on a toy car, but no forces, lips or load effects.

**What the team builds:** A hoverboard base with a handle hitch and a swappable hitch link (a rigid bar, or a spring/elastomer compliant link). Lip strips mounted on a plywood base plate on the flat garage floor or driveway. A 200-kg load cell, with FOC current telemetry over UART logged to an SD card on the ESP32. A phone for 240-fps video against a reference grid. 3D-printed threshold wedges and one commercial rubber threshold ramp. A caliper for the survey. Mechanical student: hitch links, lip fixtures, wedges, survey. Software student: logging pipeline, synchronizing force, current and video, and fitting the model.

**Cost estimate (USD):** 630

**Cost breakdown:** Base robot ~$260 (Gotrax hoverboard $139 and ESP32 Feather V2 $19.95, both verified; frame and wiring ~$100, estimate). SparkFun 200 kg load cell $96.95 plus HX711 $4.95 (verified). Plywood base plate and hardwood lip strips ~$70 (estimate). Compliant link (springs or elastomer, hardware) ~$25 (estimate). Printed wedges (filament) ~$15 (estimate). One commercial rubber threshold ramp ~$40 (UNVERIFIED estimate). Caliper ~$20 (estimate). Sandbags ~$55 (estimate). SD logging parts ~$15 (estimate). Miscellaneous ~$30. Total ~$630.

**Timeline:** Oct-Nov 2026: lip survey (early real data that also fixes the lip set); model spreadsheet; order parts; outreach (Winncy Du at SJSU; Kitts at SCU). Dec 1-20: base, hitch and synchronized logging; pilot crossings with an empty cart. Dec 21-Jan 10: lab matrix with loads. Jan 11-31: mitigations and field validation on real lips. Jan 15: checkpoint. Feb 1-20: analysis, reruns, data freeze. Feb 15-25: write. Submit Feb 26 (deadline Mar 1, 23:59 PT).

**Target venue:** IEEE/RSJ IROS 2027 (Mar 1, 2027, 23:59 PT; 8 pages). It combines a field-terrain interaction study with model validation and a new survey dataset, which matches IROS's field and service-robot interests, and 8 pages leave room for the survey, the model and the cost comparison. Fallback: CASE 2027, same deadline.

**Main risk:** Impact peaks during lip strikes are faster than the HX711 load cell can resolve (10/80 samples per second), so peak forces would read low. Fallback: use high-rate FOC phase current, calibrated against the load cell in slow pulls, as the primary peak measure; report impulse and energy metrics; check kinematics on 240-fps video. Second risk: full-load crossings of the 25 mm lip stall every time. That bounds the drive, and the ramp mitigation then becomes the main result.


## B4.v1: Holding 170 kg on a driveway with hoverboard motors: braking, power-loss runaway and the cheapest fail-safe brake for cart-towing robots

**Research question:** A full 96-gal cart weighs about 169 kg gross (Cascade spec: 37.25 lb empty plus a 336 lb rated load). Can a reused hoverboard hub-motor drive safely hold and stop one on residential driveway grades using only electrical means: active FOC holding torque, the firmware's optional electric brake, regenerative braking, or passive phase-shorting when power is lost? Or is a mechanical fail-safe brake needed? What is the cheapest configuration that passes a holding, stopping and runaway criterion adapted from powered-wheelchair practice?

**Hypothesis:** (1) Active FOC holding works while powered (creep <10 mm over 120 s on a 15% grade). On simulated power loss, though, the stock configuration freewheels, and the robot-cart pair accelerates without bound on grades of 5% or more. (2) A normally-closed relay that shorts the motor phases on power loss (~$10-20) bounds the runaway speed to a value a back-EMF model predicts (<=0.3 m/s at 15% grade with a full cart), but cannot hold at standstill. (3) A spring-applied, servo-released friction brake (~$55 of parts) holds the full cart on a 15% grade and fails safe. (4) Regenerative braking on a long descent with a fully charged pack raises the DC bus enough to trip the hoverboard BMS, which causes exactly the power loss in (1), unless a ~$20 brake-resistor clamp is added. Falsified if the unpowered drive holds on its own, if phase-shorting fails to bound speed, or if no overvoltage or BMS trip occurs at full charge.

**Measurements:** Configurations. C0: unpowered freewheel (stock). C1: FOC active hold. C2: the EFeru ELECTRIC_BRAKE option plus regen. C3: C1 plus the phase-short relay on power loss. C4: C3 plus the spring-applied friction brake. C5: C4 plus the brake-resistor clamp. Conditions: plywood ramp at 0/5/10/15% plus 2-3 real driveways whose grade is measured with an inclinometer; added fill 0/45/90/135 kg in a 96-gal cart, with a 64-gal subset; state of charge 100% and 50%. Metrics: creep over 120 s (mm, tape plus video); stopping distance and peak deceleration from 0.3 and 0.5 m/s (240-fps video against a grid, plus IMU); terminal runaway speed and distance after a simulated power cut by kill switch, with the pair belayed by rope; peak DC-bus voltage and BMS trips during 10 m descents (logged voltage divider); motor temperature after 120 s holds (IR thermometer); cart pitch excursion at the hitch during hard stops (hitch-angle encoder), which catches cart rock-off or tip. 5 reps per condition, about 400 short trials. Analysis: per-configuration pass rates with Wilson CIs against the criterion; runaway speed vs m*g*sin(theta) fitted to the back-EMF model; dollars per configuration that passes.

**Baseline:** (1) C0 and C1, the stock hoverboard behavior that hoverboard-based robots (ROMR, the Cornell base) currently rely on. (2) Published wheelchair practice: Seki et al. 2009 (IEEE TIE) control downhill speed in power-assisted wheelchairs with regenerative braking plus dynamic braking at low speed, and powered wheelchairs typically carry spring-applied electromagnetic parking brakes. The second point is general practice and is not cited to a source. (3) FSU's $299 drive subsystem (designed for 250 lb up 5 deg) as a higher-cost drive reference. Only its spec and price are used, since its brake details are not reported.

**Novelty vs prior work:** Downhill braking has been studied for EVs and for wheelchairs ([Seki et al. 2009](https://doi.org/10.1109/TIE.2009.2014747)). Regen energy has been measured on a small student robot ([Chandra 2026](https://www.oxfordjss.org/sep-2026-vol-11-issue-2/experimental-evaluation-of-regenerative-braking-performance-in-a-small-four-wheel-drive-mobile-robot-under-variable-operating-conditions)), but that work tested no towing, holding, stopping distance or power loss. The hoverboard FOC firmware has an optional electric brake that replaces the motor's 'freewheel' ([config.h](https://github.com/EFeru/hoverboard-firmware-hack-FOC/blob/master/Inc/config.h)), and no one has characterized it under load. Static tip-over analysis of a robot with a single-axle trailer on slopes exists ([Morales et al. 2013](https://doi.org/10.1109/TMECH.2011.2181955)), but without braking or power-loss experiments. No bin-to-curb robot ([SPARC](https://www.ece.ucf.edu/seniordesign/sp2018su2018/g12), [FSU](https://eng-web1.eng.famu.fsu.edu/me/senior_design/2019/team311/), [Hamzeh & Prasetyo 2026](https://jasae.org/index.php/JASAE/article/view/92)) reports any slope-safety data, and [ROMR](https://pmc.ncbi.nlm.nih.gov/articles/PMC10197097) was tested on flat floors. This would be the first measured braking and fail-safe envelope for a low-cost robot towing a heavy unmodified cart on slopes, together with a ~$55 fail-safe brake design and pass/fail evidence. Novelty check: Crossref and OpenAlex only; Google Scholar and IEEE Xplore not searched (budget exhausted).

**Prior work cited:**
- [Novel Regenerative Braking Control of Electric Power-Assisted Wheelchair for Safety Downhill Road Driving (Seki, Ishihara, Tadakuma, IEEE TIE 56(5), 2009)](https://doi.org/10.1109/TIE.2009.2014747): Regenerative plus low-speed dynamic braking to control wheelchair speed downhill, with field tests. It does not cover a towed heavy cart, power-loss runaway, holding at standstill, BMS overvoltage, or hobby hub motors.
- [Experimental Evaluation of Regenerative Braking Performance in a Small Four-Wheel-Drive Mobile Robot (Chandra, Oxford J. Student Scholarship, Mar 2026)](https://www.oxfordjss.org/sep-2026-vol-11-issue-2/experimental-evaluation-of-regenerative-braking-performance-in-a-small-four-wheel-drive-mobile-robot-under-variable-operating-conditions): Student study of regen energy recovery against speed, payload and incline. It has no towing, slope holding, stopping-distance or power-loss tests. It is a useful precedent for student-authored braking measurements.
- [hoverboard-firmware-hack-FOC config.h (EFeru)](https://github.com/EFeru/hoverboard-firmware-hack-FOC/blob/master/Inc/config.h): Offers TORQUE mode, a 15 A default per-motor current limit, and an optional ELECTRIC_BRAKE that replaces freewheel at zero torque request. It publishes no characterization under load or on slopes.
- [Static Tip-Over Stability Analysis for a Robotic Vehicle With a Single-Axle Trailer on Slopes (Morales et al., IEEE/ASME T-Mech 18(2), 2013)](https://doi.org/10.1109/TMECH.2011.2181955): Static stability analysis of a tractor plus single-axle trailer on slopes, using simulation and a large mobile manipulator. It runs no braking, runaway or low-cost hardware experiments.
- [ROMR: A ROS-based open-source mobile robot (HardwareX 2023)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10197097): A hoverboard-motor platform tested only indoors on flat floors, with no slope, braking or fail-safe tests.
- [FAMU-FSU Robotic Trash Cart (Team 311, 2019)](https://eng-web1.eng.famu.fsu.edu/me/senior_design/2019/team311/): Designed for 250 lb up 5 deg, with a $299 drive subsystem in a $1,980.85 BOM. It is teleoperated and reports no measured braking or slope-safety results.

**What the team builds:** A hoverboard base running the EFeru FOC firmware (TORQUE mode, current telemetry, optional electric brake). A normally-closed relay module that shorts each motor's three phases when controller power drops; review the current rating and wiring with a mentor first. One spring-applied friction brake per wheel: a 3D-printed lever pressing a bicycle brake pad on the tire, held off by a hobby servo, so loss of power applies the brake. A brake resistor with a MOSFET clamp on the DC bus. A voltage divider into the ESP32 ADC. An AS5600-class hitch-angle encoder and a BNO085 IMU on the robot (nothing is mounted on the cart). An adjustable plywood ramp; a belay rope to an uphill anchor, a kill switch and an e-stop. Safety protocol: nobody downhill, start at 0 kg, a mentor present for full-load tests.

**Cost estimate (USD):** 725

**Cost breakdown:** Base robot ~$260 (Gotrax hoverboard $139 and ESP32 Feather V2 $19.95, both verified; frame and wiring ~$100, estimate). Plywood ramp ~$180 (estimate). Relay modules and wiring ~$20 (estimate). Brake parts ~$55 (estimate): 2 servos ~$25, bike brake pads ~$10, springs and hardware ~$15, filament ~$5. Brake resistor, MOSFET and TVS ~$20 (estimate). Voltage logging ~$10 (estimate). IR thermometer ~$20 (estimate). Hitch-angle encoder ~$10 (estimate). Adafruit BNO085 $29.50 (verified). Sandbags ~$55 (estimate). Belay rope, anchor and carabiners ~$35 (estimate). Miscellaneous ~$30. Total ~$725. An optional commercial electromagnetic brake as a further baseline would add an UNVERIFIED ~$60-100.

**Timeline:** Oct 2026: survey driveway grades (own and consenting neighbors'); build the back-EMF runaway model; write the safety protocol and review it with a mentor; outreach (Winncy Du at SJSU; Kitts at SCU). Nov: order parts. Dec 1-20: base, relay and brake prototypes; bench tests with wheels off the ground; voltage logging. Dec 21-Jan 10: ramp tests at low fills. Jan 11-31: full-fill, state-of-charge and real-driveway tests. Jan 15: checkpoint. Feb 1-20: repeat failures, then data freeze. Feb 15-25: write. Submit Feb 26 (deadline Mar 1, 23:59 PT).

**Target venue:** IEEE CASE 2027 (Mar 1, 2027; 6+2 pages). Safety-critical, low-cost automation with pass/fail evidence fits CASE's human-centered and practical-automation scope. Fallback: IROS 2027, same day.

**Main risk:** Safety: a runaway 170 kg cart is dangerous for two students, and power-loss or overvoltage tests can damage the BMS or the pack. Fallback: belay every trial; run power-loss tests first at 0-45 kg on the plywood ramp; extrapolate to full load with the validated back-EMF model; run full-load tests only with a mentor present. Second risk: regen never trips the BMS, so hypothesis (4) is false. That is still a reportable result, and the holding and runaway results stand on their own.


## B5.v1: The return trip is a mechanism problem: where automated trucks leave carts, and a two-sided hitch that re-engages them and sets them down upright

**Research question:** After automated-truck collection, in what poses are carts left at the curb: displacement, yaw up to 180 deg, lid open, tipped over? What fraction of those poses can a low-cost robot re-engage without human help using (a) a single-sided handle hitch, (b) a two-sided hitch (handle hook plus a front-lift saddle), and (c) a passive uprighting pusher for tipped empty carts? Separately, how reliably can the robot set a cart down at the curb (upright, lid closed, little post-release movement) with drop-release versus controlled lowering?

**Hypothesis:** (1) At least 20% of post-pickup carts are rotated more than 45 deg or displaced more than 0.5 m from where they were set. A fixed dock or a replayed path (SmartCan-style) would fail on those without re-engagement. Tipped carts are rare (<=5%). (2) A single-sided hitch re-engages <=60% of surveyed poses without repositioning. The two-sided hitch raises that to >=85%, and to >=95% with scripted repositioning, while adding <=$160 of parts. (3) Drive motion plus a ~$20 pusher uprights empty tipped carts (28-37 lb) in >=80% of attempts. (4) Controlled lowering leaves the cart upright with the lid closed in >=98% of set-downs, with post-release movement under 3 cm, which is measurably better than drop-release. Falsified if the survey shows <10% of carts displaced or rotated, if the two-sided hitch adds less than 15 percentage points, or if controlled lowering is no better than dropping.

**Measurements:** (1) Pose survey on Oct-Feb collection days (about 15-20 days). For the team's own and consenting neighbors' carts: chalk tick marks on the gutter at the set-down position, then tape and protractor measurements after the truck passes (displacement, yaw, lid open, tipped). For other carts visible from the public sidewalk on 2-3 blocks: categorical yaw (about 0/90/180 deg), lid and tipped status from photos, framed to exclude people, plates and house numbers. Target >=300 cart-events. Report the empirical distribution with bootstrap CIs. (2) Re-engagement: sample 60 poses from the measured distribution, recreate them on the team's apron and gutter, and run single-sided vs two-sided hitch with 2-3 reps per pose (about 300 trials). Metrics: success without repositioning, success with repositioning, time, path length, and failures by cause. Cart pose is given by a start jig, so the study isolates the mechanism from perception. (3) Uprighting: 40 attempts on tipped empty 64/96-gal carts. (4) Set-down: 2 strategies x 3 gutter/apron cross-slopes (0/2/5%) x 2 fills (0/90 kg) x 15 reps = 180 set-downs. Metrics: upright, lid closed, displacement and rotation after release (chalk plus tape), peak hitch load while lowering. Analysis: Wilson CIs. Headline metric: the fraction of real post-pickup events each hitch handles (with and without repositioning), and how that fraction changes with hitch cost.

**Baseline:** (1) A single-sided handle hitch, as in US20200023524A1, US10046910B2 and most prototypes; the team builds it. (2) A fixed-dock/replay model: the fraction of surveyed poses inside a SmartCan-like return window, computed from the survey. SmartCan cannot return if workers do not put the can back at the dock (Interesting Engineering). (3) The status quo in student builds: FSU's charter assumes workers return the bins into the robot, and WALLEE is designed for the truck to drop the bin back onto it. (4) Drop-release as the set-down baseline.

**Novelty vs prior work:** The return trip is the documented failure point of the best-known product, [SmartCan](https://interestingengineering.com/smartcan-new-automated-trash-can-drive-itself-to-the-curb-on-trash-day), yet no source reports how automated trucks actually leave carts. [CartSeeker](https://www.government-fleet.com/10144799/mcneilus-to-debut-zero-radius-automated-side-loader) and [Heil US11208262B2](https://patents.google.com/patent/US11208262) handle carts from the truck side. The [FSU charter](https://eng-web1.eng.famu.fsu.edu/me/senior_design/2019/team311/docs/project_charter.pdf) and [WALLEE](https://www.fau.edu/engineering/senior-design/projects/spring2022/wallee-self-driving-garbage-can) assume workers or the truck reposition the bin. Every hitch found engages from one side only: the [US20200023524A1](https://patents.google.com/patent/US20200023524A1/en) handle hook, the [US10046910B2](https://patents.google.com/patent/US10046910) handle latch, and [Wheelie Drive](https://pmscienceprizes.org.nz/2019-future-scientist-media-release/)'s front lift. No re-engagement, uprighting or set-down success rates exist; [Hamzeh & Prasetyo 2026](https://jasae.org/index.php/JASAE/article/view/92) report trials only for a 35-L carried bin. A measured post-pickup pose distribution plus a low-cost two-sided re-engagement mechanism would be new, and it targets the step where commercial attempts failed. Re-detection of the cart is left to perception work; this angle covers only the mechanical side. Novelty check: OpenAlex and Crossref only; Google Scholar and IEEE Xplore not searched (budget exhausted).

**Prior work cited:**
- [SmartCan coverage (Interesting Engineering, Oct 2019)](https://interestingengineering.com/smartcan-new-automated-trash-can-drive-itself-to-the-curb-on-trash-day): Notes that the can cannot wheel itself back unless workers put it back at the dock. Gives no data on post-pickup poses and has no re-engagement mechanism.
- [CartSeeker cart recognition for McNeilus side loaders (Government Fleet, 2021)](https://www.government-fleet.com/10144799/mcneilus-to-debut-zero-radius-automated-side-loader): Truck-side AI cart detection with a claimed 96% success. Says nothing about how carts are left after dumping and offers nothing for a home robot.
- [WALLEE: Self-Driving Garbage Can (FAU Senior Design 2022)](https://www.fau.edu/engineering/senior-design/projects/spring2022/wallee-self-driving-garbage-can): The cart is strapped into the robot chassis, which has spring-loaded wheels to absorb the truck dropping it back. It has no re-engagement of a free cart and no metrics.
- [FAMU-FSU Robotic Trash Cart project charter (2019)](https://eng-web1.eng.famu.fsu.edu/me/senior_design/2019/team311/docs/project_charter.pdf): Assumes the waste worker returns the bins into the robot, so the return trip is not handled autonomously.
- [US20200023524A1: Trash and recycle bin relocation robot (abandoned)](https://patents.google.com/patent/US20200023524A1/en): Single-sided handle hook with no data on re-engagement from arbitrary orientations, uprighting or set-down.
- [Wheelie Drive (NZ high-school project, 2019 PM's Future Scientist Prize)](https://pmscienceprizes.org.nz/2019-future-scientist-media-release/): Front-lift design for an unmodified wheelie bin. It reports navigation errors but no metrics, and has no two-sided engagement or set-down data.

**What the team builds:** A hoverboard base with a two-sided hitch: a rear handle hook with a motion-actuated latch, plus a front-lift saddle on a 12 V linear actuator for carts facing the other way. A passive uprighting pusher bar on the robot nose. Scripted repositioning maneuvers that drive around the cart. Mechanical student: hitch, saddle and pusher, and running the set-down trials. Software student: the survey protocol and data sheet, sampling poses from the empirical distribution, maneuver scripts and analysis. Survey kit: chalk, tape, protractor, phone. Neighbors are asked before their curb spots are chalked. No IRB is needed because no data about people are collected.

**Cost estimate (USD):** 565

**Cost breakdown:** Base robot ~$260 (Gotrax hoverboard $139 and ESP32 Feather V2 $19.95, both verified; frame and wiring ~$100, estimate). Rear hook and latch ~$40 (estimate). Front-lift saddle on a Progressive Automations PA-03 200-lb actuator, from $137.99 (verified; a generic 12 V actuator at ~$40-60 is an UNVERIFIED cheaper option). Relay/H-bridge driver ~$15 (estimate). Uprighting pusher ~$20 (estimate). Survey supplies ~$20 (estimate). Sandbags ~$40 (estimate). Miscellaneous ~$30. Total ~$565.

**Timeline:** Oct 2026: start the pose survey on the first collection day; it needs no build and runs weekly through Feb, giving about 15-20 days. Outreach: Carpin (UC Merced; CASE/ICRA field robotics) and Elkaim (UCSC ASL). Nov: CAD the two-sided hitch; order the actuator. Dec 1-20: base and rear hook; front saddle. Dec 21-Jan 10: set-down and uprighting trials. Jan 11-31: re-engagement trials from sampled poses. Jan 15: checkpoint. Feb 1-20: finish the survey (>=300 events), fill-in trials, data freeze. Feb 15-25: write. Submit Feb 26 (deadline Mar 1, 23:59 PT).

**Target venue:** IEEE/RSJ IROS 2027 (Mar 1, 2027, 23:59 PT; 8 pages). Real-world evidence on the step where commercial attempts failed, plus a service-robot mechanism, fits IROS's service-robot topics and the 2027 theme 'Human-Centric Robots for Sustainable Life' (recycling). The survey dataset also suits an ICRA 2027 field-robotics or long-term-deployment workshop as a companion.

**Main risk:** There may be too few or unrepresentative collection events: holiday schedule shifts, rain, few consenting neighbors, or a route where workers set carts back carefully. Any of these narrows the pose distribution. Also, some cart brands may lack a front feature the saddle can lift. Fallback: widen the categorical photo survey to more blocks (public view only). If carts are almost always returned well, report that as a finding that weakens the SmartCan critique, and shift weight to the set-down and uprighting results. If there is no reliable front feature, replace the saddle with scripted repositioning to the handle side and report its time cost.


## B6.v1: The motors are the scale: sensorless mass and balance-angle estimation of unmodified carts from the tilt maneuver

**Research question:** The robot already tilts the cart back onto its wheels in a maneuver of about 3 s. During that maneuver, can hub-motor current plus a hitch-angle encoder estimate the cart's gross mass and balance angle (the tilt at which its center of gravity sits over the axle) well enough to set safe speed, braking and slope limits? The target is mass within +-10 kg and balance angle within +-3 deg. Does this match a $100 load-cell hitch, and does it remove the need for per-cart tags or databases, which are not allowed on unmodified carts?

**Hypothesis:** The pull needed to hold the cart at tilt theta follows tau(theta) proportional to m*g*(a*cos(theta) - h*sin(theta)). So the zero crossing of the current-vs-tilt curve gives the balance angle, and its amplitude gives m*a. After a one-time torque-constant and friction calibration with known sandbag loads, current-only estimates reach RMSE <=8 kg over 0-135 kg of added load and <=3 deg on balance angle. That is within 1.5x the error of a load-cell estimator. Fill-adaptive limits built on these estimates cut mean trip time for light carts by >=20% compared with fixed worst-case limits, with no increase in stalls, overspeeds or slip events on a sloped driveway. Falsified if current-only RMSE exceeds 15 kg or 6 deg, or if adaptive limits increase incidents.

**Measurements:** (1) Calibration: known sandbag loads; fit the torque constant and friction per motor, recording motor temperature. (2) Estimation trials: 64/96 gal x 8 added loads (0-135 kg in about 20 kg steps) x 2 fill distributions (sandbags low vs boxes stacked high, to vary CG height) x 2 surfaces (concrete, asphalt) x 2 grades (0% and about 5%) x 5 tilts. About 640 tilt maneuvers at about 10 s each including reset. Most of this can run in the garage regardless of weather. (3) Ground truth: gross mass from bathroom scales under the cart (cross-checked with sandbag counts). Balance angle from hand-tilting the cart to balance, read with a phone inclinometer held against the cart or from video; nothing stays on the cart. (4) Estimators compared: E1, motor current plus hitch-angle encoder (no added force sensor); E2, a 200-kg load cell in the hitch link; E0, no estimate (assume the rated 224/336 lb). (5) Downstream test: 40 garage-to-curb trips on a sloped driveway, fixed worst-case limits vs fill-adaptive limits. Metrics: trip time, stalls, overspeed, slip events, peak hitch load. Analysis: RMSE, bias and Bland-Altman of E1 and E2 against truth; error vs grade and surface; paired Wilcoxon tests with effect sizes on trip metrics; and a cost-accuracy plot (dollars vs kg of error).

**Baseline:** (1) E2, the load-cell hitch (SparkFun 200 kg load cell $96.95 plus HX711 $4.95, verified), which the team builds alongside E1. (2) E0, the worst-case assumption every current bin robot effectively makes (SPARC was designed for 50 lb). (3) The industrial alternative of reading a tag and looking up a per-cart database (Aethon US12515342B2), not allowed on unmodified carts, as the conceptual baseline. (4) Vehicle-scale RLS mass estimation (Vahidi et al. 2005, within 5% with sufficient excitation) as the accuracy reference.

**Novelty vs prior work:** Online mass estimation is standard for road vehicles ([Vahidi et al. 2005](https://doi.org/10.1080/00423110412331290446), recursive least squares on longitudinal dynamics). [Hyland, Xiao & Onal (CASE 2025)](https://doi.org/10.1109/CASE58245.2025.11163849) estimate the CoM direction of unknown payloads by adaptive pushing with a holonomic robot that carries a force sensor and an RGB camera. [Aethon US12515342B2](https://patents.google.com/patent/US12515342B2/en) adapts robot behavior to payload by reading a tag and looking up a database entry for a retrofitted cart. No work found estimates a towed two-wheeled container's mass and balance angle from the tilt maneuver using only the drive's BLDC current, with no added force sensor or tag. Bin robots assume a fixed design load ([SPARC](https://www.ece.ucf.edu/seniordesign/sp2018su2018/g12): 50 lb, against 224-336 lb ratings in the [Cascade 96 spec](https://www.hampton-pa.gov/DocumentCenter/View/4016)). The method gives payload-aware towing at no added hardware cost and puts a dollar figure on the accuracy trade-off. Novelty check: OpenAlex and Crossref only; Google Scholar and IEEE Xplore not searched (budget exhausted).

**Prior work cited:**
- [Onboard Sensing and Pushing of Unknown Payload for CoM Estimation with a Holonomic Mobile Robot (Hyland, Xiao, Onal; IEEE CASE 2025)](https://doi.org/10.1109/CASE58245.2025.11163849): Estimates only the CoM direction, by pushing with a force sensor plus an RGB camera on a holonomic robot. It does not cover towed two-wheeled carts, mass, current-only sensing or a tilt maneuver. It shows the topic fits CASE.
- [Recursive least squares with forgetting for online estimation of vehicle mass and road grade (Vahidi, Stefanopoulou, Peng; Vehicle System Dynamics 43(1), 2005)](https://doi.org/10.1080/00423110412331290446): Vehicle-scale mass and grade estimation, within 5% given sufficient excitation, using a full powertrain model. It does not address towed containers, hobby BLDC drives, or CG/balance-angle estimation.
- [US12515342B2: Adaptive mobile robot behavior based on payload (Aethon)](https://patents.google.com/patent/US12515342B2/en): Adapts the robot to payload by reading a tag on a retrofitted cart and looking up hitch height, size and maximum weight in a database. Requires a cart modification; it does not measure.
- [SPARC: Self-Powered Autonomous Refuse Cart (UCF 2018)](https://www.ece.ucf.edu/seniordesign/sp2018su2018/g12): Fixed 50 lb design load with no load sensing or adaptation, against 224-336 lb cart ratings.
- [Cascade 96-Gallon Universal Cart spec sheet](https://www.hampton-pa.gov/DocumentCenter/View/4016): Gives 37.25 lb empty and a 336 lb rated load, the range any estimator must cover. It is a spec sheet, not an estimation method.

**What the team builds:** A hoverboard base running the EFeru FOC firmware (TORQUE mode, phase-current telemetry over UART at >=50 Hz). A fixed-height handle hook; the robot tilts the cart by pulling the handle back. An AS5600-class magnetic hitch-angle encoder and a BNO085 IMU on the robot. An inline 200-kg load cell for E2, with ESP32 logging. A Python estimator that least-squares fits tau(theta) and finds the zero crossing, plus an adaptive limit table. Sandbags, stacked boxes and bathroom scales. Software student: telemetry, estimator, adaptive limits. Mechanical student: hook and encoder mount, calibration rig, test matrix.

**Cost estimate (USD):** 590

**Cost breakdown:** Base robot ~$260 (Gotrax hoverboard $139 and ESP32 Feather V2 $19.95, both verified; frame and wiring ~$100, estimate). Hook and mast ~$60 (estimate). SparkFun 200 kg load cell $96.95 plus HX711 $4.95 (verified). Adafruit BNO085 $29.50 (verified). Magnetic encoder ~$10 (estimate). Two bathroom scales ~$40 (estimate). Sandbags and boxes ~$60 (estimate). Miscellaneous ~$30. Total ~$590.

**Timeline:** Oct 2026: derive the tau(theta) model and check identifiability in a spreadsheet; outreach (Carpin at UC Merced; Wencen Wu at SJSU). Nov: order parts (check the hoverboard mainboard MCU). Dec 1-20: base, hook, encoder and telemetry; calibration. Dec 21-Jan 10: estimation matrix in the garage, unaffected by weather. Jan 11-31: surfaces, grades and adaptive-limit trips. Jan 15: checkpoint. Feb 1-20: analysis, reruns, data freeze. Feb 15-25: write. Submit Feb 26 (deadline Mar 1, 23:59 PT).

**Target venue:** IEEE CASE 2027 (Mar 1, 2027; 6+2 pages). CASE 2025 accepted the closely related onboard CoM-estimation-by-pushing paper (Hyland et al.), so the topic and the 'sensorless, zero-cost payload awareness' framing match CASE reviewers. Fallback: IROS 2027, same day.

**Main risk:** Hoverboard phase current may be a poor torque proxy near zero speed, because of cogging, static friction, temperature drift and noisy current sensing on cheap boards; E1 errors would then be too large. Fallback: an in-situ two-point calibration with the empty cart on every trip; lean on the zero-crossing (balance angle), which does not depend on the torque constant; or present E1 as the cheap end of a cost-accuracy curve and recommend E2 at $102. Also check that the hoverboard's mainboard is supported by the EFeru firmware (STM32F103/GD32F103) before buying.


## C1.v1: Cost-reliability frontier: the minimum viable bin robot

**Research question:** On one hoverboard-drive platform, five complete sensing and compute stacks are built, costing roughly $335 to $1,150 in hardware. Which is the cheapest stack whose end-to-end round-trip success (garage to curb with an unmodified 64/96-gal cart, then back) is statistically equivalent to the most expensive stack? And at which tier does a cost-normalized metric (successful round trips per $100 of BOM) peak?

**Hypothesis:** C3 (Pi 5, one camera, odometry/IMU and 2-3 printed environment markers; about $545) is within 10 percentage points of C5 (C4 plus an RTK GNSS pair; about $1,150) on round-trip success. The equivalence is tested with TOST using a ±10-point margin and n=25 per configuration. Success per $100 peaks at C3. C1 (ESP32-only dead reckoning plus ultrasonic curb stop) scores below 70% success. The hypothesis is falsified if C5 beats C3 by more than 10 points, or if C1 or C4 has the highest success per $100.

**Measurements:** Configurations, all sharing the drive, the passive hitch and the safety stop:
- C1: ESP32-S3, hub-motor odometry, IMU, taught dead-reckoning route, 2 ultrasonic sensors.
- C2: C1 plus Pi 5 and Camera Module 3, running visual teach-and-repeat and camera cart detection.
- C3: C2 plus printed AprilTags on the garage wall and a curb stake. These are environment markers, not bin markers, and their cost is counted.
- C4: C3 plus an RPLIDAR C1.
- C5: C4 plus a ZED-F9P RTK base and rover.

Metrics:
- Round-trip success (binary): the cart ends inside the municipal placement envelope and the robot re-parks in the garage box with no human touch.
- Curb placement error: distance to the curb and lateral offset (cm), plus cart yaw (deg, handles toward the street side as the city requires). Measured with a chalk grid and tape.
- Round-trip time (s), energy (Wh, INA228 at the battery) and number of interventions.

Trials:
- n=25 round trips per configuration at the primary driveway (125 total), stratified by light (day/dusk), cart size (64/96 gal) and fill (empty, or about 25 kg of sandbags).
- n=10 per configuration at a second driveway (50 total).
- About 175 round trips, roughly 30 h.

Analysis:
- Wilson 95% CIs per configuration; Newcombe CIs for the difference from C5; TOST equivalence test.
- Pareto front of success and placement error against BOM dollars.
- Cost-normalized metrics: successful round trips per $100 and dollars per percentage point of success.
- HardwareX-style BOM with purchase dates and assembly hours.
- Pearce savings S=(P-O)/P against named comparators.

**Baseline:** In-study expensive baseline: C5 (RTK + lidar + camera + markers), built and run on the same driveways under the same protocol, so the comparison is matched.

External baselines from published numbers:
- Hamzeh & Prasetyo 2026: 35-L bin, ESP32 + IR, 80 trials, 20% day and 65% night full-journey success.
- BOMs of SPARC (~$809), GRAD ($507) and FSU ($1,980.85), none of which reports performance.
- Price anchor for a commercial RTK+vision yard robot: Segway Navimow i105N at $799-1,000.

All external figures come from the linked sources. No rebuild is needed.

**Novelty vs prior work:** Existing cost-performance Pareto fronts are:
- car-scale and computed on datasets (Collin & Terán Espinoza: a ~$27k suite reaches ~99% of the best on KITTI);
- design-space proxies (Putnam's NSGA-II thesis);
- formal co-design evaluated in simulated scenarios (Zardini et al. 2022).

Low-cost robot papers argue cost from an itemized price list and do not ablate what each dollar buys (Omobot at AIM 2024, MuSHR, ROMR). In Baltazar et al. 2024 the RTK pair is about 62% of a $2,900 BOM, but RTK was never removed and re-tested.

New prior art found in this pass: Hamzeh & Prasetyo (JASAE 2026) report 80 trials of a bin-transport robot. **This contradicts prior_art.md's claim that no bin robot reports trial counts.** However, they test one configuration, a 35-L bin and one driveway, with no cost axis.

Our OpenAlex/Crossref searches (2026-10-03) found no hardware-measured cost-vs-task-success frontier for a home service robot, and none for unmodified municipal carts.

This angle differs from a localization-only cost ladder. The metric is end-to-end success, including hitching, towing, curb placement and return, and the tiers also vary compute, down to an MCU-only robot.

**Prior work cited:**
- [Collin & Terán Espinoza, Resilient Sensor Architecture Design and Tradespace Analysis for Autonomous Vehicle Localization and Mapping (2019)](https://arxiv.org/abs/1907.08541): Car-scale ($27k-$110k) suites evaluated on the KITTI dataset with an uncertainty proxy. We use $335-$1,150 stacks and physical end-to-end task trials.
- [Putnam, Multi-Objective Generation of Pareto-Optimal Perception Architectures for Autonomous Robotic Systems (MIT thesis, 2025)](https://dspace.mit.edu/entities/publication/14e39e72-b071-4fa9-8f0c-c539c4119fce): Optimizes a perception-coverage proxy against monetary cost in design space (Jackal, ANYmal). We measure real task success on built hardware.
- [Zardini, Suter, Censi, Frazzoli, Task-driven Modular Co-design of Vehicle Control Systems (2022)](https://arxiv.org/abs/2203.16640): Formal monotone co-design yielding Pareto-optimal designs, illustrated on urban driving scenarios, with no physical trials. We measure the frontier empirically.
- [Hamzeh & Prasetyo, Automated Mobile Platform for transporting a Residential Garbage Bin to the Collection Point (JASAE 2026)](https://jasae.org/index.php/JASAE/article/view/92): One configuration (toy-car base, ESP32, IR boundary), a 35-L bin, 80 trials (20% day / 65% night), no cost analysis. We test five cost tiers on unmodified 64/96-gal carts.
- [Baltazar et al., Development of a Robotic Platform with Autonomous Navigation System for Agriculture (AgriEngineering 2024)](https://mdpi-res.com/d_attachment/agriengineering/agriengineering-06-00192/article_deploy/agriengineering-06-00192.pdf): The RTK pair is ~62% of a $2,900.22 BOM, but no with/without-RTK ablation was run. RTK is one removable tier in our design.
- [Omobot: a low-cost mobile robot for autonomous search and fall detection (IEEE AIM 2024)](https://arxiv.org/abs/2408.05315): $693 itemized, date-stamped BOM, but no measurement of the performance lost without each component.
- [SPARC: Self-Powered Autonomous Refuse Cart (UCF Senior Design 2018)](https://www.ece.ucf.edu/seniordesign/sp2018su2018/g12): ~$809 GPS + camera + curb-stake bin carrier with no success rate or placement error. Its BOM is used only as a price comparator.

**What the team builds:** Mechanical student:
- Hoverboard hub-motor chassis running the open FOC firmware.
- Passive self-centering handle hitch (same on all tiers).
- Quick-swap sensor brackets so a configuration changes in under 10 min.
- E-stop.
- Curb stake and garage-wall tag mounts.

Software/perception student:
- One ROS 2 stack with configuration flags.
- C1: dead-reckoning route replay on the ESP32.
- C2: open-source visual teach-and-repeat plus a small cart detector trained on the team's own cart images.
- C3: AprilTag-aided EKF.
- C4: lidar curb and cart ranging.
- C5: RTK fusion.
- Logging: rosbag plus INA228 energy, and a phone form for trial outcomes.

Both students: placement-envelope chalk grid and the trial protocol.

**Cost estimate (USD):** 1150

**Cost breakdown:** Shared core, about $334:
- Used hoverboard (motors, mainboard, battery): est. $70, UNVERIFIED (range $40-100)
- ST-Link programmer: est. $10
- IMU: est. $25
- Adafruit INA228: $14.95 (adafruit.com/product/5832, 2026-10-03)
- Frame, casters and fasteners: est. $100
- Passive hitch parts: est. $40
- E-stop, fuses, wiring, DC-DC: est. $50
- Seeed XIAO ESP32-S3 Sense: $13.99 (seeedstudio.com, 2026-10-03)
- 2 ultrasonic sensors: est. $10

Cumulative cost by tier:
- C1 ≈ $334.
- C2 adds a Raspberry Pi 5 4GB at $130 (adafruit.com/product/5812, 2026-10-03; prices have risen, and the 8GB is $200), SD card/cooler/5 V converter at est. $40, and Camera Module 3 from $25 (raspberrypi.com). C2 ≈ $529.
- C3 adds printed tags and a stake at est. $15. C3 ≈ $544.
- C4 adds an RPLIDAR C1 at $79.99 (waveshare.com, 2026-10-03). C4 ≈ $624.
- C5 adds 2 ArduSimple simpleRTK2B Basic Starter Kits at $263.75 each (prior_art.md). C5 ≈ $1,151.

The whole study needs only the C5 parts, about $1,150. **FLAG: over $1,000.**

Cheaper options:
- Use a free NTRIP correction service instead of buying a base, if one is available locally (UNVERIFIED). Total about $890.
- Drop the RTK tier entirely. Total about $625.

Carts: the team's own and neighbors' carts, no cost.

**Timeline:** - **Oct 2026:** fix the configurations, the placement envelope (from the team's city's collection rules) and the success definition. Pre-register hypotheses in a dated document. Email Carpin (UC Merced) and Kitts (SCU) with a one-page protocol.
- **Nov:** order the RTK kits and lidar by mid-Nov. Flash the FOC firmware and run bench drive tests. Build the logging stack.
- **Dec 1-20:** the chassis and hitch drive. C1 runs.
- **Dec 21-Jan 10:** integrate C2-C3. 20 pilot trials. Freeze the protocol.
- **Jan 15:** go/no-go checkpoint and decision between IROS and CASE.
- **Jan 16-Feb 20:** 175 trials, about 30 h on weekends and dusk weekdays.
- **Feb 21-26:** analysis, Pareto figure, BOM table, draft. Submit Feb 26.
- **Mar 1, 23:59 PT:** hard deadline.

**Target venue:** IEEE/RSJ IROS 2027 (deadline Mar 1, 2027, 23:59 PT; 8 pages including references). The 2027 theme ('Human-Centric Robots for Sustainable Life', which includes recycling) and the 'service robots' topic fit. The 8 pages leave room for the configuration × trial matrix and the cost tables. Backup: IEEE CASE 2027 (also Mar 1), if reviewers would read it as an automation cost-effectiveness study.

**Main risk:** Integrating and running five full stacks is the heaviest build of any angle, and C2/C3 visual teach-and-repeat may not be robust by mid-January. Fallbacks:
- Shrink to three tiers (C1, C3, C5) with n=30 each.
- If full autonomy is unreliable at the Jan 15 checkpoint, report the frontier per sub-task (exit, curb placement, return re-acquisition) instead of whole round trips.
- RTK false fixes near the garage (as Tavasci et al. 2024 reported near facades) would be a reportable result, not a failure of the study.


## C2.v1: How much compute does a slow cart-towing robot need? Latency tolerance vs. board cost

**Research question:** Camera-guided docking to an unmodified cart and curb-stop placement are tested at 0.2-0.6 m/s. Up to what end-to-end perception latency, and down to what update rate, does success stay at or above 95%? Which is the cheapest compute board that stays inside that envelope: XIAO ESP32-S3 ($13.99), Pi 5 CPU ($130), Pi 5 + AI HAT+ (+$70) or Jetson Orin Nano Super ($249 MSRP)?

**Hypothesis:** At 0.4 m/s, docking success stays at or above 95% up to at least 300 ms added latency and down to 2-5 Hz updates. A CPU-only Pi 5, and possibly the ESP32-S3, therefore sits inside the envelope. Accelerators (AI HAT+, Jetson) give no statistically significant gain in task success (Fisher exact test, n=20 per board) but draw more power.

The hypothesis is falsified if:
- success at 0.4 m/s falls below 90% at 200 ms or less; or
- the Pi 5 CPU board is significantly worse than the Jetson on task success.

**Measurements:** Part A, controlled injection, on the fastest available board:
- Added latency Δ ∈ {0, 100, 200, 400, 800, 1600} ms and update-rate cap f ∈ {15, 5, 2, 1, 0.5} Hz, applied by a ROS 2 delay/drop node.
- Approach speed v ∈ {0.2, 0.4, 0.6} m/s.
- Start poses on a grid 2 m from the cart (±0.3 m lateral, ±20° yaw).
- 6Δ × 3v × n=10 = 180 docking trials, plus 5f × 2v × n=10 = 100. These are about 1-2 min each, so roughly 10 h.
- Curb-stop placement: a matching smaller block of 60 trials.

Part B, native boards:
- Glass-to-command latency measured with an LED-flash method (an LED in camera view; trigger timestamp vs motor command; ~1 ms resolution).
- Throughput (Hz) and power (W, from the INA228).
- n=20 docking trials per board at 0.4 m/s (80 total).

Metrics:
- First-attempt hitch engagement (contact switch).
- Lateral and yaw error at engagement (mm, deg; floor grid plus photo).
- Curb-stop error (cm).
- Docking time (s).

Analysis:
- Logistic regression of success on Δ·v and f; tolerance envelope (latency at 95% success, with bootstrap CI).
- Validate a kinematic model adapted from Falanga et al.: tolerable latency as a function of speed and hitch capture width.
- Curves of success, latency and watts against board price.

**Baseline:** Expensive compute baseline:
- The Jetson Orin Nano Super with zero injected latency.
- If no Jetson is bought, the Pi 5 + AI HAT+ is the fast tier.

The conventional way to choose compute, from the published dataset benchmarks used for comparison (Ultralytics):
- YOLO26n at 67 ms on a Pi 5 CPU (NCNN).
- YOLO26n at 4.57 ms on a Jetson Orin Nano Super (TensorRT FP16).

This angle tests whether a 15x gap in dataset latency matters for task success.

**Novelty vs prior work:** Latency-vs-speed analysis exists for fast aerial robots:
- Falanga et al. (RA-L 2019): maximum safe speed vs perception latency for quadrotor sense-and-avoid.
- Krishnan et al. (IEEE CAL 2020): the F-1 roofline linking frame rate, compute and body dynamics for aerial robots.
- MAVBench (MICRO 2018): compute effects on drone missions in closed-loop simulation.

Compute benchmarks measure only latency and throughput:
- RobotPerf benchmarks ROS 2 computational graphs, not task success.
- Alqahtani et al. and Rey et al. benchmark detectors on Pi/Jetson using datasets. Rey et al. conclude that the Pi 5 fails real-time needs for drones.
- Park et al. (Frontiers 2025) study the accuracy-latency trade-off on a Jetson AGX Orin with no task.

Our OpenAlex/Crossref searches (2026-10-03) found no study that measures task-level latency tolerance for a slow ground robot docking with, and towing, a passive cart. None maps such a tolerance onto board price and power either.

This is a systems question: how slow perception can be. It is not a detector-accuracy question.

**Prior work cited:**
- [Falanga, Kim, Scaramuzza, How Fast Is Too Fast? The Role of Perception Latency in High-Speed Sense and Avoid (IEEE RA-L 2019)](https://doi.org/10.1109/LRA.2019.2898117): Theory plus quadrotor experiments at high speed, with event cameras. No cost axis and no docking or towing. We adapt the latency-speed reasoning to slow docking and measure it on four price-tiered boards.
- [Krishnan et al., The Sky Is Not the Limit: A Visual Performance Model for Cyber-Physical Co-Design in Autonomous Machines (IEEE CAL 2020)](https://doi.org/10.1109/LCA.2020.2981022): Roofline model for aerial robots. We measure the ground-robot task envelope empirically.
- [MAVBench: Micro Aerial Vehicle Benchmarking (MICRO 2018)](https://arxiv.org/abs/1905.06388): Compute's effect on drone mission energy and performance in closed-loop simulation. We test physical ground trials with a towed load.
- [RobotPerf: An Open-Source, Vendor-Agnostic Benchmarking Suite for Robotics Computing System Performance](https://arxiv.org/abs/2309.09212): Measures ROS 2 graph latency and throughput across hardware, not robot task success.
- [Rey et al., A Performance Analysis of YOLO Models for Deployment on Constrained Computational Edge Devices in Drone Applications (2025)](https://arxiv.org/abs/2502.15737): Dataset benchmark that finds the Pi 5 fails drone real-time needs. We test whether this holds for a 0.4 m/s cart robot by measuring task success.
- [Ultralytics guide: Raspberry Pi (YOLO benchmarks)](https://docs.ultralytics.com/guides/raspberry-pi/): Per-image inference latency only (67 ms on a Pi 5 CPU). No closed-loop task.
- [Park, Kim, Ko, Real-time open-vocabulary perception for mobile robots on edge devices: accuracy-latency trade-off (Frontiers in Robotics and AI 2025)](https://doi.org/10.3389/frobt.2025.1693988): Accuracy-latency trade-off on a single high-end Jetson AGX Orin with no task outcome or price axis.

**What the team builds:** Software/perception student (owns most of this angle):
- Latency-injection and frame-drop ROS 2 node.
- LED-flash latency rig.
- Cart detector trained on 300-500 photos of the team's own carts (no people), ported to Pi 5 CPU (NCNN), AI HAT+ (Hailo) and Jetson (TensorRT).
- A minimal handle/edge detector on the ESP32-S3.
- Docking controller.

Mechanical student:
- Docking test rig: floor grid and repeatable start-pose fixtures.
- Hitch with a contact switch for automatic success logging.
- Board and camera mounts with an identical field of view across boards.
- Drive platform.

**Cost estimate (USD):** 885

**Cost breakdown:** - **Platform at C2 level:** about $529 (itemized in angle 1), including the Pi 5 4GB ($130, Adafruit, 2026-10-03), Camera Module 3 (from $25) and the XIAO ESP32-S3 Sense ($13.99).
- **Raspberry Pi AI HAT+:** from $70 (raspberrypi.com, 13 TOPS Hailo-8L).
- **Jetson Orin Nano Super:** $249 MSRP (NVIDIA blog, Dec 2024). Seeed listed a bundle at $450.30 on 2026-10-03, so price is volatile.
- **USB camera for the Jetson:** est. $30.
- **LED and timing parts:** est. $5.

Total ≈ $885 at MSRP and about $1,085 at the bundle price. **FLAG: the bundle price exceeds $1,000.** Options: borrow a Jetson from the school or a lab, or drop it and use the Pi 5 + AI HAT+ as the fast tier (about $635).

**Timeline:** - **Oct 2026:** finalize the latency grid and model. Start collecting cart images (weekends).
- **Nov:** order the AI HAT+ and Jetson (or arrange a loan). Train the detector. Bench-measure each board's latency with the LED rig. This needs no robot, so it is early data.
- **Dec:** drive base, hitch with contact switch, docking controller on the Pi 5.
- **Winter break:** injection node, docking rig, 30 pilot docks.
- **Jan 15:** checkpoint.
- **Jan 16-Feb 7:** Part A (about 340 short trials).
- **Feb 8-20:** Part B native boards (80 trials) and power logs.
- **Feb 21-26:** fit the model, write, submit Feb 26.
- **Mar 1:** deadline.

**Target venue:** IEEE/RSJ IROS 2027 (Mar 1, 2027, 23:59 PT; 8 pages). The low-cost compute and system-integration framing has a precedent there (RaGNNarok, IROS 2025, used a Pi 5). Backup: CASE 2027 (Mar 1). Companion: an ICRA 2027 workshop paper (deadlines about Mar-Apr, estimate).

**Main risk:** A null result: docking might succeed at every latency, because the final approach is slow or because ultrasonic sensors take over at close range.

Fallbacks:
- Extend speeds to 0.8-1.0 m/s.
- Add a disturbance: the cart is nudged during the approach.
- Disable ultrasonic assistance in Part A to find the knee of the curve.

A clean result that compute is not the bottleneck, so the $14-$130 board suffices, is still publishable with the model.

Secondary risk: Jetson price and availability. Borrow one or drop it.


## C3.v1: Standby, not motion: power architecture for a robot that works four minutes a week

**Research question:** A bin robot runs one or two garage-to-curb round trips a week. What share of its weekly battery energy goes to standby rather than motion? Four power architectures are compared:
- always-on Pi 5;
- Pi 5 halted with the RTC wake alarm;
- an ESP32 supervisor that hard-switches the Pi;
- MCU-only.

Which one minimizes battery and charging hardware cost while still waking reliably on collection night without a charging dock?

**Hypothesis:** With an always-on Pi 5, standby exceeds 90% of weekly energy. Raspberry Pi docs give 800 mA as the 'typical bare-board active' current (about 4 W). At that draw, a stock hoverboard pack (est. ~150 Wh, UNVERIFIED) empties in under 3 days.

With wake-alarm halt (~3 mA per Pi docs) or supervisor hard-switching:
- standby falls below 10% of weekly energy;
- weekly energy drops at least 10×;
- the stock pack covers at least 4 collection weeks without charging;
- scheduled-wake success is at least 29/30.

The hypothesis is falsified if motion energy exceeds standby energy even for the always-on design, or if sleep architectures fail more than 1 in 30 wakes.

**Measurements:** 1. **Trip energy:** INA228 at the battery, logged at 100 Hz or faster. Wh per round trip across cart fill (empty, ~25 kg, ~50 kg of sandbags inside the cart) × 2 driveways with different grades, n=10 per cell (60 trips). Normalized to Wh/(kg·m).
2. **Standby power:** a 72-h log for each of the 4 architectures, including DC-DC converter quiescent draw and the hoverboard mainboard/BMS off-state draw.
3. **Self-discharge:** 14-day rest test.
4. **Wake reliability:** 30 scheduled wakes per sleep architecture, recording time-to-ready and failures.
5. **Cold-morning runs:** if temperatures allow.

Analysis:
- Weekly budget E_week = n_trips·E_trip + 168 h·P_standby.
- The crossover duty cycle at which standby equals motion energy.
- Minimum battery capacity for 1, 2 and 4 weeks of autonomy, with a 2× margin and 80% depth of discharge.
- Cost per architecture: battery, supervisor, and charging dock if needed.
- 5-year cost per round trip: BOM, replacement battery, and electricity at the household's own tariff.

**Baseline:** In-study baseline:
- The always-on Pi 5 architecture, which is what typical hobby ROS stacks do (inference).
- The consumer practice of a charging dock, as robotic mowers use. The team costs it with a real quote, and it is UNVERIFIED here.

Published reference points:
- Mei et al. (2005): motion was under 50% of a Pioneer 3DX's power.
- Hou et al. (2018): milliwatt-level sensor and control power on a Mecanum robot.

The team measures all four architectures on the same robot.

**Novelty vs prior work:** Prior energy studies concern robots that run continuously or energy during motion:
- Mei et al. (ICAR 2005): non-motion consumers matter for a continuously operating Pioneer.
- Hou et al. (Energies 2018): models sensor, control and motion energy while moving.
- MAVBench: compute affects drone mission energy.
- McNulty et al. (J. Power Sources 2022): battery packs for 24/7 industrial AMRs.

No bin robot reports any energy data; prior_art.md's gap (e) notes that no Wh-per-trip figures exist under a towed load. Our OpenAlex searches for standby energy and duty-cycle battery sizing of mobile robots (2026-10-03) found no measured energy budget for a very-low-duty-cycle service robot, where standby rather than motion dominates. The new contributions are:
- a measured crossover duty cycle;
- a cost-optimal power architecture for weekly-duty robots.

**Prior work cited:**
- [Mei, Lu, Hu, Lee, A case study of mobile robot's energy consumption and conservation techniques (ICAR 2005)](https://doi.org/10.1109/ICAR.2005.1507454): Power models of a continuously running Pioneer 3DX, where motion is under 50% of power. We study a robot idle >99.9% of the week, with a weekly energy budget and battery cost.
- [Hou, Zhang, Kim, Energy Modeling and Power Measurement for Mobile Robots (Energies 2018)](https://doi.org/10.3390/en12010027): Models energy during movement of a Mecanum robot with milliwatt-level electronics. Not a duty-cycle, standby or Linux-SBC-dominated scenario.
- [MAVBench: Micro Aerial Vehicle Benchmarking (MICRO 2018)](https://arxiv.org/abs/1905.06388): Compute-to-total-energy relationship for drones in flight. Our compute energy matters while the robot is idle, not while it is moving.
- [McNulty et al., A review of Li-ion batteries for autonomous mobile robots (J. Power Sources 2022)](https://doi.org/10.1016/j.jpowsour.2022.231943): Battery packs for 24/7 industrial AMRs. We size the battery for 4 minutes of work per week.
- [Raspberry Pi documentation: RTC wake alarm (rtc.adoc)](https://github.com/raspberrypi/documentation/blob/master/documentation/asciidoc/computers/raspberry-pi/rtc.adoc): States the wake-alarm low-power state is ~3 mA with POWER_OFF_ON_HALT=1. This is a vendor figure that we verify on the robot under real wiring.
- [Raspberry Pi documentation: power supplies (typical bare-board active current, Pi 5: 800 mA)](https://github.com/raspberrypi/documentation/blob/master/documentation/asciidoc/computers/raspberry-pi/power-supplies.adoc): A vendor typical figure. We measure the actual standby and idle draw within the robot's full power chain.

**What the team builds:** Mechanical/hardware student:
- Battery and BMS integration.
- Fused power distribution with a MOSFET load switch for the compute rail.
- Optional separate 12 V LiFePO4 compute pack for comparison.
- Sandbag fill rig.
- Weather enclosure.

Software student:
- ESP32-S3 supervisor firmware (RTC schedule, watchdog, load switching).
- Pi 5 wake-alarm configuration.
- Synchronized energy logger (2× INA228).
- Weekly-energy model and cost/TCO notebook.

The drive platform is shared.

**Cost estimate (USD):** 625

**Cost breakdown:** - **Platform at C2 level:** about $529 (itemized in angle 1; Pi 5 4GB $130 at Adafruit, 2026-10-03).
- **Second Adafruit INA228:** $14.95 (adafruit.com/product/5832).
- **MOSFET load switch or relay:** est. $10.
- **Pi 5 RTC backup cell:** est. $5.
- **12 V ~6 Ah LiFePO4 compute pack:** est. $45, UNVERIFIED.
- **Sandbags:** est. $20.

Total ≈ $625. Optional extra: a charging-dock quote, costed but not bought.

**Timeline:** - **Oct 2026:** write the energy model. Order the INA228s, ESP32 and LiFePO4. Read the hoverboard pack label for its capacity.
- **Nov:** bench standby measurements of all 4 architectures on a bench supply. This needs no robot, so it is the earliest real data. Write the supervisor firmware.
- **Dec:** the platform drives, with the energy logger installed.
- **Winter break:** 72-h standby logs on the robot, wake-reliability trials. These run unattended over the break.
- **Jan 15:** checkpoint.
- **Jan 16-Feb 14:** 60 trip-energy runs on 2 driveways.
- **Feb 15-20:** self-discharge results, TCO model.
- **Feb 21-26:** write, submit.
- **Mar 1:** deadline.

**Target venue:** IEEE CASE 2027 (regular papers due Mar 1, 2027; 6 pages + 2 paid). Its topics include 'Sustainability and green automation', which suits a focused energy and cost-of-ownership study. Work-in-progress track Apr 1, 2027 (4 pages, not in Xplore) as a fallback. Alternatively, fold this in as a section of the angle 1 or angle 4 IROS paper.

**Main risk:** Reviewers may see standby dominance as obvious engineering, which lowers impact.

Mitigations:
- Generalize to a measured duty-cycle design rule across 3 compute tiers.
- Report the hidden standby draws: hoverboard mainboard, BMS and DC-DC converters.
- Tie the result to battery and dock cost per round trip.

Technical risk: the stock hoverboard BMS may not allow a clean low-power state. If so, add the separate compute pack and measure the BMS drain as a finding.

Fallback: publish as one section of the main paper rather than standalone.


## C4.v1: Field reliability across driveways: failure taxonomy and reliability growth of a sub-$700 bin robot

**Research question:** One frozen robot configuration (~$545-$665) is run on at least six real California driveways that differ in length, grade, surface and garage geometry, with unmodified 64/96-gal carts. Pooled across sites:
- What round-trip success rate and mean number of round trips between interventions (MRBI) does it achieve?
- Which failure classes dominate?
- Which surveyed driveway features predict failure?
- How fast does reliability grow across fix iterations?

**Hypothesis:** - Pooled round-trip success is at least 90%, with the Wilson 95% lower bound at 80% or higher.
- MRBI is at least 10.
- At least 60% of interventions fall in two classes: hitch engagement, and localization at the garage mouth or curb.
- Failure odds rise with grade and with lips over 6 mm.
- Over at least 3 fix iterations, a Crow-AMSAA fit shows reliability growth (β<1).

The hypothesis is falsified if pooled success is below 80%, if no two classes account for 60% or more of failures, or if grade and lip height show no association.

**Measurements:** Site survey per driveway:
- Length (m) and grade (% at 3 points, digital level).
- Lip and crack heights (mm), surface, garage width, overhead cover, curb type.

Trials:
- 20 round trips per driveway, mixing 64/96-gal carts, empty/half fill and day/dusk light. With 6 driveways that is 120 or more trips.
- From mid-January, real collection-night runs at the team's homes (about 5 weeks × 2 carts = about 10). These include the return trip after the crew displaced or rotated the cart.

For every intervention, log:
- Timestamp and phase: exit garage, transit, curb approach, placement, unhitch, re-acquire, return, re-park.
- Failure class, adapted from Carlson & Murphy: effector/drive, power, sensor, control/software, environment.
- Minutes to recover and dollars to fix.

Analysis:
- Wilson CIs per site and pooled.
- MRBI with a Poisson CI.
- Pareto chart of failure classes.
- Mixed-effects logistic regression (site as random effect; grade, length, lip height and light as fixed effects).
- Crow-AMSAA reliability-growth fit across the Dec-Feb build log.
- Weekly human minutes compared with the timed manual chore in the team's own household.
- Cost per successful round trip.

**Baseline:** Published baselines:
- Hamzeh & Prasetyo 2026: 80 trials at one driveway with a 35-L bin; 20% day and 65% night full-journey success. This is the only bin-transport robot with reported trial numbers that we found.
- Senior-design robots (SPARC, GRAD, FSU): no trial data.
- Carlson & Murphy: field-UGV mean time between failures of 6-20 h.
- CartSeeker: 96% truck-side pickup success claimed (industry reference).

Internal baseline: the team's own early-version robot is the start of the reliability-growth curve.

**Novelty vs prior work:** Bin-robot work offers either no trials (SPARC, GRAD, FSU, Wheelie Drive) or a single site with a small carried 35-L bin (Hamzeh & Prasetyo 2026). Long-term-autonomy deployments report hours and kilometers, mostly indoors:
- STRANDS: 104 days and 116 km.
- TritonBot: 108.7 h and 9.9 km.
- Carlson & Murphy: MTBF and a failure taxonomy for USAR and military UGVs.
- Boxan et al. 2026: a year at one forest site.

We found no multi-site reliability study, failure taxonomy or reliability-growth analysis for a low-cost residential service robot handling unmodified municipal carts. Nor have we found one that regresses failure on measured site features, which is what generalizing beyond one driveway needs. These are 'first measured' claims, as prior_art.md recommends.

**Prior work cited:**
- [Hamzeh & Prasetyo, Automated Mobile Platform for transporting a Residential Garbage Bin to the Collection Point (JASAE 2026)](https://jasae.org/index.php/JASAE/article/view/92): One driveway, a 35-L bin on a toy-car base, IR line navigation, 80 trials. No failure taxonomy, no site comparison, no unmodified municipal carts.
- [Carlson & Murphy, How UGVs physically fail in the field (IEEE T-RO 2005)](https://doi.org/10.1109/TRO.2004.838027): Failure taxonomy and an MTBF of 6-20 h for USAR/military UGVs. We adapt the taxonomy to a low-cost residential robot and add site-feature regression.
- [Hawes et al., The STRANDS Project: Long-Term Autonomy in Everyday Environments (IEEE RAM 2017)](https://doi.org/10.1109/MRA.2016.2636359): Long-term indoor security and care deployments of expensive platforms. Reports autonomy duration, not per-task success across sites, and no cost.
- [Wang & Christensen, TritonBot: First Lessons Learned from Deployment of a Long-Term Autonomy Tour Guide Robot (RO-MAN 2018)](https://doi.org/10.1109/ROMAN.2018.8525845): An indoor tour-guide robot deployment studying failure modes. Not outdoor, not multi-site, no physical object handling.
- [Boxan et al., One year in a forest: Analyzing the challenges of autonomous navigation in subarctic environments (2026)](https://arxiv.org/abs/2608.27628): Long-duration, single-site forest navigation. Finds simple proprioceptive baselines competitive. No residential task and no cost axis.
- [Wheelie Drive (NZ high school, 2019 PM's Future Scientist Prize)](https://pmscienceprizes.org.nz/2019-future-scientist-media-release/): Closest concept (unmodified wheelie bin), but reports only anecdotal navigation failures and no metrics.

**What the team builds:** One frozen configuration, likely angle 1's C3: Pi 5, camera, odometry/IMU, printed garage and curb tags, passive hitch. Any working configuration is acceptable.

Mechanical student:
- Weatherproofing for California winter rain.
- A robot that breaks down to fit in a car trunk.
- Spares kit (second used hoverboard).
- Portable tag stake.

Software student:
- Automatic phase labeling in logs.
- Phone intervention-logging form.
- Per-site setup script (teach run, tag survey).
- Analysis notebook (Wilson CIs, mixed-effects logistic regression, Crow-AMSAA fit).

Homeowners give written permission. No people are recorded: cameras face the driveway, and incidental passers-by are blurred or deleted.

**Cost estimate (USD):** 665

**Cost breakdown:** - **C3-level robot:** about $544 (itemized in angle 1; Pi 5 4GB $130 Adafruit 2026-10-03; Camera Module 3 from $25; XIAO ESP32-S3 $13.99; INA228 $14.95).
- **Spare used hoverboard for parts:** est. $50, UNVERIFIED.
- **Spare fuses and connectors:** est. $15.
- **Laser distance meter and digital level for site surveys:** est. $40.
- **Rain cover:** est. $15.

Total ≈ $665. Transport to driveways is by family car (not costed).

**Timeline:** - **Oct 2026:** recruit 6-8 driveways (family, friends, teachers) with written permission, and draft the survey sheet. Ask a teacher or mentor to confirm that no IRB is needed (no data about people is collected).
- **Nov:** order parts, write the logging and taxonomy definitions. Contact Carpin (UC Merced; outdoor Nav2, CASE) and Kitts (SCU field robotics) for evaluation-design feedback.
- **Dec:** build. The reliability-growth log starts on day one of driving.
- **Winter break:** home-driveway tuning; 3 fix iterations logged.
- **Jan 15:** freeze the configuration.
- **Jan 16-Feb 20:** 2 driveways per week (about 3 h each), plus weekly real collection-night runs.
- **Feb 21-26:** write.
- **Mar 1:** submit.

**Target venue:** IEEE/RSJ IROS 2027 (Mar 1, 2027, 23:59 PT; 8 pages). Real-world multi-site deployment evidence of a service robot fits the 2027 'Human-Centric Robots for Sustainable Life' and recycling theme, and the honest reliability numbers show what a low-cost robot actually delivers. Backup: CASE 2027 (Mar 1). Companion: an ICRA 2027 field-robotics workshop poster (deadline about Apr, estimate).

**Main risk:** The robot may not be reliable enough to start multi-site trials until late January, and rain may cancel sessions.

Fallbacks:
- Run 3-4 driveways × 20 trips. Low success numbers with a failure taxonomy are still novel.
- Make reliability growth at the home driveway the central result.
- Use rain days as a reported condition rather than a cancellation, if safe.

Permission and privacy risks are mitigated by homeowner consent and no recording of people.


## C5.v1: A ~$150 portable test course for residential cart robots: does it predict the driveway?

**Research question:** A portable test course costing about $150 is built from low-cost artifacts in the style of ASTM F45 and NIST. Its six elements are:
- offset-grid docking to an unmodified cart;
- plywood grade ramps from 0 to 10%;
- lips at ADA threshold heights (6 and 13 mm);
- a curb mock with a chalk placement grid;
- a turn-around box the size of a garage footprint;
- re-acquisition of a displaced cart.

Can the course predict real-driveway round-trip success across robot configurations accurately enough to replace most field testing?

**Hypothesis:** Field success is predicted for each configuration-driveway pair from course element pass rates combined with each driveway's surveyed features (grade, lip height, length). The predictions:
- match observed success within ±10 percentage points mean absolute error across 12 or more pairs;
- rank configurations identically at every site;
- need 25% or less of the field testing hours.

The hypothesis is falsified if the MAE exceeds 15 points or if the rankings disagree at more than one site.

**Measurements:** Course:
- Elements E1-E6, each with a written pass criterion.
- 4 configurations deliberately spanning capability: C1 MCU dead reckoning, C2 camera, C3 camera plus markers, C4 plus lidar.
- n=10 per element per configuration: 240 short trials, about 12 h.
- Test-retest: half the elements repeated on another day.

Field:
- The same 4 configurations × 3-4 driveways × n=8 round trips: 96-128 trips, about 16 h.

Metrics:
- Course: element pass rate, docking capture envelope (success vs lateral and yaw offset), maximum grade and lip passed with a loaded cart, placement error (cm).
- Field: round-trip success and failing phase.
- Testing cost: person-hours and dollars per evaluation.

Analysis:
- Predicted vs observed calibration plot, MAE and Brier score.
- Per-element predictive value: which elements explain field failures.
- Rank agreement.
- ICC for course repeatability.
- Release of drawings, protocol and reference results.

**Baseline:** Main baseline: real-driveway field testing, the expensive gold-standard evaluation the course aims to replace. The team runs it for every configuration.

Method baseline: the generic field-robot test course plan of Norris & Patterson (2019), which is offered without validation data, and NIST's industrial A-UGV docking and navigation test methods.

**Novelty vs prior work:** NIST and ASTM F45 test methods for docking and navigation explicitly use 'low cost artifacts' in place of expensive measurement systems. They target industrial A-UGVs in factories and warehouses (Bostelman et al., SPIE 2016; NIST IR 8140; NIST IR 8407).

Other test-method work:
- A BSI-listed service-robot standard covers locomotion of wheeled robots. Its content was not read here.
- Norris & Patterson (2019) propose generic field-robot course layouts without validation data.

Our OpenAlex/Crossref searches (2026-10-03) found:
- no test method for residential outdoor cart-moving robots;
- no study that validates a cheap test course against real deployment outcomes for any home service robot.

The contributions are a task-specific protocol and a measurement of its predictive validity and cost savings.

**Prior work cited:**
- [Bostelman, Hong, Legowik, Mobile robot and mobile manipulator research towards ASTM standards development (SPIE 2016)](https://doi.org/10.1117/12.2228464): F45 navigation and docking test methods using low-cost artifacts for industrial vehicles. We target residential outdoor cart robots and test whether course results predict field results.
- [Bostelman & Hong, Review of Research for Docking Automatic Guided Vehicles and Mobile Robots (NIST IR 8140, 2016)](https://doi.org/10.6028/NIST.IR.8140): Literature review supporting F45 docking standards for industrial settings (tray stations, trailers, pallets). Not outdoor, not passive two-wheeled refuse carts.
- [Yoon, Bostelman, Virts, Experiments to test the A-UGV capabilities standard (NIST IR 8407, 2021)](https://doi.org/10.6028/NIST.IR.8407): Tests an industrial A-UGV capability-reporting guide. No residential task and no predictive validation against deployments.
- [Norris & Patterson, System-Level Testing and Evaluation Plan for Field Robots: A Tutorial with Test Course Layouts (Robotics 2019)](https://doi.org/10.3390/robotics8040083): Proposes generic safety, communications and behavior test courses. No validation data and no cost analysis.
- [Robotics. Performance criteria and related test methods for service robots: Locomotion for wheeled robots (BSI listing; content not read)](https://doi.org/10.3403/30283324): Generic wheeled-robot locomotion tests (title-level only). Not task-specific to towing carts or curb placement, and no evidence it was validated against field outcomes.
- [2010 ADA Standards (U.S. Access Board), changes in level (6 mm / 13 mm thresholds)](https://www.access-board.gov/ada/): Source for the course's lip heights. Not a robot test method.

**What the team builds:** Mechanical student (owns most of this angle):
- Two plywood ramps adjustable to 0, 5, 8 and 10% grade.
- Removable 6 mm and 13 mm lip strips.
- A 15 cm curb mock.
- Start-pose fixtures for docking offsets.
- Chalk/tape placement grid.
- Displaced-cart fixtures.
- The drive platform and quick-swap sensor brackets for the 4 configurations.

Software student:
- Configuration switching.
- Automatic scoring from logs and phone video against the floor grid.
- Prediction model (pass rates × site features → field success).
- Statistics (Brier score, ICC).
- Open release of the protocol.

**Cost estimate (USD):** 775

**Cost breakdown:** - **C4-level robot:** about $624, so the lidar configuration exists (itemized in angle 1; RPLIDAR C1 $79.99 at Waveshare, 2026-10-03; Pi 5 4GB $130 at Adafruit; XIAO ESP32-S3 $13.99).
- **Course, about $150:** 2 plywood sheets est. $90, 2×4 lumber est. $25, lip strips est. $15, chalk/tape/grid est. $20.

Total ≈ $775.

**Timeline:** - **Oct 2026:** define elements and pass criteria from the cart specs, municipal placement rules and ADA thresholds.
- **Nov:** build the course in one weekend. Check course repeatability by pushing a cart by hand. Contact Carpin (CASE) and Elkaim (UCSC; low-cost Nav2 robots) for feedback.
- **Dec:** robot build.
- **Winter break:** course runs of the early configurations (C1, C2).
- **Jan 15:** checkpoint.
- **Jan 16-Jan 31:** 240 course trials.
- **Feb 1-20:** field runs on 3-4 driveways.
- **Feb 21-26:** prediction analysis, write.
- **Mar 1:** submit.

**Target venue:** IEEE CASE 2027 (Mar 1, 2027; 6 + 2 pages). Automation science and engineering reviewers value test methods and evaluation cost, and the venue fits a standards-flavored contribution. Backup or companion: an ICRA 2027 workshop on benchmarking or field robotics (deadlines about Mar-Apr 2027, estimate).

**Main risk:** The four configurations may not separate enough for a meaningful prediction test, and the course may predict field outcomes poorly.

Fallbacks:
- Increase the spread by also varying speed.
- If prediction is weak, report which elements do and do not predict, which is still a useful partial validation, together with the released protocol and reference results.

Impact risk: test-method papers can seem less exciting. Mitigate by quantifying the evaluation cost saved.


## C6.v1: The ~$60 safety layer: detecting obstacles and stopping while towing a loaded cart

**Research question:** Obstacle test pieces are adapted from the ANSI/ITSDF B56.5 test methods developed at NIST. What is the cheapest sensing-plus-braking configuration that:
- detects these pieces in the robot's path, by day and at night; and
- stops the robot and its towed, loaded 96-gal cart before contact?

And how much do towed mass and a driveway downgrade lengthen the stopping distance?

**Hypothesis:** A layer costing $60 or less (bump switch, 3 waterproof ultrasonics, 3 single-point ToF sensors):
- detects every in-path test piece at 0.6 m or more, by day and at night;
- gives zero contacts at up to 0.4 m/s with a full 96-gal cart on a downgrade of 5% or less.

The $80 2D lidar is needed only for low objects (under 10 cm) or side-entering objects. Going from an empty to a full cart lengthens stopping distance by at least 30% at 0.6 m/s on the downgrade.

The hypothesis is falsified if the cheap layer misses any in-path piece at 0.4 m/s or below, or if towed mass changes stopping distance by less than 10%.

**Measurements:** All sensors are logged simultaneously on every run, so each configuration's detection is scored offline from identical runs. Configurations: bump switch, ultrasonic array, ToF array, RPLIDAR C1, camera + detector on Pi 5 + AI HAT+, and fused combinations.

Test pieces (inanimate only):
- upright cylinder (child-leg proxy);
- horizontal cylinder lying on the driveway;
- low foam object (pet-size);
- black and white covers to vary reflectivity;
- a string-pulled side-entering object.

Conditions:
- Position: center, edge, 30° side entry.
- Light: sun, dusk, night.
- Speed: 0.2, 0.4, 0.6 m/s.

Detection runs: a fractional design with n=5 per cell, about 180 runs.

Closed-loop stop trials, for the 2 best configurations:
- 3 speeds × 3 towed masses (empty, half, full with sandbags) × flat or ~5% downgrade, n=8 per cell, about 144 runs.
- Crushable foam pieces reveal any contact.

Nuisance-stop rate: measured over 50 or more normal round trips.

Metrics:
- Detection probability and range (m).
- Reaction latency (ms).
- Stopping distance (cm; chalk marks and 60 fps phone video).
- Contact yes/no.
- False-stop rate per round trip.
- Cost ($).

Analysis:
- Logistic detection models (object height, reflectivity, light).
- Regression of stopping distance on speed, towed mass and grade.
- Maximum safe speed per configuration, with zero contacts and a 95% upper bound from the rule of three.
- Cost-safety Pareto front.

**Baseline:** In-study expensive tier: RPLIDAR C1 fused with a camera detector on a Pi 5 + AI HAT+, about $150 of extra sensing and acceleration.

External references:
- NIST B56.5-oriented obstacle tests with industrial 3D range cameras and laser scanners (Bostelman et al. 2005, 2009, 2013).
- Consumer outdoor-robot practice: Rasmussen et al. (2023) tested 19 robotic lawn mowers. Apart from one single incident, all mowers had to physically touch a hedgehog carcass to detect it.

The bump-switch-only configuration replicates that contact-based practice inside the study.

**Novelty vs prior work:** NIST's B56.5 test-method work evaluates obstacle detection for indoor industrial AGVs. It uses expensive sensors and no towed passive load (Bostelman et al. 2005/2013; Shackleford & Bostelman 2009). Other related work:
- Bell et al. (IFAC 2016) map AGV standards onto outdoor orchard robots without taking measurements.
- Salvini et al. (ACM THRI 2021) argue that ISO 13482 lacks protection for pedestrians and bystanders in public spaces. A bin robot crosses a sidewalk.
- Rasmussen et al. (2023) test mower collisions, with no towing and no cost axis.

None of the bin robots in prior_art.md reports any safety testing. We found no measured cost-vs-safety frontier for a low-cost robot that tows a heavy passive cart, and no measurement of how a towed load and a downgrade lengthen its stopping distance.

**Prior work cited:**
- [Bostelman, Hong, Madhavan, Experiments toward non-contact safety standards for automated industrial vehicles (SPIE 2005)](https://doi.org/10.1117/12.602334): Tests a 3D range camera on objects sized per US and British AGV standards, statically and indoors. No towed load, no cost frontier.
- [Bostelman, Norcross, Falco, Marvel, Development of standard test methods for unmanned and manned industrial vehicles used near humans (SPIE 2013)](https://doi.org/10.1117/12.2019063): B56.5 test methods for detecting humans and obstacles in manufacturing facilities. We adapt them outdoors to a sub-$1k residential robot with a towed cart.
- [Shackleford & Bostelman, Data collection test-bed for the evaluation of range imaging sensors for ANSI/ITSDF B56.5 (2009)](https://doi.org/10.1145/1865909.1865942): Records whether obstacles in front of a moving vehicle were detected by 3D LIDAR, sonar and 2D LMS. Industrial vehicle, no cost axis, no towing.
- [Bell, MacDonald, Ahn, Scarfe, An Analysis of AGV Standards to Inform the Development of Mobile Orchard Robots (IFAC 2016)](https://doi.org/10.1016/j.ifacol.2016.10.086): Hazard analysis mapping EN 1525 and B56.5 onto outdoor robots. No experimental measurement.
- [Salvini, Paez-Granados, Billard, On the Safety of Mobile Robots Serving in Public Spaces (ACM THRI 2021)](https://doi.org/10.1145/3442678): Argues that ISO 13482 lacks bystander requirements. Position paper without measurements. We supply measured detection and stopping data.
- [Rasmussen et al., Testing the Impact of Robotic Lawn Mowers on European Hedgehogs and Designing a Safety Test (Animals 2023)](https://doi.org/10.3390/ani14010122): 19 commercial mowers; in all but one incident detection required physical contact. No towing, no cost-vs-sensor comparison. This is our consumer-practice baseline.

**What the team builds:** Mechanical student:
- Front bumper with microswitches.
- Sensor bar holding 4 waterproof ultrasonics, 3 ToF sensors, the lidar and the camera.
- Test pieces: PVC pipe, pool-noodle and foam crush pieces.
- String-pull side-entry rig.
- Sandbag-loaded cart.
- A tether and E-stop for slope trials.

Software student:
- Synchronized multi-sensor logger.
- Staggered ultrasonic firing to avoid crosstalk.
- Stop controller using regenerative braking and current limits in the FOC firmware.
- Offline detection scoring.
- Video-based stopping-distance measurement.
- Statistics.

**Cost estimate (USD):** 835

**Cost breakdown:** - **Platform at C2 level:** about $529 (itemized in angle 1; Pi 5 4GB $130 Adafruit 2026-10-03; Camera Module 3 from $25).
- **4 waterproof ultrasonics:** est. $40.
- **3 VL53L1X ToF breakouts:** est. $45.
- **RPLIDAR C1:** $79.99 (Waveshare, 2026-10-03).
- **Raspberry Pi AI HAT+:** from $70.
- **Bumper microswitches:** est. $10.
- **Test pieces:** est. $40.
- **Sandbags:** est. $20.

Total ≈ $835. The cheap safety layer being tested is about $60 of that (switches, ultrasonics, ToF): est., UNVERIFIED unit prices.

**Timeline:** - **Oct 2026:** draft the test protocol from the openly published NIST papers. Try to get the test-piece dimensions in B56.5 / ISO 3691-4 via a mentor or library, since the standards are paywalled.
- **Nov:** order sensors. Bench-characterize detection by pushing the sensor bar on a hand cart, by day and at night. This needs no robot.
- **Dec:** platform and bumper.
- **Winter break:** logger and stop controller; pilot runs.
- **Jan 15:** checkpoint.
- **Jan 16-Feb 5:** detection runs in day, dusk and night.
- **Feb 6-20:** stopping trials and nuisance-stop round trips.
- **Feb 21-26:** write.
- **Mar 1:** submit.

**Target venue:** IEEE/RSJ IROS 2027 (Mar 1, 2027, 23:59 PT; 8 pages). Safety of service robots near the public is a reviewer concern for any home robot, and a measured cost-safety frontier is a strong application result. Backup: CASE 2027 (Mar 1), whose topics include human-centered automation.

**Main risk:** The exact B56.5 / ISO 3691-4 test-piece dimensions and pass criteria are paywalled and UNVERIFIED here.
- Fallback: use sizes described in openly available NIST papers, justify them explicitly, and frame the tests as 'adapted from'.

The tests themselves carry physical risk: a 100+ kg robot-and-cart system on a slope.
- Mitigations: tether, E-stop, gentle grades only, crushable test pieces, and no people or animals in tests.
