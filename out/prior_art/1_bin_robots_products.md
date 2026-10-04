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
