# gen_H: custom hardware and PCBs that improve low-cost robots

Generator H, written 2026-10-04. Area: open motor drivers and actuators, low-cost tactile and force sensing, encoder and IMU boards, grippers, power boards.

**Source labels used below.**
- **[code]**: I cloned the repo and read the file myself in this session.
- **[snippet]**: web-search result text only. The sandbox blocks arxiv.org, semanticscholar, themoonlight, ar5iv and most lab sites, so I could not open these papers. Re-check before citing.
- **[memory]**: a well-known paper I did not re-open this session. Verify it.
- **[est]**: a price I estimated. **[verified]**: a price taken from a search snippet with a named vendor.

---

## 0. Candidates generated and why most were killed

| # | Candidate | Verdict | Killing evidence |
|---|---|---|---|
| K1 | Add reference or differential magnetometers to AnySkin/ReSkin to cancel stray fields | **Killed (done)** | OSMO glove (arXiv 2512.08920, Dec 2025) [snippet] already uses a pair of BMM350 magnetometers per taxel plus MuMetal shielding. That cut RMS noise 57% vs. one unshielded magnetometer, tested against hand-motor and neighbour-taxel interference. |
| K2 | SimpleFOC/QDD gripper with force control for the SO-101 arm | **Killed** | Constant-force CF35-12 servo grippers are already sold for SO-ARM101 [snippet, Waveshare/Spotpear listing]. Sensorless force estimation on low-cost arms is published: Yamane et al. arXiv 2507.06174 [snippet] and input-gated bilateral teleop arXiv 2509.08226 [snippet]. |
| K3 | Magnetic-encoder retrofit for hoverboard hub motors (better low-speed FOC and odometry) | **Killed (community-done, low novelty)** | ODrive forum threads already document AS5047P retrofits on hoverboard motors [snippet, discourse.odriverobotics.com "Hoverboard + encoder" and "HoverArm"]. The EFeru FOC README already explains the 4° Hall resolution and interpolation [snippet]. |
| K4 | Output-side encoder plus backlash compensation for Berkeley Humanoid Lite's printed cycloidal actuator | **Killed** | Dual-encoder backlash measurement is standard. Backlash randomization for sim-to-real is common (arXiv 2504.00614 and others) [snippet]. Building a BHL leg costs more than the budget. The documented limitation is real, though: a 60 h endurance test showed gradually growing backlash [snippet, arXiv 2504.17249]. |
| K5 | Joint-angle Hall sensors for the RUKA tendon hand (it has no joint encoders) | **Killed (done)** | RUKA-v2 (arXiv 2603.26660, Mar 2026) [snippet] adds attachable magnetic joint encoders. |
| K6 | Thermal-drift compensation for AnySkin. The firmware disables the MLX90393's on-chip temperature compensation and the Python library throws away the temperature channel [code] | **Killed as a standalone idea (predictable)** | MLX90393-based skins already use the chip's built-in temperature sensor for compensation (Tomo et al., Sensors 16(4):491, 2016) [snippet]. Melexis has an app note on it [snippet]. Kept only as a side measurement in H1. |
| K7 | Printable magnetic 6-axis wrist F/T sensor for the SO-101 | **Killed (crowded)** | ShapeForce soft wrist (arXiv 2511.19955) [snippet]. Ouyang & Howe fiducial F/T (arXiv 2005.14250) [snippet]. TAMS 3D-printed F/T for under $20 (github.com/TAMS-Group/tams_printed_ft) [snippet]. |
| H1 | **Ferrous-object-immune magnetic skin: one-sided (Halbach) magnet layouts and a ferrite "pre-mirror" in eFlesh** | **Kept: best** | See below |
| H2 | **Electronics or elastomer: which limits slip sensing in open magnetic skins? A kHz analog-Hall board for eFlesh/AnySkin** | **Kept** | See below |
| H3 | **Smart Suction Cup on a hobby diaphragm pump: using the pump's own pulsation as a lock-in probe for seal sensing** | **Kept (weakest of the three)** | See below |

---

## H1. Making open magnetic skins work on steel: one-sided (Halbach) magnet layouts and a ferrite pre-mirror for eFlesh

### Base project and the specific limitation
- **Base:** eFlesh (NYU; Pattabiraman, Huang, Panozzo, Zorin, Pinto, Bhirangi). The sensor is a 3D-printed TPU cut-cell lattice with off-the-shelf N52 magnets, read by the 5-chip MLX90393 ReSkin/AnySkin board. Repo: https://github.com/notvenky/eFlesh (MIT) [code]. Paper: arXiv 2506.09994 [snippet].
- **Also:** AnySkin, https://github.com/raunaqbhirangi/anyskin (MIT) [code], arXiv 2409.08276 [snippet]. ReSkin board, https://github.com/raunaqbhirangi/reskin_sensor (MIT). The board is released only as 2021 Gerbers/pick-and-place in `circuits/5X_ReSkin.Zip`, with no editable source [code].
- **Limitation, with evidence:**
  - AnySkin paper: the primary limitation it inherits from ReSkin is "interference from magnetic and ferromagnetic objects in the environment" [snippet, arXiv 2409.08276].
  - eFlesh paper: this class of sensors "suffers from two main drawbacks: magnetic interference and expensive fabrication" [snippet, arXiv 2506.09994]. Its fix is alternating magnet polarities, which "cancels the dominant far-field components" and cuts stray-field intensity and cross-sensor crosstalk by about 100× [snippet]. That fix targets the field the skin *emits* and the crosstalk between sensors. It does not target a high-permeability object *touching* the skin.
  - A Dec 2025 magnetic-tactile gripper paper (arXiv 2512.00907) explicitly recommends against directly grasping high-permeability objects and suggests ≥10 mm clearance [snippet]. That is a usage restriction, not a fix.
  - Released code [code]: neither the AnySkin nor the eFlesh firmware or library has any compensation path. AnySkin's README tells users to press "B" to re-zero when drift appears.
- **Why it matters downstream:** steel is everywhere in household and industrial manipulation: cans, tools, screws, keys, shelving, sinks. A tactile fingertip that produces phantom force near steel cannot be used for force-limited grasping or slip detection on those objects.

### Research question
Can a one-sided magnet arrangement (Halbach) or a flexible ferrite outer layer make a printed magnetic skin's force estimate and slip detection immune to ferrous contact objects, without losing the deformation sensitivity of the original eFlesh design?

### Why the outcome is uncertain (both results publishable)
- **Result A (fix works):**
  - A discrete 4-orientation Halbach array of cube magnets puts its weak side toward the contact surface. A steel object then sees roughly 3 to 10× less field, so it induces a proportionally smaller perturbation at the magnetometers.
  - Force RMSE on steel falls to near the plastic-object level, and steel-can grasps become as reliable as plastic ones.
- **Result B (fix fails or trades off):**
  - Finite-length discrete arrays leak at the ends.
  - Lattice deformation rotates the magnets and breaks the cancellation, so the sensitivity gained by one-sidedness is lost.
  - Thin sheet steel saturates near N52 magnets, so the simple image model fails.
  - The ferrite layer might stiffen the skin, or might itself dominate the signal.
  - A clean negative result with a magnet-level explanation is a useful design rule for every magnetic-skin user (ReSkin, AnySkin, eFlesh, OSMO, uSkin-class).
- **A third possible outcome:** the ferrite pre-mirror raises sensitivity (the image moves 2× the skin displacement) while also shielding. That would be a surprising positive result.

### The non-obvious insight
- A high-permeability object touching the skin acts roughly like a **magnetic mirror**. Its effect on the magnetometers is approximately the field of the skin's *mirror-image magnet array*, seen from a distance of 2 × skin thickness + gap.
- So the perturbation scales with the field the skin projects **toward the object**, not toward the sensor. Far-field cancellation (eFlesh's alternating poles) and common-mode subtraction (OSMO) reduce the wrong quantity.
- A **one-sided (Halbach) layout** reduces exactly this quantity, because its strong side faces the magnetometers and its weak side faces the object.
- The second fix inverts the problem. A **flexible ferrite sheet** (the cheap NFC kind) bonded to the outer surface supplies the mirror permanently, so an external steel object adds little that is new. The sheet moves with the skin, so it may *add* signal.
- These are hypotheses to test with magpylib (method-of-images approximation) before printing, then on hardware. The mirror argument is my own reasoning; I have not seen it written up for tactile skins.

### Open-source reuse vs. what the team builds

| Component | Link | License | What it saves |
|---|---|---|---|
| eFlesh lattice generator and CAD pipeline, slip-detection code + dataset, firmware | https://github.com/notvenky/eFlesh [code] | MIT | The entire sensor body design, characterization scripts, a slip-detection LSTM and dataset (`slip_detection/data/seq_*.pt`) [code] |
| AnySkin Python library and firmware | https://github.com/raunaqbhirangi/anyskin [code] | MIT | Serial streaming, visualizer, baseline firmware |
| ReSkin 5X magnetometer board (Gerbers + BOM) | https://github.com/raunaqbhirangi/reskin_sensor [code] | MIT | A known-good board to order in week 1 as the baseline |
| MLX90393 Arduino library (burst-mode fork) | https://github.com/tesshellebrekers/arduino-MLX90393 [code] | (per repo; verify) | Driver |
| Magpylib (analytic magnet-field simulation) | https://github.com/magpylib/magpylib | BSD-2 [memory; verify] | Fast field simulation of aligned, alternating and Halbach layouts, and of mirror images |
| LeRobot + SO-101 arm | https://github.com/huggingface/lerobot | Apache-2.0 [memory; verify] | Arm control, teleop and data logging for the downstream task |

**Team builds:**
1. A KiCad re-draw of the 5X board, because there is no editable source. Variant A is a ReSkin clone. Variant B adds a back-side 5-chip layer for an OSMO-style differential reference. **PCB spin 1** goes to JLCPCB PCBA mid-Nov: about 1 week fab + 1 week shipping. MLX90393 is stocked at LCSC [snippet].
2. Printed eFlesh variants: aligned (original), alternating (eFlesh's best), 4-orientation Halbach with 3 mm cube magnets, and alternating + 0.1–0.2 mm ferrite sheet.
3. A 3D-printer-based indentation rig: an old FDM printer moves the probe, and a load cell under the sensor gives ground truth. Steel and PLA indenters have identical geometry.
4. An instrumented test object (load cell inside) for grasp-force ground truth.
5. **PCB spin 2** (early Jan) for fixes, or a gripper-fingertip form factor.

### Closest prior work and what is new
1. **eFlesh** (arXiv 2506.09994) [snippet]: alternating polarity for far-field and crosstalk. *New here:* contact with ferrous *objects*, and one-sided layouts.
2. **AnySkin** (arXiv 2409.08276) [snippet]: names the limitation, no fix.
3. **OSMO glove** (arXiv 2512.08920) [snippet]: dual-magnetometer differential plus MuMetal against motor and neighbour noise. *New:* near-field ferrous contact, which common-mode subtraction should not cancel. Included as a baseline variant.
4. **Yan et al., Halbach soft magnetic skin, Nature Machine Intelligence 2024** (HAL lirmm-04825067) [snippet]: uses the Halbach "self-decoupling" property to separate normal and shear force. *New:* Halbach used for **immunity to external ferrous objects**, made with discrete magnets in printed lattices, plus a downstream grasp task.
5. **Numerical investigation of Halbach-array flexible magnetic sensors** (PMC12693847, 2025) [snippet]: simulation only, about range and sensitivity.
6. **Lim et al., MRE-layer soft tactile sensor, Adv. Intell. Syst. 2025** (doi 10.1002/aisy.202400275) [snippet]: an iron-filled elastomer layer with fixed magnets, for high load. *New:* a ferrite layer used as a deliberate shield/mirror against external objects.
7. **Magnetic tactile-driven soft actuator** (arXiv 2512.00907) [snippet]: quantifies ferrite interference (up to 0.4 G at contact) and recommends ≥10 mm clearance. That is evidence the problem is open.
8. **GhostTac** (arXiv 2608.20817) [snippet]: EMI attacks on tactile sensors. This is adjacent (adversarial electronics), not passive ferrous objects.
9. **Yan et al., soft magnetic skin with sinusoidal magnetization, Science Robotics 2021** [memory]: related magnetization patterning.

### Experiment design (original eFlesh as baseline)
- **Factors:** skin variant ∈ {aligned (original eFlesh), alternating (eFlesh best), Halbach, alternating + ferrite}. That is 4 variants on the same board. Board variant B (differential) is a secondary arm on the best two skins only.
- **Bench study (primary, continuous):**
  - Indenters: 8 mm hemispherical tips in steel (1018 or bearing ball) and in PLA/aluminium. Aluminium controls for conductivity and eddy effects; it is non-ferrous.
  - Protocol: 25 grid locations × 5 depths × 3 repeats, per indenter, per skin.
  - Train the force regressor (eFlesh's own MLP pipeline in `characterization/` [code]) on **PLA data only**, then test on steel.
  - **Primary metric:** steel-induced force error, ΔRMSE = RMSE_steel − RMSE_PLA (N).
  - **Secondary metrics:** phantom force at 0, 2, 5 and 10 mm *non-contact* approach of a steel block; PLA-only sensitivity (counts/N) and resolution, to check that the fix does not cost sensitivity.
- **Downstream study (SO-101 with eFlesh fingertips):**
  - **Task 1, force-limited grasp:** close until the estimated force reaches 3 N, on geometry-matched cylinders in steel, aluminium and PLA. Ground truth comes from the load cell inside the object. Metric: absolute force error at stop, and premature stops caused by phantom force.
  - **Task 2, slip detection:** using eFlesh's released LSTM slip detector [code], retrained per skin on PLA objects. Lift objects with an added mass until slip. Metrics: detection latency (ms) against high-speed phone video, and false-positive rate on steel.
- **Sample size:**
  - Bench: the paired design (same location and depth, steel vs. PLA) gives 75 paired points per variant. To detect a 0.15 N difference in ΔRMSE between variants with SD of paired differences ≈ 0.3 N needs d = 0.5 → n ≈ 34 pairs for 80% power at α = 0.05. 75 is comfortable, and a bootstrap over locations handles clustering.
  - Downstream Task 1: to detect a 0.5 N difference in stop-force error between the original and the best fix, with SD ≈ 0.7 N (my assumption; measure in the pilot), needs n ≈ 32 per condition (two-sample) → **30–35 grasps per skin × object**. Restricted to 2 skins (original vs. best) × 3 objects ≈ 200 grasps, roughly 3–4 h of robot time.
  - Task 2: 40 slip trials per skin × object class.

### Measurements and analysis
- **Field model check:** magpylib prediction vs. measured stray field at 1, 3 and 5 mm above each skin (cheap Hall probe). Report the one-sidedness ratio.
- **Inference:** mixed-effects model for ΔRMSE (skin variant fixed; location random). Holm correction over 3 pairwise contrasts vs. the original. Bootstrap 95% CIs for slip latency.
- **Side measurement (absorbs K6):** baseline drift over a 30-min run next to the SO-101 gripper servo, with on-chip temperature compensation off and on. This shows whether the fix interacts with drift.

### Build list (≤ $1,000)

| Item | Cost | Status |
|---|---|---|
| MLX90393 ×30 (two board variants, spares) | ~$64 ($2.13 ea, Digikey qty 1) | [verified snippet] |
| JLCPCB PCB + PCBA, 2 spins | ~$120 | [est] |
| QT Py SAMD21 / RP2040 ×3 + Qwiic cables | ~$45 | [est] |
| N52 magnets: 3 mm cubes ×200, eFlesh-size discs ×50 | ~$40 | [est] |
| TPU filament (95A) 1 kg ×2 | ~$50 | [est] |
| Flexible ferrite (NFC) sheets | ~$15 | [est] |
| Load cells (1 kg, 5 kg) + HX711 ×3 | ~$30 | [est] |
| Steel/aluminium indenters, steel stock, cylinders | ~$40 | [est] |
| SO-101 follower arm kit (servos/electronics, self-printed parts) | ~$122 single follower; $220–240 for the leader+follower pair | [verified snippet, cnx-software / roboticscenter] |
| Used FDM printer as indentation stage (or the team's own) | $0–150 | [est] |
| Contingency | ~$150 | |
| **Total** | **≈ $700–880** | |

### Timeline (Oct 12, 2026 – Feb 26, 2027)

| Week | Hardware student | Software student |
|---|---|---|
| Oct 12 | Order ReSkin Gerber boards (baseline); start the KiCad re-draw | Set up magpylib; simulate aligned, alternating and Halbach layouts plus mirror image |
| Oct 19 | Print original eFlesh; build the indentation rig on the printer | Bring up AnySkin/eFlesh streaming; logging tool |
| Oct 26 | KiCad variants A/B; design Halbach and ferrite skins from the sims | Port eFlesh force-regression pipeline; pilot on the original |
| Nov 2 | **Order PCB spin 1 + parts (deadline Nov 13)** | Pilot: steel vs. PLA on the original skin, to confirm the effect exists and measure the SD |
| Nov 9 | Print all 4 skin variants; build the SO-101 | Power analysis update; automate indentation G-code |
| Nov 16 | Assemble SO-101; eFlesh fingertip mounts | LeRobot setup; scripted force-limited grasp |
| Nov 23 | Spin 1 arrives: test boards | Bench runs: original + alternating |
| Nov 30 | Instrumented test objects | Bench runs: Halbach + ferrite |
| Dec 7 | Fix mechanical issues; second batch of skins | Field-model vs. measured stray field |
| Dec 14 | Downstream Task 1 setup | **First full bench dataset by Dec 20** |
| Dec 21–Jan 3 | (holiday, light) Decide spin 2: fingertip form factor / fixes | Analysis v1; draft figures |
| Jan 4 | **Order PCB spin 2** if needed | Task 1 grasps: original vs. best |
| Jan 11 | Task 2 slip rig | **Go/no-go Jan 15**: is ΔRMSE reduced by ≥30%? If not, switch to the fallback framing |
| Jan 18 | Spin 2 arrives: retest best variant | Task 2 slip trials |
| Jan 25 | Differential-board secondary arm | Mixed-effects analysis; ablations |
| Feb 1 | Repeat any failed conditions | Draft paper |
| Feb 8 | Photos, CAD/KiCad release | **Data freeze Feb 14** |
| Feb 15–26 | Edit hardware sections | Final paper; submit ~Feb 26 |

### Roles
- **Hardware student (lead):** KiCad re-draw and both spins, magnet-layout CAD, printing, indentation rig, SO-101 build, test objects.
- **Software student:** magpylib design study, firmware configuration, data pipeline, force regressor and slip LSTM retraining, power analysis, statistics, LeRobot scripts.

### Main risk and fallback
- **Risk:** the hand-placed discrete Halbach pattern gives a poor one-sidedness ratio (<2×), or TPU deformation destroys it. Magpylib in week 1–3 de-risks the design before printing.
- **Fallback:** publish the characterization of *why* each layout fails on steel, plus the mirror model, which is still novel and useful. Or exploit the effect instead: "magnetic skins as ferrous pre-contact and material sensors". Steel shows a distinct non-contact signature at 2–10 mm, and the same data supports a material classifier.

### Best venue
- IROS 2027 (hardware + downstream manipulation). RA-L with the IROS option if the result is strong. CASE 2027 if framed around industrial parts handling.
- ICRA 2027 workshop (ViTac / tactile sensing) as fallback.

### Lab appeal
- **Best fit: SJSU, Prof. Winncy Du (Robotics, Sensor & Machine Intelligence Lab).** She authored *Resistive, Capacitive, Inductive, and Magnetic Sensor Technologies* (CRC) and published "Design of a GMR Sensor Array System for Robotic Pipe Inspection" (IEEE Sensors 2010). Both are listed in ../labs.md from https://www.sjsu.edu/people/winncy.du/. Magnetic-field modelling and ferrous-environment sensing are exactly her expertise. She gains a student project with a mechatronics-sensor angle and a co-advised paper.
- **Secondary: UCSC, Prof. Tae Myung Huh** (Dept. of Computer & Electrical Engineering; tactile sensing and suction grasping). His UCSC affiliation appears in the T-RO 2023 Smart Suction Cup author list [snippet]. Lab page: tml.engineering.ucsc.edu (blocked here). He is not in labs.md. Verify before contacting.
- **Tertiary:** Santa Clara RSL (Kitts) for its low-cost humanitarian hand work.

### Honest self-score
- **Novelty 7:** the problem is a stated, unaddressed limitation of a hot open sensor family. Halbach skins exist, but not for ferrous-object immunity, and the mirror argument plus ferrite pre-mirror look new. A reviewer may still call it "a known magnet trick applied to a known sensor".
- **Feasibility 7:** almost everything is reused (MIT repos, printed skins, cheap chips), and the bench data needs only a printer rig. The risks are the KiCad re-draw (no source files) and SO-101 integration time.
- **Impact 6.5:** gives the ReSkin/AnySkin/eFlesh/OSMO community a usable design rule and released files, with a clear downstream metric. It is still a sensor-design paper with a narrow but active audience.
- **Overall ≈ 6.8.**

---

## H2. Electronics or elastomer? A kHz analog-Hall readout board to test what limits slip sensing in open magnetic skins

### Base project and the specific limitation
- **Base:** eFlesh slip detection (https://github.com/notvenky/eFlesh, `slip_detection/`, MIT) [code] and the AnySkin/ReSkin 5X board.
- **Limitation, from the released code [code]:**
  - **Low sample rate.** eFlesh firmware sets MLX90393 digital filter = 4, OSR = 0. The library's datasheet table gives 4.15 ms per T+XYZ conversion, i.e. ≤ ~240 Hz per chip.
  - **Unsynchronized polling.** The 5 chips are polled with no DRDY line (`begin(addr, -1, Wire)`), so samples are unsynchronized and may repeat stale registers.
  - **Slow slip loop.** eFlesh's slip controller runs at 100 Hz on a 10-sample window (`robot/controller.py`), with an LSTM over 40-sample history.
  - AnySkin's default (digFilt = 2) is ≤ ~540 Hz per chip.
  - So existing open magnetic skins sense at 100–500 Hz. Slip and incipient-slip vibrations in other tactile modalities sit in the hundreds of Hz to kHz range [snippet: Bielefeld high-speed tactile sensor reaches 1.9 kHz frame rates "allowing incipient slip detection"; "high-frequency components of several kilohertz … immediately before object slip"].
- **Not released anywhere:** a characterization of the mechanical bandwidth of AnySkin elastomer or eFlesh TPU lattices. Nobody has shown whether a faster readout would even help.

### Research question
Is slip-detection latency in open magnetic skins limited by the readout electronics (≈100–500 Hz) or by the mechanical low-pass of the elastomer/lattice, and does a ≥5 kHz analog-Hall readout cut slip-detection latency enough to rescue more grasps on a low-cost arm?

### Why uncertain
- **Result A (electronics-limited):** the kHz board reveals vibration energy in 0.3–2 kHz at slip onset. Latency falls from ~tens of ms to a few ms, and catch-before-drop success rises.
- **Result B (mechanics-limited):** the soft skin filters everything above ~100–200 Hz, so faster electronics add nothing. That tells the field to change the skin (stiffer lattice, a rigid "whisker" insert) rather than the PCB.
- Both are design rules nobody has measured for this sensor family.
- The likely truth differs between AnySkin (thin elastomer on a rigid tip) and eFlesh (thick compliant lattice), which itself is an interesting comparison.

### Non-obvious insight
- 3-axis digital magnetometers (MLX90393) are what everyone uses because they are I²C-friendly. Slip, however, is a **1-D, high-frequency, small-amplitude** event.
- One cheap **analog linear Hall sensor** (e.g., TI DRV5055, ~20 kHz bandwidth [memory; verify]) per taxel, sampled by an MCU ADC, can sit **beside** the MLX90393s on the same board. The digital chips keep doing static force; the analog channel does vibration. That is the mechanoreceptor SA/FA split done in a $3 part.
- Alternative part: the TI TMAG5170 3-axis SPI sensor with high conversion rate [memory: up to ~20 kSPS; verify].

### Open-source reuse vs. team builds

| Component | Link | License | Saves |
|---|---|---|---|
| eFlesh slip-detection code + released dataset (`seq_*.pt`), LSTM model, robot controller | https://github.com/notvenky/eFlesh [code] | MIT | Baseline detector and baseline data at the original rate |
| eFlesh/AnySkin skins and printing pipeline | same + https://github.com/raunaqbhirangi/anyskin [code] | MIT | Sensor bodies |
| ReSkin 5X board Gerbers | https://github.com/raunaqbhirangi/reskin_sensor [code] | MIT | Baseline electronics |
| LeRobot / SO-101 | https://github.com/huggingface/lerobot | Apache-2.0 [memory] | Arm control for the grasp task |

**Team builds:**
- A new hybrid board (KiCad): 5 × MLX90393 (keeps compatibility) + 4–5 × DRV5055 analog Halls + an RP2040 or STM32G0 sampling ADC at 5–10 kHz with DMA, plus DRDY lines for MLX sync. USB streaming at about 5 ch × 10 kHz × 2 B = 100 kB/s, which is fine over USB-FS.
- **Spin 1** mid-Nov, **spin 2** early Jan (fix analog noise, layout).
- A vibration rig: a small voice-coil or phone vibration motor plus a reference accelerometer (ADXL-class), to measure each skin's mechanical transfer function.

### Closest prior work and what is new
1. **eFlesh slip detection** on Hello Stretch [snippet + code]: 100 Hz loop. Baseline.
2. **AnySkin handover/slip demo** (NYU-robot-learning/AnySkin-Handoff-Demo, credited in the eFlesh repo) [code].
3. **"A High-Speed Tactile Sensor for Slip Detection"** (Bielefeld; pub.uni-bielefeld.de/record/2306867) [snippet]: 1.9 kHz piezoresistive arrays. Not magnetic, not low-cost open.
4. **"Incipient Slip Detection by Vibration Injection into Soft Sensor"** (arXiv 2402.11879) [snippet]: active vibration, not a readout-bandwidth study.
5. **"Mass-Manufacturable 3D Magnetic Force Sensor for Robotic Grasping and Slip Detection"** (Sensors 2023, doi 10.3390/s23063031) [snippet]: magnetic slip detection at conventional rates.
6. **Tomo et al., Hall-effect soft skin (MLX90393)** (Sensors 16(4):491, 2016) [snippet].

**New here:**
- The first measured transfer function (vibration → magnetometer) of the open AnySkin and eFlesh skins.
- A hybrid digital + analog-Hall board.
- A controlled latency and grasp-rescue comparison against the original firmware and detector.

### Experiment design
- **Bench transfer function:**
  - Inputs: sine sweeps at 20 Hz–3 kHz on each skin (AnySkin-style molded skin if available, else ReSkin-style; eFlesh lattice).
  - Analog Hall output vs. reference accelerometer → Bode magnitude and −3 dB frequency.
  - 3 skin samples × 2 skin types × 3 repeats.
- **Slip latency (primary, continuous):**
  - Setup: a fixed gripper on the SO-101 holds a PLA block. Mass is added until slip, or the block is pulled by a string through a load cell.
  - Ground-truth slip onset comes from a 240 fps phone camera plus pull-force drop.
  - Three detector variants: (a) original firmware + released LSTM retrained on our data; (b) same LSTM on MLX data at the fastest synchronized rate the new board allows; (c) analog-Hall high-pass energy detector (+ small 1D-CNN).
  - Metrics: latency (ms) and false-positive rate per minute of non-slip manipulation.
- **Downstream:** "catch before drop". When slip is detected, the gripper tightens by Δ. Metric: drop rate over 40 lifts per detector × 2 objects (smooth PLA, textured).
- **Sample size:** if latency SD ≈ 15 ms and we want to detect a 10 ms reduction, d ≈ 0.67, which needs n ≈ 36 per detector (paired across the same trials, since all detectors run on the same recording, so paired n ≈ 20 suffices). **Use 60 slip events per skin type.** All three detectors run offline on the *same* recordings, which makes the comparison paired and cheap. For drop rate, 40 lifts × 2 detectors (original vs. best) detects 30% → 10% at roughly 80% power.

### Measurements and analysis
- Bode plots and −3 dB frequency per skin.
- Latency distributions; paired Wilcoxon or bootstrap CIs.
- ROC curves for detection.
- Drop-rate comparison with Fisher's exact test.
- An ablation that low-pass filters and downsamples the kHz data to 100/250/500 Hz. This directly answers "what rate is enough?".

### Build list

| Item | Cost | Status |
|---|---|---|
| MLX90393 ×20 | ~$43 | [verified snippet, $2.13 ea] |
| DRV5055 / TMAG5170 ×20 | ~$40 | [est] |
| RP2040/STM32 + passives on board, JLC PCBA 2 spins | ~$150 | [est] |
| ReSkin baseline boards | ~$40 | [est] |
| Reference accelerometer breakout + small voice coil/exciter + amp | ~$50 | [est] |
| Magnets, TPU, silicone (Ecoflex trial kit) | ~$90 | [est] |
| SO-101 follower kit | ~$122 | [verified snippet] |
| Load cell + HX711, string-pull rig | ~$30 | [est] |
| Contingency | ~$150 | |
| **Total** | **≈ $715** | |

### Timeline

| Week | Hardware | Software |
|---|---|---|
| Oct 12 | Order ReSkin baseline boards; schematic for hybrid board | Reproduce eFlesh slip LSTM on released data |
| Oct 19 | Print eFlesh; mould/obtain AnySkin-style skin | Firmware: measure true effective rate and duplicate samples on the baseline board |
| Oct 26 | Hybrid board layout | Analog Hall streaming prototype on a breadboard (DRV5055 breakout + RP2040) |
| Nov 2 | **Order spin 1 (by Nov 13)** + parts | Breadboard pilot: is there any >200 Hz content at slip? (early go/no-go signal) |
| Nov 9 | Vibration rig | DMA ADC firmware |
| Nov 16 | SO-101 build + fingertip mounts | Logging + 240 fps video sync |
| Nov 23 | Spin 1 bring-up | Transfer-function sweeps |
| Nov 30 | Slip rig | Slip recordings (skin 1) |
| Dec 7 | Fixes | Slip recordings (skin 2) |
| Dec 14 | — | **First latency dataset by Dec 20** |
| Dec 21–Jan 3 | Spin 2 design (noise fixes) | Detector training / analysis v1 |
| Jan 4 | **Order spin 2** | Downsampling ablation |
| Jan 11 | Catch-before-drop controller hardware | **Go/no-go Jan 15** |
| Jan 18–Feb 7 | Spin 2 retest; downstream drop trials | Drop trials; stats; draft |
| Feb 8–14 | Release KiCad/firmware | **Data freeze** |
| Feb 15–26 | Edit | Submit |

### Roles
- **Hardware student:** hybrid PCB (analog layout, grounding), vibration and slip rigs, SO-101 mechanics.
- **Software student:** DMA firmware, synchronization, detectors, analysis, power analysis.

### Main risk and fallback
- **Risk:** analog Hall noise (~mV) swamps the small vibration signals. Or the skins are mechanically low-pass (Result B), which is still publishable.
- **Fallback:** the paper becomes "a bandwidth characterization of open magnetic skins + synchronized-readout firmware". It is a smaller but solid workshop/CASE contribution.

### Best venue
- IROS 2027 if Result A holds with the downstream gain. Otherwise an ICRA 2027 tactile workshop or IEEE Sensors Letters.

### Lab appeal
- **SJSU Winncy Du:** Hall/GMR sensor arrays and signal conditioning are her core area (labs.md). She gains an instrumentation-heavy student project.
- **UCSC Huh** (tactile sensing; see H1 note; not in labs.md).

### Honest self-score
- **Novelty 6:** "faster sampling helps slip" sounds obvious. What redeems it is the open question of whether the skin passes the vibration at all, and the hybrid analog/digital board, though reviewers may still see it as incremental.
- **Feasibility 6:** analog mixed-signal PCB layout by a high-school student is the hard part. The breadboard pilot in early Nov and offline paired detector comparisons keep it finishable.
- **Impact 6:** a useful design rule and an open board for magnetic-skin users. The audience is mostly tactile-sensing people.
- **Overall = 6.0.**

---

## H3. Smart Suction Cup on a hobby pump: using pump pulsation as a free lock-in probe for seal and leak sensing

### Base project and the specific limitation
- **Base:** the Smart Suction Cup (Huh et al., IROS 2021, arXiv 2105.02345 [snippet]). Follow-ups: haptic search on adversarial objects (Lee, Lee, Huh, Stuart, T-RO 2023, arXiv 2309.07360 [snippet]); data-driven haptic search (arXiv 2401.06354 [snippet]); haptic contour following (IROS 2024 [snippet]).
- **How it works:** a bellows cup with four internal chambers, each with its own pressure sensor. It localizes seal breaks between quadrants with up to 97% accuracy and improves bin-picking success up to 2.5× [snippet].
- **Limitation (the original setup is industrial):**
  - It used a UR-10 arm, an ATI Axia80 wrist F/T sensor, and four Adafruit MPRLS sensors read over I²C at 166.7 Hz [snippet, T-RO paper].
  - It relies on steady (regulated) vacuum, so its flow estimates are quasi-static.
  - **No design files or code found:** GitHub repository search for "smart suction cup haptic search" returned 0 results. The design is a UC patent available for licensing (techtransfer.universityofcalifornia.edu NCD/32355) [snippet].
  - On low-cost arms people use 12 V diaphragm pumps, whose pressure pulsates at the pump stroke frequency. That ripple is the main obstacle to quasi-static differential flow sensing. *This is my inference. I could not open the paper to confirm their vacuum source, so the team must confirm it from the PDF before claiming it.*

### Research question
Can a pulsating hobby diaphragm pump, normally a noise source, serve as a free excitation signal? Specifically, can per-chamber pulsation amplitude and phase (lock-in demodulated) localize seal breaks and estimate leak size on a low-cost arm as well as, or better than, the original regulated-vacuum DC-pressure method?

### Why uncertain
- **Result A:** a leak changes each chamber's pneumatic impedance, so AC ripple transfer (like the FRF-based valve-leak detection used in process industries [snippet, US patent on leaky-valve detection via dynamic pressure transmission]) separates leak location and size *better* than DC pressure, at zero added cost.
- **Result B:** ripple amplitude is dominated by tubing and cup compliance and is insensitive to small leaks, so the low-cost path needs an accumulator to emulate regulated vacuum. That is still a useful, quantified design rule for low-cost suction tactile sensing.

### Non-obvious insight
- In the original system pump ripple is a nuisance to filter out. Treated instead as a known periodic excitation (its frequency is read from motor current), lock-in demodulation gives an **impedance measurement per chamber**: amplitude and phase. DC pressure cannot give this.
- It may also distinguish porous surfaces from geometric seal gaps, which DC flow confuses.

### Open-source reuse vs. team builds

| Component | Link | License | Saves |
|---|---|---|---|
| Published Smart Suction Cup design (geometry, sensor choice) | arXiv 2105.02345 / 2309.07360 [snippet] | Paper; **patented**, no files | Concept and sensor choice only. Team must re-create the cup |
| Adafruit MPRLS library | https://github.com/adafruit/Adafruit_MPRLS [memory] | BSD [memory] | Baseline sensor driver |
| LeRobot / SO-101 | https://github.com/huggingface/lerobot | Apache-2.0 [memory] | Arm |

**Team builds:**
- A 4-chamber cup: printed TPU inserts in a commercial bellows cup, or a silicone moulding.
- A sensor PCB with 4 fast analog pressure sensors (≥1 kHz) + an MCU with synchronous ADC. **Spin 1** mid-Nov, **spin 2** Jan.
- A pneumatics board (pump driver with current sense, valve, an optional accumulator).
- A lock-in demodulation firmware/analysis pipeline.
- A set of 3D-printed "adversarial" objects (ridges, edges, curvature).

This is **less reuse than H1/H2**, which is the main weakness.

### Closest prior work and what is new
1. Smart Suction Cup (IROS 2021) [snippet].
2. Haptic search with the Smart Suction Cup (T-RO 2023) [snippet].
3. Data-driven haptic search (arXiv 2401.06354) [snippet].
4. Haptic contour following (IROS 2024) [snippet].
5. FlexiCup, wireless multimodal suction cup with vision-tactile sensing (arXiv 2511.14139) [snippet].
6. "Grasping objects with the aid of haptics", Science Robotics (doi 10.1126/scirobotics.adp8528) [snippet: title only].

**New:**
- A low-cost arm with a hobby pump instead of a UR-10 with regulated vacuum.
- AC (lock-in) pneumatic impedance sensing per chamber instead of DC pressure.
- A direct comparison against the original DC method on the same cup.

### Experiment design (baseline = original DC method on an emulated regulated supply)
- **Supply conditions:** (i) pump + large accumulator + bang-bang regulation, which emulates the original steady vacuum (baseline); (ii) raw pulsating pump.
- **Sensing methods:** DC differential pressure (original) vs. lock-in AC amplitude/phase.
- **Bench study:**
  - Press the cup on a flat plate with calibrated leak slots: 4 quadrants × 4 slot widths, plus no leak.
  - 20 repeats each → 340 trials per supply condition, about 3 s each, so roughly 1 h automated with the arm.
  - **Primary metrics:** quadrant-localization accuracy and leak-area estimation RMSE.
- **Downstream:** haptic-search bin picking of 10 printed adversarial objects, with a simple gradient-following search driven by each signal. Metric: grasp success within ≤5 search steps.
- **Sample size:** to detect 85% vs. 70% localization accuracy (two-proportion, α = 0.05, 80% power) needs about 120 trials per condition, so 340 is well above that. For bin picking, 60 grasp attempts per condition detects 70% vs. 45%.

### Measurements and analysis
- Confusion matrices.
- Leak-area regression RMSE with bootstrap CIs.
- Logistic mixed model on grasp success (object random effect).
- Spectral analysis of ripple vs. leak state.

### Build list

| Item | Cost | Status |
|---|---|---|
| 12 V diaphragm vacuum pump ×2, solenoid valves ×2 | ~$60 | [est] |
| Fast analog pressure sensors ×6 (e.g., NXP MPXV6115V-class) | ~$90 | [est] |
| MPRLS breakouts ×4 (to replicate the original sensor) | ~$60 | [est] |
| Bellows suction cups (assorted), silicone kit | ~$60 | [est] |
| Accumulator/vacuum reservoir, tubing, fittings | ~$50 | [est] |
| PCBs (2 spins, JLC PCBA) | ~$120 | [est] |
| SO-101 follower kit | ~$122 | [verified snippet] |
| Printed objects, misc. | ~$40 | [est] |
| Contingency | ~$150 | |
| **Total** | **≈ $750** | |

### Timeline

| Week | Hardware | Software |
|---|---|---|
| Oct 12 | Read the 3 papers in full and confirm the original vacuum source; cup CAD | Pump-ripple pilot: phone-grade pressure sensor + Arduino, measure spectrum |
| Oct 19 | Prototype 4-chamber cup (insert in commercial bellows) | Lock-in demodulation code (offline) |
| Oct 26 | Sensor PCB schematic/layout | Breadboard: DC vs. AC on 1 chamber with leak slots |
| Nov 2 | **Order spin 1 + parts (by Nov 13)** | Go/no-go signal: does ripple amplitude change with leak? |
| Nov 9–16 | SO-101 build; pneumatics board | LeRobot + suction tool control |
| Nov 23–Dec 13 | Spin 1 bring-up; leak-slot plate; accumulator | Bench trials (both supply conditions) |
| Dec 14 | — | **First bench dataset by Dec 20** |
| Dec 21–Jan 3 | Spin 2 design | Analysis v1 |
| Jan 4–15 | **Order spin 2**; adversarial objects | **Go/no-go Jan 15** |
| Jan 18–Feb 7 | Bin-picking trials | Haptic-search controller; stats; draft |
| Feb 8–26 | Release files | Data freeze Feb 14; submit |

### Roles
- **Hardware student:** cup design and moulding, pneumatics, PCBs, arm tooling.
- **Software student:** lock-in DSP, controllers, experiment automation, analysis.

### Main risk and fallback
- **Risks:** (1) the original already used a pump and filtered ripple, so the "limitation" framing weakens (check in week 1); (2) the 4-chamber cup is hard to make leak-tight without the original moulds.
- **Fallback:** a quantified low-cost replication with a regulated-vs-pulsating comparison. That drops to a workshop paper.

### Best venue
- IEEE CASE 2027 (bin picking / automation). ICRA 2027 workshop fallback.

### Lab appeal
- **UCSC, Prof. Tae Myung Huh**, a co-inventor of the Smart Suction Cup. His UCSC affiliation is shown on the T-RO 2023 paper [snippet], and his lab site has a "Suction Grasping" page (tml.engineering.ucsc.edu, blocked here). He gains a low-cost, open re-implementation of his sensor and a new sensing mode. He is **not in labs.md**, so verify the HS-mentoring route. UCSC SIP may be a path.
- **Secondary:** UC Merced (Carpin) for CASE-style automation evaluation.

### Honest self-score
- **Novelty 5.5:** the pulsation-as-probe idea is new for suction tactile sensing as far as I found, but the rest is a low-cost re-implementation. And I could not read the original paper to confirm its vacuum source.
- **Feasibility 5.5:** there are no released design files, a leak-tight multi-chamber cup is fiddly, and the pneumatic DSP adds risk. Reuse is weaker than the brief wants.
- **Impact 6:** CASE-relevant with an obvious industrial angle, and the original inventor is local. It becomes a workshop paper if Result B.
- **Overall ≈ 5.7.**

---

## Notes for reviewers
- Every claim about AnySkin/eFlesh/ReSkin firmware and library behaviour comes from code I read:
  - MLX90393 settings, no DRDY, and `setTemperatureCompensation(0)` in the library's `begin()`.
  - The temperature channel masked out in `anyskin/sensor.py`.
  - eFlesh's 100 Hz slip controller.
  - Board released only as Gerbers.
- Paper statements are search snippets because arxiv.org is blocked in this sandbox.
- No citation above is invented. Items tagged [memory] are well-known works I did not re-open; verify them.
