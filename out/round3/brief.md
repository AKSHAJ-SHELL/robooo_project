# Round 3 brief (shared by generators and reviewers)

## Team and constraints
- Two high-school students in California: one mechanical, one perception/software. Part-time (school year).
- Timeline: start mid-Oct 2026; parts ordered by mid-Nov; first data by Dec 20; go/no-go Jan 15; data freeze Feb 14; submit ~Feb 26 for IEEE CASE 2027 or IROS 2027 (both due Mar 1, 2027). ICRA 2027 workshops (spring) are the fallback.
- Budget: about $1,000 total, hobby/maker parts (Raspberry Pi 5, ESP32, hoverboard-motor bases, Pi cameras, $70-120 2D lidars, cheap ToF, IMUs). Free cloud/laptop compute only.
- Home project: a low-cost robot that takes an unmodified residential refuse cart (64/96-gal) from garage to curb. Ideas do NOT have to be about the bin task, but a link to it is a plus (they can reuse the platform).
- Safety: never enter the roadway; no human-subjects data unless trivially exempt (avoid).

## What failed before (35 ideas, 2 rounds, best median overall 5.83 / 10)
Reviewers repeatedly penalized:
1. Predictable results: hypotheses derivable on paper (statics, geometry, funnel/compliance theory, beam spacing). A result must be able to come out either way, and theory alone must not settle it.
2. "Same thing but cheaper" with no new insight: cheaper re-implementations of known methods (reflector lidar localization, self-supervised bump labels = BADGR / Stavens & Thrun 2006, optical-flow slip) score ~5.
3. Missed canonical prior work (search budget limits). Search Google Scholar / arXiv / IEEE properly.
4. Straw-man baselines. Use the strongest fair baseline, ideally the original authors' own setting.
5. Claimed failure modes that do not exist in released code. Read the code before claiming a failure.
6. Underpowered or bloated experiments (n=25 equivalence tests; 1,200-cell grids). Size trials with a power analysis; prefer continuous metrics.
7. Scope too big for 12 weeks of two part-time students.
8. Impact ceiling: bin-robot-specific engineering reads as CASE-workshop level.
Levers reviewers said would raise scores: data nobody has (multi-site field data a cheap rig enables); an empirical question theory cannot settle; a predictive model validated on held-out sites; using the authors' own setting as baseline; results that matter to people beyond the bin robot.

Already explored (do not repeat): passive hitch capture envelopes; hitch-height weight transfer; curb sensor price sweep; RTK-on-driveway cost ladder; five-stack cost frontier; night teach-and-repeat; cart pose from camera/lidar; RFID cart re-ID; optical-flow dead reckoning with towed load; lip crossing force; WVN/NoMaD/DRIVE/OK-Robot on cheap hardware; bump-labeled camera step detection; reflector-post lidar vs RTK; 60 GHz radar for mowers; phone GNSS+VIO; mower stripe following; red-edge grass sensor; Hall-sensor tape guidance; control joints as landmarks; push-to-localize blind hitching; depth-to-camera distillation for carts. Full texts: out/angles/all_18_angles.md, out/ideas_v2_log.md, out/prior_art.md.

## Scoring rubric (0-10, half points)
- Novelty: 9-10 = a new question or finding a main-track IROS/CASE reviewer would call clearly new; 7-8 = new result in an active area, closest work clearly distinguished; 5-6 = known method applied to a new setting / incremental; 3-4 = largely done before; 0-2 = done.
- Feasibility (for THIS team, budget, and timeline): 9-10 = low risk, clear de-risking path, data by Dec; 7-8 = doable with identified, manageable risks; 5-6 = significant risk of not finishing or underpowered; 3-4 = likely not finishable; 0-2 = infeasible.
- Impact: 9-10 = likely IROS/CASE main-track paper that others will cite/use; 7-8 = solid CASE main-track or strong workshop paper with reuse value (data, tool, design rule); 5-6 = workshop/WIP level, narrow audience; 3-4 = class-project level.
- Overall = mean of the three. Idea score = median of reviewer overalls.
