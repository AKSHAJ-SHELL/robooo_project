# Round 3 result: impact-first ideas with lab appeal

Date: 2026-10-04. Inputs: [brief.md](brief.md) (priorities, constraints, rubric), [gen_D.md](gen_D.md), [gen_E.md](gen_E.md), [gen_F.md](gen_F.md), [E1.v2.md](E1.v2.md), [D1.v2.md](D1.v2.md), [reviews/](reviews/).

## Bottom line

- **No idea reached 7.5.** The best is **E1.v2 at a median of 6.33** (reviews 6.50 / 6.33 / 6.33; N 6.5, F 6.5, I 6.5). Scores are reported unadjusted.
- This is the highest-rated idea across all three rounds (round 1 best 5.83, round 2 best 5.67). It is also the first to get novelty and impact scores of 7 from individual reviewers (E1 v1).
- Process: 3 generators (field data that changes decisions / test an assumption the field relies on / tools others reuse) wrote 9 ideas. The top 5 got 3 blind reviewers each (prior work, methods and feasibility, impact and lab appeal). The top 2 were revised and re-scored by 3 fresh reviewers each. Reviewers were never told the 7.5 target.

## Scoreboard

| Idea | Version | Reviews | **Median** | Median N / F / I |
|---|---|---|---|---|
| **E1** Phone-scan digital twins vs the real sidewalk: does testing navigation models in a Gaussian-splat twin predict how they behave at 30 cm? | v2 | 6.50, 6.33, 6.33 | **6.33** | 6.5 / 6.5 / 6.5 |
| E1 | v1 | 6.17, 6.33, 6.50 | 6.33 | 7 / 5.5 / 7 |
| D1 "Dew or dirt?" small-robot traction on real lawns | v1 | 6.33, 5.67, 6.17 | 6.17 | 6 / 6.5 / 6 |
| D1 | v2 | 6.17, 5.83, 6.00 | 6.00 | 6 / 6.5 / 6 |
| F1 How much of an outdoor navigation result is the day it was run? | v1 | 5.83, 5.67, 5.83 | 5.83 | 6.5 / 5 / 6 |
| D2 How precise does a curbside cart need to be for automated trucks? | v1 | 5.50, 5.67, 5.67 | 5.67 | 6 / 5.5 / 5.5 |
| F3 Do simulated counterexamples (Scenic/VerifAI) happen on a real Nav2 robot? | v1 | 5.67, 5.17, 5.83 | 5.67 | 5.5 / 5 / 6 |

Not reviewed (self-scores 6.7–6.8): D3 trash calendar and sidewalk obstruction, E2 goal-error tolerance of sidewalk navigation models, E3 multi-height place recognition, F2 flat-pull vs slope on turf (partly merged into D1.v2).

## Recommendation: E1.v2

**What it is.** Navigation foundation models (CityWalker, LogoNav) are increasingly evaluated inside Gaussian-splat "digital twins" scanned with a phone (Wanderland, Vid2Sim/S2E). Nobody has checked whether those twins predict real behavior for a low, sidewalk-robot camera, or whether a twin scanned at human height misleads a 30 cm robot. E1.v2 measures it on 16 routes at 8 sites, with real-vs-real repeats as the noise floor. The main result is open-loop (policy-output divergence on teleoperated drives), so it does not depend on the policies driving well. Closed-loop runs and Kadian et al.'s SRCC confirm it.

**Why it fits your priorities.**
- *Impact:* it tests an assumption a fast-growing evaluation practice depends on. If twins mislead at low height, the people building delivery and sidewalk robots need to know.
- *Novelty:* reviewers agree the low-viewpoint, real-robot validation is open. Wanderland's code shows a ~1.1 m camera, no real-robot runs and no sim-vs-real correlation; the paper itself was not readable here.
- *Lab appeal:* UCSC Fremont (Scenic placement of a moved cart in the twin), UCSC Elkaim (Pi/ROS 2 ground robots, SIP), and the code authors at VAIL-UCLA (S2E) and NYU AI4CE (Wanderland) as outside contacts with pilot data in January.
- Cost ~$787; can reuse the bin-robot base.

**What the last reviews say to fix before you commit** (from [reviews/E1v2_R2.md](reviews/E1v2_R2.md) and the others):
1. H1 ("human-height twins diverge more") is close to predictable. Make "do image metrics like PSNR/LPIPS track policy divergence?" a co-primary hypothesis; that one can go either way.
2. Counterbalance which height is scanned first (morning light changes fast). Equalize image count and path length between scans.
3. Add a twin built from the robot's own camera frames on drive 1, evaluated on drive 2. It costs no extra field time.
4. Tighten pose matching on the real-vs-real floor, so twins aren't favored by rendering at exact poses.
5. Widen the power grid and set a minimum site count: losing 2 of 8 sites drops power from 0.82 to 0.55.
6. Make closed-loop replay conditional on the Jan 15 go/no-go.
7. Fix minor path citations; verify arXiv 2610.00731 and NavDP's real-world-consistency sentence.

## Why nothing clears 7.5, and what would

Across three rounds (about 45 ideas, 100+ reviews), feasibility is what holds scores down. Reviewers repeatedly say the timeline is too tight: two part-time students, parts by mid-November, data freeze Feb 14. A 7.5 needs roughly 7.5 on all three dimensions, including feasibility under that timeline, plus novelty a main-track reviewer calls clearly new. More rounds of idea generation have stopped moving the ceiling.

The levers that would actually change the score:
1. **A lab mentor before December.** Most remaining critiques are about experiment design and missed papers, which a grad student fixes fastest. Send the October phone-video check (step 1 of E1.v2's timeline) to Fremont and Elkaim as your opener.
2. **Relax the deadline.** Aim the full study at a later venue (e.g. IROS 2027's successor cycle or ICRA 2028, typically due in September) and submit the open-loop result to an ICRA 2027 workshop in spring. That alone would lift feasibility by about a point in most reviews.
3. **Run E1.v2's free October check now.** Real pilot numbers replace assumed variances and are the strongest thing to show a lab.
