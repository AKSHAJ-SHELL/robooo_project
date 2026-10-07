# Prior art: low-cost autonomous trash-bin-to-curb robot

Date: 2026-10-03

**Method note.** This file merges four prior-art sweeps that ran in parallel on 2026-10-03. Each covered one part of the problem: (1) bin-moving robots, products, patents and cart standards; (2) docking with, hitching to and towing unmodified wheeled carts; (3) driveway localization, curb detection and bin detection outdoors; (4) low-cost outdoor platforms and cost-vs-performance evidence. Each sweep used web search, direct page fetches, the arXiv API and Google Patents. Each then ran its own link-verification pass that re-opened every URL with curl or WebFetch (Crossref, OpenAlex or Europe PMC metadata stood in for bot-blocked publisher pages) and checked page titles and quoted figures against the sources. The four passes logged 207 URL checks (some URLs appear in more than one sweep). They removed 2 entries as unverifiable and corrected 9, and 5 claims still rest only on a search-result snippet; those are labeled in the section files. Sections 1-5 below are a synthesis, and every link in them is copied from the section files, which are appended verbatim under "Detailed prior art". Anything marked *Inference* or *Estimate* is reasoning, not a sourced fact. Prices are as seen on or before 2026-10-03 and change often. **Coverage limits:** the sweeps ran out of web-search budget. They did not keyword-search IEEE Xplore or Google Scholar for bin robots, crowdfunding campaigns, non-English markets, bin-valet services, municipal cart-placement rules, or older PR2-era cart-pushing work. Every "nobody has done X" statement below is therefore bounded by these limits.

## Executive summary

### (a) Bin-to-curb robots and products

- **The task is decades old.** Rail- and track-guided house-to-curb carts were patented in 1991 and 1994 ([US5042642A](https://patents.google.com/patent/US5042642), [US5353887A](https://patents.google.com/patent/US5353887)). Both patents have expired, and both systems need fixed infrastructure.
- **Student builds exist, but none reports quantitative field results:**
  - SPARC, UCF 2018 ([project page](https://www.ece.ucf.edu/seniordesign/sp2018su2018/g12)): a crawler carries the bin, which is strapped on. It navigates with GPS, a Pixy camera and a colored curb stake. It has no encoders, was designed for a 50 lb load, and was estimated at about $809. The conference paper gives no success rate or placement error.
  - GRAD, UCF 2020 ([project page](https://www.ece.ucf.edu/seniordesign/su2020fa2020/g16)): motors are bolted under a 32-gal can, so the bin is modified. It follows an IR tape line and was estimated at $507. The paper says its objectives were "satisfied" but gives no trial data.
  - FAMU-FSU Team 311, 2019 ([project page](https://eng-web1.eng.famu.fsu.edu/me/senior_design/2019/team311/)): a 2x6 ft platform carries both bins and is driven by BLE joystick. The BOM is $1,980.85, and it was designed for 250 lb up a 5-degree incline.
  - Wentworth, ASEE 2009 ([paper](https://peer.asee.org/autonomous-garbage-removal-system.pdf)): a 3/8-scale carrier that cost $386.52. Its RF direction finding was "very sporadic" outdoors.
  - FAU WALLEE, 2022 ([page](https://www.fau.edu/engineering/senior-design/projects/spring2022/wallee-self-driving-garbage-can)): a 96-gal can is ratchet-strapped into a chassis, which runs by RC or a preprogrammed path.
  - CSUF, 2017 ([news](https://news.fullerton.edu/?p=5190)): the bin itself is the robot. This is a California precedent.
  - **Wheelie Drive** (NZ high-school student, 2019 Prime Minister's Future Scientist Prize, [release](https://pmscienceprizes.org.nz/2019-future-scientist-media-release/)): raises the front of an unmodified wheelie bin and wheels it to the kerb. Navigation errors sometimes sent bins "into the garden or onto the road". **This is the closest precedent to the team's concept, and it is also high-school work.**
- **Products:**
  - Rezzi SmartCan ([Smithsonian, 2019](https://www.smithsonianmag.com/innovation/robotic-trash-can-takes-itself-curb-180973346/)) is a pair of retrofit wheels with a docking station. No evidence was found that it ever shipped, and it cannot return if workers misplace the can ([Interesting Engineering](https://interestingengineering.com/smartcan-new-automated-trash-can-drive-itself-to-the-curb-on-trash-day)).
  - Yarbo has announced a bin-to-curb module ([Pulse 2.0, 2025](https://pulse2.com/yarbo-over-27-million-series-b-raised-for-scaling-intelligent-yard-robot-technology)) but has published no details.
  - The cheapest verified commercial aid is the passive **Garbage Commander handle hook, $64.99** ([Gempler's](https://gemplers.com/products/single-can-garbage-can-hauling-hook-for-lawn-tractor-or-atv)). It is made for 64/96-gal carts with 9-10" handle inside widths, puts about 30% of the cart's weight on the hook, and is towed by a human-driven tractor or ATV.
- **Industry:**
  - Volvo ROAR ([2015](https://www.volvogroup.com/en/news-and-media/news/2015/sep/news-150979.html), [2016](https://www.volvogroup.com/en/news-and-media/news/2016/feb/drone-to-help-refuse-collecting-robot-find-refuse-bins.html)) fetched unmodified bins using GPS, LiDAR, cameras, an IMU, odometry and a drone. It published no cost or accuracy figures.
  - Truck-side cart recognition (CartSeeker, [Government Fleet 2021](https://www.government-fleet.com/10144799/mcneilus-to-debut-zero-radius-automated-side-loader)) claims a 96% success rate.
  - Con-Tech's truck grabber uses one sonar to make a repeatable 1-inch final approach ([US10358287](https://patents.google.com/patent/US10358287)).
- **Patents that limit novelty:**
  - [US20200023524A1](https://patents.google.com/patent/US20200023524A1) (abandoned) describes exactly an autonomous, camera-guided robot that hooks the handle of an unmodified two-wheeled cart, tilts it and drags it to the curb.
  - [US10046910B2](https://patents.google.com/patent/US10046910) (active to about 2036) covers a remote-controlled tug, built from hobby electronics, that latches the handle.
  - Other active patents cover integrated robotic bins ([US11884485B1](https://patents.google.com/patent/US11884485), [US11970334B1](https://patents.google.com/patent/US11970334)) and ramped carriers ([US10857925B1](https://patents.google.com/patent/US10857925)).
- **Bottom line:** the concept is not new. The contribution has to be *measurement* of cost against reliability, accuracy and force on real unmodified carts.

### (b) Hitching and docking with unmodified carts

- **Industrial towing of "unmodified" carts works by clamping an existing rigid steel bar on a four-wheel indoor cart:**
  - MiR's hook ([US10668617B2](https://patents.google.com/patent/US10668617); [ISR 2018](https://www.vde-verlag.de/proceedings-en/454699033.html), snippet-only).
  - The MiR250 Hook product grips a bar 80-350 mm off the floor and identifies carts with QR codes or AprilTags ([The Robot Report](https://www.therobotreport.com/mir-launches-mir250-hook-for-autonomous-cart-towing/)). It is about $42,000 per a third-party listing (low confidence, [robotomated](https://robotomated.com/explore/warehouse/mir-250-hook)).
  - MiR's newer gripper self-aligns with a passive pivot and two contact switches ([US12403591B2](https://patents.google.com/patent/US12403591B2/en)).
- **Correction to the project brief:** [US11919155B2](https://patents.google.com/patent/US11919155B2/en) (Tractonomy) requires a coupling structure fixed to the cart (frame hitch, gripping bars and a light reflector), so it is *not* a precedent for unmodified carts. Aethon ([US12515342B2](https://patents.google.com/patent/US12515342B2/en)) and Omron ([US10168711](https://patents.google.com/patent/US10168711)) also retrofit the cart.
- **Research docking is indoors and sensor-heavy:**
  - Airport trolley collection ([Xiao et al., ICRA 2022](https://arxiv.org/abs/2110.06648)) uses a 3D LiDAR, two 2D LiDARs, a solid-state LiDAR and an RGB-D camera. It reaches 0.17 m / 0.11 rad at long range (camera) and 0.03 m / 0.02 rad at close range (LiDAR).
  - Bed docking ([Lei et al. 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11408198/)) uses two single-point laser rangefinders for the last 10 cm and reaches under 5 mm and 0.5 degrees, but relies on QR markers.
  - Hospital trolley towing grips "nonmodified standard trolleys" ([ROBOT 2019](https://bibliotecadigital.unipb.pt/entities/publication/245a287e-f661-4a11-9d32-67469e9549f5)), and a wheelchair-towing robot docks at the front caster ([arXiv 2305.13902](https://arxiv.org/abs/2305.13902)).
- **Refuse carts already have standard machine interfaces.** ANSI Z245.60 Type B carts have an upper saddle and a lower lift bar, and Type G carts are gripped by the body ([ANSI webstore](https://webstore.ansi.org/standards/eia/ansiz245602018), snippet-only). Spec sheets give the key numbers:
  - 64-gal: 28 lb empty, 224 lb rated load, 5/8" x 20" axle.
  - 96-gal: 37.25 lb empty, 336 lb rated load, 0.844" x 23" axle.
  - Wheels are 10" on both sizes.
  - Sources: [Cascade 64](https://www.hampton-pa.gov/DocumentCenter/View/4017), [Cascade 96](https://www.hampton-pa.gov/DocumentCenter/View/4016), [Toter](https://www.toter.com/sites/default/files/2021-05/Two-Wheel_CART_SPECIFICATIONS_092018_DIGITAL.pdf).
- **Forces:**
  - Human hand forces on refuse bins over asphalt with gradients and obstacles ranged from 32 to 357 N ([IFA 4161](https://www.dguv.de/ifa/forschung/projektverzeichnis/ifa_4161-2.jsp)).
  - Waste-collector studies used 25 and 50 kg two-wheeled containers ([Schibye et al. 2001](https://doi.org/10.1016/s0268-0033(01)00039-0)).
  - Sweep 2's quasi-static *Estimate* is that crossing a 1/2-inch lip (the ADA bevel limit, [access-board.gov](https://www.access-board.gov/ada/)) takes roughly 5-25x the steady rolling force.
- **No paper or patent found reports a capture envelope, an engagement success rate, or a measured hitch force for a robot on a refuse cart.**

### (c) Driveway and curb localization

- **No published study covers the garage-to-curb driveway itself.**
- **Low-cost RTK (u-blox ZED-F9P, about $260 per board) is cm-level under open sky but fragile near buildings:**
  - With a patch antenna in an urban canyon it got a fix in only 4 of 8 series ([Janos & Kuras 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8401267/)).
  - Near building facades it produced silent "false fixes" of about 2 m and took 9-13 s to recover ([Tavasci et al. 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11435761/)).
  - On a moving ground robot in open space the RMSE was 0.073 m at 1.10 m/s ([Blesing et al. 2023](https://arxiv.org/abs/2306.12826)).
  - With geodetic antennas on a car it reached 14.1 mm RMSE and a 95% fix rate ([Sanna et al. 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9002666/)).
  - In survey conditions, hardware under €250 reached better than 5 cm ([Wielgocka et al. 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8001986)).
- **Cheap-camera visual SLAM fails in the dark.** In the ROVER garden benchmark, DROID-SLAM's trajectory error grew from 0.32 m by day to 5.62 m at night ([ROVER](https://arxiv.org/abs/2412.02506)). In DIDLM, ORB-SLAM3 failed completely at night ([DIDLM](https://arxiv.org/abs/2404.09622)). Bins often go out at dusk or before dawn (*Inference*).
- **Teach-and-repeat suits a fixed weekly route:**
  - Monocular visual teach-and-repeat with cm-level path following ([Clement et al.](https://arxiv.org/abs/1707.08989)).
  - BearNav, which needs only one uncalibrated camera plus odometry and comes with a convergence proof ([Krajnik et al.](https://arxiv.org/abs/1711.05348)).
  - Bio-inspired teach-and-repeat for low-cost robots with poor odometry ([Dall'Osto et al.](https://arxiv.org/abs/2010.11326)).
  - None of these was tested on a robot towing a heavy cart.
- **Simple methods can win:**
  - A one-year forest study found that complex SLAM gave "limited accuracy gains over a proprioceptive baseline while significantly increasing system fragility" ([Boxan et al. 2026](https://arxiv.org/abs/2608.27628)).
  - Wheel odometry is "viable and cost-effective" for simple tasks ([Rezende et al. 2024](https://sol.sbc.org.br/index.php/sbrlars/article/view/34065)).
  - Printed AprilTags give about 1 cm head-on at 30-70 cm, but about 16 cm at an oblique yaw ([Abbas et al. 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6960891/)).
- **Consumer yard robots publish no accuracy data:** the Navimow i105N (RTK plus vision, $1,000, [Yahoo Tech](https://tech.yahoo.com/home/articles/segway-navimow-i105n-review-cost-220012288.html)), Husqvarna EPOS (2-3 cm claimed, [press release](https://www.husqvarnagroup.com/en/press/husqvarna-expands-innovation-leadership-virtual-boundary-technology-professional-robotic)), and the vision-only [WORX Landroid Vision](https://au.worx.com/landroid/landroid-vision/).

### (d) Curb detection

- **Cheapest data point:** 3-4 side-facing ultrasonic sensors at $15 each gave 12-13.5 cm RMSE and 92-96% availability, but on a car driving parallel to the curb ([Rhee & Seo 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6470551/)).
- **Robot-scale:** a RealSense D455 on a wheelchair found the curb from 14 of 15 start positions, with 0.09 +/- 0.10 m distance error and 1.5 +/- 4.4 degree alignment error. It was tested only on an indoor mock curb ([Sivakanthan et al. 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8659845/)).
- **Monocular camera:**
  - Geometric fisheye detection from a car reached over 90% mean distance accuracy ([Panev et al.](https://arxiv.org/abs/2002.12492)).
  - Learned monocular 3D occupancy on Coco sidewalk robots reached a curb IoU of only 14.59 ([WalkOCC 2026](https://arxiv.org/abs/2606.19122)).
  - YOLOv8-seg curb detection runs on an embedded computer for pedestrians ([Ruan et al.](https://arxiv.org/abs/2408.14578)).
- **Radar and LiDAR:**
  - A single-chip TI AWR1843 radar segmented curb and driveway scenes, but results are qualitative only ([Southcott et al.](https://par.nsf.gov/servlets/purl/10493760)).
  - 4D radar reached 0.023 m median error on road boundaries ([4DRadarRBD](https://arxiv.org/abs/2503.01930)).
  - Car LiDAR exceeded 0.95 precision, recall and F1 at a 0.15 m tolerance ([CurbNet](https://arxiv.org/abs/2403.16794)).
  - Ultrasonics fused with LiDAR and camera ([CurbScan](https://arxiv.org/abs/2010.04837)).
- **Nothing found tests head-on curb approach from a 20-40 cm high robot outdoors, at night, or across sensor price points.**

### (e) Low-cost outdoor robots

- **Drive train:**
  - Hoverboard hub motors can run open FOC firmware with a torque mode and current readout ([EFeru firmware](https://github.com/EFeru/hoverboard-firmware-hack-FOC)).
  - ROMR, a peer-reviewed hoverboard-motor base, "costs less than $1500" and claims a 90 kg payload, but was tested only indoors ([HardwareX 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10197097)).
  - Cornell Tech's hoverboard base moved a trash bin on a dolly under teleoperation ([lab page](https://irl.tech.cornell.edu/mobile_hoverboard_robot_base); [IEEE Spectrum](https://spectrum.ieee.org/nyc-trash-robots)).
- **Price points:**
  - OpenBot: a $50 body, not counting the phone (ICRA 2021, [arXiv](https://arxiv.org/abs/2008.10631)).
  - EarthRover: $149-$399 ([New Atlas](https://newatlas.com/robotics/earthrover-mini-4g-rover/)).
  - MuSHR: $600-$900 ([arXiv](https://arxiv.org/abs/1908.08031)).
  - Omobot: $693, with an itemized, date-stamped BOM, accepted at **IEEE AIM 2024** ([arXiv](https://arxiv.org/abs/2408.05315)).
  - OpenMower: about €700 plus a donor mower ([GitHub](https://github.com/ClemensElflein/OpenMower)).
  - JPL Open Source Rover: about $1,600 ([GitHub](https://github.com/nasa-jpl/open-source-rover)).
  - An RTK field robot at $2,900.22, about 62% of which is the RTK pair ([Baltazar et al. 2024](https://mdpi-res.com/d_attachment/agriengineering/agriengineering-06-00192/article_deploy/agriengineering-06-00192.pdf)).
  - Commercial research UGVs: AgileX Scout Mini from $4,500 ([RobotLAB](https://www.robotlab.com/store/agilex-scout-mini/)), Clearpath Jackal $15-20k and Husky $19-24k (unofficial third-party listings).
- **None of these platforms tows a cart, and none reports traction, slope or energy data under a towed load.**

### (f) Cost-vs-performance ablations

- **The method exists only at car or research scale:**
  - Collin & Terán Espinoza define a cost-normalized localization objective, J = log det(Λ)/Cost, and plot a Pareto front on KITTI. A sensor suite of about $27,000 reached about 99% of the best performance ([Collin & Terán Espinoza 2019](https://arxiv.org/abs/1907.08541)).
  - NSGA-II sensor co-design with monetary cost as an objective, for a Jackal ([Putnam, MIT 2025](https://dspace.mit.edu/entities/publication/14e39e72-b071-4fa9-8f0c-c539c4119fce)).
  - Boxi discusses cost only qualitatively ([RSS 2025](https://roboticsproceedings.org/rss21/p134.html)).
- **Single-comparison papers:**
  - UWB nodes ($30 each) plus a short-range lidar ($930) gave 85.5% less mapping error than GMapping with the same short-range lidar. The paper sets their ~$1,080 total against a ~$2,600 long-range lidar ([Liu et al.](https://arxiv.org/abs/2106.03648)).
  - RFID, keypoint, UWB and reflector localization were compared on accuracy, power, coverage and cost for airport trolleys ([Sun et al., Robotica 2025](https://arxiv.org/abs/2303.06551)).
- **Cost-reporting norms:**
  - Pearce's savings formula is S = (P - O)/P. He found 87% average savings, and only 37.8% of open-hardware papers named a proprietary equivalent ([Pearce 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7480774/)).
  - HardwareX provides a BOM template ([Zenodo](https://zenodo.org/record/5078227)).
- **Compute:**
  - YOLO26n takes 67 ms on a CPU-only Raspberry Pi 5 (NCNN) against 4.57 ms on a $249 Jetson Orin Nano Super (TensorRT FP16). Sources: [Ultralytics Pi](https://docs.ultralytics.com/guides/raspberry-pi/), [Ultralytics Jetson](https://docs.ultralytics.com/guides/nvidia-jetson/), [NVIDIA](https://developer.nvidia.com/blog/nvidia-jetson-orin-nano-developer-kit-gets-a-super-boost/).
  - SMF-VO visual odometry runs at over 100 FPS on a Pi 5 CPU ([arXiv](https://arxiv.org/abs/2511.09072)).
- **Missing:** a hobby-scale Pareto front (about $0-$300 of sensors) measured on real task success.

### Cross-sweep consistency notes

- **US11919155:** sweep 1 left the retrofit question UNVERIFIED. Sweep 2 read the claims and confirmed that a cart-mounted coupling structure with a reflector is required. Use sweep 2's reading.
- **Cart specs:** sweeps 2 and 3 list cart wheel size and mass as coverage holes, but sweep 1 has them:
  - 10" wheels on Toter and Cascade carts, plus a 12" blow-molded option on the Cascade 96-gal.
  - Empty weights of 28 / 37.25 lb and load ratings of 224 / 335-336 lb.
  - *Inference:* 10" wheels have a 0.127 m radius, which is inside the 0.10-0.15 m range sweep 2 assumed for its lip-crossing estimate. 12" wheels (0.152 m) sit at the top of that range.
- **SPARC:** sweep 1 gives a cost (~$809, from the SD1 document), while sweep 2 found no total in the conference paper alone. The sweeps also spell one author's surname differently ("Schmitz" in sweep 1, "Schmitt" in sweep 2). This is not resolved here; check the SD1 document before citing.
- **Con-Tech:** sweep 1 cites US10974895B2 and sweep 3 cites US10358287B2. They have the same assignee, the same inventors and the same 2016-06-22 priority date, so they are likely one patent family (*Inference*).

## Cost landscape

All prices are as reported by the linked source. "Third-party" means the figure is not from the manufacturer. Rows are grouped by category and sorted roughly by price within each group.

**Bin-to-curb builds and aids**

| Approach/system | What it does | Cost/price | Source link |
|---|---|---|---|
| Garbage Commander UBL-MT handle hook | Passive hitch. The 64/96-gal cart rolls on its own wheels behind a human-driven tractor or ATV | $64.99 (ball/bolt mount); $94.99 receiver version (search snippet only) | [Gempler's](https://gemplers.com/products/single-can-garbage-can-hauling-hook-for-lawn-tractor-or-atv) |
| Wentworth autonomous garbage removal (ASEE, 2009) | 3/8-scale barrel carrier; RF navigation failed outdoors | $385.00 estimated, $386.52 actual | [ASEE PDF](https://peer.asee.org/autonomous-garbage-removal-system.pdf) |
| GRAD (UCF, 2020) | Motors under a modified 32-gal can; IR tape-line following | $307 + $200 unplanned = $507 estimated (target below $600) | [D&C doc](https://ece.ucf.edu/seniordesign/su2020fa2020/g16/documents/divide_conquer.pdf) |
| SPARC (UCF, 2018) | Crawler carrying a strapped-on bin; GPS, camera and colored curb stake | ~$809 estimated; ~$795.12 prototype parts (including a $60 can); sponsor maximum $2,000 | [SD1 doc](https://ece.ucf.edu/seniordesign/sp2018su2018/g12/files/SeniorDesign1FinalDoc.docx) |
| FAMU-FSU Robotic Trash Cart (2019) | Teleoperated platform that carries both bins | $1,980.85 BOM including tax | [BOM .xlsx](https://eng-web1.eng.famu.fsu.edu/me/senior_design/2019/team311/docs/bill_of_materials.xlsx) |

**Consumer outdoor robots**

| Approach/system | What it does | Cost/price | Source link |
|---|---|---|---|
| Kiwibot | Semi-autonomous sidewalk delivery robot with remote operators | Operator labor $2/hr; unit cost UNVERIFIED | [The Hustle](https://thehustle.co/kiwibots-autonomous-food-delivery) |
| OpenBot (ICRA 2021) | Robot body that uses a smartphone for sensing and compute | $50 body (phone excluded) | [arXiv 2008.10631](https://arxiv.org/abs/2008.10631) |
| FrodoBots EarthRover Mini / Mini+ / Zero | Teleoperated sidewalk rovers with cameras and GPS | $149/$249; $199/$299; $299/$399 (preorder/retail) | [New Atlas](https://newatlas.com/robotics/earthrover-mini-4g-rover/) |
| OpenMower | Open-source RTK retrofit for a cheap robotic mower | ~€700, excluding donor mower and RTK base | [GitHub](https://github.com/ClemensElflein/OpenMower) |
| Segway Navimow i105N | Wire-free mower with RTK plus vision | $1,000 (review); $799 on Amazon at one point (Nov 2024) | [Yahoo Tech](https://tech.yahoo.com/home/articles/segway-navimow-i105n-review-cost-220012288.html); [Slickdeals](https://slickdeals.net/f/17910381-segway-navimow-i105n-robot-lawn-mower-perimeter-wire-free-1-8-acre-rtk-vision-robotic-lawnmower-ai-assisted-mapping-virtual-boundary-app-control-58db-a-quiet-amazon-799) |
| Mammotion Yuka mini Vision / Yuka Mini 2025 | Vision-only mower (no wire, no RTK) | €1,199 (search snippet); $1,097 (Yuka Mini 2025) | [Notebookcheck](https://www.notebookcheck.net/Mammotion-Yuka-mini-Vision-robot-lawn-mower-now-available.1074026.0.html); [Freshly Charged](https://freshlycharged.com/reviews/363/2025-mammotion-yuka-mini-review) |
| WORX Landroid Vision | Camera-only wire-free mower | AUD $1,999 (L1300 on sale, from $2,499); AUD $1,499 (M600) (search snippet) | [WORX AU](https://au.worx.com/landroid/landroid-vision/) |
| Mammotion LUBA 2 AWD | AWD mower with RTK plus vision | $2,099 / $2,499 / $2,899 (1000/3000/5000) | [TechRadar](https://www.techradar.com/home/small-appliances/mammotion-luba-2-awd-robot-lawn-mower-review) |

**Research, open-source and industrial platforms**

| Approach/system | What it does | Cost/price | Source link |
|---|---|---|---|
| Ultra-low-cost wall-climbing robot (2026) | ESP32-CAM, 3D-printed chassis, crack detection | ~$25 total | [arXiv 2609.26130](https://arxiv.org/abs/2609.26130) |
| MuSHR | 1/10-scale open-source racecar | $600 basic; ~$900 with laser scanner and RGBD (vs. MIT racecar ~$1,000 / ~$2,800) | [arXiv 1908.08031](https://arxiv.org/abs/1908.08031) |
| Omobot (IEEE AIM 2024) | Indoor mecanum robot with Jetson Nano and LD19 lidar | $693 total (Jetson Nano + camera $300, LD19 $99) | [arXiv 2408.05315](https://arxiv.org/abs/2408.05315) |
| ROMR (HardwareX 2023) | ROS base on hoverboard BLDC motors, 90 kg payload claim, indoor tests only | "less than $1500" | [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10197097) |
| NASA-JPL Open Source Rover | 6-wheel rocker-bogie rover | ~$1,600 (vs. ~$3,000 original version) | [GitHub](https://github.com/nasa-jpl/open-source-rover); [Hackaday.io](https://hackaday.io/project/192609-nasa-jpl-open-source-rover-off-the-shelf-edition) |
| Milo robotic guide dog | Modified Unitree Go2, indoor/outdoor | ~$2k (vs. ~$50k for a trained guide dog) | [arXiv 2607.19530](https://arxiv.org/abs/2607.19530) |
| Baltazar et al. agricultural robot | RTK field robot; 0.103-0.217 m cross-track RMSE | $2,900.22 total; EMLID RTK pair $1,794 (~62%) | [AgriEngineering PDF](https://mdpi-res.com/d_attachment/agriengineering/agriengineering-06-00192/article_deploy/agriengineering-06-00192.pdf) |
| AgileX Scout Mini | 4WD outdoor research UGV, 10 kg payload | from $4,500 | [RobotLAB](https://www.robotlab.com/store/agilex-scout-mini/) |
| Clearpath Jackal | Outdoor research UGV, 20 kg payload | $15,000-20,000 (third-party, unofficial); "high four figures to low five figures" (2014) | [moonlakeai](https://moonlakeai.com/robots/clearpath-jackal); [IEEE Spectrum](https://spectrum.ieee.org/clearpath-hits-husky-with-shrink-ray-announces-jackal-ugv) |
| Clearpath Husky | Rugged outdoor UGV, 100 kg payload | $19,000-24,000 (third-party, unofficial) | [moonlakeai](https://www.moonlakeai.com/robots/clearpath-husky) |
| MiR250 Hook | Indoor AMR that tows existing four-wheel carts by a bottom bar; QR/AprilTag cart ID | $42,000 (third-party, "Not manufacturer-provided"; low confidence) | [robotomated](https://robotomated.com/explore/warehouse/mir-250-hook) |

**Sensors, compute and cost-analysis reference points**

| Approach/system | What it does | Cost/price | Source link |
|---|---|---|---|
| Side-facing ultrasonic curb sensors (Rhee & Seo) | 3-4 sensors; 12-13.5 cm curb RMSE on a car | $15 each (~$45-60 per set) | [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6470551/) |
| LD19 dToF 2D lidar | 0.3-12 m range, +/-45 mm accuracy, 30 klux ambient-light rating | $95.99 (Waveshare, now marked discontinued); $99 (Omobot BOM) | [Waveshare](https://www.waveshare.com/product/dtof-lidar-ld19.htm) |
| RPLidar A2 / Scanse Sweep (2017) | Hobby 2D lidars; ~4-5 m range in sunlight | $379-450 / $350 | [DIYRobocars](https://www.diyrobocars.com/2017/05/28/comparing-low-cost-2d-scanning-lidars/) |
| ArduSimple simpleRTK2B Budget | ZED-F9P RTK board | €172 each | [ArduSimple](https://www.ardusimple.com/product/simplertk2b/) |
| ZED-F9P + ANN-MB-00 patch antenna (Wielgocka et al.) | Better than 5 cm horizontal RTK in survey conditions | under €250 hardware | [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8001986) |
| SparkFun GPS-RTK2 (ZED-F9P) | RTK board; 10 mm accuracy claimed under open sky | $259.95 | [SparkFun](https://www.sparkfun.com/sparkfun-gps-rtk2-board-zed-f9p-qwiic-gps-15136.html) |
| ArduSimple simpleRTK2B Basic Starter Kit | ZED-F9P board plus ANN-MB antenna | €211 / $263.75 | [ArduSimple](https://www.ardusimple.com/product/simplertk2b-basic-starter-kit-ip65/) |
| Jetson Orin Nano Super dev kit | 67 sparse TOPS; YOLO26n in 4.57 ms (TensorRT FP16) | $249 (cut from $499) | [NVIDIA blog](https://developer.nvidia.com/blog/nvidia-jetson-orin-nano-developer-kit-gets-a-super-boost/) |
| Raspberry Pi 5 (16GB) | CPU only; YOLO26n in 67 ms (NCNN) | $305 (the only price shown on 2026-10-03) | [Raspberry Pi](https://www.raspberrypi.com/products/raspberry-pi-5/) |
| Short-range 2D lidar + UWB (Liu et al.) | Hokuyo URG-04LX plus UWB nodes, 85.5% less mapping error | ~$930 lidar + ~$30 per UWB node, ~$1,080 total (vs. ~$2,600 long-range lidar) | [arXiv 2106.03648](https://arxiv.org/abs/2106.03648) |
| Automotive LiDAR (as cited by Southcott et al.) | High-end curb and road sensing | ~$25,000 entry-level to ~$100,000 high-end | [NSF PAR](https://par.nsf.gov/servlets/purl/10493760) |
| Car-scale sensor suites (Collin & Terán Espinoza) | Pareto front of localization quality against cost on KITTI | ~$27,000 reaches ~99% of the best; $110,000 budget | [arXiv 1907.08541](https://arxiv.org/abs/1907.08541) |

**What the table shows (summary, partly *Inference*):**
- Documented bin-to-curb BOMs run from about $387 (a scale model) to $1,981, and none was measured against performance.
- A complete consumer outdoor robot with RTK and/or vision sells for about $800-$2,900, and research UGVs cost $4,500-$24k.
- A cheap RTK pair (2 x €172-€264) is a large share of any sub-$500 BOM, as it was (62%) in the Baltazar robot.
- The commercial reference points a "cheaper" claim must beat are the $64.99 passive hook (cheap but human-driven), the ~$800-$1,100 consumer RTK and vision mowers, and student BOMs of $507-$1,981.

## Gap map

### What has not been measured or done

**(a) Bin-to-curb systems**
- No bin-to-curb robot found reports trial counts, success rate, curb placement error, time or energy:
  - SPARC's paper has no results ([SPARC](https://www.ece.ucf.edu/seniordesign/sp2018su2018/g12)).
  - GRAD only claims its objectives were satisfied ([GRAD](https://www.ece.ucf.edu/seniordesign/su2020fa2020/g16)).
  - FSU's robot is teleoperated ([FSU](https://eng-web1.eng.famu.fsu.edu/me/senior_design/2019/team311/)).
  - Wentworth's navigation failed ([Wentworth](https://peer.asee.org/autonomous-garbage-removal-system.pdf)).
  - Wheelie Drive, WALLEE, CSUF and SmartCan publish no metrics.
- No documented BOM has been tied to measured performance. The cheapest commercial aid, the $64.99 passive hook ([Gempler's](https://gemplers.com/products/single-can-garbage-can-hauling-hook-for-lawn-tractor-or-atv)), has no autonomy and no engagement-reliability data.
- The return trip after collection is unaddressed:
  - Workers leave the cart displaced or rotated, which strands SmartCan ([Interesting Engineering](https://interestingengineering.com/smartcan-new-automated-trash-can-drive-itself-to-the-curb-on-trash-day)).
  - FSU's charter simply assumes workers reload the robot.
  - Re-detection and re-hitch success against the post-pickup cart pose has never been measured.
- The curb-placement accuracy target is undefined. CartSeeker claims 96% pickup success ([Government Fleet](https://www.government-fleet.com/10144799/mcneilus-to-debut-zero-radius-automated-side-loader)), and Con-Tech claims a 1-inch sonar approach ([US10358287](https://patents.google.com/patent/US10358287)). No source states how precisely a cart must be placed for an automated side-loader arm.

**(b) Hitching and docking**
- **Capture envelope.** No study gives success rate against lateral and angular docking offset for any passive or active hitch. MiR's self-aligning pivot ([US12403591B2](https://patents.google.com/patent/US12403591B2/en)) and Aethon's converging funnel ([US12515342B2](https://patents.google.com/patent/US12515342B2/en)) absorb error but quantify nothing.
- **Head-to-head hitch comparison.** No one has compared hitch strategies on the same task:
  - Handle latch ([US10046910B2](https://patents.google.com/patent/US10046910)).
  - Hook-lift-tilt ([US20200023524A1](https://patents.google.com/patent/US20200023524A1)).
  - Carry platform ([US10857925B1](https://patents.google.com/patent/US10857925)).
  - Strap-on (SPARC).
  - Axle or wheel coupling ([arXiv 2305.13902](https://arxiv.org/abs/2305.13902)).
- **ANSI interfaces unused.** No robot work uses the standard ANSI Type B saddle or lift bar as a hitch point ([ANSI](https://webstore.ansi.org/standards/eia/ansiz245602018); [Cascade 96](https://www.hampton-pa.gov/DocumentCenter/View/4016)), and no hitch has been tested across brands (Toter, Cascade, Rehrig) and both sizes.
- **Truly unmodified carts.** Industrial "unmodified" towing still uses tags or a steel crossbar ([The Robot Report](https://www.therobotreport.com/mir-launches-mir250-hook-for-autonomous-cart-towing/); [US11919155B2](https://patents.google.com/patent/US11919155B2/en)). No study meets a strict "zero added hardware, zero tags" standard on refuse carts.
- **Robot-side force data.** There is none for tilt-and-tow:
  - Human-only data exist ([IFA 4161](https://www.dguv.de/ifa/forschung/projektverzeichnis/ifa_4161-2.jsp): 32-357 N; [Schibye 2001](https://doi.org/10.1016/s0268-0033(01)00039-0): 25/50 kg).
  - Nobody has measured hitch force, traction or weight transfer for a small robot.
  - Lip and crack crossing (ADA 1/4" and 1/2" thresholds, [access-board.gov](https://www.access-board.gov/ada/)) is probably the motor-sizing bottleneck and has not been measured.
- **Outdoors.** Nearly all docking work is indoors ([Xiao et al.](https://arxiv.org/abs/2110.06648); [Lei et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC11408198/); [ROBOT 2019](https://bibliotecadigital.unipb.pt/entities/publication/245a287e-f661-4a11-9d32-67469e9549f5)).

**(c) Driveway localization**
- No measured comparison exists along a real driveway (inside the garage, garage mouth, under eaves, open driveway, curb). The obvious candidates are RTK, AprilTag plus wheel odometry, and teach-and-repeat. Prior RTK results come from static points ([Janos & Kuras](https://pmc.ncbi.nlm.nih.gov/articles/PMC8401267/)), drones ([Tavasci](https://pmc.ncbi.nlm.nih.gov/articles/PMC11435761/)), open motion-capture areas ([Blesing](https://arxiv.org/abs/2306.12826)) or cars ([Sanna](https://pmc.ncbi.nlm.nih.gov/articles/PMC9002666/)).
- RTK fix rate and false-fix rate at a garage mouth have not been measured. *Inference:* a garage mouth is a partial urban canyon.
- The effect of a towed load on odometry and teach-and-repeat accuracy is unstudied. No teach-and-repeat paper tested a robot towing a heavy cart ([Krajnik](https://arxiv.org/abs/1711.05348); [Dall'Osto](https://arxiv.org/abs/2010.11326); [Clement](https://arxiv.org/abs/1707.08989)).
- No one has run a proprioceptive-plus-one-cheap-fix ablation (wheel+IMU; +AprilTag; +RTK; +VIO) on a 10-40 m route, although [Boxan et al. 2026](https://arxiv.org/abs/2608.27628) and [Rezende et al.](https://sol.sbc.org.br/index.php/sbrlars/article/view/34065) suggest it may suffice.
- Cheap-camera night and dawn robustness on a residential route is unmeasured, even though visual SLAM is known to fail in the dark ([ROVER](https://arxiv.org/abs/2412.02506); [DIDLM](https://arxiv.org/abs/2404.09622)).
- Map staleness on a weekly route has not been studied at a single house, only in snow and forest settings ([Boxan et al. 2025](https://arxiv.org/abs/2505.01339)). *Inference:* a California winter probably changes less.

**(d) Curb and bin detection**
- No same-curb, same-robot comparison of ultrasonic, camera, cheap lidar and single-chip radar exists. It would ideally run from a 20-40 cm high robot approaching head-on, in day, dusk and night, with sensor price on the x-axis. Existing numbers come from different platforms ([Rhee & Seo](https://pmc.ncbi.nlm.nih.gov/articles/PMC6470551/); [Sivakanthan](https://pmc.ncbi.nlm.nih.gov/articles/PMC8659845/); [Panev](https://arxiv.org/abs/2002.12492); [WalkOCC](https://arxiv.org/abs/2606.19122); [Southcott](https://par.nsf.gov/servlets/purl/10493760)).
- The LD06/LD19 class of dToF hobby lidar has no peer-reviewed evaluation in sunlight. Older evidence shows that cheap lidar range shrinks in sun ([MDPI 2023](https://www.mdpi.com/2673-4591/32/1/16); [DIYRobocars](https://www.diyrobocars.com/2017/05/28/comparing-low-cost-2d-scanning-lidars/)).
- There is no public dataset of US 64/96-gal carts seen from a low robot viewpoint with yaw or keypoint labels. Existing sets are truck-view and partly European ([StreetView-Waste](https://arxiv.org/abs/2511.16440); [Agnew et al.](https://doi.org/10.1016/j.iswa.2023.200229)).

**(e) Low-cost platforms**
- Hoverboard hub-motor drives have no published towing data: pull force, slip, slope limit or Wh per trip ([EFeru firmware](https://github.com/EFeru/hoverboard-firmware-hack-FOC); [ROMR](https://pmc.ncbi.nlm.nih.gov/articles/PMC10197097), indoor only; [Cornell](https://irl.tech.cornell.edu/mobile_hoverboard_robot_base), teleoperated with the bin on a dolly).

**(f) Cost-vs-performance**
- There is no hobby-scale Pareto front built from task trials. Existing fronts are at car scale on datasets ([Collin & Terán Espinoza](https://arxiv.org/abs/1907.08541)) or use design-space proxies ([Putnam](https://dspace.mit.edu/entities/publication/14e39e72-b071-4fa9-8f0c-c539c4119fce)).
- Low-cost robot papers argue cost from a price list, not a measured trade-off ([MuSHR](https://arxiv.org/abs/1908.08031); [OpenBot](https://arxiv.org/abs/2008.10631); [Omobot](https://arxiv.org/abs/2408.05315); [ROMR](https://pmc.ncbi.nlm.nih.gov/articles/PMC10197097)).
- Only 37.8% of open-hardware papers name a proprietary equivalent ([Pearce 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7480774/)).
- Compute benchmarks use datasets, not tasks ([Ultralytics](https://docs.ultralytics.com/guides/raspberry-pi/); [Alqahtani et al.](https://arxiv.org/abs/2409.16808)). A slow bin robot may not need high frame rates, which is untested.

### Most promising openings for a cheap, measurement-driven high-school paper (flagged)

Ranking is *Inference*, based on cost, the Dec-Feb build window, two builders, and how cleanly each result can be measured. Phase 2/3 reviewers should re-check novelty with IEEE Xplore and Google Scholar, which the sweeps did not search.

1. **[FLAG] Hitch capture envelope and strategy comparison on unmodified carts.**
   - *Method:* measure engagement success against lateral offset, yaw offset, cart brand and size (64/96) and fill mass, for 2-3 hitch types such as a handle hook-lift and a lift-bar or axle hook, with and without a passive funnel.
   - *Cost:* hobby actuators, a few carts and a tape measure.
   - *Beyond:* MiR, Aethon and Tractonomy (indoor, tags or retrofits, no capture data), US20200023524A1 and US10046910 (no data), and Wheelie Drive (no metrics).
   - *Fit:* plays to the mechanical student's strengths.
2. **[FLAG] Localization cost ladder along a real driveway.**
   - *Method:* run wheel odometry + IMU only, then add a printed AprilTag, then a ~$260 ZED-F9P RTK, then a single-camera teach-and-repeat. Score each on curb placement error, success rate, and RTK fix and false-fix rate by driveway zone, with tape or chalk-grid ground truth. Report cost per centimeter or "successful round trips per $100".
   - *Beyond:* Janos & Kuras, Tavasci, Blesing and Sanna (none is a driveway), and Boxan 2026 (forest).
   - *Fit:* the software student.
3. **[FLAG] Towing characterization of a cheap drive train.**
   - *Method:* put a load cell on the hitch and log hoverboard FOC torque-mode current. Report pull force, slip and success against fill mass (empty to 224/336 lb rated loads), driveway grade, and lip height (ADA 1/4", 1/2", plus real lips measured at local driveways), along with Wh per trip.
   - *Beyond:* IFA and Schibye (human-only data) and ROMR (indoor only).
   - *Cost:* a used hoverboard plus a load cell and amplifier (prices UNVERIFIED in the sweeps).
4. **Curb-detection cost curve at robot height in day, dusk and night.**
   - *Method:* compare $15 ultrasonics, a monocular camera, a ~$96 LD19 and a depth or ToF sensor on the same residential curbs.
   - *Beyond:* Rhee & Seo (car, parallel to curb) and Sivakanthan (indoor mock curb).
   - *Risk:* outdoor ground truth and the number of curbs available.
5. **Return-trip re-acquisition.**
   - *Method:* measure re-detection and re-hitch success against how far workers displaced or rotated the cart.
   - *Status:* novel (SmartCan's known failure), but it depends on openings 1 and 2 working first, so it is better as one experiment inside a larger paper.

**Unifying frame:** openings 1-3 (and 4) can share one paper, "cost vs. measured performance for an unmodified-cart bin robot". The paper would include a HardwareX-style BOM with purchase dates, named commercial comparators ($64.99 hook, ~$1,000 Navimow, $1,981 FSU BOM, ~$42k MiR250 Hook as a third-party figure), and a cost-normalized metric in the spirit of Collin & Terán Espinoza.

### Novelty claims to avoid (already contradicted by cited prior art)

- **"First robot that takes bins to the curb."** Contradicted by the 1991/1994 patents, SPARC, GRAD, FSU, Wentworth, WALLEE, CSUF and ROAR.
- **"First robot for unmodified bins" or "first hook-the-handle bin robot."** Contradicted by Wheelie Drive (a high-school build) and US20200023524A1, and in remote-controlled form by US10046910B2.
- **"First low-cost bin robot."** Contradicted by GRAD ($507) and Wentworth ($386.52).
- **"First robot to tow unmodified carts."** Contradicted by MiR (US10668617B2, ISR 2018) and the ROBOT 2019 hospital trolley tug, though those are indoor and use steel crossbars or plates.
- **Defensible claims** are "first *measured*..." claims, for example: first measured capture envelope, first driveway localization ablation with costs, or first robot-side towing-force data on ANSI carts.

## Closest prior work checklist for novelty claims

| # | Entry | Why it matters for a novelty claim | Link |
|---|---|---|---|
| 1 | Wheelie Drive (Thomas James, NZ high school, 2019) | High-school robot lifts an unmodified two-wheeled bin and wheels it to the kerb; no paper or metrics; navigation was its weak point | [PM Science Prizes](https://pmscienceprizes.org.nz/2019-future-scientist-media-release/) |
| 2 | US20200023524A1, Trash and recycle bin relocation robot (abandoned) | Exact concept: camera-guided robot hooks the handle of an unmodified cart, tilts and drags it; no prototype data | [Google Patents](https://patents.google.com/patent/US20200023524A1) |
| 3 | US10046910B2, Semi-autonomous tug apparatus (active to ~2036) | Handle-latching tug from hobby electronics, remote-controlled; constrains a commercial handle-tug design | [Google Patents](https://patents.google.com/patent/US10046910) |
| 4 | SPARC (UCF 2018) | Autonomous bin carrier using GPS plus a curb stake; ~$809; no quantitative results | [UCF](https://www.ece.ucf.edu/seniordesign/sp2018su2018/g12) |
| 5 | GRAD (UCF 2020) | Modified 32-gal bin on a tape line; $507; no trial data | [UCF](https://www.ece.ucf.edu/seniordesign/su2020fa2020/g16) |
| 6 | FAMU-FSU Robotic Trash Cart (2019) | Teleoperated two-bin carrier; $1,980.85 BOM; 250 lb up 5 degrees | [FAMU-FSU](https://eng-web1.eng.famu.fsu.edu/me/senior_design/2019/team311/) |
| 7 | Wentworth Autonomous Garbage Removal System (ASEE, 2009) | Earliest academic build; cheap RF localization failed outdoors; $386.52 | [ASEE PDF](https://peer.asee.org/autonomous-garbage-removal-system.pdf) |
| 8 | WALLEE (FAU 2022) | Only student build targeting the 96-gal size; designed for the truck dropping the bin back | [FAU](https://www.fau.edu/engineering/senior-design/projects/spring2022/wallee-self-driving-garbage-can) |
| 9 | Rezzi SmartCan | Best-known commercial attempt; retrofit wheels; known return-trip failure | [Smithsonian](https://www.smithsonianmag.com/innovation/robotic-trash-can-takes-itself-curb-180973346/) |
| 10 | Garbage Commander UBL-MT hook | $64.99 passive handle hitch for 64/96-gal carts: the cost floor and hitch geometry reference | [Gempler's](https://gemplers.com/products/single-can-garbage-can-hauling-hook-for-lawn-tractor-or-atv) |
| 11 | Volvo ROAR | Robot that handles unmodified bins with GPS, LiDAR, cameras, IMU and a drone; the expensive-stack contrast | [Volvo 2015](https://www.volvogroup.com/en/news-and-media/news/2015/sep/news-150979.html) |
| 12 | Cornell Tech hoverboard base / Trashbot | Hoverboard drive moving a trash bin (on a dolly, teleoperated); reviewers may raise it | [Cornell IRL](https://irl.tech.cornell.edu/mobile_hoverboard_robot_base) |
| 13 | MiR existing-cart grippers (patent, ISR 2018 paper, self-aligning pivot patent) | "Transport existing carts without a docking mechanism"; passive self-alignment with contact switches; indoor steel crossbars | [US10668617B2](https://patents.google.com/patent/US10668617); [ISR 2018](https://www.vde-verlag.de/proceedings-en/454699033.html); [US12403591B2](https://patents.google.com/patent/US12403591B2/en) |
| 14 | US11919155B2 (Tractonomy) | Cited in the brief, but needs a coupling structure and reflector on the cart; use it to sharpen the definition of "unmodified" | [Google Patents](https://patents.google.com/patent/US11919155B2/en) |
| 15 | Xiao et al., Robotic Autonomous Trolley Collection (ICRA 2022) | Docking-accuracy baseline (0.17 m / 0.03 m) using five range or vision sensors | [arXiv 2110.06648](https://arxiv.org/abs/2110.06648) |
| 16 | Sun et al., indoor localization methods for trolley collection (Robotica 2025) | Published template comparing localization methods on accuracy and cost | [arXiv 2303.06551](https://arxiv.org/abs/2303.06551) |
| 17 | Lei et al., wheelchair/bed docking (2024) | Coarse-to-fine docking with two single-point rangefinders; under 5 mm, but uses QR markers | [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11408198/) |
| 18 | Rhee & Seo, low-cost ultrasonic curb detection (2019) | $15 sensors, 12-13.5 cm RMSE; car parallel to the curb | [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6470551/) |
| 19 | Sivakanthan et al., curb recognition for robotic wheelchairs (2021) | Robot-scale curb approach, 0.09 m error; indoor mock curb, D455 camera | [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8659845/) |
| 20 | Low-cost ZED-F9P RTK evidence: Janos & Kuras 2021; Tavasci et al. 2024; Blesing et al. 2023 | Fix loss and false fixes near buildings; 0.073 m dynamic RMSE in open space; none on a driveway | [PMC8401267](https://pmc.ncbi.nlm.nih.gov/articles/PMC8401267/); [PMC11435761](https://pmc.ncbi.nlm.nih.gov/articles/PMC11435761/); [arXiv 2306.12826](https://arxiv.org/abs/2306.12826) |
| 21 | Low-cost teach-and-repeat: Krajnik et al. (BearNav, IROS 2018); Dall'Osto et al. (IROS 2021) | One cheap camera plus poor odometry on a fixed route; no towed load tested | [arXiv 1711.05348](https://arxiv.org/abs/1711.05348); [arXiv 2010.11326](https://arxiv.org/abs/2010.11326) |
| 22 | ROMR (HardwareX 2023) | Hoverboard-motor base under $1,500, 90 kg payload claim; indoor only; BOM template | [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10197097) |
| 23 | Collin & Terán Espinoza, sensor tradespace (2019) | Cost-normalized metric and Pareto front at car scale; the method to copy at hobby scale | [arXiv 1907.08541](https://arxiv.org/abs/1907.08541) |
| 24 | IFA 4161, push/pull forces on refuse bins (2011) | Human-only force data (32-357 N) on outdoor asphalt; the method to replicate robot-side | [DGUV IFA](https://www.dguv.de/ifa/forschung/projektverzeichnis/ifa_4161-2.jsp) |
| 25 | Bin detection datasets: StreetView-Waste (WACV 2026); Agnew et al. 2023 | Container detection from a truck viewpoint (European classes, proprietary side-loader data); no low-viewpoint pose labels | [arXiv 2511.16440](https://arxiv.org/abs/2511.16440); [doi](https://doi.org/10.1016/j.iswa.2023.200229) |

## Detailed prior art

The four link-verified sweep files follow, appended verbatim in order: (1) bin robots and products, (2) cart docking and hitching, (3) localization and curb detection, (4) low-cost platforms and cost ablations.

## Prior Art Sweep 1: Bin-Moving Robots, Products, Patents and Cart Standards

Scope: this sweep covers robots and devices that move residential wheeled refuse carts between a home and the curb: university senior-design projects, student and hobby builds, commercial products, industrial/research programs (Volvo ROAR, automated refuse-truck arms), US patents, and the cart standards and spec sheets that set the geometry and loads a hitch for an unmodified 64/96-gal cart has to handle. Every link below was opened with WebFetch, or its claim was confirmed by a search-result snippet (marked as such), on 2026-10-03. Statements marked **Estimate** or **Inference** are the author's own reasoning and do not come from a source.

---

### A. The three known senior-design bin-to-curb robots (verified)

#### [SPARC: Self-Powered Autonomous Refuse Cart (UCF ECE Senior Design, Spring/Summer 2018, Group 12)](https://www.ece.ucf.edu/seniordesign/sp2018su2018/g12)
- Type: student project
- Who / when: A. Drayton, S. McGarvey, W. Schmitz, C. Vento; University of Central Florida, 2018. Sponsored by Selah Group Florida. Documents: [conference paper (.docx)](https://ece.ucf.edu/seniordesign/sp2018su2018/g12/files/Group%2012%20Conference%20Paper.docx), [SD1 final document (.docx)](https://ece.ucf.edu/seniordesign/sp2018su2018/g12/files/SeniorDesign1FinalDoc.docx).
- What it does / claims: A tracked/4-wheel "crawler" (2 driven wheels plus 2 casters on an aluminum box chassis) that **carries** the bin on top. Per the paper, the bin is "firmly attached to the SPARC unit, primarily via a clamp to the wheel axle of the garbage can in the rear, and grips in the front corners", with tension straps over two bars. Sensors: Pixy CMUcam5 color camera, Sharp IR rangefinder (GP2Y0A710K0F), GPS for the curb and home waypoints, a **colored stake** that marks the curb spot for final visual alignment, and RF links to a contact-charging "Home Base". Path planning is a node graph with reflexive/greedy re-weighting. Electronics: Arduino Zero MCU, 4S8P 18650 pack (14.8 V, 20 Ah). The design load is 50 lb, and the motors were sized to "pull 45 Pounds" plus the chassis.
- Cost or price info (with source): The SD1 doc's Table 15 estimates "~$809" total, the prototype parts list totals "~$795.12" (including a $60 32-gal can), and the sponsor's maximum budget was $2,000.
- Relevance: This is the closest US precedent with a full design document. It shows a carry-on-platform architecture and GPS-plus-landmark curb localization.
- Gap: The conference paper reports **no quantitative results** (no success rate or placement error). The design payload of 50 lb is far below the cart load ratings of 224/335 lb (see Section F). The motors have no encoders ("The motors have no digital or analog output"), so the robot has no odometry. The bin must be strapped onto the robot.

#### [GRAD: Garbage & Recycle Automated Disposal (UCF ECE Senior Design, Summer/Fall 2020, Group 16)](https://www.ece.ucf.edu/seniordesign/su2020fa2020/g16)
- Type: student project
- Who / when: A. Khan, H. Nassereddeen, S. Bhuria, S. Quinlan; UCF, Fall 2020. Documents: [conference paper (PDF)](https://ece.ucf.edu/seniordesign/su2020fa2020/g16/documents/conference_paper.pdf), [divide-and-conquer doc (PDF)](https://ece.ucf.edu/seniordesign/su2020fa2020/g16/documents/divide_conquer.pdf).
- What it does / claims: **Modifies the bin itself.** Two gear motors are mounted on a metal frame under a 32-gal Toter can, reusing the can's own two wheels as a 3-wheel differential drive with a front swivel wheel. Navigation is **IR line following of tape laid from garage to curb**. An HC-SR04 ultrasonic sensor stops the robot within 1 ft of an obstacle. Other hardware: Arduino Mega 2560, ESP8266 Wi-Fi with a Firebase Android app ("Drive to Curb"/"Return Home" buttons), and a 30 W solar panel. The motor sizing assumed about 79 lb on a 10% grade, giving about 30.6 N of grade resistance. Targets: end within 1 ft of the goal, and start moving within 2 min of a command.
- Cost or price info: The D&C doc estimates "$307.00 + $200 (unplanned fees) = $507.00", with a stated target of "below $600" and a total device weight target under 70 lb.
- Relevance: This is a cheap-infrastructure baseline (a tape line). It shows the "modify the bin" approach that our project wants to avoid.
- Gap: The bin is modified, and it is 32-gal rather than 64/96. The robot needs a tape path. The paper claims objectives "were satisfied" but gives no trial counts or error data, and the testing it describes is mostly app/database unit testing.

#### [Robotic Trash Cart (FAMU-FSU College of Engineering Senior Design, 2018-19, Team 311)](https://eng-web1.eng.famu.fsu.edu/me/senior_design/2019/team311/)
- Type: student project
- Who / when: O. Flores, J. Emerson, J. Williams, B. Morkos. FAMU-FSU (the "FSU 2019" project). Documents: [abstract](https://eng-web1.eng.famu.fsu.edu/me/senior_design/2019/team311/docs/abstract.pdf), [project charter](https://eng-web1.eng.famu.fsu.edu/me/senior_design/2019/team311/docs/project_charter.pdf), [bill of materials (.xlsx)](https://eng-web1.eng.famu.fsu.edu/me/senior_design/2019/team311/docs/bill_of_materials.xlsx), [operation manual](https://eng-web1.eng.famu.fsu.edu/me/senior_design/2019/team311/docs/operation_manual.pdf).
- What it does / claims: A 2x6 ft aluminum frame with a fiberglass-grating floor that **carries both bins**. A gate lets waste workers reach the bins. Two wheelchair motors sit mid-frame with two casters, allowing zero-point turns. Per the abstract it was "designed... to carry a 250 pound load up a 5-degree incline", with 5 degrees chosen from the ADA ramp limit. The final prototype is **teleoperated with a Bluetooth (BLE) joystick** according to the abstract and operation manual. Autonomy appears only as future work on the spring poster. The charter assumes the "Waste Engineer will return the bins into the RTC".
- Cost or price info: The BOM total is **$1,980.85** including tax: frame $938.41, drive $299, power $301.59, control $66.77, wheels $120.50.
- Relevance: This is the expensive end of the carry-platform design space. Its BOM is a citable cost baseline.
- Gap: The robot is not autonomous and has a large footprint. It depends on waste workers putting the bins back into the cart, and it reports no field-trial data.

---

### B. Other academic and student bin-to-curb projects

#### [Autonomous Garbage Removal System (ASEE paper, Wentworth Institute of Technology)](https://peer.asee.org/autonomous-garbage-removal-system.pdf)
- Type: paper (ASEE PEER; student design-course paper)
- Who / when: D. Brosnan, D. Hawes, M. Nielsen, S. Badjou. Junior-level Electromechanical Design course, Spring 2009. The exact conference could not be confirmed because the landing page returned 403.
- What it does / claims: A 3/8-scale motorized cart that carries barrels. It uses a BASIC Stamp 2, a Parallax PING ultrasonic sensor, Sharp GP2D12 IR sensors, and a bumper switch. Curb and house navigation was meant to use RF direction finding with a Handi-Finder antenna pair and transmitters at the curb and the house. Push-buttons under the barrels detect when the barrels are emptied/removed, which triggers the return trip.
- Cost or price info: Estimated $385.00, actual $386.52 (paper).
- Relevance: This is the earliest academic bin-to-curb robot found. It documents a **failed** low-cost localization method: outdoors the RF readings were "very sporadic and seemed random", and the stopping system was "not completed".
- Gap: It is a scale model with no successful full navigation. The paper cites a 2008 "trashrobot.com" product and US patents 5,042,642 and 5,353,887 (verified below). trashrobot.com itself is **UNVERIFIED**.

#### [WALLEE: Self-Driving Garbage Can (FAU Senior Design, Spring 2022)](https://www.fau.edu/engineering/senior-design/projects/spring2022/wallee-self-driving-garbage-can)
- Type: student project
- Who / when: Six ocean/mechanical engineering students at Florida Atlantic University, 2022.
- What it does / claims: A 96-gal can sits inside a metal chassis, and "ratchet straps attach the front and back bars on the trash can to the chassis." It has two front drive wheels and **spring-loaded swivel rear wheels to absorb impact when the garbage truck deposits the container**. It runs by remote control or a preprogrammed path.
- Cost or price info: none published on the page.
- Relevance: This is the only student project found that explicitly targets the 96-gal size and designs for the truck dropping the bin back onto the robot.
- Gap: The sensors are not disclosed, and the page gives no cost and no performance data. The robot carries the bin rather than hitching to it.

#### [Self-Driving Trash Bin (Cal State Fullerton CompE capstone, June 2017)](https://news.fullerton.edu/?p=5190)
- Type: student project
- Who / when: K. Nguyen, D. Martinez, E. Soto; advisor Kiran George; CSUF, 2017. This is a California precedent.
- What it does / claims: A motorized bin (the bin itself is the robot) controlled from an Android app. It "can detect obstacles in its path, as well as when the trash has been removed from the bin." The team noted it is "not fully weather proof."
- Cost or price info: none.
- Relevance: This is a California university precedent, which may be useful when pitching to CA labs.
- Gap: It replaces the bin rather than using an unmodified municipal cart. No sensor, localization or metric details are published.

#### [Wheelie Drive (Thomas James, Burnside High School, NZ; 2019 Prime Minister's Future Scientist Prize)](https://pmscienceprizes.org.nz/2019-future-scientist-media-release/)
- Type: student project (high school)
- Who / when: Thomas James, Year 13 student, Christchurch, NZ. He won the $50,000 Future Scientist Prize in 2019. An earlier [1News report (Nov 2018)](https://www.1news.co.nz/2018/11/01/meet-the-15-year-old-kiwi-inventor-of-the-bin-bot-a-robot-which-wheels-out-bins) covers him at age 15 (video only).
- What it does / claims: The robot "raises the front of a wheelie bin off the ground, wheels it to the kerb" and returns it. He first attached to the rear of the bin, then pivoted to a front-mounted design **to avoid altering the standard council bin**. Development went through computer modeling, then Lego prototypes, then a full-size robot over "over two years". The release reports navigation errors "sometimes sending the wheelie bin into the garden or onto the road". A search-result snippet says it senses its surroundings with "a distance sensor and compass". This is **not confirmed on the fetched page**.
- Cost or price info: "limited budget"; no figure.
- Relevance: **This is a direct precedent: a high-school-built robot that moves an unmodified two-wheeled bin to the curb.** A reviewer could cite it against a novelty claim of "first low-cost robot for unmodified bins".
- Gap: There is no paper, no published metrics, no cost breakdown and no localization comparison. Navigation reliability was explicitly its weak point.

#### [BinBot collaboration/ideas (HSBNE hackerspace forum, Dec 2015)](https://forum.hsbne.org/t/binbot-collaboration-ideas/1340)
- Type: other (hobbyist concept discussion)
- Who / when: Brisbane hackerspace members, Dec 2015.
- What it does / claims: A concept for relocating 35+35 bins in a villa compound. Options discussed were a custom electric frame, a forklift with mecanum wheels, and a skid-steer with a lift. Contributors suggested ArduRover GPS autonomy and said 1-3 cm (RTK/DGPS) accuracy, embedded ground markers or painted lines would be needed.
- Cost or price info: none.
- Relevance: Practitioners judged that consumer GPS alone is insufficient for bin placement, which supports a localization cost-vs-accuracy study.
- Gap: It is a concept only, with no evidence it was built.

---

### C. Commercial products and startups

#### [SmartCan by Rezzi (Smithsonian Magazine, Oct 15 2019)](https://www.smithsonianmag.com/innovation/robotic-trash-can-takes-itself-curb-180973346/)
- Type: product (pre-launch)
- Who / when: Rezzi (Massachusetts); inventor Andrew Murray; 2019. Also covered by [Interesting Engineering (Oct 1 2019)](https://interestingengineering.com/smartcan-new-automated-trash-can-drive-itself-to-the-curb-on-trash-day).
- What it does / claims: Per Smithsonian, "SmartCan is essentially a pair of robotic wheels that are compatible with any municipal-issued trash receptacle", meaning the bin's wheels and base are modified or retrofitted rather than the bin being towed. It is scheduled from an app. The original design used two docking stations (home and curb). The curb station was later dropped "to accommodate local laws and pedestrian safety", and SmartCan "now operates by the user 'teaching' it by taking it out once from its original docking station to the curb." Interesting Engineering pointed out a flaw: if workers don't put the can back precisely at the dock, "the trash can won't be able to wheel itself back."
- Cost or price info: Price was undisclosed in 2019, with release expected by the end of 2020. **No evidence found that it shipped, and no retail price was found.** Current status is UNVERIFIED.
- Relevance: This is the best-known commercial attempt. It shows the business case and the "return trip after workers move the bin" failure mode.
- Gap: It requires a retrofit kit on each bin, and it has no published performance or cost data.

#### [Yarbo modular yard robot: announced bin-to-curb module (Pulse 2.0, Apr 18 2025)](https://pulse2.com/yarbo-over-27-million-series-b-raised-for-scaling-intelligent-yard-robot-technology)
- Type: product (announced future module)
- Who / when: Yarbo, Series B news, April 2025.
- What it does / claims: Future modules include "moving your garbage bins to the curb, dog waste picking, and even fruit harvesting".
- Cost or price info: Not stated in the article. Core robot pricing is UNVERIFIED here.
- Relevance: A well-funded consumer outdoor-robot company sees bin moving as a market, which supports the paper's motivation.
- Gap: There is no published mechanism, hitch design or availability, and a multi-thousand-dollar yard platform (price **UNVERIFIED**) is the opposite of a low-cost dedicated device.

#### [Garbage Commander UBL-MT single-can hauling hook (Gempler's listing)](https://gemplers.com/products/single-can-garbage-can-hauling-hook-for-lawn-tractor-or-atv)
- Type: product (passive towing hitch)
- Who / when: Garbage Commander; current listing.
- What it does / claims: The cart's handle rests in a "patented mountain hook channel" and is pinned with a PTO clip. **The cart stays on its own wheels** while towed behind a lawn tractor/ATV/golf cart. The hook "raises operating height by 8" and extends it out an additional 8"". It fits handles with "9" to 10" inside widths". "Operating weight on hook is 75 lbs." About 30% of the can's weight rests on the support arm. It is designed for 64- and 96-gal carts.
- Cost or price info: **$64.99** for the ball/bolt mount (listing). A receiver-mounted version at $94.99 appears in a search-result snippet only.
- Relevance: **This is the strongest evidence that a cheap passive handle hitch works on unmodified 64/96-gal carts.** It provides real design numbers: handle width, lift height, and the fraction of the load on the hitch.
- Gap: It needs a human-driven vehicle. There is no autonomy, no alignment or docking, and no measured engagement reliability.

---

### D. Industrial / research programs and refuse-truck automation

#### [ROAR: Robot-based Autonomous Refuse handling (Volvo Group press release, Sep 2015)](https://www.volvogroup.com/en/news-and-media/news/2015/sep/news-150979.html)
- Type: other (industry-academic research program)
- Who / when: Volvo Group, Chalmers, Mälardalen University, Penn State, and Renova; 2015-2016. Follow-ups: [Volvo, Feb 2016 drone release](https://www.volvogroup.com/en/news-and-media/news/2016/feb/drone-to-help-refuse-collecting-robot-find-refuse-bins.html), [TechXplore, Feb 2016](https://techxplore.com/news/2016-02-refuse-collecting-robot-successfully.html).
- What it does / claims: A robot dispatched from a refuse truck fetches bins, brings them to the truck lift, and returns them, supervised by the driver. A roof-mounted drone finds the bins. The robot localizes with **GPS, LiDAR, cameras, IMU and odometry against a pre-loaded neighborhood map**. A camera with human detection pauses emptying if a person comes too close. The prototype was built in four months. Mälardalen built the robot, Chalmers did task management, and Penn State built the driver 3D interface.
- Cost or price info: not disclosed.
- Relevance: This is the most-cited "robot handles unmodified wheeled bins" program. It shows the expensive sensor stack that a low-cost study can ablate against.
- Gap: It published no cost, success-rate or placement-accuracy figures (in these sources). The hardware is research-grade and expensive, and the bin-gripping mechanism is not described in the releases.

#### [CartSeeker cart-recognition for McNeilus side loaders (Recycling Product News, Aug 2021)](https://www.recyclingproductnews.com/article/37059/big-truck-rental-purchases-mcneilus-zero-radius-side-loader-with-cart-recognition-technology)
- Type: product (refuse-truck automation)
- Who / when: Eagle Vision Systems with McNeilus; 2021.
- What it does / claims: AI-based recognition "identifies and locates curbside waste carts" and fully automates the truck's lift arm with no joystick.
- Cost or price info: none.
- Relevance: Commercial vision already detects and grabs unmodified carts at the curb. **Inference:** carts are visually consistent enough for learned detectors.
- Gap: It runs on truck-scale hardware, publishes no accuracy numbers, and isn't usable by a homeowner robot.

#### [US10974895B2: Automated container handling system for refuse collection vehicles (Google Patents)](https://patents.google.com/patent/US10974895)
- Type: patent
- Who / when: Con-Tech Manufacturing; inventors G. McNeilus, J. Cunningham, B. Meldahl; priority 2016-06-22; granted 2021-04-13; active.
- What it does / claims: A vehicle camera feeds a cab monitor. Sonar on the grabber base lets it "approach as close as one inch" repeatably. A **converging grabber with opposed fingers** seizes the cart body, and one button runs the cycle under a PLC.
- Cost or price info: n/a.
- Relevance: A cheap ultrasonic sensor is enough for the final approach to a standard cart in an industrial product. This is a useful low-cost analog for robot-to-cart docking.
- Gap: It is truck-mounted and grips the cart body to dump it, not to tow it.

#### [US11208262B2: Refuse container engagement (The Heil Co.) (Google Patents)](https://patents.google.com/patent/US11208262)
- Type: patent
- Who / when: The Heil Co.; inventors D. Lewis, S. Maroney, C. Blanchard; priority 2019-04-23; granted 2021-12-28; active to about 2040.
- What it does / claims: Container sensors (ultrasonic, RADAR/LIDAR, optical) or camera images with ML detect the cart and estimate its **width**. The two gripper arms then automatically open to about 4 in wider than the detected width before closing.
- Cost or price info: n/a.
- Relevance: This shows that width estimation of an unmodified cart is the key parameter for engagement, and that the industry does it with cheap ranging sensors.
- Gap: It is truck-scale, with no consumer or tow use and no published accuracy.

---

### E. Patents on residential trash-cart conveyance (design constraints)

*None of this is legal advice. Patents do not prevent publishing a research paper, but they matter if the device is commercialized.*

#### [US10046910B2: Semi-autonomous tug apparatus (Google Patents)](https://patents.google.com/patent/US10046910)
- Type: patent
- Who / when: K. Wagner, B. Lew, T. Domingo; filed 2015-12-17; granted 2018-08-14; **active, expires about 2036-09-12**.
- What it does / claims: Claim 1 (sole independent claim) covers a tug "for latching to a handle on a front side of a bin supported on the opposite back side by support wheels". It has a housing with a rearward "toe" carrying a **castor wheel**, two independently driven wheels, a **swivel-mounted elongated lifting arm** reaching to handle height, and a latch device. Together these are configured so that, when latched, they "**hold the castor wheel elevated from the support surface**." In the spec it is remote-controlled over Bluetooth from an Android phone.
- Cost or price info: n/a.
- Relevance: **This is the most design-constraining active patent for a "hook the handle and tilt the cart" robot.** A tug whose castor lifts off the ground when it latches the handle, with a swivel arm, reads closely on claim 1.
- Gap: It is remote-controlled only, with no autonomy, localization or curb detection. Design-around ideas (**Inference**): keep a permanently grounded caster or a 4-wheel base, use a rigid hitch with no swivel arm, or engage the lower lift bar or axle instead of the handle.

#### [US20200023524A1: Trash and recycle bin relocation robot (Google Patents)](https://patents.google.com/patent/US20200023524A1)
- Type: patent (application)
- Who / when: Hesham Mohamed (individual); filed 2019-07-17; published 2020-01-23; **abandoned**.
- What it does / claims: A robot uses a rotating 360° camera with AI (OpenCV/TensorFlow) to find bins and tells bins apart by barcode label and color. A U-shaped hook on a linear-actuator arm extends "until it reaches the horizontal pipe" of the handle, lifts the bin slightly, and drags "the bins on their wheels" to the curb one at a time. It also has ultrasonic sensors.
- Cost or price info: n/a.
- Relevance: This is **prior art for the exact concept** of an autonomous robot hooking an unmodified two-wheeled cart's handle. Because it is abandoned there are no enforceable claims, but it defeats a "novel concept" claim.
- Gap: It is paper-only, with no prototype data, no cost and no metrics.

#### [US11884485B1: Autonomous refuse container (AI Inc) (Google Patents)](https://patents.google.com/patent/US11884485)
- Type: patent
- Who / when: Ali Ebrahimi Afrouzi / AI Inc; priority 2017-09-13; granted 2024-01-30; active. Continuation: [US12466641B2](https://patents.google.com/patent/US12466641), granted 2025-11-11, active to about 2038.
- What it does / claims: A robot chassis with an image sensor captures images, builds a map, plans a path, and receives from an app "a schedule for emptying refuse **stored in a container of the robot** at a refuse collection location" (day, time, frequency, dwell time). It then navigates there on schedule. US12466641 claim 1 is the method version with the same "container of the robot" language. The spec describes stereo cameras, depth sensors, corner ToF sensors and a modular container variant.
- Cost or price info: n/a.
- Relevance: These patents cover the integrated "robotic bin" plus app-scheduled mapping.
- Gap / constraint: **Inference:** a robot that tows a separate, unmodified municipal cart and holds no refuse "in a container of the robot" appears to fall outside the literal claim language. Confirm with counsel before commercializing.

#### [US11970334B1: Automated, self-moving trash or recycling bin (Google Patents)](https://patents.google.com/patent/US11970334)
- Type: patent
- Who / when: R. McLaughlin, J. Callet / Synchronous Technologies & Innovations; filed 2023-10-11; granted 2024-04-30; active to about 2043.
- What it does / claims: Claim 1 covers an autonomous bin with an integrated receptacle and lid, two driven wheels, a free support wheel with a **controller-adjusted leveling mechanism**, and a controller. The spec also describes a retrofit attachment that bolts to a standard bin's base, and lists GPS, axle odometry, inclinometer, weight, proximity and IR dock-alignment sensors.
- Cost or price info: n/a.
- Relevance: This is recent and active, and it covers the "self-moving bin" space.
- Gap: Whether any granted claim covers the retrofit attachment is **UNVERIFIED** (claim 1 does not). There are no performance data.

#### [US10857925B1: Battery operated autonomous robotic trash can carrier (Google Patents)](https://patents.google.com/patent/US10857925)
- Type: patent
- Who / when: T. Sahota; filed 2020-05-15; granted 2020-12-08; active to about 2040.
- What it does / claims: A frame with a **platform floor** that carries cans, loaded through electronically deployable side ramps. Sensors listed are sonar, LIDAR, cameras, GPS and weight sensors. It can run fully or partly autonomously, or by RF/phone remote.
- Cost or price info: n/a.
- Relevance: It covers the carry-on-platform-with-ramps architecture (similar to the FSU RTC and WALLEE).
- Gap: There is no hitching, no prototype data and no cost.

#### [US10576017B2: Automatic trash can delivery device (Google Patents)](https://patents.google.com/patent/US10576017)
- Type: patent
- Who / when: N. Soucy; filed 2018-10-08; granted 2020-03-03; **expired (fee-related)**.
- What it does / claims: A body with a holding aperture that the can sits inside. The device follows ground-mounted "sensor guides" along a fixed path, with optional GPS and app control.
- Cost or price info: n/a.
- Relevance: This is prior art for guide-line or infrastructure navigation (compare GRAD's tape line).
- Gap: It carries the bin rather than towing it, and needs ground infrastructure.

#### [US9085207B1: Tow hitch rigging arm (Google Patents)](https://patents.google.com/patent/US9085207)
- Type: patent
- Who / when: J. Sweet; filed 2013-12-11; granted 2015-07-21; **expired 2023 (fee-related)**.
- What it does / claims: A bar from a vehicle hitch ends in upturned U-shaped hooks that engage the refuse container's **handles**. The container rolls on its own wheels.
- Cost or price info: n/a.
- Relevance: The expired passive handle-hook geometry is free to use and is the same idea as the Garbage Commander product.
- Gap: It is passive and human-driven.

#### [US5042642A: Automatic trash cart (Google Patents)](https://patents.google.com/patent/US5042642) and [US5353887A: Household trash delivery system (Google Patents)](https://patents.google.com/patent/US5353887)
- Type: patent (two entries, both **expired**)
- Who / when: D. Ullrich, granted 1991-08-27; J. Putnam, granted 1994-10-11.
- What they do / claim: US5042642 uses a rail laid 40-80 ft from house to curb with a chain conveyor that drives a two-barrel cart, triggered by push-button or radio. US5353887 uses a track-guided cart with a single drive wheel, a programmable timer and pressure-sensitive bumpers.
- Cost or price info: n/a.
- Relevance: These show that the "scheduled bin-to-curb" problem is more than 30 years old. Novelty has to come from the method and the measurements, not the task.
- Gap: Both need fixed infrastructure and carry the bin.

#### [US20090008888A1: Garbage transport device (Google Patents)](https://patents.google.com/patent/US20090008888A1)
- Type: patent (application, **abandoned**)
- Who / when: J. Boulden; filed 2008-06-17.
- What it does / claims: A motorized platform with removable sides runs on fixed trolley-style tracks to the curb, operated with a garage-door-opener-style remote button.
- Cost or price info: n/a.
- Relevance: More infrastructure-based prior art.
- Gap: It needs tracks, the bin rides on a platform, and there is no autonomy.

#### [US11919155B2: AMR system for improved docking with a wheeled cart (Google Patents)](https://patents.google.com/patent/US11919155)
- Type: patent (cross-reference; industrial cart docking)
- Who / when: Tractonomy Robotics (inventors K. Chintamani, G. Dorme); priority 2020-09-01; granted 2024-03-05; active to about 2042.
- What it does / claims: An AMR aligns using a broadband emitter and narrowband reflection sensing on the cart's coupling structure. Two gripper hands latch onto "elongated gripping elements" (bars) on the cart, and a tapered guide with a 55-75° entry absorbs approach error. The design does not need cart brakes.
- Cost or price info: n/a.
- Relevance: This is the industrial analog of hitching to a bar. **Inference:** the ANSI Type B cart's **lower lift bar** (see Section F) is a standardized "elongated gripping element" already present on every Type B cart.
- Gap: It is industrial and expensive, and appears to rely on a cart coupling structure. Whether the cart needs a retrofit structure is **UNVERIFIED**.

---

### F. Standards and physical facts for designing a hitch for an unmodified cart

#### [ANSI Z245.60-2018: Waste Containers, Compatibility Requirements (ANSI Webstore)](https://webstore.ansi.org/standards/eia/ansiz245602018)
- Type: standard (paywalled)
- Who / when: Published by EIA/NWRA (ANSI Z245 committee); 2018 edition, superseding [Z245.60-2008](https://webstore.ansi.org/Standards/EIA/ANSIZ245602008).
- What it does / claims: According to the search-result snippets (the webstore returned 403 to WebFetch), the 2008 edition "establishes dimensional requirements for all waste containers commonly used in the collection, compaction and transportation of solid waste and recyclables". The 2018 edition "applies to newly manufactured containers". Manufacturer sheets use its designations: **Type B** carts suit semi-automated bar-locking lifters, which use the upper saddle plus the lower lift bar, and **Type G** carts suit fully automated grabber arms that grip the body (Rehrig sheets below, plus a Cascade/municipal spec in a search snippet). The companion performance standard sets the design load. Toter states standard carts are rated for "3-1/2 lbs./gallon" ([Toter sales sheet](https://www.toter.com/sites/default/files/2024-10/Waste__Recycling_Carts_Sales_Sheet_2024.pdf)), which gives 64 x 3.5 = 224 lb and 96 x 3.5 = 336 lb and matches the vendor ratings below.
- Cost or price info: The standard must be purchased. Price not captured.
- Relevance: **Every compliant Type B cart has the same lift interfaces (an upper saddle and a lower lift bar) at compatible heights.** A hitch designed to these interfaces should transfer across brands.
- Gap: The exact dimensions were not obtained because the standard is paywalled. Either buy the standard or measure 3+ carts from different brands. No robotics paper found uses these interfaces for towing.

#### [Toter Two-Wheel Cart Specifications (Toter / Wastequip, TOT047-092018)](https://www.toter.com/sites/default/files/2021-05/Two-Wheel_CART_SPECIFICATIONS_092018_DIGITAL.pdf)
- Type: standard (manufacturer spec sheet)
- Who / when: Toter (Wastequip), 2018. Also the [2024 sales sheet](https://www.toter.com/sites/default/files/2024-10/Waste__Recycling_Carts_Sales_Sheet_2024.pdf).
- What it does / claims: The **64-gal** EVR II measures 31-1/2 x 24-1/4 x 41-3/4 in (L x W x H), has a **224 lb** load rating and 10" wheels. The **96-gal** measures 35-1/2 x 29-3/4 x 43-1/4 in, has a **335 lb** load rating and 10" wheels. A footnote says smaller carts are "below Type B saddle height, which requires the collector to lift the cart approx. 3 inches for semi-automated lifters". The 2024 sheet lists the ANA96 at 35.75 x 29.75 x 43.25 in and 335 lb.
- Cost or price info: not listed. Empty weight is not on these sheets.
- Relevance: Use these figures for the robot's footprint, hitch height and worst-case payload.
- Gap: There is no handle or lift-bar geometry, and no empty weight.

#### [Cascade 96-Gallon Universal Cart, Sterling Series spec sheet (hosted by Hampton Township, PA)](https://www.hampton-pa.gov/DocumentCenter/View/4016)
- Type: standard (manufacturer spec sheet)
- Who / when: Cascade Cart Solutions, Rev. 11/18.
- What it does / claims: H 46" x W 23" x D 31.5". **Empty weight 37.25 lb, load rating 336 lb.** Wheels are 10" injection-molded or 12" blow-molded. The axle is HSLA steel, **0.844" diameter x 23" long**. Lift areas: "In-molded upper saddle lift area" and a "factory installed composite **lower lift bar**" with 360° rotation.
- Cost or price info: not listed.
- Relevance: These are concrete numbers for hitch design: axle and lift-bar engagement, and a gross worst-case mass of about 373 lb / 169 kg (**Estimate**: 37.25 + 336).
- Gap: Lift-bar height and handle geometry are not given.

#### [Cascade 64-Gallon Universal Cart, Sterling Series spec sheet (hosted by Hampton Township, PA)](https://www.hampton-pa.gov/DocumentCenter/View/4017)
- Type: standard (manufacturer spec sheet)
- Who / when: Cascade Cart Solutions, Rev. 11/18.
- What it does / claims: H 44" x W 22" x D 26.5". **Empty weight 28 lb, load rating 224 lb.** 10" wheels. Axle **5/8" diameter x 20" long**. It has the same upper saddle and lower lift bar.
- Cost or price info: not listed.
- Relevance: The worst-case gross mass is about 252 lb / 114 kg (**Estimate**: 28 + 224).
- Gap: As above.

#### [Rehrig Pacific 65-Gal EnviroCore Roll-Out Cart (product page)](https://www.rehrigpacific.com/waste-and-recycling/products/65-gallon-envirocore-roll-out-cart) and [95-Gal EnviroCore Roll-Out Cart (product page)](https://www.rehrigpacific.com/waste-and-recycling/products/95-gallon-envirocore-roll-out-cart)
- Type: standard (manufacturer spec)
- Who / when: Rehrig Pacific (Los Angeles, CA); current. The [roll-out cart brochure (PDF)](https://www.rehrigpacific.com/download_file/view/9ac6c305-ac12-456a-a576-3ba4a9145d12/901) has the same figures (this link now resolves to an EnviroGuard/EnviroCore summary sheet whose spec table lists the 35/65/95-gal dimensions and weights quoted below).
- What it does / claims: The 65-gal measures D 26.87-27.0" x W 26.5-26.78" x H 43.1-43.6" (varies by sheet/version) and weighs **29.75 lb** empty. The 95-gal measures W 29.2" x D 33.3" x H 43.5"; its weight is not listed ("--"). Both "Meet/Exceed all ANSI type B & G container standards". Features include a "Continuous one-piece handle", a "Textured body... for fully-automated collection", an optional embedded RFID tag, and the front lifting skirt "now internal".
- Cost or price info: not listed.
- Relevance: These give a third brand for cross-brand hitch tests. The cart's own RFID tag option is a possible cheap identification cue.
- Gap: The 95-gal empty weight and handle dimensions are missing.

#### [BS EN 840-1:2020: Mobile waste and recycling containers, Part 1: 2-wheeled containers up to 400 L for comb lifting devices (DIN Media)](https://dinmedia.de/en/standard/bs-en-840-1/324692893)
- Type: standard (paywalled)
- Who / when: CEN, published 2020-04-17. The 4-wheel counterpart is [SFS-EN 840-2:2020](https://store.sfs.fi/en/sfs-en-840-2-2020), covering containers up to 1,300 L for trunnion/comb lifters.
- What it does / claims: It specifies the dimensions and design of 2-wheeled containers "with a nominal volume up to 400 l for comb lifting devices". These are EU and UK wheelie bins (the bin type in ROAR and Wheelie Drive).
- Cost or price info: paywalled.
- Relevance: Citing both ANSI Z245.60 (US) and EN 840-1 (EU) lets a paper argue that a hitch works across standardized cart families. EU bins use a front "comb" bar for lifting, not the US saddle/lift-bar interface.
- Gap: The dimensions themselves were not obtained.

#### [StreetView-Waste: A Multi-Task Dataset for Urban Waste Management (arXiv 2511.16440, WACV 2026)](https://arxiv.org/abs/2511.16440)
- Type: dataset
- Who / when: D. Paulo, J. Martins, H. Proença, J. Neves; Nov 2025.
- What it does / claims: Street-level images, framed for garbage-truck monitoring, with tasks for **waste container detection**, tracking, and overflow segmentation. CC BY 4.0.
- Cost or price info: free.
- Relevance: Could be used to pretrain or evaluate a bin detector.
- Gap: The container types (EU vs. US carts) and the viewpoint (truck height vs. a robot at knee height) are not confirmed and may not match.

---

### Gaps and opportunities
- **No bin-to-curb robot found reports quantitative field results.** SPARC's paper has none. GRAD claims its objectives were "satisfied" without data. The FSU RTC is teleoperated. The Wentworth RF navigation failed outdoors. Wheelie Drive, WALLEE, CSUF and SmartCan publish no metrics. A study with N repeated garage-to-curb-and-back trials (success rate, curb placement error and heading, time, energy) would be the first measured benchmark.
- **The cost record is thin and points the wrong way.** The documented BOMs are about $387 (Wentworth, scale model), $507 (GRAD, modified bin plus tape line), about $809 (SPARC) and $1,981 (FSU RTC), and none was evaluated against performance. The cheapest verified commercial aid is a **$64.99 passive handle hitch** (Garbage Commander). A cost-vs-performance ablation (sensor sets, localization methods, hitch types) with measured outcomes fills a clear gap.
- **Architecture gap: towing an unmodified cart is under-documented.** Most builds carry the bin on a platform (SPARC, FSU, WALLEE, Wentworth; Sahota and Soucy patents) or modify or replace it (GRAD, CSUF, SmartCan; AI Inc and Synchronous patents). Hook-and-tilt designs exist only as a high-school prize project (Wheelie Drive), an abandoned patent (US20200023524), a remote-control tug patent (US10046910) and passive tractor hitches. None has published engagement-reliability data.
- **Standard cart interfaces are unexploited.** ANSI Type B carts have a standardized upper saddle and lower lift bar, and the spec sheets give axle sizes (5/8" x 20" on the 64-gal, 0.844" x 23" on the 96-gal) and handle widths (9-10" per the Garbage Commander listing). A hitch designed to these interfaces, and tested across three brands (Toter, Cascade, Rehrig) and both sizes for engagement success and misalignment tolerance, is novel and cheap to run. The tapered-entry idea in US11919155 is a model.
- **Realistic load testing is missing.** SPARC was designed for 50 lb against cart ratings of 224 lb (64-gal) and 335-336 lb (96-gal), set by ANSI's 3.5 lb/gal rule. A paper should report pull force, slip, and success at measured fill masses and driveway grades (GRAD assumed 10%, FSU 5°). With about 30% of cart weight on a handle hitch (Garbage Commander), a full 96-gal cart could put on the order of 100+ lb on the hitch (**Estimate**), which strongly shapes the drive design.
- **Low-cost localization for the curb is the documented failure point.** SPARC used GPS plus a colored stake, GRAD a tape line, and the Wentworth RF failed. HSBNE practitioners said 1-3 cm RTK would be needed, and ROAR used GPS+LiDAR+camera+IMU. A ladder of localization methods by cost (tape line, fiducial/AprilTag stake, consumer GPS, RTK GPS, camera curb detection), each scored on placement error, is a well-posed, measurable study.
- **The return trip is an open problem.** Workers leave the cart displaced or rotated (Interesting Engineering's critique of SmartCan; FSU's charter simply assumes workers reload the robot). Industry handles cart detection with cheap sensors: sonar on Con-Tech's grabber, ultrasonic/optical plus ML width estimation in Heil's patent, and CartSeeker vision. Measuring re-detection and re-hitch success against cart pose offset after pickup is a concrete, novel experiment.
- **The patent landscape suggests a design-around.** The active claims cover a caster-lifting swivel-arm handle tug (US10046910, to 2036), robots that hold refuse "in a container of the robot" (AI Inc), integrated bins with leveling (US11970334) and ramped platform carriers (US10857925). **Inference:** a robot that tows an unmodified cart through its lift bar or handle, keeps a grounded caster, and stores no refuse itself avoids their literal language. This is a point worth stating in the paper's related work, but it is not legal advice.
- **The novelty bar is real.** The concept itself is decades old (1991 and 1994 patents) and already built by a high schooler (Wheelie Drive, 2019) and in an abandoned patent. The paper's contribution must be **measurement**: cost-vs-performance and reliability across real carts, loads and driveways, not "a robot that takes out the trash".

### Searches run
WebSearch (standard mode) queries, in order:
1. `UCF senior design SPARC trash can robot curb 2018`
2. `UCF senior design GRAD garbage robot autonomous delivery 2020`
3. `FSU senior design 2019 autonomous trash can robot curb`
4. `Volvo ROAR robot refuse handling project`
5. `self-driving trash can SmartCan Rezzi takes itself to the curb price`
6. `robot that takes trash bins to the curb product autonomous garbage can mover`
7. `ANSI Z245.60 refuse cart compatibility dimensions standard`
8. `Toter 96 gallon cart specifications empty weight rated load capacity pdf`
9. `"bin relocation robot" OR "trash can to curb" patent autonomous robot hitch wheeled refuse container` (failed: tool classifier timeout; not rerun)
10. `EN 840 wheeled waste containers two wheels dimensions trunnion comb lifting standard` (failed; replaced by #23)
11. `wheelie bin robot takes bin to kerb autonomous student project`
12. `Cascade Engineering cart 96 gallon spec sheet empty weight lbs ANSI Z245.60`
13. `Rehrig Pacific 96 gallon roll out cart specifications empty weight`
14. `Cascade Cart Solutions 96 gallon two-wheel cart product weight load rating ANSI Type B`
15. `patent "trash and recycle bin relocation robot"` (first attempt cut off; rerun succeeded)
16. `patents.google.com autonomous robot moving waste container to curb engage wheeled trash cart` (cut off; not rerun)
17. `Rezzi SmartCan trash can robot launch 2023 2024 price preorder`
18. `motorized trash can mover device hitch tows garbage can to curb remote control product`
19. `ROAR robot refuse bin Chalmers Mälardalen Penn State thesis bin detection grasp`
20. `automated side loader arm grabber refuse cart vision automatic cart detection patent refuse vehicle`
21. `ANSI Z245.60 Type B Type G cart definition semi-automated lifter automated arm grip zone`
22. `"Z245.60" 2018 OR 2023 waste containers compatibility dimensions WASTEC current edition`
23. `EN 840 mobile waste containers wheelie bin standard parts 1 2 dimensions comb trunnion lifting device`
24. `Yarbo robot trash can module takes garbage bin to curb`
25. `trash can hauler hitch tow multiple garbage cans behind lawn tractor ATV product price`
26. `robot tows trash bins to curb startup 2024 2025 autonomous bin mover launch` (**not executed**: the session's shared web-search budget was exhausted)

arXiv API keyword queries (via WebFetch): `"wheelie bin" OR "refuse bin" OR "garbage bin" OR "trash bin" OR "refuse collection"` and `(refuse AND robot) OR "garbage truck" OR ("trash can" AND robot) OR ("waste container" AND robot)`. These found **no arXiv paper on robots that move residential bins**. The only relevant hit was the StreetView-Waste dataset.

Documents downloaded and read in full or in part: SPARC conference paper and SD1 doc; GRAD conference paper and D&C doc; FSU abstract, charter, BOM, poster, targets and operation manual; Wentworth ASEE PDF; Toter 2018 and 2024 sheets; Cascade 35/64/96-gal sheets; Rehrig 65-gal sheets and brochure.

**Coverage limits** (follow-up recommended): no searches were run of IEEE Xplore or Google Scholar keywords, YouTube/Kickstarter/Indiegogo bin-robot campaigns, non-English markets (Japan, Korea, China, Europe), commercial curbside "bin valet" services, or municipal cart-placement rules for automated trucks (spacing and orientation). The searches were cut short by the shared web-search budget.

### Removed during verification
- **RoboTrash Machine (NuVu Studio, Wayland; high-school studio)**, link https://wayland.nuvustudio.com/posts/175291-final-updates. Reason: on 2026-10-03 the URL returns a 302 redirect to the NuVu homepage (cambridge.nuvustudio.com), no Wayback Machine snapshot exists, and the only support for its description was a search-result snippet that could not be re-checked. The entry is unverifiable, so it was removed from Section B. The original claim (UNVERIFIED) was a remote-controlled robot that uses a stepper-raised hook to pull a trash can by its handle to the curb.

### Link verification (2026-10-03)
- **URLs checked: 52** (unique; each was fetched with curl and the page title or content was matched against its entry. All 14 Google Patents titles match the patent numbers and titles cited, and quoted spec figures were checked against the downloaded PDFs for Toter, Cascade, Rehrig, ASEE, GRAD and FSU).
- **OK: 50.** 48 returned HTTP 200 with matching content. TechXplore returned 403 to curl, but WebFetch confirmed the page ("Refuse-collecting robot successfully tested", Feb 26 2016, ROAR). ANSI Z245.60-2008 returned 403, but a Wayback Machine snapshot (2025-09-14) confirmed the quoted description ("Establishes dimensional requirements for all waste containers...").
- **Fixed: 2 (content corrections, no URL changes).** (1) The SmartCan quote "Motorized wheels attach to existing municipal trash receptacles" does not appear on the Smithsonian page and was replaced with the article's actual wording. (2) The Rehrig brochure link was annotated: it now resolves to a differently titled summary sheet, but that sheet has the same spec figures.
- **Removed: 1** (NuVu RoboTrash Machine: the link is dead and redirects to the homepage; see above).
- **Confirmed only via search snippet: 1.** ANSI Z245.60-2018 webstore page: 403 to both curl and WebFetch, and no archive snapshot exists. It rests on the original author's search snippet and could not be re-confirmed here because the web-search budget was exhausted. Separately, the Wheelie Drive "distance sensor and compass" detail was already labeled as snippet-only in the text.


---

## Prior art sweep #2: Docking with, hitching to, and transporting unmodified wheeled carts

Scope: how robots (industrial AMRs, research platforms, residential bin movers) find, couple to, and move wheeled carts they did not build. We also cover the physics of tilting and towing a two-wheeled refuse cart and the cheapest coupling methods that have been documented. Everything below is filtered through one question: what could a hobby-budget robot that moves an unmodified 64/96-gal municipal cart learn from this work, and where is the gap it could fill?

**Confidence legend.** "Verified" means the page was opened and the claim was read there. "Snippet" means only a search-result snippet confirmed the claim because the page blocked fetching. "UNVERIFIED" means not confirmed. Anything marked *Our estimate / derivation* is our own reasoning, not a citation.

**Headline correction to the project brief.** US11919155 (Tractonomy) is *not* a patent for docking with unmodified carts. Its claims require a **coupling structure (frame hitch + gripping elements + light reflector) fixed to the cart**. In that patent, "generic carts" means carts of different sizes and shapes. Several other "no modification needed" claims in industry also turn out to depend on fiducial tags or an existing rigid steel crossbar. Details are in the entries below.

---

### A. Patents: AMRs engaging existing carts (industrial)

#### [US11919155B2: Autonomous mobile robot system for improved docking with a wheeled cart](https://patents.google.com/patent/US11919155B2/en)
- Type: patent
- Who / when: Tractonomy Robotics BV (Ghent, Belgium). Inventors Keshav Chintamani and Geert Dorme. Filed 2021-08-26, granted 2024-03-05. Google Patents lists a 2025 reassignment to Keshav Chintamani. EP counterpart: EP3960691B1. (Verified)
- What it does / claims: The AMR has at least two robot arms, each with a gripper hand, that grip at least two "elongated gripping elements... disposed equidistant from a centre" on a **coupling structure on the cart**. That coupling structure includes "a reflector unit which is configured to selectively reflect light", which the AMR uses to estimate orientation. A docking controller tracks reference points and a rotation angle α and computes a "docking correction factor". The patent says the coupling structure "may be fixed to said cart by means of fasteners" or "provided during cart production". It argues the approach handles improperly parked or unbraked carts. Its background criticizes MiR's WO2016165721 hook because that hook needs a "perfectly horizontally-oriented bar". (Verified)
- Cost or price info: none.
- Relevance to our bin-to-curb robot: The closed-loop "docking correction factor" idea (track features, correct during approach) transfers directly. The patent also shows that even the state of the art for "generic" carts adds hardware to the cart.
- Gap: It requires a retrofit hitch plus a reflector. It is indoor-only, does not cover plastic refuse carts, and reports no cost or tolerance numbers. A tag-free, retrofit-free hitch on a refuse cart would be clearly distinct.

#### [US10668617B2: Robotic cart pulling vehicle for automated pulling of carts](https://patents.google.com/patent/US10668617)
- Type: patent (same family as WO2016165721A1 and EP3283308)
- Who / when: Mobile Industrial Robots A/S (MiR). Inventor Niels Jul Jacobsen. Filed 2016-04-11, granted 2020-06-02. (Verified)
- What it does / claims: "a hook element for gripping the cart frame... flexibly attached via a pivot point". The robot finds the cart with proximity sensors and reverses until its support brackets touch the cart frame. A linear actuator then closes the hook, clamping the existing frame between hook and brackets. No special cart hitch is needed, but the cart must have a rigid frame member. (Verified)
- Cost or price info: none in the patent. See MiR250 Hook in section C.
- Relevance: This is the canonical "clamp an existing bar with one linear actuator" design. On a refuse cart the candidate bars are the molded handle, the steel axle, and the front lift bar or lip.
- Gap: It is designed for four-wheel industrial carts with a steel crossbar on flat indoor floors, so there is no tilt phase and no outdoor terrain. It publishes no capture-tolerance data.

#### [US12403591B2: Gripping system for an autonomous guided vehicle](https://patents.google.com/patent/US12403591B2/en)
- Type: patent
- Who / when: Mobile Industrial Robots A/S. Inventors Lars Hjorth Hansen and Mikkel Steen Pedersen. Priority 2020-06-09, granted 2025-09-02. (Verified)
- What it does / claims: The end effector has a movable hook and two lateral brackets. Two sensor arms protrude from it, and when one arm contacts the cart first, the effector "pivot[s] around its pivot point" to self-align. Once both side sensors are pressed, the hook closes via a linear actuator. The patent says roughly the same pulling force transfers at different gripping heights. Alignment needs no markers, only contact sensors. (Verified)
- Cost or price info: none.
- Relevance: Passive compliance plus two contact switches is very cheap. It is a template for "mechanism instead of expensive perception" in the last few centimetres of docking.
- Gap: The patent gives no capture-envelope numbers (lateral or angular misalignment tolerated), it is indoor-only, and it targets four-wheel carts.

#### [US11577560B2: Automated carrier tugger mounted on an autonomous mobile robot for tugging a carrier](https://patents.google.com/patent/US11577560B2/en)
- Type: patent
- Who / when: Tata Consultancy Services. Inventors V. P. Bangalore Srinivas, P. P. Kamble, and V. R. Chintalapalli Patta. Filed 2021-03-19, granted 2023-02-14. (Verified)
- What it does / claims: A "single rear clamp" goes below the carrier's horizontal bar and front clamps with flanges engage vertical bars. Separate motors drive the vertical (height) and horizontal (reach) axes. A camera on a swivel adaptor plate guides the approach. It is meant for unmodified roll cages. (Verified)
- Cost or price info: none.
- Relevance: Shows that height-adjustable clamping can handle different bar heights, and refuse-cart handle and lift-bar heights differ between brands.
- Gap: Two motorized axes add cost. It is indoor-only, works on roll cages rather than tippable two-wheel carts, and reports no measurements.

#### [US12515342B2: Adaptive mobile robot behavior based on payload](https://patents.google.com/patent/US12515342B2/en)
- Type: patent (related application [US20230150321A1](https://patents.google.com/patent/US20230150321A1/en), now abandoned)
- Who / when: ST Engineering Aethon Inc. Filed 2022-11-15, granted 2026-01-06. (Verified)
- What it does / claims: Each cart carries a **universal receiver hitch** with an ID ("RFID tag, visual label, barcode, QR code"). A database stores the hitch height and the cart's size and maximum weight. The robot sets its tow-arm height from the database, and the hitch's "converging side members" self-center the end effector before clamps close on the side posts. (Verified)
- Cost or price info: none.
- Relevance: Converging guides (a funnel) are a cheap, purely passive way to absorb docking error.
- Gap: Carts are modified, since the hitch and tag are retrofitted. This is the baseline an "unmodified cart" paper argues against.

#### [US10168711B2: Method and apparatus for autonomous conveyance of transport carts](https://patents.google.com/patent/US10168711)
- Type: patent
- Who / when: Omron (formerly Omron Adept Technologies). Filed 2016-09-14, granted 2019-01-01. (Verified)
- What it does / claims: The robot drives underneath the cart, a wedge on the robot mates with a V-shaped receptacle on the cart's underside, and a motorized latch draws them together. The cart needs that mating receptacle, a normally-engaged brake, and reference features the robot can recognize. (Verified)
- Cost or price info: none.
- Relevance: Clear example of the "modify the cart" industrial approach, useful as a contrast.
- Gap: Requires cart modification and under-ride clearance. Refuse carts have neither.

#### [US11613007B2: Intelligent robotic system for autonomous airport trolley collection](https://patents.google.com/patent/US11613007)
- Type: patent
- Who / when: Chinese University of Hong Kong (Max Q.-H. Meng et al.). Filed 2020-03-16, granted 2023-03-28. (Verified)
- What it does / claims: A deep neural network on RGB images detects idle trolleys. The manipulator has "a structure same as a head portion of the trolley", so the robot "fork[s] the trolley by coupling the manipulator to the back" of it. The patent says this "does not require remodeling the existing trolleys". (Verified)
- Cost or price info: no prices, but it argues the design saves the cost of remodeling trolleys.
- Relevance: The end effector copies the object's own mating geometry. For us the analogue is an end effector shaped like the truck-arm or semi-automated lifter interface that refuse carts are already standardized to (see ANSI Z245.60, section F).
- Gap: Airport interior only, with an expensive sensor stack (see the Xiao et al. paper below).

#### [KR20240080297A: Mecanum wheel based tow robot for autonomous driving of rolling platform](https://patents.google.com/patent/KR20240080297A/en)
- Type: patent (granted as KR102731560B1 per Google Patents)
- Who / when: Seoul National University and Seoul National University of Science and Technology. Filed 2022-11-29. (Verified)
- What it does / claims: The platform (a wheelchair) rolls onto an entry ramp on the robot. Expandable arms with elastic tips then press outward against the inner surfaces of the platform's auxiliary (caster) wheels, coupling by friction. Only the auxiliary wheels are lifted, which "minimizes lifting load". No modification to the platform is required. (Verified)
- Cost or price info: none.
- Relevance: Shows coupling through the wheels instead of the frame. A refuse cart's steel axle and wheels are at a fixed low height and much stronger than its plastic body.
- Gap: The platform must roll itself onto the ramp, which a passive bin cannot do. Indoor only, with no measurements in the patent.

### B. Patents: residential trash-bin movers (hitch-relevant)

#### [US20200023524A1: Trash and recycle bin relocation robot](https://patents.google.com/patent/US20200023524A1/en)
- Type: patent application (**abandoned** in 2022 per Google Patents)
- Who / when: Hesham Mohamed. Filed 2019-07-17, published 2020-01-23. (Verified)
- What it does / claims: A "U shaped" metal hook on an angle bar sits on a linear actuator. The robot raises the hook under the bin's "horizontal pipe or cylindrical shaped bin handle" until "the trash can side sitting on the ground is lifted few inches off the ground, enabling the robot to push or pull the bin on the bins wheels." The application covers "commonly used outdoor waste bins that do not need to be modified". Navigation uses duct-tape line following, or image matching against pictures captured in a training run. A camera with AI locates the bins. (Verified)
- Cost or price info: none.
- Relevance: **This is the closest prior art to a tilt-and-tow hitch on unmodified carts.** It is abandoned, so it creates no active-patent obstacle (not legal advice).
- Gap: No prototype data: no forces, docking tolerance, success rate, cost, or outdoor localization. A measured implementation would be new evidence.

#### [US10046910B2: Semi-autonomous tug apparatus](https://patents.google.com/patent/US10046910)
- Type: patent (active, expected expiry 2036)
- Who / when: Kevin Wagner, Bryan Lew, and Timothy Domingo (individual assignee). Filed 2015-12-17, granted 2018-08-14. (Verified)
- What it does / claims: An arm swivels out from the tug and carries a latch: "a downwardly and rearwardly angled pressure plate" and a catch plate form a nest around the bin's handle. As the tug moves rearward, an actuator hook rotates the latches closed and a keeper plate locks them. The design is "noninvasive and can readily latch to conventional bins without modification." Electronics are an Arduino UNO R3 with a Bluefruit EZ-Link Bluetooth shield, driven by a stock Android app, with differential drive. It is remote-controlled, not autonomous. (Verified)
- Cost or price info: none stated, but the parts named are hobby-grade.
- Relevance: A purely mechanical self-locking latch on the handle, built from hobby electronics, is exactly the team's cost tier.
- Gap: Teleoperated only. There is no perception, autonomous docking, or measured latch capture envelope. The patent is active, so a commercial copy would need a design-around (a research prototype is a separate question; not legal advice).

#### [US10857925B1: Battery operated autonomous robotic trash can carrier](https://patents.google.com/patent/US10857925B1/en)
- Type: patent
- Who / when: Taranpreet Randhawa Sahota. Filed 2020-05-15, granted 2020-12-08. (Verified)
- What it does / claims: A framed carrier with a floor and an "electro mechanically deployed ramp". Cans are loaded onto the platform and carried. Sensors are sonar, LiDAR, and cameras, and it follows a predefined route or remote control. (Verified)
- Cost or price info: none.
- Relevance: The "carry" alternative to towing, which avoids the tilt problem.
- Gap: Large and heavy, and the patent does not explain how a bin gets up the ramp without a human. No data.

#### [US11970334B1: Automated, self-moving trash or recycling bin](https://patents.google.com/patent/US11970334)
- Type: patent (see also [US11884485B1, Autonomous refuse container, AI Inc](https://patents.google.com/patent/US11884485))
- Who / when: Synchronous Technologies & Innovations. Filed 2023-10-11, granted 2024-04-30. US11884485B1 (AI Inc, Ali Ebrahimi Afrouzi) was published 2024-01-30. (Verified)
- What it does / claims: Both describe bins with **built-in** drive, sensors, and navigation, so they replace the municipal cart. US11970334 also mentions an attachment version. (Verified)
- Cost or price info: none.
- Relevance: These define the "modified or replacement bin" baseline. A municipally issued cart usually cannot be swapped out, which is the argument for working with unmodified carts.
- Gap: They do not work with the city's existing cart.

### C. Commercial cart-moving AMRs

#### [MiR250 Hook (launch coverage, The Robot Report, 2021-06-15)](https://www.therobotreport.com/mir-launches-mir250-hook-for-autonomous-cart-towing/)
- Type: product
- Who / when: Mobile Industrial Robots, launched June 2021. (Verified)
- What it does / claims: The gripper "can interface with almost any existing cart" whose bottom cross beam sits **80 mm to 350 mm** above the floor. "QR codes placed on individual carts" or AprilTags identify carts. Specs: tows 500 kg, 2 m/s, 188 kg robot, 11 h at maximum load. Marketing says "no need to... purchase new carts". (Verified; corroborated by [Automated Warehouse](https://www.automatedwarehouseonline.com/?p=3880).)
- Cost or price info: **$42,000** per [robotomated.com](https://robotomated.com/explore/warehouse/mir-250-hook). This is a third-party aggregator whose page says "Not manufacturer-provided", so treat it as low confidence. MiR does not publish a price.
- Relevance: The industrial reference point for "towing unmodified carts". In practice it relies on fiducial tags plus a steel cross beam. Useful as the high-cost baseline in a cost comparison.
- Gap: Indoor floors, four-wheel carts, fiducials, roughly $42k (third-party figure). It has no tilt phase and no outdoor driveway terrain.

#### [Tractonomy ATR1 / ATR2 autonomous towing robots (Robotics Tomorrow, 2023-06-23)](https://www.roboticstomorrow.com/story/2023/06/autonomous-towing-robots-speeding-up-material-handling/20748/)
- Type: product
- Who / when: Tractonomy Robotics (Ghent), 2023. (Verified)
- What it does / claims: A "robotic gripper arm as a docking mechanism that could 'snap on'" to the cart, guided by cameras and computer vision. ATR1 tows 400 kg at more than 1 m/s and can "dock with carts in under 20 seconds". ATR2 adds dual-arm adaptive docking with 600 or 800 kg capacity at 1.8 to 2.5 m/s. The article says it can "tow any type of cart". (Verified)
- Cost or price info: not disclosed.
- Relevance: Docking time (under 20 s) is a concrete industrial benchmark to compare against.
- Gap: The marketing ("any type of cart") **conflicts with the company's own patent US11919155**, which needs a coupling structure on the cart. The product is indoor-only.

#### [Zebra/Fetch CartConnect500 brochure (via CSSI, 2021)](https://cssi.com/wp-content/uploads/cssi_fetch-cartconnect500-AMR-brochure.pdf)
- Type: product
- Who / when: Fetch Robotics / Zebra Technologies, brochure dated 2021. (Verified, PDF text extracted.)
- What it does / claims: A lift-module AMR that carries a **purpose-built FetchCart500**: a 200 lb cart with 600 lb payload. The robot weighs 1,111 lb (505 kg), has a maximum payload of 800 lb and top speed of 1.5 m/s, and uses **2× SICK 2D laser scanners (30 m, 275°) plus eight 3D cameras** for 360° coverage. (Verified)
- Cost or price info: not in the brochure.
- Relevance: A concrete example of the industrial sensor bill of materials (two safety lidars and eight depth cameras) that a low-cost design can be measured against.
- Gap: Requires its own carts and costs far more than a hobby budget.

*Not verified this sweep:* how OTTO Motors engages carts. The [OTTO page](https://ottomotors.com/resources/videos/autonomously-transport-payloads-between-stands-and-push-carts-with-otto/) only says it uses "first-party and third-party custom attachments... including carts".

### D. Research papers: docking to, towing, and collecting wheeled objects

#### [Robotized transportation of existing carts (ISR 2018)](https://www.vde-verlag.de/proceedings-en/454699033.html)
- Type: paper (ISR 2018, 50th International Symposium on Robotics, Munich, 2018-06-20/21)
- Who / when: Niels Jul Jacobsen (Mobile Industrial Robots ApS), 2018. (Snippet: the page redirects and returns 403 to fetch.)
- What it does / claims: A grasping device that exploits the fact that "most carts have a robust bottom frame where wheels are attached", allowing carts to be transported "without any additional docking mechanism or other major modification". The paper reports development and deployment experience. (Snippet)
- Cost or price info: none.
- Relevance: The peer-reviewed counterpart of MiR's hook patent, and the citation for "grip the existing frame".
- Gap: Industrial four-wheel carts on indoor floors. No published tolerance analysis was found in this sweep.

#### [Robotic Autonomous Trolley Collection with Progressive Perception and Nonlinear Model Predictive Control (ICRA 2022)](https://arxiv.org/abs/2110.06648)
- Type: paper
- Who / when: Anxing Xiao, Hao Luan, Ziqi Zhao, Yue Hong, Jieting Zhao, Weinan Chen, Jiankun Wang, and Max Q.-H. Meng. arXiv 2021, ICRA 2022. (Verified, full PDF read.)
- What it does / claims: A mobile manipulator collects airport luggage trolleys. Sensors are **a 3D LiDAR, two 2D LiDARs, a solid-state LiDAR, and an RGB-D camera**. The fork manipulator is driven by a DC motor, with a draw-wire encoder for feedback and block detection. Perception works in two stages. At long range, YOLO-style detection plus keypoints feed PnP (Perspective-n-Point pose estimation), giving mean error **0.17 m / 0.11 rad**. At short range, LiDAR plane detection on the trolley backplane gives **0.03 m / 0.02 rad**. Planning uses nonlinear MPC with control barrier functions. The trolley dataset has 1,200 images for detection and 800 for keypoints. (Verified)
- Cost or price info: none, but five range or vision sensors implies a high bill of materials. *Our inference, not stated in the paper.*
- Relevance: A far-camera / near-range-sensor docking pipeline transfers directly to bins, and these error numbers are a published baseline to compare a cheap sensor against.
- Gap: Indoor and very sensor-heavy, with no cost-versus-accuracy ablation and no test of how much docking error the gripper can tolerate.

#### [Autonomous Multiple-Trolley Collection System with Nonholonomic Robots: Design, Control, and Implementation](https://arxiv.org/abs/2401.08433)
- Type: paper (arXiv preprint, 2024-01-16)
- Who / when: Peijia Xie, Bingyi Xia, Anjun Hu, Ziqi Zhao, Lingxiao Meng, Zhirui Sun, Xuheng Gao, Jiankun Wang, and Max Q.-H. Meng. (Verified)
- What it does / claims: "a lightweight manipulator and docking mechanism, optimized for the sequential stacking and transportation of multiple trolleys", with vision-based control via online quadratic programming using control Lyapunov and control barrier functions. Demonstrated in real-world tests. (Verified)
- Cost or price info: none.
- Relevance: A recent example of the same group's docking work, which reviewers will expect to see cited.
- Gap: Indoor, with research-grade hardware and no cost analysis.

#### [A Systematic Evaluation of Different Indoor Localization Methods in Robotic Autonomous Luggage Trolley Collection at Airports](https://arxiv.org/abs/2303.06551)
- Type: paper (Robotica, vol. 43, 2025, pp. 542–560)
- Who / when: Zhirui Sun, Weinan Chen, Jiankun Wang, and Max Q.-H. Meng. (Verified)
- What it does / claims: Compares RFID, keypoints, UWB, and reflectors for trolley-collection localization on **accuracy, power consumption, coverage, cost, and scalability**. Keypoints came out best indoors. (Verified)
- Cost or price info: cost is one of the evaluation axes (specific dollar figures not retrieved).
- Relevance: **A published template for exactly the "cheaper, proven by measurement" framing**: several sensing options compared on accuracy against cost.
- Gap: Indoor and localization-only. It does not cover outdoor driveways or hitching.

#### [Development of an autonomous mobile towing vehicle for logistic tasks (ROBOT 2019)](https://bibliotecadigital.unipb.pt/entities/publication/245a287e-f661-4a11-9d32-67469e9549f5)
- Type: paper (4th Iberian Robotics Conference, ROBOT 2019, Porto. Published 2020, DOI 10.1007/978-3-030-35990-4_54 as listed by the repository.)
- Who / when: Cláudia Rocha, Ivo Sousa, Francisco Ferreira, Héber Sobreira, José Lima, Germano Veiga, and António Paulo G. M. Moreira (INESC TEC / IPB). (Verified)
- What it does / claims: A hospital trolley-towing robot fleet with "an innovative gripping system capable of grasping and pulling nonmodified standard trolleys just by coupling a plate". The robots identify and dock trolleys, use elevators, and were tested at FEUP and Braga Hospital. (Verified)
- Cost or price info: none.
- Relevance: Academic precedent for "unmodified trolley" towing, and the phrase reviewers will search for.
- Gap: The abstract does not detail the coupling mechanism. Indoor only.

#### [Design and Operation of Autonomous Wheelchair Towing Robot](https://arxiv.org/abs/2305.13902)
- Type: paper (arXiv 2023-05-23, submitted to *Intelligent Service Robotics*)
- Who / when: Hyunwoo Kang, Jaeho Shin, Jaewook Shin, Youngseok Jang, and Seung Jae Lee. (Verified)
- What it does / claims: A towing robot docks to the **front caster wheel** of a manual wheelchair using "a novel docking mechanism to facilitate easy docking and separation". It has mecanum drive, and a downward camera follows color-coded floor lanes. (Verified)
- Cost or price info: none.
- Relevance: Coupling at the wheel, plus very cheap camera lane-following navigation, which is comparable to a painted driveway line.
- Gap: Indoor only, and whether the wheelchair needs modification is not stated in the abstract.

#### [High-precision docking of wheelchair/beds through LIDAR and visual information (Frontiers in Bioengineering and Biotechnology, 2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11408198/)
- Type: paper (DOI 10.3389/fbioe.2024.1446512)
- Who / when: Xiangxiao Lei, Chunxia Tang, and Xiaomei Tang, 2024. (Verified)
- What it does / claims: Docking happens in three phases. Beyond 80 cm, LiDAR and IMU with improved A* handle navigation. From 10 to 80 cm, a camera reads **QR markers on the bed frame**. Under 10 cm, **two TF40 single-point laser rangefinders** measure distance and tilt. Reported results: docking gap error **under 5 mm** and angle deviation **under 0.5°**. (Verified)
- Cost or price info: no prices given.
- Relevance: Shows that the final centimetres can be handled with two cheap single-point rangefinders. This coarse-to-fine design is a strong low-cost template.
- Gap: Uses QR markers (a cart modification) and works indoors only.

#### [Wheelchair Maneuvering with a Single-Spherical-Wheeled Balancing Mobile Manipulator](https://arxiv.org/abs/2404.13206)
- Type: paper (arXiv 2024-04-19)
- Who / when: Cunxi Dai, Xiaohan Liu, Roberto Shu, and Ralph Hollis (CMU ballbot). (Verified)
- What it does / claims: A bimanual ballbot pushes an **unmodified** wheelchair, using quasi-static analysis for the nonholonomic cart. It tracked velocity with loads from **11.8 to 79.4 kg** at up to 0.45 m/s and 0.3 rad/s. (Verified)
- Cost or price info: none (the ballbot is a research-only platform).
- Relevance: A model of a towed nonholonomic object whose mass varies widely, analogous to an empty versus full bin.
- Gap: Extremely expensive platform, indoors.

#### [A Model Predictive Approach for Online Mobile Manipulation of Nonholonomic Objects using Learned Dynamics](https://arxiv.org/abs/1912.09565)
- Type: paper (arXiv 2019, revised 2020)
- Who / when: Roya Sabbagh Novin, Amir Yazdani, Andrew Merryweather, and Tucker Hermans (University of Utah). (Verified)
- What it does / claims: Learns the dynamics of wheeled "legged objects" found in hospitals (walkers, tables, chairs) from force and motion data. A mixed-integer convex MPC chooses which leg to grasp and what force to apply. (Verified)
- Cost or price info: none.
- Relevance: Learning a towed object's dynamics from measured force is relevant if the robot has to adapt to bin fill level.
- Gap: Indoor, with a research mobile manipulator.

#### [Partial Motion Imitation for Learning Cart Pushing with Legged Manipulators](https://arxiv.org/abs/2603.26659)
- Type: paper (arXiv 2026-03-27)
- Who / when: Mili Das, Morgan Byrd, Donghoon Baek, and Sehoon Ha (Georgia Tech). (Verified)
- What it does / claims: A Unitree Go2 with a WidowX arm learns to push a kid-sized shopping cart **in simulation**, with 99.9% success in IsaacLab and 94.4% in MuJoCo sim-to-sim transfer. The paper says carts "with passive wheels remain particularly challenging". (Verified)
- Cost or price info: none.
- Relevance: Shows current frontier interest in wheeled-object pushing, and that the real-world case is still open.
- Gap: Simulation only, and an expensive legged platform.

### E. Student projects (hitch details only; bin-to-curb navigation is covered in another sweep)

#### [SPARC: Self-Powered Autonomous Refuse Cart (UCF Senior Design, Spring/Summer 2018)](https://ece.ucf.edu/seniordesign/sp2018su2018/g12/files/Group%2012%20Conference%20Paper.docx)
- Type: student project
- Who / when: Alexis Drayton, Sean McGarvey, Wyatt Schmitt, and Chris Vento (UCF ECE), 2018. Funded by Selah Group Florida. (Verified, .docx text extracted.)
- What it does / claims: A four-wheel crawler (two driven wheels and two casters) that **the user straps the trash can onto** with tension straps over two metal bars. The concept describes "a clamp to the wheel axle of the garbage can in the rear, and grips in the front corners" for square semi-automated bins. It uses a PixyCam, GPS, and a colored stake marking the curb spot. (Verified)
- Cost or price info: described as a tight budget, with no total found in the extracted text.
- Relevance: Prior student work did not solve autonomous hitching. A human did the coupling.
- Gap: No autonomous docking or hitching, and no measurements reported in the paper.

#### [Team 311: Robotic Trash Cart (FAMU-FSU Senior Design, 2019)](https://eng-web1.eng.famu.fsu.edu/me/senior_design/2019/team311/docs/abstract.pdf)
- Type: student project
- Who / when: FAMU-FSU College of Engineering ME senior design Team 311, 2019. (Verified, PDF text extracted.)
- What it does / claims: A 2×6 ft aluminum frame with a fiberglass base that **carries** the bins, with a gate so collectors can reach them. It has two driven wheels plus casters, a Bluetooth controller, and was "designed... to carry a 250 pound load up a 5-degree incline". (Verified)
- Cost or price info: not in the abstract.
- Relevance: The "carry platform" alternative, and its 5° incline design spec.
- Gap: Teleoperated, with no hitching to the cart.

### F. Physics: tilting, towing, and lip-crossing a two-wheeled cart

#### [Mechanical load on the low back and shoulders during pushing and pulling of two-wheeled waste containers compared with lifting and carrying of bags and bins (Clinical Biomechanics, 2001)](https://doi.org/10.1016/s0268-0033(01)00039-0)
- Type: paper
- Who / when: B. Schibye, K. Søgaard, D. Martinsen, and K. Klausen, 2001. (Verified via Europe PMC metadata and abstract, PMID 11470296.)
- What it does / claims: Seven waste collectors pushed and pulled a **two-wheeled container loaded with 25 or 50 kg**, with push/pull force measured by a 3D force transducer. L4/L5 compression was 605–1445 N and shoulder torque 1–38 Nm. "No relation exists between the size of the external force and the torque at the low back." (Verified)
- Cost or price info: none.
- Relevance: The same object class as ours, and 25 and 50 kg are reasonable robot test loads. Handle-force magnitudes are in the full text, which was not retrieved.
- Gap: Human operators only. Nobody has measured the hitch and traction forces a *robot* needs for the same task.

#### [Force direction and physical load in dynamic pushing and pulling (Ergonomics, 2000)](https://doi.org/10.1080/001401300184477)
- Type: paper
- Who / when: M. P. de Looze, K. van Greuningen, J. Rebel, I. Kingma, and P. P. Kuijer, 2000. (Verified via Europe PMC, PMID 10755660.)
- What it does / claims: Force direction changes with handle height and force level. Pulling force went from about 14° upward to near horizontal as height and force increased. (Verified)
- Cost or price info: none.
- Relevance: Hitch height and pull angle change the vertical load on the hitch. For a robot, that load is also its traction.
- Gap: Four-wheel cart and human subjects, with no tilting container.

#### [IFA 4161: Feasibility study into the measurement of stress upon the musculoskeletal system during the pushing and pulling of large refuse bins](https://www.dguv.de/ifa/forschung/projektverzeichnis/ifa_4161-2.jsp)
- Type: other (German statutory accident insurance research project, completed 08/2011)
- Who / when: IFA (Institut für Arbeitsschutz der DGUV) with Berufsgenossenschaft für Transport und Verkehrswirtschaft. (Verified)
- What it does / claims: 120, 240, and 1100 L bins were fitted with 3D hand-force dynamometers, and ten refuse workers used them on an **asphalt test track with gradients and obstacles**. Hand forces ranged from **32 N** (sustained push, downhill, half-full 120 L) to **357 N** (initial push, full 1100 L, obstacle course). "The dynamic influence of the forces has a significant bearing upon the result." (Verified)
- Cost or price info: none.
- Relevance: 240 L is about 63 US gal (*our unit conversion*), close to the 64-gal cart. This is real outdoor-asphalt force data with an instrumented-bin method the team could copy cheaply using a load cell on the hitch.
- Gap: Per-condition numbers for the 240 L bin are not in the summary page. Human operators only.

#### [Hand forces, ground reaction forces and task duration when pushing a hand truck: results of a laboratory study (BAuA)](https://www.baua.de/EN/Service/Publications/Essays/article4260)
- Type: paper
- Who / when: BAuA (German Federal Institute for Occupational Safety and Health). Year not confirmed. (Verified during link check: page title and abstract match.)
- What it does / claims: Quantifies physical load when pushing hand trucks under varying **load, path inclination, and surface**. (Verified)
- Cost or price info: none.
- Relevance: A two-wheeled hand truck is mechanically similar to a tilted refuse cart.
- Gap: Numbers not retrieved (UNVERIFIED).

#### [2010 ADA Standards for Accessible Design (U.S. Access Board): §303 changes in level, §405.2, §406.2](https://www.access-board.gov/ada/)
- Type: standard
- Who / when: U.S. Access Board, 2010 Standards. (Verified, text extracted from the page.)
- What it does / claims: §303.2: "Changes in level of ¼ inch (6.4 mm) high maximum shall be permitted to be vertical." §303.3: ¼ to ½ inch "shall be beveled with a slope not steeper than 1:2". §303.4: more than ½ inch "shall be ramped". §405.2: ramp running slope not steeper than 1:12. §406.2: curb-ramp counter slopes not steeper than 1:20, and transitions "shall be at the same level". (Verified)
- Cost or price info: none.
- Relevance: A citable design envelope for lip heights (6.4 mm and 13 mm) and slopes (1:12) to test against.
- Gap: Residential driveway aprons and garage thresholds are not necessarily ADA-governed, so real lips may be larger. Measuring a sample of real driveways would itself be a contribution.

#### [Rolling resistance (CasterHQ engineering note)](https://casterhq.com/blogs/engineering-specifications/rolling-resistance)
- Type: other (vendor engineering note, moderate confidence)
- Who / when: CasterHQ, undated. (Verified)
- What it does / claims: Rolling coefficients by wheel material: forged steel 0.01–0.015, phenolic 0.02–0.03, 95A polyurethane 0.025–0.035, pneumatic 0.04–0.06, soft rubber 0.06–0.08. "Breakaway force runs 1.5 to 3 times higher than steady-state rolling." Going from 4" to 8" wheels cuts resistance about 50%. Rough asphalt is a "×1.8" multiplier. (Verified)
- Cost or price info: none.
- Relevance: Gives the inputs for sizing motors for the steady-tow phase.
- Gap: Vendor numbers for indoor casters. No measurements exist for refuse-cart wheels on driveway asphalt or concrete.

#### [Rolling resistance (Engineering ToolBox)](https://engineeringtoolbox.com/amp/rolling-friction-resistance-d_1303.html)
- Type: other (reference table)
- Who / when: Engineering ToolBox, undated. (Verified)
- What it does / claims: F = cW, and alternatively F = c_l·W/r, so resistance falls with wheel radius. Car tires: 0.01–0.015 on concrete, 0.02 on tar or asphalt, 0.2–0.4 on loose sand. (Verified)
- Cost or price info: none.
- Relevance: A textbook formula plus surface ranges for the analytical model.
- Gap: Car and bicycle tires only, not refuse-cart wheels.

#### [ANSI Z245.60: Waste Containers, Compatibility Dimensions (ANSI webstore)](https://webstore.ansi.org/standards/eia/ANSIZ245602008)
- Type: standard (paywalled)
- Who / when: ANSI / EIA, 2008 edition listed. (Snippet: the page returns 403 to fetch.)
- What it does / claims: Sets "compatibility dimensions for manufacturers so that containers can be safely used with refuse vehicles". It covers lifter types including semi-automated bar-locking (Type B) and automated arm (Type G). (Snippet)
- Cost or price info: paywalled (price not verified).
- Relevance: **Refuse carts are already standardized for machine engagement.** A hitch designed to the ANSI interface (lift bar or arm-grip zone) should fit every compliant cart. That is a strong argument for generality in an "unmodified cart" paper.
- Gap: The actual dimensions were not verified in this sweep and should be obtained, for example from a library copy or a city cart procurement spec.

**Back-of-envelope statics for a two-wheeled cart (our derivation, not a citation; all parameter values are assumptions):**
- *Breakaway tilt.* Let *m* be the cart plus contents, *a* the horizontal distance from the axle to the centre of gravity (CG), and *H* the hitch height above the axle. Pulling horizontally at the hitch, the force needed to start tilting is about F = m·g·a/H. Example: m = 50 kg, a = 0.20–0.30 m, H = 1.0 m gives F ≈ 98–147 N. A lower hitch (smaller H) needs proportionally more force, which is why handle-height hooks are attractive. This is in the same range as the 32–357 N human forces measured by IFA.
- *Balance.* At tilt angle θ = atan(a/h_cg) the CG sits over the axle and the hitch load goes to roughly zero. Tilting further shifts part of the bin's weight onto the robot's hitch, which **adds normal force to the robot's drive wheels**. That weight transfer helps traction for a light robot.
- *Steady rolling.* F ≈ c·m·g. With c = 0.02–0.08 (CasterHQ range) and m = 50 kg, F ≈ 10–39 N. With the ×1.8 rough-asphalt factor, about 18–71 N.
- *Lip or crack crossing (quasi-static, no momentum).* Per wheel, F/N = √(2rh − h²)/(r − h). For wheel radius r = 0.10–0.15 m (assumed; actual cart wheel sizes UNVERIFIED): h = 6.4 mm gives **0.30–0.38**, h = 13 mm gives **0.44–0.57**, and h = 25.4 mm gives **0.66–0.89**. Crossing even an ADA-legal ½-inch lip therefore needs about **5–25× the steady rolling force** unless momentum or approach angle helps. That makes it the likely motor-sizing and traction bottleneck, and a clean variable to measure.

### G. Cheapest documented ways to grasp or hitch a wheeled container

| Method | Documented in | Cart modification? | Actuators | Relative bill-of-materials tier (*our estimate*) | Notes for a 64/96-gal plastic cart |
|---|---|---|---|---|---|
| Passive spring latch on handle; robot pushes or pulls without lifting | US10046910B2 | None | 0 for the latch (mechanical) | Lowest | Hobby electronics (Arduino + Bluetooth) in the patent. No tilt, so the cart's front lip or feet may drag. Active patent. |
| Hook under handle, raised by linear actuator (tilt-and-tow) | US20200023524A1 | None | 1 linear actuator | Low | Closest analogue to how a person moves a cart. Abandoned application. Hitch load gives traction. |
| Hook + bracket clamp on an existing frame bar | US10668617B2, US12403591B2, ISR 2018 | None, but needs a rigid bar (MiR tags carts with QR or AprilTag for ID) | 1 linear actuator + 2 contact switches | Low–medium | On refuse carts the steel axle or the lift bar is the only rigid bar (UNVERIFIED geometry). Self-aligning pivot and contact switches are cheap. |
| Converging-funnel receiver with clamps | US12515342B2 | Yes (retrofit hitch + ID tag) | 1–2 | Medium | The funnel idea transfers; the retrofit does not. |
| Wheel or caster coupling | arXiv 2305.13902, KR20240080297A | None | 1–2 | Low–medium | The axle and wheels are the strongest part of the cart; couple low and keep the CG low. |
| End effector copying the object's mating geometry (fork) | US11613007B2 | None | 1 motor | Low–medium | Analogue: copy the ANSI Type B/G lifter interface. |
| Carry on a platform with a ramp | US10857925B1, FSU 2019 | None | 1 (ramp) + large chassis | High (size and weight) | Bulky. Getting the bin onto the ramp autonomously is unsolved in these sources. |
| Strap onto a crawler | UCF SPARC 2018 | None, but a human must strap it | 0 | Low | Not autonomous. |
| Under-ride wedge, lift pins, or reflector hitch | US10168711B2, US12227218B1, US11919155B2 | Yes | 1–2 | Medium–high | Excluded by the "unmodified" constraint. |
| Magnets | (none found) | n/a | n/a | n/a | They do not work on a plastic cart body. Whether some carts have a steel lift bar or axle a magnet could use is UNVERIFIED. |

### Also seen (verified, lower relevance)
- [US12227218B1, Cart lift robotic transport (Amazon, granted 2025-02-18)](https://patents.google.com/patent/US12227218): lift pins mate with recesses on the cart's underside, so the cart is modified.
- [US11479284B2, Automated shopping cart retrieval (Toshiba Tec, granted 2022-10-25)](https://patents.google.com/patent/US11479284): a camera-guided lead cart latches onto a line of nested shopping carts, which a push unit then moves.
- [US10233056B1, Grasping apparatus for transporting rolling racks (Brauer, granted 2019-03-19)](https://patents.google.com/patent/US10233056B1/en): guide and actuating armatures close around an unmodified rack frame or wheels, actuated through cables or levers.
- [US9669857B1, Propulsion device for hand-pushed equipment (Rainey, 2017, expired)](https://patents.google.com/patent/US9669857B1/en): an adaptor clamps to the shopping cart's lower rear crossbar through a yaw joint, and the cart itself acts as the steering element.
- [Autonomous Mobile Robot for Transportation of Hospital Carts (Vongbunyong et al., KMUTT, 2022 poster)](https://kirim.kmutt.ac.th/converis/portal/detail/Publication/1001078416?lang=en_GB): a towing mode that grasps cart handles plus a lifting mode for medium carts.
- [Human Body Mechanics of Pushing and Pulling (Argubi-Wollesen et al., Safety and Health at Work, 2016)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5355528): a review that cites Schibye 2001 and notes that "Waste collectors handling the larger... (1,100 L, 148 kg) containers considerably exceeded the proposed MAF of 186N".
- [Laboratory for Validation of Rolling-Resistance Models (Larsen et al., Int. J. Applied Mechanics, 2021)](https://forskning.ruc.dk/da/publications/laboratory-for-validation-of-rolling-resistance-models/): a drum rig for small wheels. The rolling coefficient rises with surface roughness, speed, and load.
- [Mechanical and Stability Analysis of Hand Truck (S. Park, APS SESAPS 2017 abstract)](https://meetings-archive.aps.org/ses/2017/w1/27): statics and tilt-platform stability of hand trucks versus load CG position.
- [Rezzi SmartCan (ChannelNews, 2019-10-02)](https://www.channelnews.com.au/robotic-dust-bin-that-goes-walkabout/): a motorized replacement bin with an app and docking station. Price not announced.

### Gaps and opportunities
1. **"Unmodified" is rarely truly unmodified.** MiR tags carts with QR codes or AprilTags. Tractonomy's patent needs a frame hitch and reflector even though its marketing says "any type of cart". Aethon, Omron, and Amazon all retrofit hitches, receptacles, or recesses. A paper that defines and meets a strict "zero added hardware, zero tags" standard on refuse carts would occupy clear territory.
2. **Refuse carts are already machine-interface standardized (ANSI Z245.60), but no robot work exploits that.** Designing the hitch to the standard lifter interface and testing it across several brands would turn "works on my bin" into a generality claim. Next step: verify the dimensions.
3. **No published capture-envelope or docking-tolerance study for a passive hitch.** MiR's self-aligning pivot with contact switches and Aethon's converging funnel absorb error, but none of these sources quantify how much. Measuring success rate against lateral and angular offset, with versus without a passive funnel, would be a cheap, novel, measurable result.
4. **Cost-versus-accuracy ablation is a proven paper format that has not been applied here.** The trolley robot uses five range or vision sensors and reaches 0.03 m / 0.02 rad, and the bed-docking work gets under 5 mm using two cheap single-point rangefinders. Sun et al. (Robotica) evaluate localization on accuracy *and* cost. Repeating that design for bin docking with hobby sensors (monocular camera, 2D ToF or single-point lidar, ultrasonic) is directly supported by precedent.
5. **No robot-side force data for tilt-and-tow.** Human studies (Schibye: 25/50 kg two-wheeled containers. IFA: 32–357 N on asphalt with obstacles) exist, but nobody has measured hitch force, traction, and weight transfer for a small robot towing a refuse cart. A load cell on the hitch is enough to replicate the IFA method.
6. **Lip and crack crossing is likely the binding constraint and is unstudied.** Our quasi-static estimate says a ½-inch lip needs about 0.44–0.57 × wheel load, against 0.01–0.08 for rolling. A measured force-versus-lip-height-versus-fill-level curve, plus a survey of real driveway and curb lips against the ADA ¼"/½" thresholds, would be original data.
7. **The hitch strategies have never been compared head-to-head.** Latch (US10046910), hook-lift tilt (US20200023524), carry platform (US10857925, FSU), and strapping (UCF SPARC) all exist on paper with no data. A controlled comparison of 2–3 strategies on success rate, peak force, energy per trip, and parts cost fits a short paper.
8. **Nearly all docking work is indoors** (warehouse, hospital, airport). Outdoor slope, wet surfaces, cracks, and lighting changes are untested for cart docking. Even a modest outdoor evaluation would extend the literature.
9. **Wheel or axle coupling is underexplored for two-wheeled cart.** Wheelchair caster docking (Kang et al.) and friction wheel coupling (KR20240080297A) show it works for other objects. A low, axle-level hitch could lower the CG and the tipping risk compared with handle-level hooks. Worth one prototype.

### Searches run
WebSearch (standard mode), in order:
1. `US11919155 patent cart docking autonomous mobile robot` (cut off, no results; the patent was fetched directly instead)
2. `patent autonomous robot moving trash bin to curb`
3. `autonomous mobile robot tow unmodified cart patent caster wheels gripping`
4. `Tractonomy Robotics cart docking AMR`
5. `"Robotized transportation of existing carts" ISR 2018`
6. `MiR Hook 250 cart gripper automatically picks up carts specifications`
7. `Fetch Robotics CartConnect autonomous cart transport existing carts`
8. `OTTO Motors cart tugger attachment OTTO 100 cart`
9. `MiR Hook price USD autonomous cart towing robot cost`
10. `autonomous mobile robot price "$" MiR250 cost per unit tugger AMR price range` (cut off)
11. `airport luggage trolley collection robot paper docking lidar`
12. `mobile robot autonomous docking towing hospital cart paper arXiv`
13. `shopping cart collection robot autonomous paper IEEE`
14. `"Design and Operation of Autonomous Wheelchair Towing Robot" arXiv`
15. `arxiv Kang wheelchair towing robot docking front caster mecanum 2023`
16. `"Development of an Autonomous Mobile Towing Vehicle for Logistic Tasks" hospital trolley gripping`
17. `legged robot pushing cart wheeled object manipulation arXiv`
18. `arxiv.org "wheelchair towing robot" Kang 2305`
19. `wheelie bin pushing pulling force ergonomics study refuse cart handle force measurement`
20. `ANSI Z245.60 refuse cart dimensions lift bar handle compatibility standard`
21. `hand truck tipping force analysis two-wheeled cart stability pull force paper`
22. `rolling resistance coefficient small wheels concrete asphalt caster measurement study`
23. `ADA 303 changes in level 1/4 inch vertical 1/2 inch beveled curb ramp`
24. `wheel obstacle climbing force step height wheel radius analysis wheelchair caster bump paper`
25. `Toter 96 gallon cart specifications...` and `Rehrig Pacific 96 gallon roll out cart spec sheet...`: **not executed** because the shared session web-search budget was exhausted.

Lookups other than WebSearch:
- Citation and similar-document lists on the Google Patents pages for US11919155B2 and US10668617B2 (source of the MiR, TCS, Aethon, and Brauer patents).
- Europe PMC ID lookups for PMIDs 11470296 and 10755660.
- Full-text extraction of arXiv 2110.06648, the CartConnect500 brochure, the UCF SPARC .docx, the FSU abstract, and the access-board.gov ADA page.

**Known coverage holes:**
- Manufacturer cart specifications (wheel diameter, axle and lift-bar height, empty weight, rated load) for Toter, Rehrig, and Cascade carts.
- ANSI Z245.60 dimensions.
- OTTO cart engagement details.
- Older mobile-manipulator cart-pushing literature (PR2-era work), which was not retrieved.
- Push/pull force magnitudes from the Schibye 2001 full text and the BAuA hand-truck study.

### Link verification (2026-10-03)
- URLs checked: 49 (unique)
- OK (resolve and page title/subject matches the entry): 49. Most via curl (HTTP 200 + page title); The Robot Report and Automated Warehouse (403 to curl) confirmed via WebFetch; the two DOIs (Schibye 2001, de Looze 2000) confirmed via Crossref and Europe PMC metadata; BAuA page re-fetched successfully and upgraded from Snippet to Verified.
- Fixed: 0
- Removed: 0
- Confirmed only via search snippet (bot-blocked, not re-confirmed in this check): 2 (ISR 2018 vde-verlag.de page, which redirects to a bot-blocked TIB record; ANSI Z245.60 webstore page). Both remain labeled "Snippet" in their entries.
- Spot-checked central claims on patent pages (US11919155B2 reflector unit/fasteners, US20200023524A1 abandoned/"do not need to be modified", US10046910B2 Arduino UNO R3/Bluefruit, US12515342B2 dates), the robotomated $42,000 figure and "Not manufacturer-provided" note, the IFA 32-357 N range, and the CartConnect500, FSU and UCF SPARC document text: all match.


---

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


---

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



---

