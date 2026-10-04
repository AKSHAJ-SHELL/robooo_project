# Other research angles: brief (shared by generators and reviewers)

## What the user wants
- General robotics research. It does NOT need to relate to the trash-bin robot.
- Areas named by the user: improving robot models (learning, VLA / navigation / manipulation policies), SLAM and localization, or custom hardware such as an improved custom PCB (motor driver, sensor board, compute carrier) for specific tasks.
- Method: start from an EXISTING low-cost / open robotics project by another team (a paper, open-source robot, or open hardware). Find a LIMITATION that team stated or that is visible (paper limitations section, GitHub issues, follow-up papers, forum complaints). Then improve on it or extend it, and measure the improvement against the original team's own setup.
- Not building something completely new. Build on what exists.
- Reuse open-source code, models, datasets and hardware designs as much as possible so the team doesn't build from scratch. Every idea must list exactly what it reuses (repo links, licenses where easy to find) and what the team actually has to build.
- Still needs: real (if modest) novelty, so a reviewer thinks "there's something here worth reading"; impact; and a nearby lab that would want to help.

## Team and constraints
- Two high-school students in California: one mechanical/hardware (can do CAD, 3D printing, soldering, simple PCB layout in KiCad), one software/perception (Python, ROS 2, basic ML). Part-time.
- Timeline: start mid-Oct 2026; parts ordered by mid-Nov (PCB fab from JLCPCB/PCBWay takes ~1-2 weeks); first data by Dec 20; go/no-go Jan 15; data freeze Feb 14; submit ~Feb 26 for IEEE CASE 2027 or IROS 2027 (both due Mar 1, 2027). ICRA 2027 workshops (spring) are the fallback.
- Budget: about $1,000 total. Free compute only (laptop, free Colab/Kaggle).

## Lessons from 3 earlier rounds (~45 ideas, best median 6.33/10)
1. Predictable results (derivable on paper) score low. The outcome must be able to go either way.
2. "Same thing, cheaper" with no new insight scores ~5. Fixing a documented limitation with a measurable gain is different and better, but the fix must not be obvious or already done by a follow-up paper.
3. Missed canonical prior work hurts: search properly (Scholar, arXiv, GitHub, follow-up papers citing the original).
4. Use the original team's own setup/code as the baseline, not a straw man.
5. Read the released code before claiming a limitation exists.
6. Size experiments with a power analysis; prefer continuous metrics; keep factor grids small.
7. Feasibility under the March 1 deadline is what kept scores down. Reusing open-source parts is the main way to raise it.

## Reachable labs (details in ../labs.md)
UCSC Autonomous Systems Lab (Elkaim; Pi + ROS 2 + Nav2 ground robots, low-cost open autonomy, HS mentoring via SIP) and SIP hosts Kobayashi (off-road UGV traversability), Sanfelice, Fremont (robustness, Scenic); UC Merced Robotics Lab (Carpin; outdoor/ag ROS 2 navigation, multi-robot, CASE); Santa Clara Robotic Systems Lab (Kitts; field rovers, multi-robot, low-cost devices); UCLA LEMUR (Mehta; cheap printable robots, lidar odometry, multi-robot localization); SJSU Wencen Wu (multi-robot sensing, cooperative perception); SJSU Winncy Du (sensors, mechatronics). Each idea must name the best-fit lab, the specific work of theirs it connects to, and what they gain.

## Scoring rubric (0-10, half points), same as before
- Novelty: 9-10 clearly new to a main-track IROS/CASE reviewer; 7-8 new result in an active area, closest work clearly distinguished; 5-6 known method in a new setting / incremental; 3-4 largely done; 0-2 done.
- Feasibility (THIS team, budget, timeline): 9-10 low risk, data by Dec; 7-8 doable with manageable risks; 5-6 significant risk or underpowered; 3-4 likely not finishable; 0-2 infeasible.
- Impact: 9-10 likely main-track paper others cite/use; 7-8 solid CASE main-track or strong workshop paper with reuse value; 5-6 workshop/WIP, narrow audience; 3-4 class-project level.
- Overall = mean; idea score = median of reviewer overalls.
