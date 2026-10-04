## Prior-art sweep #3: Localization, curb detection and bin detection outdoors on a budget

Scope: this sweep covers how a cheap ground robot could (1) localize on a residential driveway between garage and curb, (2) detect the curb or road edge, (3) detect and estimate the pose of an unmodified 64/96-gal wheeled cart, and (4) keep working on the same weekly route through seasons and lighting changes. Wherever a source reported them, accuracy and sensor-cost numbers are recorded so the team can build an accuracy-vs-cost argument.

Each entry ends its "Who / when" line with a **Link check** tag. "opened" means the URL was fetched and the claims were read on the page. "search snippet" means a web-search result returned that URL with a snippet confirming the claim, but the page itself was not readable (403, paywall, or captcha). Anything labeled *Inference* is our own reasoning and not a sourced fact.

---

### A. Outdoor visual-SLAM benchmarks (verifying ROVER and DIDLM)

#### [ROVER: A Multi-Season Dataset for Visual SLAM (arXiv 2412.02506)](https://arxiv.org/abs/2412.02506)
- Type: dataset / paper
- Who / when: Schmidt, Daubermann, Mitschke, Blessing, Meyer, Enzweiler, Valada (Esslingen Univ. of Applied Sciences and Univ. of Freiburg, with ANDREAS STIHL AG as industrial partner). arXiv Dec 2024, v3 Jul 2025. Published in IEEE Transactions on Robotics, vol. 41, pp. 4005-4022, 2025. Project page: [iis-esslingen.github.io/rover](https://iis-esslingen.github.io/rover). Link check: opened (abs + HTML v3).
- What it does / claims: the platform is a prototype robotic lawn mower driven at 0.5 m/s. Sensors are a Joy-IT Pi Camera (monocular, 640x480, rolling shutter), an Intel RealSense D435i (RGB-D + IMU), an Intel RealSense T265 (stereo fisheye + IMU) and a VectorNav VN100 IMU. Ground truth comes from a Leica TS16 total station (mm-level). The dataset has 39 recordings at 5 locations (park, campus, two gardens) in all four seasons and at day, dusk and night, totaling 7.2 km and 311 min. It evaluates OpenVINS, VINS-Fusion, ORB-SLAM3, SVO Pro, DROID-SLAM, DPVO and DPV-SLAM. Findings: stereo-inertial and RGB-D do best in good light with moderate vegetation, and most systems perform poorly in low light and high vegetation, especially in summer and autumn. Example: DROID-SLAM (D435i RGB-D) had 0.32 m ATE by day and 5.62 m at night. Monocular deep methods (DPVO, DPV-SLAM) showed scale problems in larger areas, and VINS-Fusion produced no valid trajectories in several configurations.
- Cost or price info (with source) if any: the paper gives no prices. Sensor prices were not verified in this sweep.
- Relevance to our bin-to-curb robot: this is the closest published benchmark to a residential yard and driveway (garden-scale, mower-height camera). It shows that a $-class camera running visual SLAM is unreliable at night and dusk, which matters because carts usually go out the evening before or the early morning of trash day.
- Gap: no paved driveway or curb segment, no towed or pushed load, no cost-vs-accuracy analysis, and no simple non-SLAM baselines (wheel odometry + fiducial, RTK).

#### [DIDLM: A SLAM Dataset for Difficult Scenarios Featuring Infrared, Depth Cameras, LIDAR, 4D Radar, and Others under Adverse Weather, Low Light Conditions, and Rough Roads (arXiv 2404.09622)](https://arxiv.org/abs/2404.09622)
- Type: dataset / paper
- Who / when: Gong, He, Su, Li, Wu, Z. J. Wang. arXiv v1 Apr 2024, v2 Jan 2025, v3 Mar 2026. Funded by NSF China. Project page: [gongweisheng.github.io/DIDLM.github.io](https://gongweisheng.github.io/DIDLM.github.io/). Link check: opened (abs + HTML v2).
- What it does / claims: data comes from a tracked ground robot (low speed) and a roof-mounted car rig (up to 30 km/h). Sensors are 4D mmWave radar, infrared camera, depth camera, 3D LiDAR, RGB camera, GPS and IMU. Conditions are snow, rain, night and bumpy roads (speed bumps), over 18.5 km, 69 min and ~660 GB. Seven algorithms were benchmarked (Livox-SLAM, CT-ICP, ORB-SLAM3, DSO on RGB and thermal, 4DRT-SLAM, GS-SLAM, R3LIVE). Reported failures: RGB ORB-SLAM3 failed completely at night. Snow severely degraded all LiDAR methods. R3LIVE failed when rain covered the lens. Visual SLAM lost feature tracking on bumpy segments, and ATE on high-speed speed-bump runs reached tens to hundreds of meters.
- Cost or price info (with source) if any: none given.
- Relevance to our bin-to-curb robot: shows that low light and rain break camera-only SLAM, and that radar and infrared are the robust modalities. A driveway robot running at dawn in winter rain sees exactly these conditions, though at a much smaller scale.
- Gap: vehicle and campus scale with expensive sensor suites. No evaluation of cheap single sensors, and no short-range (<50 m) repeated-route tasks.

#### [Benchmarking 6DOF Outdoor Visual Localization in Changing Conditions (arXiv 1707.09092)](https://arxiv.org/abs/1707.09092)
- Type: paper / dataset (CVPR 2018 spotlight)
- Who / when: Sattler, Maddern and co-authors including Torii, Sivic and Pajdla (full author list not checked). 2017-2018. Benchmark site: visuallocalization.net. Link check: opened (abs).
- What it does / claims: introduces the Aachen Day-Night, RobotCar Seasons and CMU Seasons benchmarks. Concludes that long-term visual localization is unsolved, especially across night and seasonal change.
- Cost or price info (with source) if any: none.
- Relevance to our bin-to-curb robot: it is the standard citation for saying that a map taken in one season or lighting may not localize in another. The weekly bin route is a small instance of this problem.
- Gap: city or car scale and camera-only. No low-cost robot, and no single-house route.

#### [4Seasons: Benchmarking Visual SLAM and Long-Term Localization for Autonomous Driving in Challenging Conditions (arXiv 2301.01147)](https://arxiv.org/abs/2301.01147)
- Type: dataset / paper (IJCV)
- Who / when: Wenzel, Yang, Wang, Zeller, Cremers. arXiv Dec 2022, revised Jun 2025. Link check: opened (abs).
- What it does / claims: stereo + IMU data with RTK-GNSS ground truth, recorded across a year in 9 environments, including a multi-level parking garage, urban streets with tunnels, countryside and highway. Argues that VO, place recognition and map-based localization must be evaluated jointly.
- Cost or price info (with source) if any: none.
- Relevance to our bin-to-curb robot: the garage-to-street transition (no GNSS indoors, then open sky) is the same as ours at car scale. It is also a methodological template for using RTK-GNSS as ground truth.
- Gap: car platform. No residential driveway, no small robot, no cost axis.

---

### B. Residential / yard localization: wire-free robot lawn mowers (the closest commercial analog)

#### [Husqvarna press release: virtual boundary technology (EPOS) for Professional Robotic mowing](https://www.husqvarnagroup.com/en/press/husqvarna-expands-innovation-leadership-virtual-boundary-technology-professional-robotic)
- Type: product (press release)
- Who / when: Husqvarna Group, 17 Sep 2019. Link check: opened.
- What it does / claims: EPOS is a satellite (RTK-GNSS) navigation system claiming 2-3 cm accuracy, used for wire-free virtual boundaries on professional Automower models. Rollout to selected professional customers in the US, France, Germany and Sweden in 2020, managed through Husqvarna Fleet Services.
- Cost or price info (with source) if any: no price in the release.
- Relevance to our bin-to-curb robot: this is the industry claim for RTK accuracy in yards (2-3 cm). The team's measurements near a garage can be compared against it.
- Gap: a professional product with no published error distribution near buildings. It does not handle loads or curbs.

#### [Segway Navimow i105N review (Yahoo Tech, Aug 22 2024)](https://tech.yahoo.com/home/articles/segway-navimow-i105n-review-cost-220012288.html)
- Type: product (review)
- Who / when: Yahoo Tech review, 22 Aug 2024. Link check: opened.
- What it does / claims: a wire-free mower for lawns up to 1/8 acre. It combines RTK-GNSS with camera-assisted positioning so it "never gets lost, even in areas with weak GPS signals". The reviewer notes that RTK can be tricky with an obstructed sky view and can cause the mower to stop. Navigation was imperfect at corners and on parallel lines.
- Cost or price info (with source) if any: $1,000 USD (same review). A Slickdeals listing returned by search showed $799 on Amazon at one point: [Slickdeals](https://slickdeals.net/f/17910381-segway-navimow-i105n-robot-lawn-mower-perimeter-wire-free-1-8-acre-rtk-vision-robotic-lawnmower-ai-assisted-mapping-virtual-boundary-app-control-58db-a-quiet-amazon-799) (opened; listing dated 21 Nov 2024).
- Relevance to our bin-to-curb robot: **this is a key cost anchor.** A complete consumer robot with RTK + vision localization, drive train and battery sells for about $800-1,000. A hobbyist bin robot that claims to be "low-cost" has to be compared against this number.
- Gap: it mows grass only. It is not built to drive on a driveway pulling a cart, and no localization accuracy data is published.

#### [Mammotion LUBA 2 AWD review (TechRadar)](https://www.techradar.com/home/small-appliances/mammotion-luba-2-awd-robot-lawn-mower-review) and [Mammotion Yuka mini Vision (Notebookcheck)](https://www.notebookcheck.net/Mammotion-Yuka-mini-Vision-robot-lawn-mower-now-available.1074026.0.html)
- Type: product
- Who / when: Mammotion. Link check: TechRadar opened (prices and vision/RTK wording confirmed on the page, 2026-10-03). Notebookcheck: search snippet only (403 on fetch).
- What it does / claims: LUBA 2 AWD combines RTK with camera vision (the TechRadar page lists it as "RTK + AI Vision" / "UltraSense AI Vision & RTK"). The Yuka mini Vision needs no boundary wire and no RTK, uses three onboard cameras, and covers lawns up to ~700 m².
- Cost or price info (with source) if any: LUBA 2 AWD list prices of $2,099 (1000), $2,499 (3000) and $2,899 (5000) (TechRadar, opened). Yuka mini Vision €1,199 (Notebookcheck snippet). The Yuka Mini 2025 was listed at $1,097 US by [Freshly Charged](https://freshlycharged.com/reviews/363/2025-mammotion-yuka-mini-review) (opened).
- Relevance to our bin-to-curb robot: the industry is moving from RTK toward **vision-only** wire-free navigation at about $1,100-1,200. That is a direct "cheaper sensor" trend the paper can cite.
- Gap: no published accuracy for vision-only versus RTK operation, and no driveway or curb task.

#### [WORX Landroid Vision (WORX Australia product page)](https://au.worx.com/landroid/landroid-vision/)
- Type: product
- Who / when: WORX. Link check: opened (navigation description). Prices are from a search snippet of the same site.
- What it does / claims: camera-based AI navigation with no wire and no RTK. A full-HD HDR wide-angle camera feeds a neural network every 0.05 s to recognize grass, edges and obstacles.
- Cost or price info (with source) if any: search snippet from WORX AU showed L1300 at AUD $1,999 (sale, from $2,499) and M600 at AUD $1,499. US price was not verified.
- Relevance to our bin-to-curb robot: shows that a single-camera grass/non-grass edge classifier is shipping commercially. A grass-vs-pavement classifier could likewise keep a bin robot on the driveway. *Inference.*
- Gap: no published accuracy. Grass edges are not curbs, and it is not designed to drive on hardscape.

#### [Local Navigation and Docking of an Autonomous Robot Mower using Reinforcement Learning and Computer Vision (arXiv 2101.06248)](https://arxiv.org/abs/2101.06248)
- Type: paper
- Who / when: Taghibakhshi, Ogden, West. arXiv Jan 2021. Link check: opened (abs).
- What it does / claims: single-camera docking of a robot mower using YOLO detection + Double DQN, with no GPS or other position sensors. Claims "centimeter-level accuracy from arbitrary initial locations and orientations" and describes the approach as inexpensive.
- Cost or price info (with source) if any: no figures.
- Relevance to our bin-to-curb robot: a published precedent for camera-only, low-cost docking of a small outdoor robot. This is analogous to docking to a trash cart.
- Gap: docks to a fixed station, not to a movable and variably posed cart. No cost-vs-accuracy comparison.

---

### C. Sidewalk delivery robot localization

#### [US20180253107A1: Mobile robot system and method for autonomous localization using straight lines extracted from visual images (Starship Technologies)](https://patents.google.com/patent/US20180253107A1/)
- Type: patent
- Who / when: Starship Technologies OU. Inventors Heinla, Volkov, Roberts, Mandre. Priority 2 Nov 2015, published 6 Sep 2018. Related: [US20210302989A1](https://patents.google.com/patent/US20210302989A1/en) (map generation from straight lines). Link check: opened (US20180253107A1). The related patent was also opened (title confirmed).
- What it does / claims: at least 2 cameras, with a preferred embodiment of 9 (including 4 stereo pairs). It extracts straight lines (Canny + Hough), matches them to a stored map with a particle filter, and fuses GPS, odometry, gyro, accelerometer and magnetometer. Claimed localization error is at most 10 cm, preferably at most 5 cm, and more preferably at most 3 cm. The robot travels at 3-6 km/h and weighs 10-25 kg.
- Cost or price info (with source) if any: none.
- Relevance to our bin-to-curb robot: driveways and garages are full of straight edges (expansion joints, garage-door frames, curb lines). Line-based localization is a plausible cheap-camera method. *Inference.*
- Gap: these are patent claims, not measured results. The system uses 9 cameras and a pre-built map, and it was not evaluated in an independent study.

#### [Human-guided burrito bots raise questions about the future of robo-delivery (The Hustle)](https://thehustle.co/kiwibots-autonomous-food-delivery)
- Type: other (journalism)
- Who / when: Conor Grant, The Hustle, 1 Oct 2024. Link check: opened.
- What it does / claims: Kiwibots navigate with GPS + cameras under "parallel autonomy". Remote operators in Colombia send waypoint instructions every 5-10 s at $2/hour. Top speed is 1.5 mph, and the average campus trip is about 200 m. The article quotes the idea that "it's cheaper to pay people $2/hour than build a cutting-edge Lidar system."
- Cost or price info (with source) if any: operator labor $2/hr (article). Robot unit cost was not stated, and a ~$2,500 figure seen in search results could not be tied to a source, so it is UNVERIFIED.
- Relevance to our bin-to-curb robot: a real example of trading sensor cost for human supervision. Our robot cannot rely on that and must be fully autonomous on a short route, which is a framing point.
- Gap: no published localization accuracy, and the design depends on teleoperation.

#### [WalkOCC (method name) in: Monocular 3D Occupancy Perception for Robots on Sidewalks via Hybrid 2D-3D Learning (arXiv 2606.19122)](https://arxiv.org/abs/2606.19122)
- Type: paper / dataset
- Who / when: Ma, Lin, Liu, He, Ricketts, Squicciarini, Zhou. Affiliations: UCLA, Coco Robotics and MIT (Bolei Zhou is listed under both UCLA and Coco). arXiv Jun 2026, v2 Sep 2026. Link check: opened (abs + HTML v2).
- What it does / claims: monocular 3D semantic occupancy for sidewalk robots, explicitly targeting subtle structures "such as curbs and gutters." Introduces the Sidewalk3D dataset: **10 hours of data from 3 robots** (corrected during verification; the HTML v2 data-collection section states 10 hours from 3 robots) in touristy, residential and commercial districts, day and night. Coco robots carry a forward fisheye RGB camera (20 fps), a 3D LiDAR (10 fps), an IMU (40 fps) and wheel odometry. **Curb class IoU was only 14.59** for WalkOCC (vs. 8.82 for the FlashOCC baseline).
- Cost or price info (with source) if any: none.
- Relevance to our bin-to-curb robot: (1) it documents Coco's sensor stack, which uses a 3D LiDAR, so Coco is not a cheap-sensor platform. (2) It provides strong evidence that **learned monocular curb segmentation is still hard** (IoU around 15%), which motivates geometric or active cheap sensors for curb finding. (3) It connects to a UCLA lab.
- Gap: no cost analysis and no driveway-to-street transitions. Dataset code and data are "will be made available" (not verified as released).

---

### D. Low-cost RTK-GNSS accuracy near trees and buildings

#### [Evaluation of Low-Cost GNSS Receiver under Demanding Conditions in RTK Network Mode (Sensors 2021, 21(16):5552)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8401267/)
- Type: paper
- Who / when: Janos and Kuras, 2021. DOI 10.3390/s21165552. Link check: opened.
- What it does / claims: u-blox ZED-F9P with either the u-blox ANN-MB-00 patch antenna or a Leica AS10 survey antenna, compared with a Leica GS18T. Seven points range from open sky to tree-obstructed to forest-like to an urban canyon (buildings + trees). Open-sky and forest-like points stayed within a few cm (open sky under ±2 cm; forest-like points within ±3 cm and ±1 cm). In the urban canyon (point 7) the AS10 antenna got a fixed solution in only 3 of 8 series. **With the cheap patch antenna in the urban canyon: about 2-7 cm plan offsets, about 24 cm height offset, and a fix in 4 of 8 series (50%).** (Numbers corrected during verification, read from the paper's results via WebFetch; the earlier ±0.7/±1.5/±6.4 cm and 60% figures could not be found in the paper.) Conclusion: ZED-F9P + patch antenna "is only suitable for precision measurements in conditions with high availability of open sky."
- Cost or price info (with source) if any: no prices in the paper. See the SparkFun/ArduSimple entry below.
- Relevance to our bin-to-curb robot: a garage mouth, with a house wall on one side and eaves overhead, is a partial urban canyon. Expect RTK fix loss exactly where the robot leaves or enters the garage.
- Gap: static points only, not a moving robot. No residential driveway geometry, and no comparison with non-GNSS cheap alternatives.

#### [Behavior of Low-Cost Receivers in Base-Rover Configuration with Geodetic-Grade Antennas (Sensors 2022, 22(7):2779)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9002666/)
- Type: paper
- Who / when: Sanna, Pisanu, Garau, 2022. DOI 10.3390/s22072779. Link check: opened.
- What it does / claims: ZED-F9P base-rover car tests. In an urban loop with buildings and open sectors: **95.17% real-time fix, 14.1 mm horizontal RMSE in real time** (4 mm post-processed), and ~8 s average re-acquisition after signal loss. Repeats the conclusion that the patch antenna suits only wide-open sky and that geodetic antennas improve results substantially.
- Cost or price info (with source) if any: not stated.
- Relevance to our bin-to-curb robot: gives the upper-bound accuracy of a hobby RTK module in moving use. The ~8 s re-acquisition time matters when the robot drives out of a garage.
- Gap: car-mounted with good antennas. No under-eave or garage-exit test at robot speed.

#### [Static Positioning under Tree Canopy Using Low-Cost GNSS Receivers and Adapted RTKLIB Software (Sensors 2023, 23(6):3136)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10056071/)
- Type: paper
- Who / when: Tomaštík and Everett, Sensors, Mar 2023. DOI 10.3390/s23063136. Link check: opened (PMC abstract, 2026-10-03).
- What it does / claims: compares a Google Pixel 5 and a u-blox ZED-F9P under open sky and tree canopy, leaf-on and leaf-off, using ten 20-min static sessions post-processed with the RTKLIB demo5 fork. Per the abstract, the F9P gave "consistent results with sub-decimeter median horizontal errors even under tree canopy", while the Pixel 5 had errors under 0.5 m in open sky and about 1.5 m under canopy.
- Cost or price info (with source) if any: not captured.
- Relevance to our bin-to-curb robot: suggests that leaf-on and leaf-off differences matter for yards with trees. It also gives a phone-GNSS baseline (~1.5 m), which is not enough to place a cart at the curb. *Inference.*
- Gap: static and post-processed, not real-time on a moving robot.

#### [Evaluation of Forest Features Determining GNSS Positioning Accuracy of a Novel Low-Cost, Mobile RTK System Using LiDAR and TreeNet (Remote Sensing 2022, 14(12):2856)](https://doi.org/10.3390/rs14122856)
- Type: paper
- Who / when: Abdi, Uusitalo, Pietarinen, Lajunen. Remote Sensing, 15 Jun 2022. DOI 10.3390/rs14122856. Link check: MDPI returns 403; title, authors and abstract confirmed via Crossref and OpenAlex metadata.
- What it does / claims: a ZED-F9P in movable RTK mode along forest logging trails in southern Finland, checked against a geodetic receiver and LiDAR. Top factors affecting accuracy were tree height, ground elevation, aspect, canopy-surface elevation and tree density; tree height above 14 m and tree density above 30% significantly increased positioning errors. (A previously quoted ">50 cm error above 50-65% canopy closure" claim could not be confirmed in the abstract and was removed.)
- Cost or price info (with source) if any: not captured.
- Relevance to our bin-to-curb robot: driveways shaded by large trees could fall into this regime. That supports a fallback localization mode.
- Gap: forest, not suburban. No robot control loop.

#### [SparkFun GPS-RTK2 Board - ZED-F9P (Qwiic)](https://www.sparkfun.com/sparkfun-gps-rtk2-board-zed-f9p-qwiic-gps-15136.html) and [ArduSimple simpleRTK2B Basic Starter Kit IP67 (ArduSimple product page)](https://www.ardusimple.com/product/simplertk2b-basic-starter-kit-ip65/)
- Type: product
- Who / when: SparkFun (link check: opened, price shown Oct 2026). ArduSimple (link check: opened, price shown Oct 2026; the original geo-matching link returned 404 and was replaced).
- What it does / claims: SparkFun claims 10 mm 3D RTK accuracy and 2.5 m without corrections. The ArduSimple kit is the ZED-F9P + ANN-MB antenna.
- Cost or price info (with source) if any: **SparkFun board $259.95** (antenna not stated as included). **ArduSimple kit €211 / USD $263.75** (ArduSimple site, Oct 2026). *Inference:* a base + rover pair costs roughly $500-550 before antennas, or the team can use a free or state NTRIP network if one is available locally (not verified for any California county).
- Relevance to our bin-to-curb robot: this is the RTK line item for the bill of materials. It is roughly half the price of an entire Navimow i105N.
- Gap: vendor accuracy is an open-sky claim (see Janos & Kuras above).

---

### E. Visual teach-and-repeat (including low-cost variants)

#### [Visual teach and repeat for long-range rover autonomy (J. Field Robotics, 2010)](https://doi.org/10.1002/rob.20342)
- Type: paper
- Who / when: Furgale and Barfoot, JFR 2010, DOI 10.1002/rob.20342. Link check: publisher page returns 403; title, authors and abstract (32 km, 99.6%, 45 m-3.2 km) confirmed via Crossref/OpenAlex metadata. Link replaced from an openpolar.no mirror (bot wall) to the DOI.
- What it does / claims: the foundational stereo VT&R system. It builds a chain of overlapping submaps while piloted, then repeats the route. Over 32 km were driven with 99.6% autonomy, in single runs from 45 m to 3.2 km, without GPS, in urban and High-Arctic settings.
- Cost or price info (with source) if any: none.
- Relevance to our bin-to-curb robot: the canonical citation for "drive it once, repeat it weekly", which is exactly the garage-to-curb use case.
- Gap: research-grade stereo rig and compute. No low-cost bill of materials.

#### [Monocular Visual Teach and Repeat Aided by Local Ground Planarity (arXiv 1707.08989)](https://arxiv.org/abs/1707.08989)
- Type: paper (Field and Service Robotics, STAR vol. 113)
- Who / when: Clement, Kelly, Barfoot. 2017, revised 2019. Link check: opened (abs).
- What it does / claims: a monocular VT&R that recovers scale by assuming the ground near the vehicle is locally planar and the camera height is known. It ran 4.3 km autonomously with centimetre-level path-following accuracy, "on par with" stereo VT&R even in non-planar terrain.
- Cost or price info (with source) if any: none stated.
- Relevance to our bin-to-curb robot: a driveway is close to planar, so one cheap camera can give metric repeat accuracy.
- Gap: no cost analysis, and no towed or pushed load.

#### [Navigation without localisation: reliable teach and repeat based on the convergence theorem (arXiv 1711.05348)](https://arxiv.org/abs/1711.05348) and [BearNav (CTU Chronorobotics)](https://chronorobotics.fel.cvut.cz/open-science/stroll-bearnav)
- Type: paper (IROS 2018) + open-source software
- Who / when: Krajnik, Majer, Halodova, Vintr (Czech Technical University), 2017-2018. Code: gestom/stroll_bearnav (ROS). Link check: both opened.
- What it does / claims: the robot replays its taught velocities and uses the camera only to correct heading. The authors prove that position error does not diverge. No camera calibration is needed, and the paper reports robustness to imperfect odometry, few landmarks, illumination changes and natural environment change.
- Cost or price info (with source) if any: none.
- Relevance to our bin-to-curb robot: **very well suited to a cheap robot**. The method needs only one uncalibrated camera + wheel encoders on a fixed weekly path.
- Gap: no published evaluation with a cart attached (load-induced wheel slip), on driveway slopes, or across months of one route at a single house.

#### [Fast and Robust Bio-inspired Teach and Repeat Navigation (arXiv 2010.11326)](https://arxiv.org/abs/2010.11326)
- Type: paper (IROS 2021)
- Who / when: Dall'Osto, Fischer, Milford. 2020-2021. Link check: opened (abs).
- What it does / claims: teach-and-repeat designed for **low-cost robots with poor odometry and a low-resolution monocular camera**. It is mainly odometry-driven with periodic lightweight visual correction. Tested on the Consequential Robotics MiRo and a Clearpath Jackal over more than 6,000 m indoors and outdoors. It succeeded where state-of-the-art systems failed (low resolution, bad odometry, lighting change) and transferred routes across platforms without retuning.
- Cost or price info (with source) if any: no prices given.
- Relevance to our bin-to-curb robot: the strongest published support that a cheap camera + bad wheel odometry is enough for a fixed route.
- Gap: no metric repeat-error table in the abstract, no outdoor residential route, and no load.

#### [Keeping an Eye on Things: Deep Learned Features for Long-Term Visual Localization (arXiv 2109.04041)](https://arxiv.org/abs/2109.04041)
- Type: paper
- Who / when: Gridseth and Barfoot, 2021-2022. Link check: opened (abs).
- What it does / claims: learned features integrated into multi-experience VT&R. In **35.5 km** of closed-loop path following, robots followed routes taught in daylight in all lighting conditions, including darkness.
- Cost or price info (with source) if any: none.
- Relevance to our bin-to-curb robot: shows that day-taught, night-repeated operation is possible with learned features. This is relevant to pre-dawn trash days.
- Gap: research platform and GPU. No low-cost hardware study.

---

### F. Fiducial (AprilTag / ArUco) localization accuracy

#### [Analysis and Improvements in AprilTag Based State Estimation (Sensors 2019, 19(24):5480)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6960891/)
- Type: paper
- Who / when: Abbas, Aslam, Berns, Muhammad, 2019. DOI 10.3390/s19245480. Link check: opened.
- What it does / claims: with the camera pointing at the tag center at 30-70 cm depth, mean error is about 1.0 cm (x) and 0.4 cm (y). At a 110° camera yaw and 70 cm, error grows to about 16 cm with variance increasing "manifold". Proposed fixes (soft yaw correction, active yaw gimbal, a Gaussian-process sensor model for Bayes filters) improved x accuracy from 4.4 cm to 0.8 cm. **Outdoor tests used a large 305x305 cm tag on the ground.**
- Cost or price info (with source) if any: none. Tags are printable. *Inference:* near-zero marginal cost.
- Relevance to our bin-to-curb robot: a tag on the garage wall and possibly a tag on the cart or at the curb spot is the cheapest absolute-position fix available. The paper quantifies how accuracy falls with viewing angle.
- Gap: short range. No study of sunlit or wet driveway conditions at 2-10 m with a cheap camera.

#### [Fiducial Markers for Pose Estimation: Overview, Applications and Experimental Comparison of the ARTag, AprilTag, ArUco and STag Markers (J. Intell. Robot. Syst. 101, 2021)](https://link.springer.com/doi/10.1007/s10846-020-01307-9)
- Type: paper
- Who / when: Kalaitzakis, Cain, Carroll, Ambrosi, Whitehead, Vitzilaios, JINT 2021. Title and authors confirmed via [OpenAlex](https://api.openalex.org/works/doi:10.1007/s10846-020-01307-9). Link check: Springer page is paywalled (redirect to login). Metadata opened via OpenAlex. Scope from search snippet.
- What it does / claims: compares four marker systems on accuracy, detection rate and compute cost, including simulated shadows and motion blur, and single, bundle and multi-size configurations.
- Cost or price info (with source) if any: none.
- Relevance to our bin-to-curb robot: guidance for choosing a marker family that survives shadows (common on driveways in the morning).
- Gap: numeric results were not accessible in this sweep. Not tested on real outdoor ground robots in sunlight.

---

### G. Wheel / visual odometry drift over tens of meters

#### [Comparison of Wheel Odometry and Visual Odometry for Low-Cost Vehicle Navigation (SBR 2024)](https://sol.sbc.org.br/index.php/sbrlars/article/view/34065)
- Type: paper
- Who / when: Rezende, Silva, Marques, XVI Brazilian Robotics Symposium (SBR) 2024, pp. 91-96. Link check: opened (abstract page).
- What it does / claims: compares encoder wheel odometry with monocular VO for low-cost vehicles. Concludes that VO can be more accurate in complex environments, but WO "remains a viable and cost-effective option for simpler navigation tasks", especially when wheel-radius errors are correlated and do not exceed ±0.26%.
- Cost or price info (with source) if any: not in the abstract.
- Relevance to our bin-to-curb robot: a driveway is a "simple navigation task". This paper supports wheel odometry + occasional correction as a defensible cheap baseline.
- Gap: drift distances and surfaces were not visible in the abstract. No load or slope.

Related drift evidence elsewhere in this file: ROVER (DROID-SLAM 0.32 m day vs 5.62 m night ATE), DIDLM (visual SLAM loses tracking on bumps), and Boxan et al. 2026 (complex SLAM gave "limited accuracy gains over a proprioceptive baseline", see section J).

---

### H. Curb detection (LiDAR, depth, monocular, ultrasonic, radar)

#### [Low-Cost Curb Detection and Localization System Using Multiple Ultrasonic Sensors (Sensors 2019, 19(6):1389)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6470551/)
- Type: paper
- Who / when: Rhee and Seo (Yonsei Univ.), 2019. DOI 10.3390/s19061389. Link check: opened.
- What it does / claims: 3-4 side-facing ultrasonic sensors on a car, with ground-reflection filtering, reliability classification and trend matching. Results: **3 sensors gave 92.08% availability and ~12 cm RMSE; 4 sensors gave 96.04% availability and 13.50 cm RMSE.** Naive averaging gave 99.01% availability but 97.57 cm RMSE. Tested in Incheon. Performance is limited when the curb is at a large angle to the vehicle (tests used about 10°).
- Cost or price info (with source) if any: **$15 per ultrasonic sensor** (paper), so about $45-60 of sensors.
- Relevance to our bin-to-curb robot: **the best published accuracy-per-dollar curb data point.** It gives about 12 cm lateral accuracy for about $50, which may already meet a "place the cart within N cm of the curb" requirement.
- Gap: a car at road speed parallel to the curb. Our robot approaches the curb roughly head-on at low speed and low height, and that case has not been tested.

#### [CurbScan: Curb Detection and Tracking Using Multi-Sensor Fusion (arXiv 2010.04837)](https://arxiv.org/abs/2010.04837)
- Type: paper (IEEE ITSC 2020)
- Who / when: Baek, Tai, Bhat, Ellango, Shah, Fuseini, Rajkumar (CMU). Oct 2020. Also listed on the [CMU RI page](https://www.ri.cmu.edu/publications/curbscan-curb-detection-and-tracking-using-multi-sensor-fusion). Link check: opened (arXiv).
- What it does / claims: fuses sparse 3D LiDAR, a mono camera and low-cost ultrasonics, with Kalman tracking. Over 90% accuracy within 4.5-22 m on KITTI and within 0-14 m on their own data. Runs at about 10 ms/frame on an i7 and 100 ms on a Xavier.
- Cost or price info (with source) if any: none given.
- Relevance to our bin-to-curb robot: shows that ultrasonics add lateral-distance accuracy cheaply on top of sparse LiDAR.
- Gap: vehicle scale with LiDAR. No ablation that removes the LiDAR.

#### [Road Curb Detection and Localization with Monocular Forward-view Vehicle Camera (arXiv 2002.12492)](https://arxiv.org/abs/2002.12492)
- Type: paper (IEEE T-ITS, vol. 20 no. 9, 2019, per the arXiv record)
- Who / when: Panev, Vicente, De la Torre, Prinet (affiliations not checked). Link check: opened (abs).
- What it does / claims: a calibrated fisheye monocular camera, 3D template fitting + HOG/SVM + temporal tracking. Estimates vehicle-to-curb distance with **mean accuracy above 90%**, plus curb orientation, height and depth in real time. Validated on 11 videos with point LiDAR ground truth.
- Cost or price info (with source) if any: none. A monocular camera is the cheapest imaging sensor. *Inference.*
- Relevance to our bin-to-curb robot: a geometric (not deep-learned) monocular curb detector that is small enough for a Raspberry Pi-class computer. *Inference.*
- Gap: car viewpoint. Not tested from 20-40 cm height or on US rolled curbs.

#### [Automated Curb Recognition and Negotiation for Robotic Wheelchairs (Sensors 2021, 21(23):7810)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8659845/)
- Type: paper
- Who / when: Sivakanthan, Castagno, Candiotti, Zhou, Sundaram, Atkins, Cooper (Univ. of Pittsburgh, Univ. of Michigan, VA), Nov 2021. DOI 10.3390/s21237810. Link check: opened.
- What it does / claims: an Intel RealSense D455 depth camera on the MEBot wheelchair. Curb detected at **14/15 start positions (45 trials)**. Final alignment error 1.5 ± 4.4° and **distance error 0.09 ± 0.10 m**. Height estimate 0.21 m vs 0.20 m actual. Limitations: straight curbs only (fails on rounded corners), single side-mounted camera, indoor mock curb under controlled lighting.
- Cost or price info (with source) if any: D455 price was not verified in this sweep.
- Relevance to our bin-to-curb robot: the closest published low-speed, robot-scale curb approach with numbers (about 9 cm).
- Gap: indoor mock curb only, not outdoors in sunlight. Not compared with cheaper sensors.

#### [CurbNet: Curb Detection Framework Based on LiDAR Point Cloud Segmentation (arXiv 2403.16794)](https://arxiv.org/abs/2403.16794)
- Type: paper + dataset (3D-Curb)
- Who / when: Zhao, Ma, Qi, Liu, Liu, Ma. arXiv Mar 2024. Link check: opened (abs + HTML; 7,100 frames and the >0.95 at 0.15 m tolerance result confirmed in the HTML).
- What it does / claims: the 3D-Curb dataset has 7,100 annotated LiDAR frames built on SemanticKITTI, described as the largest curb point-cloud set. The method exceeds 0.95 average precision, recall and F1 at 0.15 m tolerance. Notes that nuScenes, KITTI and SemanticKITTI lack curb annotations.
- Cost or price info (with source) if any: none. For LiDAR cost context, Southcott et al. (below) cite about $25,000 for entry-level and up to $100,000 for high-end automotive LiDAR.
- Relevance to our bin-to-curb robot: the high-cost, high-accuracy end of the curb accuracy-vs-cost curve.
- Gap: car LiDAR. Irrelevant to a hobby budget except as an upper bound.

#### [Millimeter Wave Radar-Based Road Segmentation (Clarkson Univ.; NSF PAR)](https://par.nsf.gov/servlets/purl/10493760)
- Type: paper
- Who / when: Southcott, Zhang, Liu (Clarkson University). Venue appears to be a SPIE proceedings paper (not confirmed). Link check: opened (PDF text extracted).
- What it does / claims: a **TI AWR1843 single-chip automotive FMCW radar** + DCA1000EVM capture board, mounted at bumper height. Scenes include **pavement to curb, a driveway flanked with snow, a ~2 cm cement barrier between pavement and grass, and a pavement-to-grass transition.** A "joint variance" boundary detector ran in 0.69 ms (vs. 87-114 ms for CFAR). Segmentation agreed strongly with ground truth on easy transitions (curb) and degraded on hard ones (flat pavement-to-grass). Results are qualitative (figures) with no numeric accuracy.
- Cost or price info (with source) if any: no radar price given. The paper cites LiDAR at about $25k-100k.
- Relevance to our bin-to-curb robot: **a single-chip radar that works in the dark and in snow, already tested on curb and driveway scenes.** A possible night-robust curb sensor. *Inference:* TI eval boards are hobby-accessible, but price was not verified.
- Gap: no numeric accuracy, no robot, Matlab post-processing, and no cost comparison.

#### [Road Boundary Detection Using 4D mmWave Radar for Autonomous Driving (4DRadarRBD, arXiv 2503.01930)](https://arxiv.org/abs/2503.01930)
- Type: paper
- Who / when: Wu and Noh, Mar 2025. Link check: opened (abs).
- What it does / claims: the first road-boundary detection method using 4D mmWave radar. Reports **93% boundary-point segmentation accuracy, 0.023 m median distance error**, and a 92.6% error reduction vs. baseline. Pitches radar as a cost-effective alternative to camera and LiDAR.
- Cost or price info (with source) if any: "cost-effective" claim with no price.
- Relevance to our bin-to-curb robot: radar can reach cm-level boundary distance. A mid-cost point on the curve.
- Gap: car-scale 4D imaging radar. Boundaries tested are fences, bushes and roadblocks, not low residential curbs.

#### [Multi-faceted Sensory Substitution for Curb Alerting: A Pilot Investigation in Persons with Blindness and Low Vision (arXiv 2408.14578)](https://arxiv.org/abs/2408.14578)
- Type: paper
- Who / when: Ruan, Hamilton-Fletcher, Beheshti, Hudson, Porfiri, Rizzo, Aug 2024. Link check: opened (abs).
- What it does / claims: an RGB camera + embedded computer running YOLOv8 segmentation trained on a custom curb dataset. Gives earlier warning than a cane with similar curb-orientation information.
- Cost or price info (with source) if any: none.
- Relevance to our bin-to-curb robot: shows that a commodity camera + YOLOv8-seg curb detector runs on embedded hardware. This is the likely software baseline for our team.
- Gap: no metric accuracy reported in the abstract. Pedestrian viewpoint.

---

### I. Trash-bin / wheelie-bin detection and pose estimation

#### [StreetView-Waste: A Multi-Task Dataset for Urban Waste Management (arXiv 2511.16440)](https://arxiv.org/abs/2511.16440)
- Type: dataset / paper (WACV 2026)
- Who / when: Paulo, Martins, Proença, Neves, Nov 2025. Link check: opened (abs + HTML).
- What it does / claims: **36,478 fisheye images and 71,170 container instances** from two 180° fisheye cameras on the flanks of garbage trucks. Tasks are detection, tracking and overflow segmentation. Seven container classes (default, glass, paper, packaging, biodegradable, oil, battery). **YOLOv11 got the best mAP@[.5:.95] of 0.77** (per class 0.61-0.85). License CC BY 4.0, with restricted access via a data license.
- Cost or price info (with source) if any: none.
- Relevance to our bin-to-curb robot: the largest recent public container-detection benchmark. Usable for pretraining.
- Gap: European-style street containers seen from a truck. **Not US 64/96-gal residential carts, not a low ground-robot viewpoint, and no 6-DoF or yaw pose labels.**

#### [Detecting the overfilled status of domestic and commercial bins using computer vision (Intelligent Systems with Applications, 2023)](https://doi.org/10.1016/j.iswa.2023.200229)
- Type: paper
- Who / when: Agnew, Mewada, Grua, Eising, Denny, Heffernan, May 2023. DOI 10.1016/j.iswa.2023.200229. Link check: DOI resolves (200); title and authors confirmed via Crossref and abstract via OpenAlex. Link replaced from DOAJ (403 bot wall) to the DOI.
- What it does / claims: builds detection and instance-segmentation datasets from commercial collection-route video for **automated side loader (ASL) bins** and front-end loader bins. State-of-the-art models reached mAP of 0.8 or higher.
- Cost or price info (with source) if any: none.
- Relevance to our bin-to-curb robot: ASL bins are the same class of wheeled cart we target. Evidence that off-the-shelf detectors reach about 0.8 mAP on them.
- Gap: proprietary dataset, truck viewpoint, fill-status task. No pose estimation for docking.

#### [US11527072B2: Systems and methods for detecting waste receptacles using convolutional neural networks (McNeilus)](https://patents.google.com/patent/US11527072B2/en)
- Type: patent
- Who / when: McNeilus Truck and Manufacturing. Inventors Szoke-Sieswerda, McIsaac, Van Kampen. Priority 24 Oct 2017, granted 13 Dec 2022. Link check: opened.
- What it does / claims: a truck-mounted camera + **MobileNet-SSD** CNN classifies receptacles (garbage, recycling, compost) with bounding boxes, then triggers automatic arm grasp, lift and dump.
- Cost or price info (with source) if any: none.
- Relevance to our bin-to-curb robot: industry uses a lightweight MobileNet-SSD-class detector for exactly these carts. That supports running a small detector on hobby compute.
- Gap: truck arm, not a ground robot docking to the cart. No accuracy numbers in the patent.

#### [US10358287B2: Automated container handling system for refuse collection vehicles (Con-Tech)](https://patents.google.com/patent/US10358287)
- Type: patent
- Who / when: Con-Tech Manufacturing. Inventors McNeilus, Cunningham, Meldahl. Priority 22 Jun 2016, granted 23 Jul 2019. Link check: opened.
- What it does / claims: a camera feeds a cab monitor to locate the container. **An active sonar transducer on the grabber base** measures proximity, so that "an approach as close as one inch is repeatably possible". Controlled by a PLC.
- Cost or price info (with source) if any: none.
- Relevance to our bin-to-curb robot: industry precedent for **camera for coarse location + ultrasonic for the final approach** to a cart. This is a cheap combination for docking.
- Gap: truck arm. No robot or performance data.

#### [CartSeeker (McNeilus product page)](https://mcneilusgarbagetrucks.com/cartseeker?hsLang=en) and [Government Fleet article, 2 Jun 2021](https://www.government-fleet.com/10144799/mcneilus-to-debut-zero-radius-automated-side-loader)
- Type: product
- Who / when: McNeilus (Oshkosh), debuted at Waste Expo, June 2021. Link check: both opened.
- What it does / claims: an AI camera recognizes carts, a **LiDAR distance sensor** verifies range, and the arm is fully automated with one button. Works in rain, snow and heat, but may error if water or dust covers the LiDAR face. The article claims a **96% success rate**, corrects for "color and size of carts, angles, differing backgrounds, lighting and weather... proximity to other carts", "performs nearly perfectly in normal day time conditions", and reduces costs by 8%.
- Cost or price info (with source) if any: no system price.
- Relevance to our bin-to-curb robot: a commercial benchmark for cart-recognition reliability (96%). It also implies what the truck needs at the curb: a cart that is reachable and properly spaced. *Inference:* the curb-placement accuracy target should come from what ASL arms tolerate.
- Gap: vendor claim with no published method. Placement tolerances are not specified on the page.

#### [Volvo ROAR: Drone to help refuse-collecting robot find refuse bins (Volvo Group, 25 Feb 2016)](https://www.volvogroup.com/en/news-and-media/news/2016/feb/drone-to-help-refuse-collecting-robot-find-refuse-bins.html) and [Chalmers ROAR project page](https://research.chalmers.se/en/project/6868)
- Type: student/academic project + industry demo
- Who / when: Volvo Group, Chalmers, Mälardalen Univ., Penn State, Renova. 2015-2016. Link check: both opened.
- What it does / claims: a robot fetches refuse bins, empties them into the truck and returns them. A quadcopter from the truck roof finds bin positions **and orientations**. The robot uses GPS, LiDAR, cameras, IMU and odometry plus a prior map of likely bin locations. Prototype built in 4 months.
- Cost or price info (with source) if any: none.
- Relevance to our bin-to-curb robot: the closest academic precedent for a ground robot moving wheeled bins. It uses expensive sensors and a drone, which is the opposite of our cheap-sensor thesis.
- Gap: no publications listed on the project page. No cost data and no residential driveway use.

---

### J. Long-term / seasonal / lighting robustness of repeated routes

#### [Toward Teach and Repeat Across Seasonal Deep Snow Accumulation (arXiv 2505.01339)](https://arxiv.org/abs/2505.01339)
- Type: paper
- Who / when: Boxan, Krawciw, Barfoot, Pomerleau (affiliations not checked; the paper links the FoMo dataset site). May 2025. Link check: opened (abs).
- What it does / claims: routes were taught, then repeated after 4, 44 and 113 days with snow accumulation, using LiDAR and FMCW-radar T&R. LiDAR did better when ground points were excluded. Radar localized on old maps with small deviations but failed on recent maps when vehicle pitch or roll was high.
- Cost or price info (with source) if any: none.
- Relevance to our bin-to-curb robot: shows that the map can go stale across seasons even on a fixed route. This motivates "re-teach" or multi-experience strategies for a weekly route.
- Gap: expensive sensors in a forest. No cheap camera and no residential setting.

#### [One year in a forest: Analyzing the challenges of autonomous navigation in subarctic environments (arXiv 2608.27628)](https://arxiv.org/abs/2608.27628)
- Type: paper
- Who / when: Boxan, Lauzon, Vannini, Turgeon-Roy, Pomerleau. Aug 2026 (very recent). Link check: opened (abs).
- What it does / claims: one year and 64 km of data, testing 9 odometry, localization and mapping methods across cameras, LiDARs and radars. Visual and radar methods were "prone to failure due to a few matching features between runs, even within the same season". Only LiDAR methods completed cross-season localization. **Complex SLAM showed "limited accuracy gains over a proprioceptive baseline while significantly increasing system fragility."**
- Cost or price info (with source) if any: none.
- Relevance to our bin-to-curb robot: **strong, current evidence for the cheap-sensor thesis.** A proprioceptive baseline (wheels + IMU) with simple absolute fixes may beat fragile SLAM on a short fixed route.
- Gap: forest, not driveway. No cost-vs-accuracy framing.

Also relevant to this sub-topic and listed above: ROVER (section A, seasonal and night failures in gardens), Sattler et al. 2018 and 4Seasons (section A), Gridseth & Barfoot 2021 (section E, darkness repeats), and Krajnik et al. / Dall'Osto et al. (section E, illumination-robust T&R).

---

### Accuracy vs. sensor cost: numbers found in this sweep

| Task | Sensor (cost if verified) | Reported accuracy | Setting | Source |
|---|---|---|---|---|
| Curb lateral distance | 3-4 ultrasonic @ **$15 each** | 12-13.5 cm RMSE, 92-96% availability | car, urban | Rhee & Seo 2019 |
| Curb distance + alignment | RealSense D455 (price not verified) | 0.09 ± 0.10 m, 1.5 ± 4.4°, 14/15 positions | wheelchair, indoor mock curb | Sivakanthan 2021 |
| Curb distance | monocular fisheye (cheap, no price) | >90% mean accuracy | car | Panev 2019 |
| Curb 3D occupancy | monocular fisheye (learned) | **curb IoU 14.59** | Coco sidewalk robots | WalkOCC 2026 |
| Road boundary | 4D mmWave radar (no price) | 93% seg. acc., 0.023 m median | car | Wu & Noh 2025 |
| Curb/grass boundary | TI AWR1843 single-chip radar (no price) | qualitative only | bumper height | Southcott et al. |
| Curb | automotive LiDAR (~$25k-100k cited) | >0.95 at 0.15 m tolerance | car / KITTI | CurbNet 2024 |
| Position | ZED-F9P + patch antenna (**$259.95** board) | ~2-7 cm plan / ~24 cm height offset, fix in 4 of 8 series in urban canyon | static | Janos & Kuras 2021 |
| Position | ZED-F9P + geodetic antenna | 14.1 mm RMSE, 95% fix | car, urban | Sanna 2022 |
| Position | Pixel 5 phone GNSS | ~0.5 m open, ~1.5 m canopy | static | Tomaštík & Everett 2023 |
| Position | printed AprilTag + camera | ~1 cm at 30-70 cm head-on; ~16 cm at oblique yaw | close range | Abbas 2019 |
| Position (claim) | 9 cameras, line features | ≤10 cm (pref. ≤3 cm) claimed | sidewalk | Starship patent |
| Position (claim) | RTK (EPOS) | 2-3 cm claimed | pro mowers | Husqvarna 2019 |
| VSLAM trajectory | RealSense D435i RGB-D (DROID-SLAM) | 0.32 m ATE day vs 5.62 m night | garden | ROVER |
| Whole product | RTK + vision mower | n/a | **$1,000 (Navimow i105N)**; LUBA 2 AWD from $2,099 | yard | Yahoo; TechRadar |
| Whole product | vision-only mower | n/a | **€1,199 (Yuka mini Vision)** | yard | Notebookcheck (snippet) |

---

### Gaps and opportunities

- **No published localization study of the garage-to-curb driveway itself.** RTK studies show the cheap patch-antenna ZED-F9P gets a fix in only about half of the series, with cm-level plan and ~24 cm height offsets, in building-plus-tree canyons (Janos & Kuras 2021) and takes about 8 s to re-acquire (Sanna 2022). Mowers (Navimow, Husqvarna EPOS) publish no error data. A measured comparison along a real driveway (inside garage, garage mouth, under eaves, open driveway, curb) of RTK vs. AprilTag + wheel odometry vs. teach-and-repeat, against a tape-measure or total-station ground truth, would be new and cheap to run.
- **Cost-vs-accuracy curve for curb finding at robot scale is missing.** Existing numbers come from different platforms: ultrasonic about 12 cm for ~$50 on a car (Rhee & Seo), depth camera about 9 cm indoors on a wheelchair (Sivakanthan), monocular >90% on a car (Panev), learned monocular curb IoU about 15% (WalkOCC), and qualitative single-chip radar (Southcott). A head-to-head on the same residential curbs, from a 20-40 cm high robot, in day, dusk and night, with sensor price on the x-axis, appears not to exist.
- **Proprioception + one cheap absolute fix may be enough.** "One year in a forest" (2026) found complex SLAM gave limited gains over a proprioceptive baseline while adding fragility. Rezende et al. (2024) find wheel odometry viable for simple tasks, and Dall'Osto et al. and Krajnik et al. show T&R works with poor odometry and cheap cameras. An ablation of wheel+IMU only vs. +AprilTag vs. +RTK vs. +VIO on a 10-40 m route is a clean, publishable experiment.
- **Night and dawn robustness is a real failure mode for cheap visual SLAM.** In ROVER, DROID-SLAM error grew from 0.32 m to 5.62 m at night. In DIDLM, ORB-SLAM3 failed outright at night. Trash carts often go out after dark or before sunrise, so measuring cheap alternatives (IR-lit or retroreflective fiducials, ultrasonic, single-chip radar) under that lighting is a strong angle. *Inference about trash-day timing.*
- **No public dataset of US 64/96-gal carts from a low robot viewpoint with pose labels.** StreetView-Waste (WACV 2026) and Agnew et al. (2023) are truck-perspective, and StreetView-Waste uses European container classes. A small labeled set (cart bounding box + yaw + handle-side keypoints) at 0.3-3 m would fill this gap. Industry patents use MobileNet-SSD (McNeilus) or camera + sonar for the final approach (Con-Tech), which are good cheap baselines to cite.
- **Load effect on odometry and repeat accuracy is unstudied.** None of the T&R or odometry papers above tested a robot pushing or towing a heavy two-wheeled cart. Measuring how wheel-odometry drift and T&R lateral error change with an empty vs. full cart is a novel, low-cost experiment. *Inference: cart mass ranges were not verified in this sweep.*
- **Seasonal staleness on a weekly route.** Boxan et al. (2025) show maps degrade over 4-113 days, and ROVER shows summer/autumn vegetation hurts VSLAM. A 10-12 week log of one driveway route (Dec-Feb) with a cheap camera, reporting T&R success rate vs. map age, fits the build window and is directly relevant. *Inference: California winter may show smaller changes than the snow studies.*
- **The commercial cost anchor is about $800-1,200 for a complete outdoor robot with RTK and/or vision** (Navimow i105N, Yuka mini Vision). A "cheaper than existing approaches" claim must name its comparison set explicitly: university senior-design bin robots (sweep #1), mowers, and delivery robots. It should report bill-of-materials cost per cm of placement accuracy.
- **Curb-placement accuracy target is undefined in the literature.** CartSeeker reports 96% pickup success and the Con-Tech patent claims a 1-inch sonar approach, but no source gives how precisely a cart must be placed for an ASL arm. Deriving a target (for example from city cart-placement rules, covered in another sweep) and measuring placement error vs. that target would ground the accuracy requirement.

### Searches run

WebSearch (standard mode unless noted). The session web-search budget ran out partway through, and the remaining lookups used WebFetch and the arXiv API.
1. ROVER 2024 outdoor visual SLAM benchmark dataset garden robot arXiv
2. DIDLM dataset degraded illumination LiDAR SLAM benchmark arXiv
3. u-blox ZED-F9P RTK accuracy evaluation under trees near buildings low-cost study
4. curb detection low-cost sensor sidewalk robot paper
5. Husqvarna EPOS RTK virtual boundary robotic mower accuracy 2-3 cm reference station
6. Segway Navimow price RTK + VSLAM wire-free mower US price i105
7. Mammotion Luba 2 AWD price RTK vision robot mower
8. Worx Landroid Vision camera-based wire-free mower no RTK price
9. Mammotion Yuka mini price vision RTK-free robot mower 2025
10. Starship Technologies delivery robot localization cameras map of lines edges no GPS accuracy
11. Kiwibot robot cost localization semi-autonomous remote operators cameras
12. Coco delivery robot teleoperated sidewalk navigation cost per robot
13. Starship Technologies patent "localisation" mobile robot straight lines extracted from camera images map data (patents.google.com only)
14. visual teach and repeat low-cost monocular camera outdoor route following paper
15. BearNav teach and repeat Krajnik low-cost robot seasonal changes
16. "Navigation without localisation" reliable teach and repeat convergence theorem Krajnik arXiv
17. Furgale Barfoot visual teach and repeat long-range rover autonomy 2010 Journal of Field Robotics
18. AprilTag outdoor localization accuracy distance sunlight evaluation fiducial markers comparison ArUco
19. Kalaitzakis fiducial markers pose estimation experimental comparison ARTag AprilTag ArUco STag
20. "Fiducial Markers for Pose Estimation" Kalaitzakis Journal of Intelligent & Robotic Systems 2021 ArUco accuracy results
21. wheel odometry drift percent distance traveled outdoor low-cost robot visual odometry comparison grass pavement
22. Visual Teach and Repeat Barfoot Furgale stereo VT&R lateral path-tracking error centimeters arXiv
23. "Static Positioning under Tree Canopy Using Low-Cost GNSS Receivers" horizontal error (one earlier attempt was cut off)
24. ZED-F9P ANN-MB-00 urban environment NRTK semi-open obstructed Sensors 2023 3136 (one earlier attempt was cut off)
25. SparkFun GPS-RTK2 ZED-F9P board price
26. ArduSimple simpleRTK2B price ZED-F9P starter kit
27. curb detection wheelchair depth camera RGB-D smart wheelchair curb step detection paper
28. 3D curb detection dataset LiDAR benchmark arXiv 2023 2024
29. mmWave radar curb detection low-cost automotive radar road boundary paper
30. wheelie bin detection dataset garbage can curbside deep learning refuse truck camera
31. automated side loader refuse truck automatic cart detection arm camera LiDAR "cart" grab system
32. trash bin pose estimation robot grasping waste container autonomous refuse collection robot arXiv
33. automated side loader cart recognition "96%" success rate visual recognition carts color size angles
34. Volvo ROAR robot refuse handling wheelie bin robot Chalmers drone 2016
35. garbage truck trash bin perception CNN color recognition autonomous driving stop grasp target trash bin paper
36. "Bin status" detection automated side loader front-end loader video computer vision dataset mAP Intelligent Systems with Applications 2023
37. Open Images dataset "Waste container" class bounding boxes (not executed: search budget exhausted)

arXiv API queries (export.arxiv.org/api/query): `all:"trash bin" AND robot`; `all:"garbage bin" AND detection`; `all:"waste container" AND detection`; `all:curb AND detection AND sidewalk`; `all:curb AND stereo AND detection`; `ti:curb AND ti:detection`; `ti:"trash can"`; `ti:"garbage can"`; `ti:"wheelie bin"` (no hits); `ti:"changing conditions" AND ti:localization`; `ti:4Seasons`; `ti:"lawn mower" AND localization`; `"robotic lawn mower" AND RTK`; `ti:"teach and repeat" AND "long-term"`; `mower AND robot AND localization`; `"multi-experience" AND "teach and repeat"`; `"experience-based navigation"`; `apriltag AND outdoor AND localization`; `"low-cost" AND "visual inertial" AND outdoor AND benchmark`; `"sidewalk robot" AND localization`; `"delivery robot" AND "low-cost" AND localization`; `driveway AND robot`; `ti:sidewalk AND ti:robot`; `ti:GNSS AND ti:RTK AND robot`; `ti:"wheel odometry" AND outdoor`; `ti:fiducial AND outdoor`; `ti:"visual teach"`; `abs:AprilTag AND outdoor AND accuracy`; `abs:odometry AND drift AND "low-cost" AND outdoor`; `abs:"u-blox" AND robot`; `abs:lawn AND robot AND RTK`.

Fetch failures (so the related claims are snippet-level or omitted): MDPI pages (403); one PMC page (captcha); Springer (login redirect); IEEE Xplore 9555800 (HTTP 418, so it was not used); TIB/VDE (403); Roboflow Universe (403); Notebookcheck (403); TechRadar and Tom's Guide (truncated); DuckDuckGo HTML (captcha); Bing (irrelevant results). No price for RealSense, OAK-D, RPLIDAR, Livox or TI radar boards could be verified, so none is given.

### Removed during verification

- "Trash-bin perception for automated garbage trucks (CNN identification + color classification), AIIPCC 2022" (vde-verlag.de/proceedings-en/565932026.html). Removed: the VDE link redirects to TIB, which shows a bot wall; the exact title and authors were never confirmed, and a Crossref search of AIIPCC 2022 did not find a matching paper.

### Link verification (2026-10-03)

- URLs checked: 54 unique (all resolved by curl except geo-matching 404; DOAJ, MDPI, Notebookcheck 403; Springer, openpolar.no and VDE/TIB bot walls).
- OK: 46 (resolved, or blocked but title confirmed via Crossref/OpenAlex, and content matched the entry; link-check tags upgraded for Slickdeals, Freshly Charged, US20210302989A1, PMC10056071 and CurbNet after opening them).
- Fixed: 7. Links replaced: 4 (geo-matching 404 -> ArduSimple product page, with the price updated to EUR 211 / USD 263.75; openpolar.no -> doi.org/10.1002/rob.20342; DOAJ -> doi.org/10.1016/j.iswa.2023.200229; MDPI -> doi.org/10.3390/rs14122856, with the title and authors corrected and an unconfirmed ">50 cm above 50-65% canopy" claim removed). Content corrected on a working link: 3 (WalkOCC: the dataset is 10 h from 3 robots, not 1,010 h from 33; Janos & Kuras urban-canyon numbers; LUBA 2 "3D Vision & RTK fusion" wording).
- Removed: 1 (AIIPCC 2022 VDE entry, see above).
- Confirmed only via search snippet: 1 URL (Notebookcheck, Yuka mini Vision EUR 1,199), plus the WORX AU prices and the Kalaitzakis et al. scope sentence, which rest on snippets of URLs that were opened or are otherwise confirmed.
