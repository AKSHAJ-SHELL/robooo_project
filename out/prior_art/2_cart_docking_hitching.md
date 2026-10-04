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
