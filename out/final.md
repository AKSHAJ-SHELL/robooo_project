# Final recommendation: research angles for a low-cost bin-to-curb robot

Date: 2026-10-04. Inputs: [venues.md](venues.md), [labs.md](labs.md), [prior_art.md](prior_art.md), [rounds.md](rounds.md), [angles/](angles/).

## Bottom line (read this first)

- **No angle reached the 8.5 survival threshold. None reached the 7.5 revision threshold either.** Five angles were reviewed, each by 5 adversarial reviewers. Every one scored between **5.33 and 5.83** (median overall). Under the rules, nothing was eligible for revision, so the process stopped after round 1. The scores were not adjusted.
- Per your rule, here are the **top 3 by score anyway**:

| Rank | Angle | Median overall | Novelty / Feasibility / Impact (medians) |
|---|---|---|---|
| 1 | **B1: Passive self-centering hitch: how much sensing does mechanism make unnecessary?** | **5.83** | 6 / 5.5 / 6 |
| 2 (tie) | **B2: "Borrowed weight": hitch height as a free traction source** | **5.67** | 5 / 6.5 / 5.5 |
| 2 (tie) | **A4: Curb-edge detection sensor price sweep ($5 to $269)** | **5.67** | 6 / 6 / 5.5 |
| 4 | A1: Is RTK worth it on a driveway? | 5.33 | 5 / 5.5 / 5.5 |
| 5 | C1: Five-stack cost-reliability frontier | 5.33 | 6 / 4 / 5.5 |

- **Why everything landed around 5.5.** The 25 reviews agree on three points:
  1. **The task itself is not new.** University senior-design projects (UCF SPARC 2018, UCF GRAD 2020, FAMU-FSU 2019) have built bin-to-curb robots. So has a 2019 NZ high-school prize winner (Wheelie Drive), and patents date back to 1991. A 2026 paper (Hamzeh & Prasetyo) reports 80 trials of a bin robot. The contribution has to be a measured result that is *not predictable in advance*. "Funnel beats hook" and "statics predicts weight transfer" were judged predictable.
  2. **The experiment plans were underpowered or bloated.** Typical problems were n=25 per arm with equivalence tests that cannot pass, and condition grids of about 1,200 cells.
  3. **Impact ceiling.** For a first paper from a high-school team, reviewers saw these as CASE or workshop level, not IROS main track.
- **What would raise the scores.** Reviewers independently gave the same fixes (below). Those fixes were **not re-scored**, because the rules allowed revision only at ≥7.5. Treat the fixed versions as promising but unvalidated.
- **Coverage caveats.**
  - Only 5 of the 18 generated angles were reviewed. You cut the protocol to 5 angles × 5 reviewers × 5 rounds, and I chose which 5. The other 13 are unscored, in [angles/all_18_angles.md](angles/all_18_angles.md).
  - Web-search rate limits hit the research and generation agents. Several novelty checks by the generators used OpenAlex and Crossref, not Google Scholar or IEEE Xplore. The reviewers did search, capped at about 15 searches each.

---

## 1. B1: Passive self-centering hitch (median 5.83)

Full text: [angles/B1.v1.md](angles/B1.v1.md). Reviews: [rounds.md § B1.v1](rounds.md).

**Question (as generated).** The robot engages an unmodified 64/96-gal cart by its molded handle. What is the region of approach error (lateral, yaw, speed) within which a ~$20 passive self-centering hitch latches with ≥90% probability, compared with a rigid hook? How many dollars of docking sensing does that tolerance make unnecessary?

**What the reviewers objected to.** "Funnel beats bare rigid U-hook" is predictable from compliance and chamfer theory ([Whitney 1982](https://doi.org/10.1115/1.3149634)). The rigid hook, modeled on the abandoned [US20200023524A1](https://patents.google.com/patent/US20200023524A1/en), is a straw man. The ~1,400-trial grid is too big.

**Recommended experiment design** (reviewer-consensus fix, not re-scored):
- **Turn it into a design law.** Make the contribution a **design law plus validation** rather than a head-to-head.
- **Variables.** Vary V-guide convergence angle (30/45/60°) and mouth width. Include a *fair* rigid baseline: a chamfered or flared hook like the $64.99 [Garbage Commander](https://gemplers.com/products/single-can-garbage-can-hauling-hook-for-lawn-tractor-or-atv), at 2–3 clearance widths.
- **Model.** Derive a simple quasi-static "does the cart center or slide away?" condition from guide angle, friction and cart mass/fill. Fit the measured capture half-width against it.
- **Cost link.**
  - Measure terminal docking-error distributions for three cheap approach setups: odometry only; odometry plus a ~$5 ultrasonic; odometry plus an LD19-class lidar at ~$99.
  - Predict end-to-end success by combining each error distribution with the measured capture envelopes.
  - Validate with ~50 autonomous engagements using the cheapest setup.
- **Smaller grid.** Screen coarsely, then concentrate trials at the capture boundary.

**Baseline.** A chamfered rigid hook (fair version) on the same robot. The sensing-heavy published alternative: [Xiao et al., ICRA 2022](https://arxiv.org/abs/2110.06648) reach 3 cm / 0.02 rad docking using LiDAR.

**Measurements.**
- Latch success (limit switch).
- Post-latch centering error (chalk grid plus overhead photo).
- Whether the cart gets shoved more than 10 cm.
- Peak engagement force (load cell).
- Logistic-regression 90% capture contours with bootstrap CIs.
- Sensing dollars needed for 95% engagement.

**Build list (~$620, from the angle's breakdown; items marked "est." are estimates):**
- Gotrax hoverboard base, $139
- ESP32 Feather V2, $19.95
- Frame, caster and wiring, ~$100 (est.)
- PETG hitch heads, springs and bearings, ~$85 (est.)
- SparkFun 200 kg load cell plus HX711, $101.90
- Sandbags, ~$30 (est.)
- Jig and chalk grid, ~$40 (est.)
- Ultrasonic, ~$5
- LD19-class lidar, ~$99
- Carts are borrowed, not bought.

**Main risk.** Handle and rear-wall geometry may vary by brand, and light empty carts (28–37 lb) may get shoved instead of centered. Either would make the envelope small or brand-specific. Fallback: report per-brand envelopes and approach more slowly.

---

## 2 (tie). B2: "Borrowed weight": hitch height as traction (median 5.67)

Full text: [angles/B2.v1.md](angles/B2.v1.md).

**Question (as generated).** For a light (12–15 kg) hoverboard robot towing a cart by its handle, how does hitch height control the vertical load transferred to the drive wheels? How does that change the drawbar pull before slip and the success of uphill starts? Which height maximizes traction margin without ballast?

**What the reviewers objected to.** A lever-arm moment balance plus Coulomb friction is textbook tractor and hand-truck mechanics ([Persson & Johansson 1967](https://doi.org/10.13031/2013.39801)). The commercial Garbage Commander already advertises ~30% weight transfer. The hoverboard may hit its current limit before the wheels slip. Vertical hitch load was measured only statically.

**Recommended experiment design** (reviewer-consensus fix, not re-scored):
- **The headline.** Make it a **sizing rule**: the minimum robot mass and motor current for 95% start success, as a function of hitch height *and fore-aft hitch position relative to the drive axle*.
- **Non-obvious limits.** Include the limits statics alone doesn't predict: robot pitch-over, caster unloading and cart jackknife.
- **Dynamic loads.** Measure vertical and horizontal hitch force *during* pulls, not just at rest.
- **Stall test first.** Run a bench stall-current test in Oct–Nov. If slip can't be reached, frame the paper as "motor-limited vs traction-limited sizing".

**Baseline.**
- The same robot with a high, non-transferring hitch plus sandbag ballast, measured directly.
- The carry-everything design of [FAMU-FSU Team 311](https://eng-web1.eng.famu.fsu.edu/me/senior_design/2019/team311/) ($1,980.85 BOM).

**Measurements.**
- Static load transfer: 6 heights × 2 cart sizes × 4 fills.
- Drawbar pull at slip on dry concrete, wet concrete and asphalt.
- Uphill-start success on 0–15% ramps plus real driveways.
- Energy per trip (Wh).
- Fitted μ per surface with CIs.

**Build list (~$790):**
- Hoverboard base with EFeru FOC firmware, ~$260 (check that the mainboard is supported before buying)
- Adjustable mast and hook, ~$90 (est.)
- Load cell plus HX711, $101.90
- Plywood ramp, ~$180 (est.)
- Sandbags, ~$55 (est.)
- Two bathroom scales, ~$40 (est.)
- Anchor, strap and chocks, ~$30 (est.)

**Main risk.** The motor current limit (EFeru default 15 A per motor) could mask the traction limit.

---

## 2 (tie). A4: Curb-edge detection price sweep (median 5.67)

Full text: [angles/A4.v1.md](angles/A4.v1.md).

**Question (as generated).** For a 20–40 cm-tall robot approaching the curb head-on, how do these sensors compare on the *same curbs*? Metrics are detection rate, false stops and stop-distance error, across curb type, lighting and wetness.
- $5 ultrasonic
- $20 VL53L5CX 8×8 ToF
- $25 camera
- ~$99 2D lidar
- $269 OAK-D Lite stereo

**What the reviewers objected to.**
- **Wrong target.** A driveway usually meets the street at a *curb cut or rolled lip*, not a vertical curb, and many cities specify where carts go.
- **Weak reference sensor.** The OAK-D Lite is passive stereo, so it is a weak "gold standard" at night.
- **Matrix too thin.** About 300 approaches spread over about 1,200 condition cells leaves most cells nearly empty.

**Recommended experiment design** (reviewer-consensus fix, not re-scored):
- **Real target.** Re-anchor to the actual placement target: driveway-apron and curb-cut edges plus one vertical curb. Take the placement rule from named California city cart-placement instructions.
- **Fewer sensors.** Compare 3–4 configurations, each priced as a full system with compute.
- **Fewer conditions.** Use two lighting levels (sun, night) and 3 edge types, with ≥30 approaches per cell.
- **Hand rig first.** Collect most data on a **hand-pushed rig** at robot height. This is robot-independent, removes risk, and can start in November.

**Baseline.** The depth camera on the same curbs. Published numbers:
- [Rhee & Seo 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6470551/): ultrasonic on a car parallel to the curb.
- [Sivakanthan et al. 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8659845/): D455 on a wheelchair at an indoor mock curb.

**Measurements.**
- Detection rate (Wilson CIs).
- First-detection range.
- Stop-distance error (cm).
- False stops per 10 m.
- Cost-vs-performance curve.

**Build list (~$877, of which ~$230 is the shared robot base):**
- HC-SR04 ×2, $10.50
- VL53L5CX ×2, $39.90
- Pi Camera 3, from $25
- 2D lidar, ~$99
- OAK-D Lite, $269
- Pi 5 4GB, $110
- Waterproof ultrasonics, ~$24 (est.)
- Hand rig and mounts, ~$40 (est.)

**Main risk.** Rolled curbs and curb-cut lips (1–3 cm) give a very weak signal, so the cheapest sensors may fail exactly the case that matters. Reviewers consider an honest "cheap sensors work for vertical curbs but not rolled curbs" still publishable.

---

## Best venue and deadline

From [venues.md](venues.md), with links verified:

- **Primary for B1 / B2 (mechanism, cost-effectiveness): IEEE CASE 2027, regular papers due Mon Mar 1, 2027.** The deadline is confirmed on the official site, and the format is 6 pages plus 2 paid. The generators and reviewers both saw these as automation and cost-effectiveness engineering studies, which fits CASE better than IROS. CASE requires a full (non-student) registration for an accepted paper. Fallback: the CASE WIP track (4 pages, due Apr 1, not in Xplore).
- **Alternative: IROS 2027 (Florence), Mon Mar 1, 2027, 23:59 PT, 8 pages including references.** venues.md recommends it for its sustainability/recycling theme and cheaper student registration. Reviewers rated these angles below IROS main-track level, though. Decide at the **Jan 15, 2027** checkpoint based on pilot data, and do not submit to both.
- **A4:** CASE (same deadline), or an **ICRA 2027 workshop paper**. ICRA 2027 is in Seoul; workshops are announced Jan 31, 2027, with likely mid-March to late-April deadlines.
- **Too late or out of scope** for a March 1–2 plan: AIM (moved to Jan 26), ARSO (Dec 1, 2026), SoutheastCon (Dec 30–31, 2026), RoboSoft (out of scope; extended abstracts due Jan 15). ARSO 2027 is in **Mountain View, Mar 13–15**, which is worth attending to meet the California labs in person.
- **Internal milestones** (from venues.md):
  - Order long-lead parts by mid-Nov.
  - First data by Dec 20.
  - Go/no-go on Jan 15.
  - Data freeze on Feb 14.
  - Submit Fri Feb 26.

## Labs to approach and what to show them

From [labs.md](labs.md). Every high-school research program verified there runs in **summer 2027**, after the deadline. Before March, realistically ask for **feedback on the evaluation design**, not a position.

| Lab | Why | Pitch with | Show them |
|---|---|---|---|
| **UC Santa Cruz Autonomous Systems Lab (Gabriel Elkaim)**, fit 9 | Mentored high-school projects through UCSC's Scholar Immersion Program in 2024–2026. The 2026 project was a Pi + ROS 2 differential-drive robot, close to your stack. | Any angle | Apply to the program (portal Jan 15 – Feb 26, 2027) plus a short note with a demo video. |
| **Santa Clara Robotic Systems Lab (Christopher Kitts)**, fit 7.5 | Low-cost field rovers; undergraduate-staffed lab that invites contact and visits | B1 / B2 | 60-second video of the hitch latching from offset approaches, plus the capture-envelope or traction plot |
| **SJSU (Winncy Du)**, sensors and mechatronics | Natural fit for the mechanical student | B1 / B2 / A4 | The hitch mechanism and the load-cell rig; the sensor bar for A4 |
| **UC Merced Robotics Lab (Stefano Carpin)**, fit 7.5 | Outdoor ROS 2 Nav2; publishes at CASE and was a CASE Best Paper winner | A4, or the evaluation design of any angle | The cost-vs-performance table; one concrete question about the experimental design for a CASE paper |
| **UCLA LEMUR (Ankur Mehta)**, fit 7.5 | "Towards One-Dollar Robots" matches the cost thesis | B1 (mechanism replacing sensing) | Follow the lab's join-page format; frame the request as asking for feedback, not asking to join |
| **SJSU (Wencen Wu)**, fit 7 | Paper on a small autonomous parking vehicle; K-12 outreach | A4 | Curb-stop accuracy results |

What every lab will want: a working demo video, a measured plot (not a plan), a one-page summary with the research question, the baseline and the cost table, and evidence you'll finish.

## Do the top 3 combine into one paper?

**B1 + B2: yes. Combining them is the strongest option.**
- **Same robot and hitch.** Both run on the same hoverboard robot with the same handle hitch and the same load cell.
- **One story.** *"A ~$20 passive hitch that does the work of sensors and ballast."* The hitch geometry sets both the capture tolerance (fewer dollars of sensing) and the weight transfer (no ballast, smaller motors).
- **Shared design variables.** Mouth and convergence angle drive capture; height and fore-aft position drive traction.
- **Size and venue.** It is one build of about $700–800, and one coherent CASE paper.
- **Scope.** Cut each half's matrix to what the reviewers called the non-obvious part: the B1 design law and the B2 limits that statics misses.

**Adding A4: no.** It needs a separate sensor bar and different experiments, so three studies in 12 weeks would repeat C1's mistake. C1 scored the lowest feasibility (4/10) for exactly that "do everything" scope. Run A4 as a separate hand-rig study, either as a follow-on ICRA-workshop paper or as a short perception section if B1+B2 finish early.

**Honest expectation.** Even combined and fixed, the reviewers' evidence points to a solid CASE or workshop paper and a strong college-application story, not a likely IROS main-track acceptance. The fixes have not been re-scored. If you want a number, the next step is one more review round on a revised B1+B2 angle; that would go beyond your 7.5 rule, so it's your call.

## Main risks (overall)

1. **Predictability.** Reviewers' top objection was that results are foreseeable. Frame every hypothesis so it could come out the other way, and put the design law or model at the center.
2. **Statistical power.** Size trials with a power analysis; prefer continuous metrics (cm, degrees, N) over pass/fail.
3. **Hardware risk.** Check that the hoverboard mainboard is supported by EFeru firmware, and that motor current limits won't mask the traction limit, before buying.
4. **Weather and timeline.** January–February rain in California; the data freeze is Feb 14.
5. **Safety.** A full 96-gal cart is about 169 kg. Belay slope tests, use an e-stop, and never enter the roadway.
