# Making it more novel: "same capability, much cheaper" ideas (round 2)

Date: 2026-10-04. Full ideas, all 45 reviews and the revisions are in [ideas_v2_log.md](ideas_v2_log.md).

## What was run

- **15 new ideas** from three strategies, 5 each:
  - **R:** a cheaper copy of a published result (e.g. the [Wild Visual Navigation](https://arxiv.org/abs/2404.07110) navigation method, the NoMaD navigation model, and the DRIVE slip-learning method, each on hobby hardware).
  - **S:** software replaces hardware (motor current, IMU or a cheap camera standing in for a costly sensor).
  - **P:** a cheap open version of a commercial feature (mower boundaries, cart docking, obstacle stopping).
- **Requirements for every idea:** name the expensive reference with its cost, state one non-obvious insight, and give an experiment with enough trials to detect a real difference.
- **Round 1:** 3 adversarial reviewers per idea, same rubric as before.
- **Round 2:** the top 5 were revised to answer their critiques, then re-scored from scratch by 3 fresh reviewers. This is a stated departure from the original ≥7.5 revision rule.

## Result

**No idea reached 7.5. The best median overall was 5.67, the same ceiling as round 1 (5.83).** Revision moved the top ideas by only −0.33 to +0.33.

| Rank | Idea | Strategy | N / F / I | Overall | Cost |
|---|---|---|---|---|---|
| 1 | **S2.v2**: A self-trained $25 camera vs. a $429 active-stereo depth camera on 3–25 mm ground steps. The camera learns from bumps the robot's wheels feel, and the question is whether those bump labels, not the camera's optics, set the smallest detectable step. | Software replaces hardware | 6 / 5.5 / **6** | 5.67 | ~$860 |
| 1 | **R2.v2**: The NoMaD navigation model on a $15–78 computer. The model's 8 discarded candidate paths are used to slow the robot when they disagree. | Cheaper copy | **6** / 6 / 5.5 | 5.67 | ~$580 |
| 1 | **R5.v2**: Bin docking pose from a $14 camera, measured from where the wheels touch the ground, compared against a $96 2D lidar. Works on cart brands it has never seen. | Cheaper copy (bin task) | 5 / **7** / 5.5 | 5.67 | **~$370** |
| 1 | **R3.v2**: How good must slip labels be? A $40 optical-flow sensor vs. the published lidar labels, tested with the DRIVE slip-learning code and data. | Cheaper copy | 5 / **7** / 5.5 | 5.67 | ~$660 |
| 1 | **P2.v1**: Four retroreflective posts and a $96 lidar vs. RTK GPS for yard and driveway robots. | Commercial-feature clone | 5 / 6.5 / 5.5 | 5.67 | — |

The other 10 ideas scored 4.17–5.33. Ranks are tied at 5.67, so the order is by novelty and impact sub-scores. The weakest idea, R4 (the OK-Robot pick-and-place system on a cheap $482 arm robot), scored 4.17.

## Why "cheaper" alone doesn't score as novel

Across both runs there were 20 ideas and 70 reviews, and no idea scored above about 6 overall. The reviewers' reasons repeat:

1. **The insight was already published.**
   - S2's "the robot labels its own camera with bumps" is the method of BADGR and earlier work by Stavens and Thrun (2006), and the proposal hadn't cited them.
   - P2's reflector-and-lidar localization was already checked against GNSS in a 2022 paper.
   - Generators searched first, but search limits meant they sometimes missed the canonical paper.
2. **The result can be derived on paper.**
   - R3: label bias vs. label noise in a linear model is textbook.
   - R5: ground-contact back-projection error follows from geometry.
   - P2: lidar hit counts follow from angular spacing.
   - Reviewers penalize a hypothesis that can't come out the other way.
3. **The failure being fixed doesn't happen.**
   - R2.v1 assumed slow compute disturbs NoMaD's camera context.
   - Reviewers read the released code and found the camera queue fills independently of inference speed.
4. **Calibration.** The rubric reserves 9–10 for a likely IROS or CASE main-track paper. Twelve weeks of part-time work by two high schoolers rarely reaches that, so the 8.5 bar is close to unreachable for any idea in this scope. That's a property of the bar, not of these ideas.

## How to actually raise novelty

These levers come from what the reviewers said would raise scores:

1. **Collect data nobody has.**
   - Novelty can come from data no one has collected rather than from the method. A cheap robot or hand rig is perfect for collecting data at many sites.
   - The A1 reviewers' strongest fix was a robot-free RTK fix and false-fix survey across **15–25 driveways**, with sky-view photos, plus a model that predicts fix quality from the geometry.
   - A low-viewpoint dataset of **US curb cuts and rolled curbs**, or of **unmodified carts across brands**, is similar. That data does not exist.
2. **Find an empirical result that could go either way and that theory can't settle.** S2.v2 is closest: whether the robot's bump labels, not the camera's optics, set the smallest detectable step. To fix it, cite BADGR and Cross-Modal Supervision, and test more than two wheel sizes so the claimed relationship is actually identifiable.
3. **Use the authors' own setting as the baseline,** not a straw man. R2.v2 ran NoMaD at the original paper's own 4 Hz / 0.2 m/s operating point, and it got the best novelty score (6). It still needs a hypothesis that isn't already built into the original controller code.
4. **Read the code before claiming a failure mode.** R2.v1 lost half a point because the failure it set out to fix doesn't happen in the released code.

## Recommendation

- **Choose a direction by about Oct 20.** Parts need to be ordered by mid-November for a Mar 1 CASE or IROS submission, so re-running review rounds now costs more than it gains.
- **Best novelty plus bin-robot continuity: R5.v2 (camera-only cart pose) combined with a cross-brand cart dataset.**
  - It is cheap (~$370) and has the highest feasibility (7).
  - Releasing the first low-viewpoint dataset of unmodified US refuse carts across brands turns "derivable geometry" into "data nobody has".
  - Pair it with the hitch from B1 in `final.md` for a docking story: a cheap camera finds the cart, and a passive hitch absorbs the leftover error.
- **Best standalone research question: S2.v2,** with BADGR and Cross-Modal Supervision cited and the wheel-size relationship tested properly. It has the highest impact score (6) of any of the 20 ideas. It also fits the bin robot, because the 1–3 cm curb-cut lip is exactly the hard case from A4.
- **Realistic target:** IEEE CASE 2027 (Mar 1) or an ICRA 2027 workshop, plus a strong college-application story. Don't plan around IROS main-track acceptance.
- **A mentor matters more than another round of ideas.** Reviewers repeatedly flagged experiment design, and a faculty or grad mentor fixes that faster. UCSC's Elkaim lab, Santa Clara's Kitts and SJSU's Du are in [labs.md](labs.md).
