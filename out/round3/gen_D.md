# Generator D, round 3: "Field data that changes decisions"

Date: 2026-10-04. Strategy: find a question where two students with a portable rig can collect multi-site field data that nobody has published, fit a simple predictive model, validate it on held-out sites, and change what a real audience does. The answer must not be derivable on paper.

**Search caveat (please read).** From this sandbox, Google Scholar, arXiv, IEEE Xplore, ScienceDirect, MDPI, ResearchGate, OpenAlex, Semantic Scholar and Google Patents all returned egress blocks (403) when opened directly. Novelty checks therefore used about 35 web-search queries (standard and extended). The tool returns each result's title, URL and a content snippet. **Every link below appeared in those search results, and the claim attached to it comes from the snippet. I could not open the full pages.** Where a snippet did not settle a point, I say "unsure". Reviewers with full access should check the "what is new" claims against items 1 to 3 of each prior-work list first.

---

## Candidates considered and killed

| # | Candidate | Verdict | Why |
|---|---|---|---|
| K1 | Robot proprioception as a proxy for ADA "firm and stable" on decomposed-granite paths | Killed | The US Access Board's Rotational Penetrometer research already correlates the RP with wheelchair work and walking effort across surfaces ([Access Board conclusions](https://www.access-board.gov/research/exterior-surfaces/accessible-exterior-surfaces/conclusions/)). A robot version would be a cheaper re-instrumentation. |
| K2 | Accuracy of DEM-derived sidewalk incline for wheelchair and robot routing | Killed | Already done: DEM resolution versus slope accuracy, and LiDAR-DEM cross-slope checked against an inclinometer ([GMU thesis](https://mars.gmu.edu/handle/1920/10295)). Also a poor fit for IROS/CASE. |
| K3 | Do Street View accessibility labels predict physically measured barriers? | Killed | Validation literature exists: [Hara et al. CHI 2013](https://makeabilitylab.cs.washington.edu/media/publications/Hara_CombiningCrowdsourcingAndGoogleStreetViewToIdentifyStreetLevelAccessibilityProblems_CHI2013.pdf) and [Urban Sci. 2025](https://doi.org/10.3390/urbansci9040130). Robotics novelty is low. |
| K4 | Soil compaction and turf wear from daily robotic-mower traffic | Killed | The [ROBO-GOLF final report](https://sterf.org/wp-content/uploads/2024/09/ROBO-GOLF_final-report-to-STERF.pdf) measured compaction under robotic versus manual mowing. Repeated lightweight-robot wheeling effects are in [Soil & Tillage Res. 2023](https://www.sciencedirect.com/science/article/pii/S0167198723001587). |
| K5 | Magnetic-anomaly localization along sidewalks and driveways | Killed | Close prior work on suburban vehicle magnetic map-matching ([arXiv 2411.06543](https://arxiv.org/abs/2411.06543v1)) and patents ([EP4107482B1](https://data.epo.org/gpi/EP4107482B1)). It also sits next to the brief's excluded "control joints / Hall tape" landmark ideas. Incremental. |
| K6 | Delivery-robot IMU as a city sidewalk trip-hazard inspector | Killed | "[Leveraging Sidewalk Robots for Walkability-Related Analyses](https://arxiv.org/pdf/2507.12148)" (2025) occupies this space, and smartphone or wheelchair-IMU roughness work is old. It would read as a known method on a new platform. |
| K7 | Cellular teleop coverage at sidewalk level versus FCC maps | Killed | An IMC-style measurement paper, not robotics. Drive-test literature is large. |
| K8 | Skid-steer versus articulated turf damage when turning | Killed | Predictable in direction (articulation scuffs less, as Husqvarna and Ventrac already market). Repeated damage to other people's lawns also creates a consent problem. |
| K9 | "Campus bias": are university test sites representative of residential sidewalks for robot evaluation? | Runner-up, not chosen | High lab appeal, because each lab's own campus would be characterized. But it needs Nav2 trials at many distant sites, and intervention counts would be low and noisy (underpowered). Feasibility is about 5. |

The three survivors are below, best first.

---

## Idea D1: "Is it the dew or the dirt?" Time-varying traction of small robots on real lawns, and whether free weather data can predict it on unseen lawns

**Research question.** On real residential and park lawns, how much of a small wheeled robot's traction variation comes from the *time-varying* wetness state (leaf-surface water from dew or mist, versus soil water from rain or irrigation) rather than from the *lawn itself* (species, thatch, cut height, soil)? And can a model using only free inputs (weather-station data, time of day, a phone photo) predict peak traction and slope limit on held-out lawns as well as an in-situ probe?

**Who benefits and how much.**
- **Robot-mower makers.** Husqvarna, Segway Navimow, Mammotion, Ecovacs, Worx and Sunseeker all advertise slope ratings (up to about 45–80%). They also ship "rain delay" settings and traction control as heuristics. A validated split between leaf wetness and soil water tells them two things. First, whether a dew sensor or weather-API gate should replace the rain sensor. Second, what slope to *derate to* in which hours. Today their own support pages tell users to wait for the lawn to dry, with no number ([Navimow](https://navimow.com/blogs/navimow-academy/what-to-do-if-your-navimow-slips-on-slopes)).
- **Field and agricultural robotics researchers.** Vision slip models (Angelova; SlipNet) assume traction is a function of terrain *class* plus slope. If the same lawn swings more between 7 am and 3 pm than between lawns, those models are structurally blind. That is a design rule the whole traversability community would need to absorb.
- **Solar-farm and vineyard mowing robots** (an inter-row grass problem).
- **Agricultural robots on irrigated ground.** In Carpin's RAPID setting, robots drive irrigated vineyard rows.

**Why the outcome is uncertain.** The turf literature disagrees on the sign of the effect. Penn State's traction work reports both positive and negative correlations between soil water and traction across studies, and found traction *increased* with soil water on tall fescue ([PSU SSRC report](https://plantscience.psu.edu/research/centers/ssrc/documents/effects-of-turfgrass-cutting-height-and-soil-conditions-on-traction.pdf/@@download/file/effects-of-turfgrass-cutting-height-and-soil-conditions-on-traction.pdf)). Cenek et al. found that a *lightly loaded* tyre is much more sensitive to wetness than a locked car wheel ([TRID](https://trid.trb.org/View/783691)). Small robots are the lightly loaded case, which hints that leaf film could dominate. Both outcomes are publishable:
- **Result A: leaf wetness dominates.** A morning-dew derate is needed, and vision models need a time and weather input.
- **Result B: soil water and species dominate, and dew is negligible for lugged wheels.** Vision-plus-terrain-class models are adequate, rain sensors are the wrong gate, and makers should gate on hours since irrigation.

A third possible outcome is a tread-by-wetness interaction: lugs make the robot soil-limited while smooth tyres make it film-limited. That would be a direct wheel-design rule. Theory cannot settle this. Turf traction mixes Coulomb friction on a water film, root-mat shear and lug penetration, and published signs conflict.

**Non-obvious insight.** The key variable for small-robot traction on grass may not be visible in any single image. It is a *hidden temporal state* (leaf film, soil water), and a factorial manipulation can separate it cleanly:
- Mist a test strip to wet the leaves without changing soil water.
- Irrigate the evening before and test the next afternoon to wet the soil while the leaves are dry.

Nobody appears to have run this 2×2 for any vehicle, let alone a 10–15 kg robot.

**Closest prior work (from search-result listings; full pages could not be opened from this sandbox) and what is new.**
1. Angelova, Matthies et al., "Learning and prediction of slip from visual information," RSS 2006 ([RSS](https://roboticsproceedings.org/rss02/p14.html), [JPL pdf](https://robotics.jpl.nasa.gov/media/documents/Angelova06LearningSlip.pdf)). Slip as a function of slope per visually recognized terrain class (soil, sand, gravel, woodchips). *New:* wetness state as a time-varying hidden variable, a within-terrain variance decomposition, and grass with a factorial wetness manipulation.
2. Yakubu et al., SlipNet, 2024 ([arXiv 2409.02273](https://arxiv.org/abs/2409.02273)). Segmentation plus probabilistic slip, trained mainly on Vortex-simulated deformable soils. *New:* real multi-site turf data, and a test of whether *any* image-only predictor can capture the dew effect.
3. Cenek, Jamieson & McLarin, "Frictional characteristics of roadside grass types," NZ ([TRID](https://trid.trb.org/View/783691), [pdf](https://saferroadsconference.com/wp-content/uploads/2016/05/Peter-Cenek-Frictional-Characteristics-Roadside-Grass-Types.pdf)). Car-tyre drag and locked-wheel tests, dry versus wet. Clover gives about 60% of ryegrass braking friction, and a lightly loaded tyre is more wetness-sensitive. *New:* a driven-wheel small robot, leaf versus soil water separated, multiple lawns, held-out prediction. The species finding motivates species as a covariate.
4. Penn State SSRC turf traction (McNitt group): cutting height and soil water versus traction with the PennFoot device ([report](https://plantscience.psu.edu/research/centers/ssrc/documents/effects-of-turfgrass-cutting-height-and-soil-conditions-on-traction.pdf/@@download/file/effects-of-turfgrass-cutting-height-and-soil-conditions-on-traction.pdf), [method paper](https://pure.psu.edu/en/publications/development-and-evaluation-of-a-method-to-measure-traction-on-tur/)). Cleated *shoe* traction on maintained research plots. *New:* wheels rather than cleats, uncontrolled residential lawns, a leaf-film manipulation, and a predictive model for robots.
5. "Designing Hybrid Mobility for Agricultural Robots," *Machines* 13(7):572, 2025 ([MDPI](https://www.mdpi.com/2075-1702/13/7/572)). Wheeled versus tracked slip at 4 slopes × 3 soil moistures in orchards. Wheeled slip rises with moisture. *New:* turf rather than bare orchard soil, leaf film versus soil water, multiple sites, held-out prediction from free data. Theirs is the closest result on the soil-water side.
6. Fritz et al. (TU Graz), traversability costs from standardized locomotion experiments plus earth-observation data, RAS 2023 ([ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0921889023001331), data at robonav.ist.tugraz.at/data). Per-terrain costs for 4 robots on alpine terrain. Unsure whether weather states were modeled. A related search snippet says weather "heavily affects" traversability, which suggests they flagged it as a limitation. *New:* explicit wetness-state factor and within-site temporal variance.
7. Kim et al., tractor traction versus soil moisture during plowing, Soil & Tillage Res. 2021 ([ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0167198720306334)). Large-tractor regime. Shows the soil-moisture effect is established for heavy machines, not for 10 kg wheels on turf.
8. Grass-cutting robot for inclined surfaces ([PMC9823410](https://pmc.ncbi.nlm.nih.gov/articles/PMC9823410/)). A platform demo with "no slipping observed". There is no wetness factor and no traction measurement.

**Experiment design.**
- **Unit.** One drawbar-pull "ramp" (about 40 s). The robot is tethered through a load cell to a ground stake and ramps wheel torque slowly. The logs give the pull-versus-slip curve, the peak traction coefficient μ_peak = F_peak/W, and slip at 90% of peak.
- **Factors (small grid).**
  - Leaf wetness: dry / wet. Wet comes from natural dew *or* a 0.2–0.3 mm hand mist on the strip just before testing, measured with a leaf-wetness sensor.
  - Soil water: as-found / raised. Raised means irrigated 12–20 h earlier with leaves dried by afternoon, measured with a capacitive probe calibrated gravimetrically per lawn.
  - Tread: smooth hoverboard rubber / bolt-on lug band (mower-style).
  - This gives 2×2×2 = 8 cells per lawn.
- **Sites.** 14 lawns: own and neighbours' yards, a school field, and 2–3 park lawns with permission. Spread across species (cool-season fescue or rye, warm-season Bermuda or kikuyu going dormant, clover-rich). 10 lawns are for model fitting and 4 are held out from the start; leave-one-lawn-out CV runs inside the 10.
- **Replication.** Each lawn gets 2 visits per soil state on different days, with 3 spots × 2 pulls per cell per visit. That is about 14 × 2 × 2 × (2 leaf × 2 tread) × 6 ≈ 1,340 pulls.
- **Session load.** About 3 pulls per minute plus setup, so about 25 min per lawn-visit. That makes 56 lawn-visits across about 10 weeks (Nov 20 to Feb 7), roughly 5–6 per week. Dew visits are 6:45–7:30 am before school, about once a week per student.
- **Slope validation.** On 4 lawns with natural 10–30% slopes, run step-up climb tests with ballast to find the climbable grade. Compare it with the grade predicted from flat-ground μ_peak (sin θ + c_rr ≈ μ_peak·cos θ).
- **Power.** Assume pilot-plausible values: within-session SD of μ_peak about 0.05, between-visit SD about 0.04, and smallest effect of interest Δμ = 0.05 (about a 5–7% slope-rating change, which matters to makers). With 14 lawns, paired leaf-wet versus leaf-dry contrasts per visit are averaged over 6 pulls, so the per-visit contrast SD is about 0.05·√(2/6) ≈ 0.03 plus visit noise. 28 lawn-visits per soil state then give power above 0.9 at α = 0.05 for Δμ = 0.05 (mixed model, lawn random intercept). The held-out test (4 lawns × 8 cells × ~2 visits ≈ 64 cell-means) is enough for an RMSE comparison with bootstrap CIs.
- **The decision-relevant comparison.** Fit four model families and score them on the held-out lawns:
  - (M1) Image-only: pretrained image embedding or terrain class, the Angelova/SlipNet-style baseline.
  - (M2) Free data: CIMIS station dew point, hours since rain, reference ET, time of day, plus the phone photo.
  - (M3) In-situ probe: soil water, leaf-wetness sensor, pocket penetrometer.
  - (M4) Proprioceptive: μ estimated from the robot's own current-versus-slip during the first 3 m of normal driving.

  The headline is the held-out RMSE ranking and how much variance each stage explains.

**Strongest fair baseline.**
- An image-conditioned slip regressor trained in the Angelova/SlipNet style on the *same* pulls (fair: same data, same split). This is the field's default assumption.
- Industry practice: a constant slope rating with a rain-sensor pause.
- For the instrument side: a turf-science shear/torque test. A DIY studded-disc torque test after the PQS studded-disc apparatus is cheap (a torque wrench). A PennFoot-class device is out of budget, so the paper must say so.

**Measurements and analysis.**
- Drawbar force: 200 kg S-beam load cell plus HX711 at 80 Hz.
- Wheel speed from hub Hall sensors. Ground speed from a draw-wire encoder on the tether, or a downward optical-flow camera as backup.
- Motor current.
- Soil volumetric water: capacitive probe, gravimetric calibration with kitchen-oven drying of cores.
- Leaf wetness: sensor plus a photo of a filter-paper blot.
- Grass height and species: photo plus manual ID. Thatch depth: core.
- Air temperature and dew point.
- Analysis:
  - Linear mixed model μ_peak ~ leaf × soil × tread + species + height + (1 | lawn/visit).
  - Variance decomposition: within-lawn temporal share versus between-lawn share. This is the headline number.
  - Held-out RMSE with 95% bootstrap CIs for M1–M4.
  - Slope-limit validation (predicted versus measured grade).
- Release a CSV dataset with all covariates.

**Build list (target ≈ $640).** "Verified earlier" means the price was verified in the project's round-1 docs (out/final.md). "Est." means estimated and not re-verified this session.

| Item | Cost | Status |
|---|---|---|
| Gotrax hoverboard (motors, battery, Hall sensors) | $139 | verified earlier |
| ESP32 Feather V2 | $19.95 | verified earlier |
| SparkFun 200 kg load cell + HX711 | $101.90 | verified earlier |
| Plywood/aluminum chassis, ballast mounts, tether hardware, ground stake | $80 | est. |
| Lug bands / bolt-on cleats for wheels (PETG or rubber strip) | $25 | est. |
| Draw-wire encoder (or rotary encoder + spool) | $35 | est. |
| 3 capacitive soil-moisture probes + small digital scale for gravimetric calibration | $45 | est. |
| Leaf-wetness sensor (research-grade, about $150, or DIY grid) | $150 | est. |
| Pocket penetrometer / torque wrench for studded-disc test | $40 | est. |
| Raspberry Pi already owned (logging on laptop) | $0 | — |
| **Total** | **≈ $637** | |

**Timeline.**
- Oct 15–31: lawn recruitment (14 sites, written permission). Bench test of the hoverboard drive with the FOC firmware current limit. Check that slip can be reached on dry turf at 15 kg (the key de-risk).
- Nov 1–15: order parts. Write pull-ramp firmware and logger. Do probe calibration.
- Nov 16–30: rig integration. Pilot on 2 home lawns. Measure the SDs and re-run the power analysis.
- Dec 1–20: first 4 lawns, all 8 cells, one visit each.
- **Data by Dec 20:** about 380 pulls on 4 lawns, a first variance decomposition, and the leaf-versus-soil sign.
- Dec 21–Jan 10: winter break. Rain season gives natural soil-wet states. Do lawns 5–10 and second visits.
- **Jan 15 go/no-go:** is the within-lawn temporal share measurable (CI excludes 0)? If not, pivot the headline to species/tread effects plus the held-out predictor.
- Jan 16–Feb 7: 4 held-out lawns. Slope-validation climbs on 4 sloped lawns.
- Feb 8–14: data freeze. Fit M1–M4.
- Feb 15–26: write-up, dataset release, submission.

**Main risk and fallback.**
- **Risk:** the hoverboard current limit (about 15 A per motor) is reached before peak traction on dry, dense turf, or ballast makes the robot unrepresentative.
- **Fallback:** convert to a towed braked-wheel rig (the robot or a hand cart tows a single instrumented test wheel with a brake). This is the standard single-wheel tester layout, and it gives the same μ-slip curves independently of drive limits.
- **Secondary risk:** dry California winter weeks. Mitigation: the irrigation and mist manipulations make the experiment independent of weather.

**Best venue.** IROS 2027 (field robotics / traversability). Alternates: RA-L with IROS option, or CASE 2027 if framed as robotic-mower automation. Dataset track at an ICRA 2027 workshop as the fallback.

**Lab appeal.**
- **Best fit 1: UCSC, Nobby Kobayashi.** SIP 2026 project ECE-08, "Unmanned Autonomous Ground Vehicle Terrain Traversability for Unstructured Environments" (slip, slope) ([SIP 2026 projects](https://sip.ucsc.edu/2026-research-projects/)).
  - *What the lab gains:* a ready-made ground-truth traction rig and labeled multi-site dataset its SIP interns can use for traversability models, plus a concrete negative or positive result on time-varying traction. Helping costs one or two feedback calls.
- **Best fit 2: UC Merced, Stefano Carpin.** RAPID (Robot-Assisted Precision Irrigation Delivery), where robots drive irrigated vineyards and the lab predicts soil moisture with ML ([UCSC CPS RAPID page](https://cps.soe.ucsc.edu/node/347), [RAPID publications](https://rapid.berkeley.edu/publications.html)). Also his ICRA 2024 Nav2 paper on letting robots traverse grass that lidar sees as an obstacle ([arXiv 2407.18535](https://arxiv.org/abs/2407.18535)).
  - *What the lab gains:* a measured link from soil moisture to traction lets RAPID's moisture maps double as traversability or slip maps, an extension of their "grass is traversable" costmap. Students offer the data and the rig.

**Link to the bin robot.** It reuses the hoverboard drive base and load cell. Driveway-edge grass and wet-morning slip on the way to the curb are the same physics.

**Honest self-score.**
- **Novelty 7.** Soil-moisture effects on traction are known for tractors and cleats. The leaf-versus-soil factorial for small wheels, the within-lawn temporal variance share, and held-out prediction from free weather data appear new, but a reviewer may still call it "terramechanics in a new setting."
- **Feasibility 7.5.** Simple rig, local sites, manipulations independent of weather, data by Dec 20. The main risk (drive current limit) has a standard fallback.
- **Impact 7.** It gives a design and firmware rule to a large consumer-robot industry and a structural caveat to vision-slip models, with a reusable dataset. Main-track IROS is plausible only if the temporal-variance result is striking.
- **Overall about 7.2.**

---

## Idea D2: "How precise does a curbside cart need to be?" Measuring how cart pose affects automated side-loader collection in the field

**Research question.** In real residential collection, how do cart pose (distance from the truck's path or curb, yaw, and spacing to the neighbouring cart or obstacle) affect the time to service each cart, the number of re-grabs, and post-dump displacement or tip-over? Below what pose error does placement stop mattering?

**Who benefits and how much.**
- **Haulers and cities.** Automated side-loader (ASL) routes service roughly 1,000+ carts per truck-day, and industry material quotes 8–12 s per dump cycle ([fleet guide, low-authority](https://fleetrabbit.com/blogs/post/automated-side-loader-asl-garbage-truck-guide)). A 1 s per-cart placement penalty therefore costs about 17 truck-minutes per route-day. Cities write detailed placement rules (3 ft apart, wheels at curb, handles facing the house), and some now *refuse* to service misplaced carts ([Amarillo](https://abc7amarillo.com/news/local/improperly-placed-curbside-carts-no-longer-being-picked-up-after-march-4), [Cranbrook](https://cranbrook.ca/news/keeping-space-between-garbage-bins-recycling-carts-important-for-proper-collection)). Nobody has published which rule terms actually cost time.
- **Truck OEMs automating the arm.** McNeilus/Oshkosh CartSeeker claims 96% recognition and 8% cost reduction ([McNeilus](https://mcneilusgarbagetrucks.com/cartseeker), [Recycling Today](https://www.recyclingtoday.com/news/mcneilus-acquires-cartseeker-eagle-vision-systems)). A public pose-versus-service-time curve is the human-operated baseline they need to beat and the input distribution they must handle.
- **Cart-moving robot designers, including this team's bin robot.** The curve sets the robot's placement-accuracy spec. Is ±30 cm good enough, or must it be ±5 cm? Every bin-to-curb robot needs that spec, and it decides how much sensing the robot needs.

**Why the outcome is uncertain.**
- **Result A: within reach, placement barely matters.** Arm reach is 8–12 ft and drivers compensate. City rules are then over-specified, and bin robots can be cheap and coarse.
- **Result B: sharp penalties above some thresholds.** For example, spacing under about 0.5 m forces two arm cycles or a truck reposition, and yaw over about 30° causes re-grabs. Rules are then justified and robots must hit a tight spec.

Penalties may also differ strongly by grabber type (claw versus Python-style arms) and by stream (trash, recycling, green trucks). This is a joint human-machine system, so no model predicts it on paper. It depends on driver strategy, joystick dynamics, the gripper funnel and truck stopping position.

**Non-obvious insight.**
- The binding constraint may be the *truck's stopping decision* (one stop per cart versus one stop for a pair), not arm reach. That would make *spacing and pairing* far more important than distance from the curb, which is the term cities emphasize.
- A privacy-preserving, lidar-only curbside station can measure all of this from private property without touching the roadway. That makes it a reusable, cheap way for cities to audit any placement rule.

**Closest prior work (from search-result listings; pages not openable here) and what is new.**
1. Everett et al., "Curbside Collection of Yard Waste I: Estimating Route Time" and "II: Simulation and Application," J. Environ. Eng. 122(2), 1996 ([TRID I](https://trid.trb.org/View/458193), [ASCE II](https://ascelibrary.com/doi/abs/10.1061/%28ASCE%290733-9372%281996%29122%3A2%28115%29)). Route time from set-out rate, collection time per stop and travel time. Route time is nearly linear in set-out rate. *New:* time per cart as a function of *cart pose*, measured per cart, for automated arms (theirs predates widespread ASL arms).
2. "Modeling Municipal Solid Waste Collection Systems Using Derived Probability Distributions I," J. Environ. Eng. 2001 ([ASCE](https://ascelibrary.com/doi/10.1061/%28ASCE%290733-9372%282001%29127%3A11%281031%29)). Stop-time distributions for route models. *New:* conditioning those distributions on measurable pose covariates.
3. McNeilus CartSeeker product and acquisition news (links above). The vendor claims 96% success and 8% cost reduction but publishes no pose-versus-time data. *New:* public, per-cart field data and a tolerance curve.
4. Patents on automated container handling and camera/sensor-guided grabbers: US10358287B2 and US10974895B2 ([Google Patents](https://patents.google.com/patent/US10358287), [US10974895](https://patents.google.com/patent/US10974895)), and "Refuse collection vehicle controls" US11332307 ([USPTO pdf](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11332307)). These cover how to automate the grab, not how placement affects it in practice.
5. Municipal placement guidance (Cranbrook 3 ft spacing; Amarillo refusal policy; Sammamish sidewalk-blocking notice, [link](https://www.sammamish.us/news/please-be-a-good-neighbor-don-t-block-sidewalks)). Rules are stated without evidence. *New:* the evidence.
6. Unsure: there may be unpublished hauler time-and-motion studies or OEM telematics. The paper should say so and invite comparison. I found none in public search.

**Experiment design.**
- **Stations.** 3 curbside lidar stations, each on a consenting household's front yard (never in the roadway). Each has a Pi 5, an LD19 2D lidar about 40 cm above grade scanning the gutter and parking lane, and a battery. An optional low-resolution Pi camera is cropped to cart height and used only to label arm events; frames are deleted after labeling and no faces or plates are kept. Stations cover about 25–35 m of frontage (about 6–10 houses) and run 5 am–2 pm on collection day.
- **Sites.** Choose 3 sites with different haulers or cities if possible. Add a 4th station in Jan–Feb as the **held-out site**.
- **Natural (observational) arm.** Every cart in view is measured: footprint fit gives its pose relative to curb line and neighbours. Each of the 2–3 streams per day is a separate truck and pass, so about 3 sites × 12 collection days × ~2.5 streams × ~15 carts ≈ 1,300 cart events.
- **Designed arm.** Only the team's own carts and consenting neighbours' carts are placed at prescribed poses from a small fractional design:
  - distance 0.1 / 0.5 / 1.0 m from the curb face
  - yaw 0 / 30 / 60°
  - spacing to partner cart 0.2 / 0.6 / 1.2 m

  That is 9 runs per site in an L9 array, repeated across weeks, about 150 designed events in total. The worst case for residents is a missed pickup of their own cart, and they consent in advance.
- **Outcomes (continuous where possible).**
  - Per-cart handling time: lidar sees the cart footprint vanish and reappear.
  - Per-stop truck dwell time: large occluder present.
  - Number of arm approaches (labeled from short video, or lidar arm returns).
  - Post-dump pose change (Δposition, Δyaw).
  - Binary: tip-over, skipped cart, manual intervention. These are reported descriptively because they are rare.
- **Power.** Assume handling time mean about 10 s, SD about 3 s, and driver/truck random effects. A two-level contrast with SD 3 s needs n ≈ 2·(1.96+0.84)²·3²/Δ² per level. For Δ = 1 s that is about 141 per level, so the designed arm alone (about 50 events per level in the L9) can only detect Δ ≈ 1.7 s at α = 0.05 and power 0.8. That is adequate to catch a large threshold penalty (Result B) but not small effects, and it says nothing about interactions. The observational arm (n ≈ 1,300) carries the 1 s resolution and supports a smooth regression of handling time on pose (GAM) with driver/truck random intercepts.
- **Generalization.** There are only about 9 driver-truck combinations. The paper must state this as a limitation and test on the held-out 4th station.
- **Model.** Handling time ~ s(distance) + s(yaw) + s(spacing) + stream + (1 | truck-driver). From this, derive the "tolerance region" where the predicted penalty is under 0.5 s. Validate RMSE and the tolerance boundary on the held-out station.

**Strongest fair baseline.**
- Everett-style constant stop-time route models (placement-agnostic). Do pose covariates reduce held-out prediction error of per-stop time, and by how much?
- The cities' own rule as a binary classifier ("compliant / non-compliant") predicting penalty, compared against the fitted tolerance region.

**Measurements and analysis.** Per above. Cart footprint fit by RANSAC rectangle on the lidar scan, validated against tape-measured poses (target error under 3 cm, under 3°). Event segmentation is checked against video labels on a 10% subsample (report precision and recall). Release the anonymized event table and station code.

**Build list (≈ $760).** Verified-earlier prices from out/final.md; the rest are estimates.

| Item | Cost | Status |
|---|---|---|
| 3 × LD19-class 2D lidar | $297 | ~$99 each, verified earlier |
| 2 × Raspberry Pi 5 (4 GB) + SD (one Pi already owned) | $140 | est. |
| 3 × Pi Camera v3 (optional labeling) | $75 | est. |
| 3 × 20 Ah USB-C power banks / LiFePO4 packs | $120 | est. |
| 3 × weatherproof enclosures + tripods/stakes | $90 | est. |
| Tape, chalk, inclinometer app, calibration targets | $20 | est. |
| 4th station parts (reuse after site rotation) | $0 | — |
| **Total** | **≈ $742** | |

**Timeline.**
- Oct 15–31: recruit 3–4 host households (written consent and a neighbour notice letter). Confirm collection days and stream schedules. Write a one-page privacy statement (lidar-only data; video deleted after labeling).
- Nov 1–15: order parts. Write the lidar logger and cart-footprint fitter. Test on the team's own curb with carts in known poses.
- Nov 16–30: first station live on the home street. Fix event detection on the first 2 collection days.
- Dec 1–20: all 3 stations live.
- **Data by Dec 20:** about 3 collection days × 3 sites ≈ 300 cart events, first designed runs, and a first handling-time-versus-spacing plot.
- Dec 21–Jan 14: continue (collection runs through the holidays, possibly shifted). Complete L9 replicates.
- **Jan 15 go/no-go:** is per-cart handling-time noise (SD) under about 4 s, and is event detection above 90% precision and recall? If not, fall back to the descriptive tolerance and tip-over study.
- Jan 15–Feb 14: add the held-out 4th site. Data freeze Feb 14.
- Feb 15–26: modeling, write-up, CASE submission.

**Main risk and fallback.**
- **Risk 1: few driver-truck combinations limit generalization.** Fallback: report driver as a random effect and frame the result as a measurement method plus first data, with an open protocol cities can repeat.
- **Risk 2: pre-dawn darkness and parked cars occlude the view.** Mitigation: lidar is light-independent. Choose sites with driveway-dense frontage (fewer parked cars).
- **Risk 3: human-subjects concern** (drivers are part of the system). Mitigation: no identifiable data, outcome defined as machine cycle and cart pose. If any doubt remains, ask a host lab's IRB office for an exemption determination in October. That is a cheap ask, and it is a reason to involve a university lab.

**Best venue.** IEEE CASE 2027 (automation of a large-scale service process; a natural audience). Fallback: ICRA 2027 workshop on field or service robotics. A municipal or industry version could later go to *Waste Management*.

**Lab appeal.**
- **Best fit 1: UC Merced, Stefano Carpin.** CASE is his venue (CASE 2018 Best Paper), and his CASE 2025 work on stochastic orienteering (Zuzuárregui & Carpin, GNN-powered MCTS) needs *stochastic service-time models*. Per-cart handling-time distributions conditioned on pose are exactly such a model for a real routing problem. CV: [carpincvonline.pdf](https://sites.ucmerced.edu/files/scarpin/files/documents/carpincvonline.pdf).
  - *What the lab gains:* a real-world service-time dataset for routing and orienteering benchmarks and a CASE co-authorship at little cost.
- **Best fit 2: SJSU, Wencen Wu.** "Design and Implementation of a Small-scale Autonomous Vehicle for Autonomous Parking," IEEE CACRE 2021, which is a pose-tolerance docking problem, and her NSF cooperative-perception project on roadside sensing ([publications](https://sites.google.com/sjsu.edu/wencen/publications)).
  - *What the lab gains:* a roadside lidar-station deployment with labeled events for cooperative-perception students, plus a docking-tolerance analogue.

**Link to the bin robot.** Direct and strong: it produces the placement-accuracy spec the bin robot must meet. It also gives the robot a second value proposition (hauler-side time savings) beyond homeowner convenience.

**Honest self-score.**
- **Novelty 7.5.** I found no published pose-versus-service-time data for automated collection. It is a new, concrete empirical question with an obvious use.
- **Feasibility 6.5.** Only one collection day per site per week, household consent, and few drivers. Hardware risk is low, but data volume and generalization are the risks.
- **Impact 6.5.** Haulers, OEMs, cities and every cart-robot designer would use it. It is CASE main-track level, not IROS, and generalization from about 9 truck-driver pairs will draw criticism.
- **Overall about 6.8.**

---

## Idea D3: "Does the trash calendar predict where sidewalk robots get stuck?" Collection-day sidewalk obstruction across cities with different cart-placement rules, and schedule-aware costmaps

**Research question.** How much do collection-day carts reduce the effective clear width of residential sidewalks (and how much do they push into the street-side lane instead) under different city placement rules? Can a model built from the municipal collection calendar plus static GIS features predict segment-level blockage on held-out neighbourhoods well enough to improve a sidewalk robot's global plans?

**Who benefits and how much.**
- **City planners and solid-waste departments.** Rules differ ("in the street at the curb" versus "on the parkway strip" versus "at the driveway apron"). The trade-off between sidewalk blockage (ADA) and street or bike-lane blockage has never been measured. This would hand them a free policy lever with numbers.
- **Sidewalk delivery-robot operators** (Serve and Coco in LA, Starship): when and where to expect blockage, and whether to ingest public collection calendars. Accessibility incidents with robots have already pulled robots off sidewalks ([GovTech, Pittsburgh](https://www.govtech.com/products/Access-Concerns-Take-Robots-Off-Oakland-Pa-Sidewalks.html)), and operators are quietly collecting obstruction data themselves ([Next City](https://nextcity.org/urbanist-news/could-delivery-robots-help-pay-for-better-sidewalks)).
- **Wheelchair routing apps.** Project Sidewalk labels trash cans as "temporary obstacles" from Street View imagery, but has no notion of *when* they occur ([labeling guide](https://sidewalk-madison.cs.washington.edu/labelingGuide/obstacles)).

**Why the outcome is uncertain.** The direction ("carts block sidewalks on trash day") is predictable. The *magnitudes and their drivers* are not:
- **Result A:** compliance and parkway strips absorb most carts. Sidewalk blockage is rare and short (carts back within about 8 h), and the calendar adds little.
- **Result B:** blockage persists a day or more and depends more on the placement rule than on sidewalk width. A calendar prior then cuts robot reroutes substantially.
- Possibly **Result C:** "in-street" rules simply move the obstruction into bike or parking lanes, a policy trade-off with data on both sides.

Compliance is human behaviour at the population level, so theory cannot predict it.

**Non-obvious insight.** For residential sidewalk robots, the dominant time-varying obstacle may be *exogenously scheduled* and published by the city. A robot can then get a periodic map prior *for free*, without the weeks of self-observation that FreMEn-style or CoPA-Map-style spectral models need. Whether that free prior beats learning from observation on unseen streets is testable.

**Closest prior work (from search-result listings; pages not openable here) and what is new.**
1. Krajník et al., FreMEn (frequency map enhancement for long-term autonomy) ([CTU seminar page](https://robotics.fel.cvut.cz/cras/?p=154), [habilitation](https://dspace.cvut.cz/bitstream/handle/10467/75585/Habilitace_Krajn%C3%ADk_2018.pdf?sequence=1)). Periodic environment states learned from long robot observation. *New:* an external calendar prior, transfer to never-observed streets, and residential outdoor sidewalks.
2. Stuede & Schappler, CoPA-Map, spatio-temporal human activity with periodic priors from robot observations ([arXiv 2203.06911](https://arxiv.org/abs/2203.06911)). Indoor or campus, people not objects. *New:* scheduled objects, city-rule natural experiment.
3. "Long-term navigation for autonomous robots based on spatio-temporal map prediction," RAS 2024 ([ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0921889024001076)). Forecasts future maps on multiple time scales for global planning. *New:* exogenous calendar features and a held-out-neighbourhood test.
4. Project Sidewalk obstacle labels (link above) and Hara et al. CHI 2013 (link in kill table). Static, imagery-time snapshots. *New:* repeated, time-indexed physical clear-width measurements.
5. Sani, Sgorbissa & Carpin, ICRA 2024, Nav2 local-costmap plugin ([arXiv 2407.18535](https://arxiv.org/abs/2407.18535)). The plugin pattern this work would extend with a *temporal* prior layer.
6. Delivery-robot accessibility reporting ([Next City](https://nextcity.org/urbanist-news/could-delivery-robots-help-pay-for-better-sidewalks); [NJ Bike-Ped center](https://njbikeped.org/autonomous-delivery-robots-in-jersey-city/)). Problem statements without measured data.

**Experiment design.**
- **Rig.** A hand-pushed survey cart (or the team robot driven at walking pace): LD19 2D lidar at 40 cm plus wheel encoder plus phone GNSS. It gives a clear-width profile every 10 cm and detects street-side carts within about 5 m.
- **Sites.** 6 residential routes of about 1 km each, in 3 cities with different placement rules (2 routes per city, chosen for contrasting parkway presence). 4 routes are used for fitting; 2 are held out (one city entirely held out in a second split).
- **Schedule.** Each route is surveyed at 4 time points per collection cycle: evening before, collection morning, collection evening, and next afternoon. Plus one non-collection-day control. Run 4 cycles per route over Nov–Feb. That is about 6 × 4 × 5 = 120 surveys at about 25 min each, roughly 6 per week split across two students.
- **Unit.** 20 m segment-visit. 300 segments × 20 visits ≈ 6,000 segment-visits.
- **Outcomes.**
  - Continuous: minimum clear width per segment, and the fraction of length under 0.91 m (ADA 36") and under robot thresholds (0.7 m robot; 1.5 m robot-plus-wheelchair passing).
  - Street-side cart count and encroachment.
  - Persistence: hours until the segment returns to its baseline width.
- **Power.** The primary contrast is placement rule (3 levels) × collection phase. Segments are nested in routes, so the effective N for the rule effect is routes (6), which is weak. The design is therefore powered for the *within-route* collection-phase effect and the persistence curve (thousands of segment-visits; detects a 5 cm change in mean minimum width easily). The between-city rule effect is reported as an estimate with wide CIs: a natural experiment, not a confirmatory test. This limitation must be stated.
- **Robot evaluation.** On the recorded maps, replay a Nav2 global planner with (a) a static costmap, (b) static plus a learned-from-observation periodic layer (FreMEn-style, trained on the fitting routes' history), and (c) static plus a calendar-prior layer (no observation of the target route). Count blocked-path replans and detour length on the held-out routes.

**Strongest fair baseline.** FreMEn-style periodic models trained on as much history as the team has. This is the established method from the original authors' line, fairly tuned. Also a "static map plus reactive replanning" baseline, which is what Nav2 does by default.

**Measurements and analysis.** Mixed models of minimum width ~ phase × rule + parkway + sidewalk width + (1 | route/segment). Survival curves for cart persistence. Held-out AUC and Brier score for segment blockage, calendar model versus FreMEn versus static. Replan counts with bootstrap CIs. Release the dataset and a Nav2 "calendar layer" plugin.

**Build list (≈ $430).**

| Item | Cost | Status |
|---|---|---|
| LD19-class 2D lidar | $99 | verified earlier |
| Raspberry Pi 5 + SD (or reuse) | $80 | est. |
| Survey cart (garden cart or jogging-stroller frame) + mounts | $80 | est. |
| Wheel encoder + ESP32 Feather V2 | $35 | est. / $19.95 verified earlier for ESP32 |
| Battery + enclosure | $60 | est. |
| Phone GNSS (owned), tape and calibration targets | $15 | est. |
| Spare / second lidar for redundancy | $60 | est. |
| **Total** | **≈ $430** | |

**Timeline.**
- Oct 15–31: choose 3 cities and their rules (from city websites), 6 routes, and collection calendars.
- Nov 1–20: build the cart. Validate clear-width accuracy against tape (target ±3 cm).
- Nov 21–Dec 20: 2 cycles on 4 routes.
- **Data by Dec 20:** about 32 surveys, a first persistence curve, and the first rule contrast.
- Dec 21–Jan 14: cycles 3–4 and the 2 held-out routes.
- **Jan 15 go/no-go:** is blockage frequent enough (≥5% of segment-visits under 0.91 m on collection day)? If not, the headline becomes "Result A: rules work" plus street-side encroachment.
- Jan 15–Feb 7: build the Nav2 replay and calendar layer.
- Feb 14: freeze. Feb 26: submit.

**Main risk and fallback.**
- **Risk:** blockage is rare (Result A) and the robot-planning gain is small, which leaves a measurement-only paper.
- **Fallback:** pivot to the policy trade-off (sidewalk versus street encroachment by rule), which stays informative for cities. Submit to an ICRA 2027 workshop or a TRB-type venue.
- **Secondary risk:** few routes per rule. Mitigation: present the rule effect as estimation, not a test.

**Best venue.** IROS 2027 (long-term autonomy / social navigation track) or CASE 2027. Realistically strongest as an ICRA 2027 workshop paper plus dataset if the planning gain is modest.

**Lab appeal.**
- **Best fit 1: UCSC ASL, Gabriel Elkaim.** Pi + ROS 2 + Nav2 differential-drive robots and the lab's open-source low-cost-autonomy aim. SIP 2026 CSE-11, "Embedded AI and Navigation on a Differential-Drive Robot using Raspberry Pi, ROS 2, and Docker" ([SIP 2026](https://sip.ucsc.edu/2026-research-projects/); [ASL](https://asl.soe.ucsc.edu/home)).
  - *What the lab gains:* a Nav2 temporal-prior costmap plugin and a real outdoor sidewalk dataset its SIP interns can run on their Pi robots next summer. Low effort, reusable.
- **Best fit 2: UC Merced, Carpin.** The ICRA 2024 Nav2 costmap-plugin paper (above): a direct methodological sibling (semantic correction of the costmap, extended to temporal correction).

**Link to the bin robot.** It tells the bin robot where to leave the cart (street versus parkway) to minimize sidewalk blockage. The robot itself is also a temporary sidewalk obstacle on collection day.

**Honest self-score.**
- **Novelty 6.** The measurement is new, and calendar-as-prior is a neat twist. But "trash cans block sidewalks" is predictable in direction, and periodic map models exist.
- **Feasibility 8.** Simple hand-pushed rig and public sidewalks. No permissions beyond public right-of-way, and data come quickly.
- **Impact 6.** Useful to planners, accessibility apps and delivery operators. The robotics contribution is thin unless the calendar prior clearly beats FreMEn on unseen streets.
- **Overall about 6.7.**

---

## Ranking summary

| Rank | Idea | N / F / I | Overall |
|---|---|---|---|
| 1 | D1: Dew or dirt? Time-varying small-robot traction on lawns | 7 / 7.5 / 7 | 7.2 |
| 2 | D2: How precise must a curbside cart be? Pose versus automated side-loader service | 7.5 / 6.5 / 6.5 | 6.8 |
| 3 | D3: Does the trash calendar predict sidewalk blockage? | 6 / 8 / 6 | 6.7 |

D2 and D3 can share collection-day field days and hardware. D1 shares the drive base and load cell with the bin robot. A two-idea portfolio of D1 (IROS) plus D2 (CASE) fits the $1,000 budget only if lidars and Pi boards are shared. I estimate about $1,050 combined, so it would need one fewer D2 station.
