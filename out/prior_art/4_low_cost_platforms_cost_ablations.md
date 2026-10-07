## Prior art #4: Low-cost outdoor robot platforms and cost-vs-performance evidence

Scope: this sweep covers (a) low-cost, outdoor-capable mobile bases (hoverboard hub-motor builds, open-source rovers, low-cost field/agricultural robots) and commercial research UGVs as price anchors, (b) papers that measure performance against monetary cost (sensor/compute ablations, low-cost lidar/GNSS evaluations, Pareto and cost-normalized analyses), (c) norms for reporting cost and reproducibility, and (d) measured perception/SLAM performance on low-cost embedded compute. Every link below was opened with WebFetch or returned by a WebSearch result whose snippet supported the claim. Anything marked **UNVERIFIED** or **estimate** is our own inference, not a sourced fact. Prices were checked on or before 2026-10-03 and change often (see the Raspberry Pi entry).

---

### A. Low-cost outdoor-capable platforms (DIY, open source, products)

#### [hoverboard-firmware-hack-FOC (open firmware for hoverboard mainboards)](https://github.com/EFeru/hoverboard-firmware-hack-FOC)
- Type: other (open-source firmware)
- Who / when: GitHub user EFeru, GPL-3.0. About 1.8k stars and 1.4k forks at fetch time. A ROS 2 hardware interface that depends on this firmware is [DataBot-Labs/hoverboard_ros2_control](https://github.com/DataBot-Labs/hoverboard_ros2_control) (Jazzy/Humble, 78 stars).
- What it does / claims: Field-Oriented Control (FOC) firmware for stock hoverboard mainboards (STM32F103RCT6 or GD32F103RCT6), giving "reduced noise and vibrations", "smooth torque output and improved motor efficiency". It offers voltage, speed (closed-loop) and torque modes, with UART, PWM, PPM, iBUS, ADC and I2C inputs on the two 4-pin side cables. The README lists builds including wheelchairs, bobbycars, TranspOtterNG and a ROS driver.
- Cost or price info: none on the page. **Estimate (UNVERIFIED):** a used hoverboard bought locally is likely the cheapest way to get two in-wheel BLDC motors, a controller and a battery.
- Relevance to our bin-to-curb robot: this is the most likely drive train for a sub-$500 robot. Torque mode and the reported motor current let us measure traction and towing force directly, which a cost-vs-performance paper needs.
- Gap: the repo publishes no characterization of traction, towing force, slope climbing or energy per trip with a heavy towed load. A bin-robot study could supply that measured data.

#### [ROMR: A ROS-based open-source mobile robot (HardwareX 2023)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10197097)
- Type: paper (HardwareX, DOI 10.1016/j.ohx.2023.e00426)
- Who / when: Nwankwo, Fritze, Bartsch, Rueckert (Montanuniversität Leoben repository), 2023.
- What it does / claims: an open-source base with two 350 W hoverboard BLDC hub motors, an ODrive v3.6 controller, Jetson Nano plus Arduino Mega, RPLidar A2M8, RealSense D435i/T265 and an MPU-9250 IMU. Claims a 90 kg maximum payload. Tests were indoor: speed stability at 0.5–2.5 m/s, payload, Hector-SLAM and AMCL.
- Cost or price info: "costs less than $1500". Table 1 compares it with 11 commercial platforms, most in the $2,000–24,000 range. The BOM (Table 7) uses HardwareX columns: designator, quantity, unit cost (€), total cost (€), source, material type.
- Relevance to our bin-to-curb robot: this is the closest peer-reviewed precedent for a hoverboard-motor base with a large payload. It is also a template for how to present a BOM and a table of commercial alternatives.
- Gap: evaluated only indoors in a lab. It has no outdoor, slope or traction tests, no towing or docking, and no ablation that varies the sensor suite to show what each dollar buys.

#### [Mobile Hoverboard Robot Base (Cornell Tech Interaction Lab)](https://irl.tech.cornell.edu/mobile_hoverboard_robot_base)
- Type: student project / lab open-hardware page
- Who / when: Cornell Tech Interaction Lab (Wendy Ju's group). Related fieldwork: [Field Notes on Deploying Research Robots in Public Spaces](https://arxiv.org/abs/2404.18375) (Bu, Bremers, Colley, Ju; CHI LBW 2024). Press coverage of the HRI 2023 trash-barrel study: [IEEE Spectrum, 2023-03-16](https://spectrum.ieee.org/nyc-trash-robots).
- What it does / claims: a deconstructed hoverboard driven by an ODrive, with a Raspberry Pi running ROS 2 Humble. It is "designed to be attached to everyday objects — like a trash bin, a cart, or furniture". The "Trashbot" setup mounts a trash bin on a Rubbermaid BRUTE dolly. The robots were teleoperated (Wizard-of-Oz), not autonomous (Spectrum).
- Cost or price info: the [BOM page](https://irl.tech.cornell.edu/mobile_hoverboard_robot_base/bom) lists parts and vendor links but no prices or total.
- Relevance to our bin-to-curb robot: direct evidence that a hoverboard drive can move a trash bin. This is the nearest mechanical prior art from a well-known HRI lab, and reviewers may raise it.
- Gap: here the robot is the bin, rebuilt on a dolly. Nobody docks to and tows an unmodified municipal cart. Control is teleoperated, and there is no cost total, no autonomy and no performance metric.

#### [NASA-JPL Open Source Rover](https://github.com/nasa-jpl/open-source-rover)
- Type: student project / open hardware
- Who / when: NASA JPL, now maintained by community builders. Apache 2.0.
- What it does / claims: a 6-wheel rocker-bogie rover built from COTS parts (mostly goBILDA) with a Raspberry Pi. Top speed is about 1.6 m/s ([docs](https://open-source-rover.readthedocs.io/en/stable/)).
- Cost or price info: "~$1600 (about the cost of a TurtleBot 3 Waffle)" (GitHub/docs). This is "almost half" the original version's roughly $3,000 ([Hackaday.io, off-the-shelf edition](https://hackaday.io/project/192609-nasa-jpl-open-source-rover-off-the-shelf-edition)).
- Relevance to our bin-to-curb robot: a well-known price point for a hobbyist outdoor rover that reviewers will recognize. It is useful as a "commodity outdoor rover" baseline cost.
- Gap: no autonomy evaluation, no towing or docking, no cost-performance data. **Inference (UNVERIFIED):** its small gearmotors are probably not sized to tow a loaded cart.

#### [OpenMower (open-source RTK robotic lawn mower)](https://github.com/ClemensElflein/OpenMower)
- Type: product / open-source project
- Who / when: Clemens Elflein and community. About 6.7k stars. Software is GPL/MIT and documentation is CC BY-NC-SA 4.0.
- What it does / claims: replaces the mainboard of cheap robotic mowers (first the YardForce Classic 500) with a Raspberry Pi-based board and RTK GPS, giving "GPS-guided, map-aware" mowing without a perimeter wire.
- Cost or price info: about €700 for the build, excluding the donor mower and the RTK base station (GitHub README).
- Relevance to our bin-to-curb robot: the strongest hobbyist precedent for RTK autonomy in a residential yard on a consumer budget, and the "cheap donor chassis + RTK" pattern applies directly to a driveway robot.
- Gap: there is no peer-reviewed accuracy or reliability evaluation, and it is not tested near buildings or on driveways. It does no towing or docking, and gives no breakdown of what the RTK adds versus cheaper localization.

#### [EarthRover Mini / Zero (FrodoBots), New Atlas 2025-04-09](https://newatlas.com/robotics/earthrover-mini-4g-rover/)
- Type: product
- Who / when: FrodoBots (Singapore), reported by Ben Coxworth, 2025-04-09.
- What it does / claims: small 4G-teleoperated sidewalk rovers with front and rear cameras and GPS, rated IP34 with 4–5 h of runtime. The company says the technology is used by UC Berkeley, NUS and Georgia Tech.
- Cost or price info: EarthRover Mini $149 preorder / $249 retail. Mini+ $199/$299. Zero $299/$399 (New Atlas).
- Relevance to our bin-to-curb robot: sets a floor price for an outdoor platform with camera and GPS. It is useful when arguing which price bracket our robot sits in.
- Gap: too small to tow anything, built for teleoperation, and no published per-task performance data from the vendor.

#### [MuSHR: A Low-Cost, Open-Source Robotic Racecar for Education and Research](https://arxiv.org/abs/1908.08031)
- Type: paper (arXiv, v3 2023)
- Who / when: Srinivasa et al., University of Washington Personal Robotics Lab, 2019 (revised 2023).
- What it does / claims: a 1/10-scale open-source racecar with a full autonomy stack and tutorials.
- Cost or price info (PDF, Sec. V "Affordability & Performance"): the basic platform without sensors is "$600 (a similar MIT racecar setup costs about $1,000)". With a laser scanner and RGBD camera it is "around $900 (a similar MIT racecar setup costs about $2,800)".
- Relevance to our bin-to-curb robot: the standard way robotics papers argue "low-cost", with an itemized price set against a named, established platform of similar function.
- Gap: the section asserts "not sacrificing autonomous navigation performance", but the text we read has no matched-task performance comparison against the pricier platform. That is a price comparison, not a cost-performance measurement. The platform is indoor-oriented.

#### [OpenBot: Turning Smartphones into Robots (ICRA 2021)](https://arxiv.org/abs/2008.10631)
- Type: paper (ICRA 2021)
- Who / when: Matthias Müller, Vladlen Koltun, 2020/2021.
- What it does / claims: a roughly $50 robot body that uses an Android phone for sensing and compute. It demonstrates person following and real-time autonomous navigation in unstructured environments, and is "robust across different smartphones and robot bodies".
- Cost or price info: $50 body (abstract). The phone is excluded from that number.
- Relevance to our bin-to-curb robot: shows a flagship IEEE venue accepting a paper whose main contribution is cost. The phone-as-compute idea is a possible low-cost tier.
- Gap: small indoor/outdoor toy-scale body with no load handling. Its cost claim leaves out the phone, which is a reporting pitfall to avoid.

#### [Omobot: a low-cost mobile robot for autonomous search and fall detection (IEEE AIM 2024)](https://arxiv.org/abs/2408.05315)
- Type: paper (accepted to IEEE AIM 2024)
- Who / when: Ahamad, Ataei, Devabhaktuni, Dhiman, 2024.
- What it does / claims: an indoor mecanum-wheel robot with Jetson Nano, LD19 lidar and wireless charging, searching a home and detecting falls. A homography viewpoint transform improves YOLOv8-Pose by 6–12%.
- Cost or price info (PDF Table I): total **$693**. Line items include Jetson Nano with camera $300, LD19 lidar $99, motors with mecanum wheels $90, IMU $3. "Priced based on market price between November 2022 and December 2023."
- Relevance to our bin-to-curb robot: AIM, one of our target venues, accepted a low-cost robot paper with an itemized, date-stamped BOM. It also gives a sourced price for the LD19 lidar.
- Gap: indoor only, and it does no ablation of what the money buys (for example, what performance is lost without the $99 lidar).

#### [Development of a Robotic Platform with Autonomous Navigation System for Agriculture (AgriEngineering 2024)](https://mdpi-res.com/d_attachment/agriengineering/agriengineering-06-00192/article_deploy/agriengineering-06-00192.pdf)
- Type: paper (AgriEngineering 6:3362–3374, DOI 10.3390/agriengineering6030192)
- Who / when: Baltazar, Coelho, Valente, de Queiroz, Villar (Federal University of Viçosa, Brazil), 2024.
- What it does / claims: a differential-drive field robot (Jetson Nano, two Arduino Unos, EMLID Reach RTK rover and base, BNO055 IMU) running point-to-point PI steering. Cross-track RMSE was 0.217 m with waypoints only at the vertices and 0.103 m with waypoints every 3 m.
- Cost or price info (Table 1, prices from August 2024): total **$2,900.22**. The pair of EMLID Reach RTK modules alone is **$1,794**, about 62% of the BOM by our arithmetic. The discussion notes that systems with lower cross-track error used costlier sensors.
- Relevance to our bin-to-curb robot: a peer-reviewed low-cost outdoor robot with RTK and clear path-tracking metrics. It shows that RTK can dominate a low-cost BOM.
- Gap: the RTK-vs-cheaper-localization trade-off is discussed only qualitatively. The authors did not run the same robot with and without RTK or report cost-normalized accuracy.

#### [Milo, a Fully Autonomous Indoor/Outdoor Robotic Guide Dog](https://arxiv.org/abs/2607.19530)
- Type: paper (arXiv, submitted to CoRL 2026)
- Who / when: Golemo, Wolski, Moniz, Pal, 2026-07.
- What it does / claims: an open-source guide-dog system on a modified Unitree Go2 with onboard voxel mapping and a learned obstacle-avoidance policy. Evaluated on indoor and outdoor obstacle courses: "smoother navigation and fewer handler collisions" than costmap baselines.
- Cost or price info: "approximately $2k USD" versus about $50k for a trained guide dog (abstract).
- Relevance to our bin-to-curb robot: a recent example of framing cost against the incumbent service rather than other robots. The analogous framing for us is the robot versus a paid bin-valet service or existing bin robots.
- Gap: a different task, and the cost claim compares against a service rather than measuring sensor/compute trade-offs.

#### [Clearpath Jackal (price anchor): IEEE Spectrum launch article, 2014](https://spectrum.ieee.org/clearpath-hits-husky-with-shrink-ray-announces-jackal-ugv)
- Type: product
- Who / when: Clearpath Robotics. Article by Evan Ackerman, 2014-09-15.
- What it does / claims: a small outdoor research UGV that ships with integrated PC, GPS, IMU and wireless.
- Cost or price info: Spectrum (2014) says Clearpath expected the price to "settle somewhere in the high four figures to low five figures". A third-party listing ([moonlakeai](https://moonlakeai.com/robots/clearpath-jackal)) gives $15,000–$20,000 with a 20 kg payload. That listing is unofficial, since Clearpath does not publish list prices.
- Relevance to our bin-to-curb robot: the research-UGV price reviewers will compare against, roughly 15–40x a hobby build by our estimate.
- Gap: a research base, not a solution to any task. Its payload rating is small relative to towing a loaded cart (inference).

#### [Clearpath Husky (price anchor): third-party listing](https://www.moonlakeai.com/robots/clearpath-husky)
- Type: product
- Who / when: Clearpath Robotics. Listing accessed 2026-10-03.
- What it does / claims: a rugged outdoor research UGV with 100 kg payload (50 kg all-terrain) per the listing.
- Cost or price info: $19,000–$24,000 (third-party, unofficial). A separate search snippet attributed $30,000 to the Husky A300 on robotomated.com (not opened; **UNVERIFIED**).
- Relevance to our bin-to-curb robot: the commercial base whose payload class matches cart towing, which makes it the honest high-cost comparison.
- Gap: same as Jackal: a generic base with no task-level evaluation.

#### [AgileX Scout Mini (price anchor): RobotLAB listing](https://www.robotlab.com/store/agilex-scout-mini/)
- Type: product
- Who / when: AgileX Robotics. Listing accessed 2026-10-03.
- What it does / claims: a compact 4WD outdoor UGV with 10 kg payload (20 kg with mecanum wheels) and 2.7 m/s top speed.
- Cost or price info: "Starting at $4,500" (RobotLAB).
- Relevance to our bin-to-curb robot: the cheapest commercial outdoor research base we verified. It is a natural "commercial baseline" price in a cost table.
- Gap: low payload, and no task autonomy is included.

---

### B. Papers and data that measure cost vs. performance

#### [Resilient Sensor Architecture Design and Tradespace Analysis for Autonomous Vehicle Localization and Mapping](https://arxiv.org/abs/1907.08541)
- Type: paper (arXiv cs.RO, 2019)
- Who / when: Anne Collin, Antonio Terán Espinoza, 2019-07.
- What it does / claims: greedy sensor selection under a budget ($110,000 per selection) using SLAM uncertainty on KITTI sequences. It defines a cost-normalized objective, "cost-benefit: J = log det(Λ(s))/Cost(s)", and plots a Pareto front. PDF text: "there are architectures costing about $27,000, which achieve about 99% of the highest performance", combining stereo cameras with cheaper lidars instead of long-range lidar.
- Cost or price info: sensor prices range up to more than $100,000 per suite.
- Relevance to our bin-to-curb robot: the clearest published template for a cost-performance Pareto front and a cost-normalized metric in robot localization. We can copy the method at hobby scale.
- Gap: car-scale budgets, analysis on a dataset rather than a physical task, and no sub-$1k sensors. A bin-robot study could build the same Pareto front from real task trials with $10–$250 sensors.

#### [Multi-Objective Generation of Pareto-Optimal Perception Architectures for Autonomous Robotic Systems (MIT thesis, 2025)](https://dspace.mit.edu/entities/publication/14e39e72-b071-4fa9-8f0c-c539c4119fce)
- Type: other (master's thesis, MIT System Design and Management)
- Who / when: Rachael M. Putnam, 2025.
- What it does / claims: uses NSGA-II to co-design sensor type, count and placement against an entropy-based perception utility and **monetary cost M ($)**. In a Clearpath Jackal case study it finds 11 Pareto-optimal designs; an ANYmal-C study finds 25.
- Cost or price info: cost is an explicit optimization objective (exact figures not extracted).
- Relevance to our bin-to-curb robot: recent evidence that "cost as an axis" is a live research framing, and a citable method.
- Gap: it optimizes a perception-coverage proxy in design space, not measured task success on a deployed low-cost robot.

#### [Boxi: Design Decisions in the Context of Algorithmic Performance for Robotics (RSS 2025)](https://roboticsproceedings.org/rss21/p134.html)
- Type: paper (Robotics: Science and Systems XXI, 2025)
- Who / when: Frey, Tuna, Fu, Weibel, Patterson, Krummenacher, Müller, Nubert, Fallon, Cadena, Hutter, 2025.
- What it does / claims: a multi-sensor payload study finding that "time synchronization, calibration, and sensor modality have a crucial impact on the state estimation performance". It frames the analysis "in the context of cost considerations" and offers a sensor-suite "cookbook".
- Cost or price info: discussed qualitatively; no figures extracted.
- Relevance to our bin-to-curb robot: high-end evidence that cheap sensors can fail through bad synchronization and calibration rather than the sensor itself. Low-cost ablations should control for these.
- Gap: high-end research payload, not a sub-$1k robot, and no formal Pareto front.

#### [Cost-effective Mapping of Mobile Robot Based on the Fusion of UWB and Short-range 2D LiDAR (IEEE/ASME T-Mech)](https://arxiv.org/abs/2106.03648)
- Type: paper (IEEE/ASME Transactions on Mechatronics, accepted; arXiv 2021)
- Who / when: Ran Liu, Yongping He, Chau Yuen, Billy Pik Lik Lau, Rashid Ali, Wenpeng Fu, Zhiqiang Cao, 2021.
- What it does / claims: fusing UWB ranges with a short-range Hokuyo URG-04LX (5.6 m) gives "85.5% less mapping error than conventional GMapping with short-range LiDAR" in feature-sparse indoor spaces.
- Cost or price info (PDF Sec. V): "The price of our short-range 2D LiDAR is about 930 USD and each UWB node costs about 30 USD... total cost... about 1080 USD. However, a long-range 2D LiDAR (... Hokuyo UST-20LX ...) costs about 2600 USD."
- Relevance to our bin-to-curb robot: a model for arguing "cheap sensor + cheap infrastructure beats expensive sensor" with explicit dollar figures. Cheap beacons or fiducials at the curb or garage are the analogous idea for us.
- Gap: indoor, and $930 is "low-cost" only by 2021 lab standards. No sub-$100 lidars, and it reports a single comparison point rather than a curve.

#### [Feasibility of Using Low-Cost Dual-Frequency GNSS Receivers for Land Surveying (Sensors 2021)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8001986)
- Type: paper (Sensors 21(6):1956, DOI 10.3390/s21061956)
- Who / when: Wielgocka, Hadas, Kaczmarek, Marut, 2021.
- What it does / claims: a u-blox ZED-F9P with a u-blox ANN-MB-00 patch antenna, tested against geodetic-grade equipment. Signal strength (C/N0) was more than 7 dB-Hz weaker than a geodetic receiver, especially at low elevation. RTK and network RTK reached horizontal accuracy better than 5 cm and sub-decimeter vertical accuracy (abstract, via search snippet and PMC page).
- Cost or price info: "The current price of the hardware is lower than 250 EUR" (PMC page).
- Relevance to our bin-to-curb robot: the canonical peer-reviewed source for "about €250 of GNSS gets about 5 cm RTK", which is the RTK point in any sensor-cost ablation.
- Gap: static surveying conditions, not a moving robot beside a house or garage. No comparison with camera-based or fiducial curb localization.

#### [Accuracy evaluation of a Low-Cost Differential Global Positioning System for mobile robotics (IEEE Sensors 2023)](https://arxiv.org/abs/2306.12826)
- Type: paper (IEEE Sensors 2023)
- Who / when: Blesing, Finke, Hoose, Schweigert, Stenzel, 2023.
- What it does / claims: a ROS-enabled ZED-F9P DGPS/RTK setup with corrections from a public SAPOS service versus a locally built low-cost base. A moving robot was tracked by an outdoor 12-camera VICON system over 60 m². Static repeatability spans were about 1–3 cm. Dynamic translation RMSE (PDF Table III) was **0.073 m at 1.10 m/s**, 0.114 m at 1.68 m/s, 0.125 m at 2.07 m/s, 0.147 m at 2.57 m/s and 0.175 m at 3.12 m/s.
- Cost or price info: described as low-cost. No dollar total extracted.
- Relevance to our bin-to-curb robot: the best-matched evidence that a moving ground robot gets about 7 cm RTK error at walking speed. That sets the bar a camera or fiducial approach must meet for curb placement.
- Gap: the authors list comparison with a professional-grade receiver as future work. Testing was in an open motion-capture area, not next to a garage wall or under eaves.

#### [Reliability of RTK Positioning for Low-Cost Drones' Navigation across GNSS Critical Environments (Sensors 2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11435761/)
- Type: paper (Sensors, DOI 10.3390/s24186096)
- Who / when: Tavasci, Nex, Gandolfi, 2024.
- What it does / claims: a u-blox F9P (Holybro H-RTK F9P) flown past building façades and through a tunnel. Fix was lost after about 10 s, recovery took 9–13 s, and **"false fixes"** reached meter-level error (about 2 m vertical) while still flagged as fixed. The authors recommend rejecting solutions with HRMS/VRMS above 3–5 cm.
- Cost or price info: none extracted.
- Relevance to our bin-to-curb robot: the garage end of a driveway is exactly a façade or multipath environment. This is citable evidence that cheap RTK can fail silently there.
- Gap: drones, not ground robots. Nobody measured RTK fix and false-fix rates along a residential driveway from garage to curb.

#### [Precision RTK GNSS for low-cost robotic systems (USQ undergraduate thesis, 2021)](https://sear.unisq.edu.au/51802/)
- Type: student project
- Who / when: Simon Castles, University of Southern Queensland, 2021.
- What it does / claims: ArduSimple ZED-F9P boards, XBee radio and STM32. Measured cross-track error of 12.13 mm and heading accuracy of 0.45°.
- Cost or price info: framed as low-cost. Current board price: ArduSimple lists [simpleRTK2B Budget](https://www.ardusimple.com/product/simplertk2b/) (ZED-F9P) at **€172** each. A rover-plus-base pair needs two boards (our inference) plus antennas.
- Relevance to our bin-to-curb robot: shows that an undergraduate can build a working low-cost RTK system, which matters for a feasibility argument with high-school builders.
- Gap: a farm use case with open sky, and no cost-vs-alternative comparison.

#### [Calibration of 2D LiDAR sensors (seminar slides, Silesian Univ. of Technology, 2022)](https://cobotagv.aei.polsl.pl/images/files/seminary_2022/Calibration_of_2D_LiDARs_PB.pdf)
- Type: other (seminar slides, not peer-reviewed)
- Who / when: Piotr Biernacki, Silesian University of Technology, 2022.
- What it does / claims: compared two hobby lidars (RPLidar A1, A2) with two industrial safety scanners (SICK microScan3, Leuze RSL425) against a Leica DISTO over roughly 0.1–2.25 m. Raw RMSE: RPLidar A2 0.0064 m, RPLidar A1 0.0079 m, SICK 0.0124 m, Leuze 0.0218 m (PDF tables). Linear calibration reduced the errors further.
- Cost or price info: none in the slides. **Inference:** the industrial scanners cost far more than the RPLidars.
- Relevance to our bin-to-curb robot: at docking ranges under about 2.5 m, cheap lidars can match or beat industrial scanners on raw range accuracy. That supports using a cheap lidar for hitching.
- Gap: indoor and short range only, no sunlight, no LD06/LD19, not peer-reviewed.

#### [A Comparative Study of Multiple 2D Laser Scanners for Outdoor Measurements (Engineering Proceedings 32, 2023)](https://www.mdpi.com/2673-4591/32/1/16)
- Type: paper (conference proceedings, MDPI; DOI 10.3390/engproc2023032016). The page returned 403 to WebFetch, so the claim rests on the search snippet; title, DOI and URL confirmed via the Crossref record.
- Who / when: Shamim, Jafri (per Crossref), 2023.
- What it does / claims (search snippet): outdoor comparison of compact 2D scanners. "URG-04LX and UTM-30LX have less dependency on direct sunlight exposure... while RP Lidar shows significant variations."
- Cost or price info: not extracted.
- Relevance to our bin-to-curb robot: driveway operation is in sunlight, so cheap triangulation lidars may degrade. This is a cost-vs-robustness axis to measure.
- Gap: does not cover the cheaper dToF LD06/LD19 class, and gives no task-level effect such as curb or bin detection rate versus illuminance.

#### [Comparing low-cost 2D scanning Lidars (DIYRobocars, 2017)](https://www.diyrobocars.com/2017/05/28/comparing-low-cost-2d-scanning-lidars/)
- Type: other (practitioner blog)
- Who / when: "zlite" (DIY Robocars), 2017-05-28.
- What it does / claims: RPLidar A2 versus Scanse Sweep. **Outdoors in sunlight both topped out at about 4–5 m**, against 14–16 m indoors for the A2.
- Cost or price info: RPLidar A2 $379–$450 and Scanse Sweep $350 (2017). Today's dToF class: Waveshare lists the [LD19](https://www.waveshare.com/product/dtof-lidar-ld19.htm) at **$95.99** (now marked discontinued), spec ±45 mm (0.3–12 m), 4500 Hz sampling, **30 klux** ambient-light tolerance. Omobot's BOM lists the LD19 at $99.
- Relevance to our bin-to-curb robot: practical evidence that cheap 2D lidar range shrinks sharply in sun. Curb detection at a few meters may still work, and this is an easy ablation to run.
- Gap: anecdotal, with no peer-reviewed sunlight evaluation of the LD06/LD19 (none found in our searches).

#### [A comparative evaluation of low-cost IMUs for unmanned autonomous systems (IEEE MFI 2010)](https://sites.ucmerced.edu/yqchen/publications/comparative-evaluation-low-cost-imus-unmanned-autonomous-systems)
- Type: paper (IEEE Int. Conf. on Multisensor Fusion and Integration for Intelligent Systems, 2010)
- Who / when: Chao, Coopmans, Di, Chen (YangQuan Chen's group, now UC Merced MESA Lab), 2010.
- What it does / claims: comparative evaluation of low-cost IMUs. The abstract was not available on the page (**details UNVERIFIED**).
- Cost or price info: not extracted.
- Relevance to our bin-to-curb robot: a precedent for low-cost sensor comparison from a California lab (UC Merced), useful for lab outreach.
- Gap: aerial focus and old hardware, with no ground-robot task metric.

---

### C. Norms for reporting cost and reproducibility

#### [Economic savings for scientific free and open source technology: A review (HardwareX 2020)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7480774/)
- Type: paper (HardwareX, DOI 10.1016/j.ohx.2020.e00139)
- Who / when: Joshua M. Pearce, 2020.
- What it does / claims: reviewed 86 HardwareX and 33 PLOS Open Source Toolkit hardware articles. Average savings versus proprietary equivalents were **87%** (89% Arduino-based, 92% RepRap 3-D printed, 94% both). **92.4%** of articles reported device cost, but only **37.8%** had a proprietary-equivalent cost.
- Cost or price info: defines savings as **S = (P − O)/P**, where P is the proprietary price and O is the open-source cost in USD, "limited to the material costs". It acknowledges that proprietary prices include assembly, warranty and support.
- Relevance to our bin-to-curb robot: the standard formula for a "% cheaper" claim, and a warning to report labor hours and name a real commercial equivalent.
- Gap: a materials-only comparison with no performance normalization. A bin-robot paper can go further by reporting cost per successful task or a cost-performance Pareto front.

#### [Return on investment for open source scientific hardware development (Science and Public Policy 2015)](https://digitalcommons.mtu.edu/materials_fp/97)
- Type: paper (DOI 10.1093/scipol/scv034)
- Who / when: Joshua M. Pearce, 2015.
- What it does / claims: a method to value open hardware as the savings users get by replicating it, scaled by downloads. The syringe-pump case study shows ROI of "hundreds to thousands of percent".
- Cost or price info: methodology only.
- Relevance to our bin-to-curb robot: supports a "release the BOM and code" argument in the paper's impact section.
- Gap: not robotics-specific, and no performance dimension.

#### [HardwareX manuscript templates (Zenodo)](https://zenodo.org/record/5078227)
- Type: standard (journal template)
- Who / when: Todd Duncombe (HardwareX), published 2021-07-07, version July 2022.
- What it does / claims: the official HardwareX manuscript template in .docx, .odt, .tex and PDF. Requirements are detailed in the Guide for Authors. The Elsevier guide page returned 403 to WebFetch, so we could not quote it directly. The BOM convention, as used in ROMR (above), is designator, component, number, cost per unit, total cost, source of materials and material type, with the currency stated.
- Cost or price info: n/a.
- Relevance to our bin-to-curb robot: adopting the HardwareX BOM columns plus a purchase-date column (as Omobot and Baltazar et al. did) makes a "low-cost" claim auditable. It also makes a later HardwareX companion paper easy to write.
- Gap: the template standardizes reporting but requires no cost-vs-performance analysis.

How IEEE-venue robotics papers in this sweep make a "low-cost" claim credible, as observed in the entries above:
1. An itemized BOM with a purchase-date window: Omobot (AIM 2024) "Nov 2022–Dec 2023", Baltazar et al. "August 2024".
2. A named, price-matched comparator: MuSHR versus MIT RACECAR; ROMR versus 11 commercial platforms; Liu et al. versus a long-range Hokuyo.
3. A cost-normalized objective or Pareto front: Collin & Terán Espinoza.

Most papers do only 1 and 2.

---

### D. Low-cost embedded compute for perception and SLAM (measured)

#### [A Comprehensive Evaluation of Deep Learning Object Detection Models on Heterogeneous Edge Devices](https://arxiv.org/abs/2409.16808)
- Type: paper (arXiv cs.CV, v3 revised 2026-07)
- Who / when: Alqahtani, Cheema, Rodriguez, Toosi, 2024–2026.
- What it does / claims: benchmarks YOLOv8 n/s/m, EfficientDet-Lite and SSD on Raspberry Pi 3/4/5 (with and without Coral TPU), Pi 5 with AI HAT+, Jetson Nano and Jetson Orin Nano, measuring latency, energy and mAP. The Orin Nano gives "the most favorable overall balance across most model families". SSD MobileNet V1 has the lowest latency and energy but also the lowest accuracy.
- Cost or price info: not extracted.
- Relevance to our bin-to-curb robot: a citable, multi-device baseline for choosing the compute tier in a cost ablation.
- Gap: benchmark images, not a robot task. No cost-normalized metric was extracted.

#### [A Performance Analysis of YOLO Models for Deployment on Constrained Computational Edge Devices in Drone Applications](https://arxiv.org/abs/2502.15737)
- Type: paper (arXiv, 2025)
- Who / when: Rey, Bernardos, Dobrzycki, Carramiñana, Bergesio, Besada, Casar, 2025-02.
- What it does / claims: YOLOv8n/s on Jetson Orin Nano, Orin NX and Raspberry Pi 5, with post-training quantization. YOLOv8n reached 52 FPS on Orin NX (65 FPS INT8). The Pi 5 "failed to satisfy the real-time processing needs in spite of its suitability for low-energy consumption applications."
- Cost or price info: none extracted.
- Relevance to our bin-to-curb robot: evidence that a CPU-only Pi 5 struggles with real-time CNN detection, which motivates an accelerator or a lighter perception tier.
- Gap: drone framing, and "real-time" is defined for aerial video rather than a slow ground robot. A bin robot at under 1 m/s may tolerate much lower FPS, which is worth measuring.

#### [Ultralytics guide: Raspberry Pi (YOLO benchmarks)](https://docs.ultralytics.com/guides/raspberry-pi/) and [Ultralytics guide: NVIDIA Jetson](https://docs.ultralytics.com/guides/nvidia-jetson/)
- Type: other (vendor documentation benchmarks)
- Who / when: Ultralytics. Pages accessed 2026-10-03 (Jetson results "benchmarked with Ultralytics 8.4.33").
- What it does / claims: YOLO26n on a **Raspberry Pi 5** takes **67.03 ms/image with NCNN** (about 15 FPS), 125.99 ms with ONNX and 299.09 ms with PyTorch. YOLO11n with ONNX runs at 6.79 FPS against 7.79 FPS for YOLO26n. On a **Jetson Orin Nano Super**, YOLO26n takes **4.57 ms (TensorRT FP16)** and 3.80 ms (INT8), with mAP50-95 of 0.480 and 0.449. Times exclude pre- and post-processing.
- Cost or price info: see the next entry for board prices.
- Relevance to our bin-to-curb robot: two devices measured with the same software stack, which makes a clean "latency per dollar" comparison possible.
- Gap: COCO-style inference only, with no end-to-end robot loop or power under load.

#### [Jetson Orin Nano Super Developer Kit price and specs (NVIDIA blog, 2024-12-17)](https://developer.nvidia.com/blog/nvidia-jetson-orin-nano-developer-kit-gets-a-super-boost/) and [Raspberry Pi 5 product page](https://www.raspberrypi.com/products/raspberry-pi-5/)
- Type: product
- Who / when: NVIDIA (2024-12-17) and Raspberry Pi Ltd (page accessed 2026-10-03).
- What it does / claims: the Orin Nano Super has 67 sparse / 33 dense TOPS and 7/15/25 W modes. The Pi 5 uses a BCM2712 with four Cortex-A76 cores at 2.4 GHz.
- Cost or price info: Orin Nano Super dev kit **$249** (cut from $499). On 2026-10-03 the Pi 5 page displayed only one price: **"Raspberry Pi 5 16GB is available now for $305."** Prices for other RAM variants were not shown and must be checked at purchase.
- Relevance to our bin-to-curb robot: compute is a major cost line, and prices are volatile, so every price in the paper should be date-stamped.
- Gap: n/a (price anchors).

#### [Benchmark of multistream inference on Raspberry Pi 5 with Hailo-8 (Seeed wiki)](https://wiki.seeedstudio.com/benchmark_of_multistream_inference_on_raspberrypi5_with_hailo8/)
- Type: other (vendor benchmark)
- Who / when: Seeed Studio. Accessed 2026-10-03.
- What it does / claims: YOLOv8m at 640×640 on a Pi 5 with a Hailo-8 accelerator runs at **39.82 FPS on PCIe Gen2 and 76.99 FPS on Gen3** for a single stream, dropping to 16.94 FPS with 4 streams.
- Cost or price info: not on the page. The accelerator price is **UNVERIFIED** here.
- Relevance to our bin-to-curb robot: a middle tier (Pi 5 plus accelerator) between a CPU-only Pi and a Jetson.
- Gap: a vendor benchmark, not peer-reviewed, and no robotics task.

#### [Jetson-ORB-SLAM3: Accuracy-Preserving GPU Implementation for Edge Computing Devices](https://arxiv.org/abs/2608.17874)
- Type: paper (arXiv, 2026-08-18)
- Who / when: Roy, Yadav, Jain, 2026.
- What it does / claims: a GPU ORB front end on Jetson Orin Nano with 94.7% keypoint and 99.9% descriptor agreement against the CPU detector. It sustains **32 FPS mean over 11 EuRoC sequences** (monocular-inertial) on the 7 W device. CNN loop-closure queries take 2.2 ms (180x faster).
- Cost or price info: none. The device is about $249 per NVIDIA above.
- Relevance to our bin-to-curb robot: the most recent measured visual SLAM rate on the cheapest Jetson. It is the high-compute point for a visual-localization ablation.
- Gap: EuRoC (indoor drone) data, not an outdoor driveway, and no Raspberry Pi comparison.

#### [Run Your Visual-Inertial Odometry on NVIDIA Jetson: Benchmark Tests on a Micro Aerial Vehicle](https://arxiv.org/abs/2103.01655)
- Type: paper (arXiv, 2021)
- Who / when: Jeon, Jung, Lee, Choi, Myung, 2021-03.
- What it does / claims: compares VINS-Mono, VINS-Fusion, Kimera, ALVIO, Stereo-MSCKF, ORB-SLAM2 (stereo) and ROVIO on Jetson TX2, Xavier NX and AGX Xavier for accuracy, CPU use and memory. Introduces the KAIST VIO dataset.
- Cost or price info: none extracted.
- Relevance to our bin-to-curb robot: the standard method for a VIO-algorithm-by-board matrix that our team could replicate at lower price points.
- Gap: older Jetsons, aerial motion, no price axis and no Raspberry Pi.

#### [SMF-VO: Direct Ego-Motion Estimation via Sparse Motion Fields](https://arxiv.org/abs/2511.09072)
- Type: paper (arXiv, 2025, revised 2026-07)
- Who / when: Yang, Yoon, Jung, Lim, 2025.
- What it does / claims: lightweight visual odometry that estimates velocity directly from optical flow and achieves **"over 100 FPS on a Raspberry Pi 5 using only a CPU"**.
- Cost or price info: none.
- Relevance to our bin-to-curb robot: shows that a CPU-only Pi 5 can run visual odometry far faster than CNN detection, which supports a low-cost camera-only localization tier.
- Gap: odometry rather than global localization, and no driveway or curb task.

#### [RaGNNarok: A Light-Weight Graph Neural Network for Enhancing Radar Point Clouds on Unmanned Ground Vehicles (IROS 2025)](https://arxiv.org/abs/2507.00937)
- Type: paper (IROS 2025)
- Who / when: Hunt, Luo, Hallyburton, Nillongo, Li, Chen, Pajic (2025).
- What it does / claims: enhances mmWave radar point clouds for localization, SLAM and navigation on low-cost UGVs, with **7.3 ms inference on a Raspberry Pi 5** and no extra compute.
- Cost or price info: radar called "cost-effective". No figures extracted.
- Relevance to our bin-to-curb robot: an IROS example of "Pi 5 as the compute" accepted at a target venue. Radar is a weather-robust sensor option for night pickups.
- Gap: indoor-oriented evaluation, and no cost-performance curve.

#### [TinyNav: End-to-End TinyML for Real-Time Autonomous Navigation on Microcontrollers](https://arxiv.org/abs/2603.11071)
- Type: paper (CUCAI 2026, Canadian Undergraduate Conference on AI)
- Who / when: Roy, Jadallah, Lapid, Ahmad, Afroushe, Bayrak, 2026-03.
- What it does / claims: a 23k-parameter 2D CNN on an ESP32 maps a 20-frame window of depth data to steering and throttle with **30 ms inference latency**.
- Cost or price info: not stated in the abstract.
- Relevance to our bin-to-curb robot: (1) a microcontroller-only tier, the cheapest point on a compute Pareto front, and (2) an undergraduate-authored venue precedent.
- Gap: no quantitative task success in the abstract, and no load-handling task.

#### [Nano-U: Efficient Terrain Segmentation for Tiny Robot Navigation (TAROS 2026)](https://arxiv.org/abs/2605.10210)
- Type: paper (TAROS 2026)
- Who / when: Pizzolato, Pasti, Bellotto, 2026.
- What it does / claims: a binary terrain-segmentation network with "a few thousand parameters", distilled and quantized to run on an **ESP32-S3** via the Rust MicroFlow engine. Tested on the Botanic Garden dataset and a custom agricultural dataset (TinyAgri).
- Cost or price info: none extracted.
- Relevance to our bin-to-curb robot: microcontroller-class outdoor segmentation. Driveway-vs-lawn or drivable-surface segmentation is a near analogue to curb and driveway-edge detection.
- Gap: latency and accuracy figures not extracted, no driveway or curb classes, no cost comparison.

#### [Design and Implementation of an Ultra-Low-Cost Wall-Climbing Robot for Infrastructure Crack Detection](https://arxiv.org/abs/2609.26130)
- Type: paper (arXiv, 2026-08)
- Who / when: Modak, Pretom, Tarafder, Drew, 2026.
- What it does / claims: a robot built for about **$25** in total, with an ESP32-CAM, a 3D-printed chassis and fan adhesion. Crack detection uses a two-stage YOLOv8 plus CNN/EfficientNet-B0 pipeline. Whether inference runs on board is not stated in the abstract.
- Cost or price info: about $25 total (abstract).
- Relevance to our bin-to-curb robot: a 2026 example of a paper whose headline is extreme low cost.
- Gap: unclear on-board versus off-board compute, which shows why a cost claim must state where computation happens. Not a ground-vehicle task.

---

### Gaps and opportunities

- **No published towing or docking characterization of hoverboard hub-motor drives.** ROMR claims 90 kg payload but tested only indoors. The Cornell hoverboard base carries a bin on a dolly under teleoperation. The FOC firmware has a torque mode but no published measurements. A bin-robot paper could report pull force, wheel slip, slope limit and Wh per trip while towing 64/96-gal carts, with the drive-train cost alongside.
- **Cost-performance Pareto analysis exists only at car or research scale.** Collin & Terán Espinoza work in the $27k–$110k range on KITTI data, Putnam optimizes a perception proxy for a Jackal, and Boxi discusses cost only qualitatively. There is room for a hobby-scale Pareto front (about $0 to $300 of sensors: camera only, + LD19 lidar, + ZED-F9P RTK, + fiducials) measured on real task success and final curb-placement error.
- **Low-cost RTK has not been evaluated along residential driveways next to a house or garage.** Wielgocka shows about 5 cm RTK in survey conditions. Blesing shows 7–17 cm dynamic RMSE in open space. Tavasci shows silent false fixes of about 2 m near façades. Baltazar's RTK pair was about 62% of a $2,900 BOM. A study could measure fix rate, false-fix rate and placement error from garage to curb, and ask whether about €172–250 of RTK beats a cheaper camera or fiducial method.
- **No peer-reviewed sunlight evaluation of dToF hobby lidars (LD06/LD19).** The outdoor 2D-scanner study (MDPI 2023) found RPLidar sensitive to direct sun. DIYRobocars reports only 4–5 m range in sun. The LD19 is specified at 30 klux. The team could measure bin and curb detection rate against illuminance (a $20 lux meter) and time of day.
- **Compute benchmarks use datasets, not tasks.** The Ultralytics, Alqahtani, Rey and Jetson-ORB-SLAM3 results are on COCO or EuRoC. CPU Pi 5 YOLO26n takes about 67 ms versus 4.6 ms on the Orin Nano Super (TensorRT FP16), yet a slow bin robot may not need high FPS. Reporting task success, latency and power per dollar for ESP32 (TinyNav/Nano-U tier), Pi 5, Pi 5 + Hailo and Orin Nano would fill this gap.
- **Low-cost platform papers argue cost by price list, not by measured trade-off.** MuSHR asserts "not sacrificing" performance, OpenBot excludes the phone from its $50, and Omobot and ROMR give BOMs without ablations. A cost-normalized metric would be a distinguishing contribution: in the spirit of Collin's J = log det/Cost, for example "successful round trips per $100 of hardware" or "placement error vs BOM $".
- **Credible cost reporting conventions exist but are seldom fully applied.** Pearce found only 37.8% of open-hardware papers name a proprietary equivalent, and his savings formula counts materials only. Prices also move: the Pi 5 page showed only "16GB $305" on 2026-10-03, and the LD19 is now listed as discontinued. A strong paper would include a HardwareX-style BOM with purchase dates, assembly hours, and named commercial comparators (AgileX Scout Mini from $4,500; Jackal $15–20k and Husky $19–24k, both unofficial third-party listings).
- **Cheap infrastructure versus an expensive sensor is unexplored for curbs and bins.** Liu et al. show $30 UWB nodes plus a cheaper lidar can match a $2,600 lidar indoors. The bin-robot analogue is a few dollars of printed fiducials or a reflector at the curb or garage, compared head-to-head against RTK and lidar on placement accuracy.
- **Mechanical and price-floor prior art reviewers may raise:** Cornell's hoverboard Trashbot (bin-as-robot, teleoperated), OpenMower (consumer RTK yard robot, about €700 plus donor) and EarthRover ($149–$299 outdoor camera+GPS rover). Our claim must be "autonomous docking with an unmodified municipal cart at cost X with measured performance Y", not merely "a cheap outdoor robot".

### Searches run

WebSearch, 39 queries ("standard" unless noted). The session-wide WebSearch budget (200) was exhausted near the end of this sweep, so the last four planned queries could not run and were partly replaced by arXiv API queries via WebFetch.
1. hoverboard hub motor robot open source firmware FOC outdoor robot
2. JPL Open Source Rover cost build price
3. low-cost outdoor mobile robot under $1000 paper evaluation arXiv
4. Clearpath Jackal price USD
5. ROMR ROS-based open-source mobile robot HardwareX hoverboard
6. Clearpath Husky price robot research platform cost
7. AgileX Scout Mini price USD
8. evaluation of low-cost 2D lidar LD06 LD19 RPLIDAR accuracy comparison paper
9. low-cost RTK GNSS u-blox ZED-F9P versus survey-grade receiver accuracy comparison paper
10. HardwareX bill of materials template cost guidelines for authors
11. Raspberry Pi 5 visual SLAM ORB-SLAM3 benchmark frame rate Jetson Orin Nano comparison
12. HardwareX "Bill of materials summary" "Designator" "Cost per unit" "Source of materials" "Material type"
13. Pearce "return on investment" open source scientific hardware cost savings commercial equivalent
14. cost-performance trade-off sensor suite autonomous mobile robot localization Pareto lidar camera GNSS cost
15. low-cost agricultural robot open source FarmBot Acorn Twisted Fields price
16. Pearce "Economic savings for scientific free and open source technology: A review" HardwareX 2020
17. "Sensors" 2021 u-blox ZED-F9P low-cost receiver performance RTK field experiments
18. low-cost 2D LiDAR outdoor sunlight performance evaluation RPLIDAR LD06 paper (extended)
19. "Calibration of 2D LiDARs" RPLidar A1 A2 comparison
20. wheelchair motor robot platform low cost outdoor ROS build
21. Raspberry Pi 5 YOLO object detection FPS benchmark Hailo AI Kit vs Jetson Orin Nano
22. arXiv benchmark edge devices YOLOv8 Raspberry Pi 5 Jetson Orin Nano latency energy paper 2024
23. hoverboard motors robot ROS hoverboard_driver mobile robot outdoor project
24. Cornell Tech trash barrel robots New York City HRI paper Wendy Ju
25. low-cost RTK GNSS mobile robot navigation evaluation under trees buildings multipath ZED-F9P robot accuracy fix rate
26. "low-cost" sensors ablation lidar vs camera vs RTK autonomous navigation robot cost accuracy comparison arXiv field robot (extended)
27. OpenMower open source RTK GPS robotic lawn mower YardForce ZED-F9P cost
28. FrodoBots EarthRover low-cost sidewalk robot price research dataset
29. OpenBot Turning Smartphones into Robots ICRA 2021 $50 robot body
30. HardwareX low-cost open-source agricultural field robot RTK GNSS cost evaluation
31. MuSHR low-cost open-source robotic racecar cost arXiv
32. ArduSimple simpleRTK2B price ZED-F9P board USD
33. LDROBOT LD19 LD06 lidar price DFRobot specifications 4500 samples sunlight
34. "High-Accuracy Adaptive Low-Cost Location Sensing Subsystems for Autonomous Rover in Precision Agriculture"
35. IEEE Access 2020 GNSS receivers used in precision agriculture low-cost comparison 8955794
36. low-cost lidar vs camera SLAM outdoor comparison cost-effectiveness mobile robot Livox Mid-360 vs RealSense vs RPLIDAR evaluation
37. robot navigation "cost-effectiveness" sensor configuration ablation "price" success rate localization error low-cost vs high-end sensors study (extended)
38. arXiv evaluation consumer-grade sensors vs high-end sensors SLAM benchmark price comparison dataset low-cost IMU camera lidar
39. benchmarking low-cost and medium-cost IMU AGV operation performs equally well

Blocked by the budget (not run): "Run Your Visual-Inertial Odometry on NVIDIA Jetson" benchmark tests (later found via the arXiv API); Delmerico/Scaramuzza VIO benchmark on embedded computers; Raspberry Pi 5 ROS 2 slam_toolbox CPU benchmark; ORB-SLAM3 on Raspberry Pi 4 frame rate.

arXiv API queries (export.arxiv.org via WebFetch):
- all:"visual-inertial odometry" AND Jetson AND benchmark
- all:"Raspberry Pi 5" AND (SLAM OR odometry)
- all:ESP32 AND ("object detection" OR robot OR TinyML)
- all:"low-cost" AND "mobile robot" AND outdoor AND (hoverboard OR "open-source")
- abs:"low-cost" AND outdoor AND robot AND (USD OR $ OR dollars OR affordable)
- abs:cost AND Pareto AND (sensor OR sensing) AND robot

Found but not opened or not used (for coverage judgment): LeVoir et al., "High-Accuracy Adaptive Low-Cost Location Sensing Subsystems for Autonomous Rover in Precision Agriculture", IEEE OJIA 2020 (title, authors and venue confirmed via the DOAJ search result only). Pini et al., "Experimental Testbed and Methodology for the Assessment of RTK GNSS Receivers Used in Precision Agriculture", IEEE Access 2020 (search snippet only). "Static Positioning under Tree Canopy Using Low-Cost GNSS Receivers" (Sensors 2023; the PMC page was CAPTCHA-blocked). Twisted Fields Acorn (forum domain did not resolve; price undetermined). SuperDroid Robots wheelchair-motor ATR platforms (pages returned 403; price **UNVERIFIED**). Lidar Variability (arXiv 2507.04321), which compares Livox Mid-360/Avia with Ouster but gives no price data.

### Link verification (2026-10-03)

- URLs checked: 52 (unique)
- OK: 51. 47 returned HTTP 200 to curl with matching page title/content; 1 (PMC8001986) was CAPTCHA-blocked for curl but confirmed with WebFetch; 3 returned 403/406 to curl but were confirmed with WebFetch (DIYRobocars, Raspberry Pi 5 page, Zenodo HardwareX templates). Key figures spot-checked in source text (Baltazar $2,900.22 / $1,794 / 0.217 m / 0.103 m; Biernacki RMSE values; Pearce 87% / 92.4% / 37.8%; ROMR "less than $1500"; Wielgocka "lower than 250 EUR").
- Fixed: 0 links (one metadata correction: authors of the Engineering Proceedings 32 lidar paper added from Crossref).
- Removed: 0
- Confirmed only via search snippet: 1 (mdpi.com/2673-4591/32/1/16: 403 to curl and WebFetch; title/DOI/URL confirmed via Crossref, but the sunlight claim rests on the earlier search snippet).

