# University Labs Open to High-School Researchers: Fit for the Low-Cost Trash-Bin Robot

**Date:** 2026-10-03
**Project:** low-cost autonomous robot that moves unmodified 64/96-gal municipal carts between garage and curb. Goal: an IEEE paper submitted by March 1–2, 2027.
**Team:** two high-school students (software/perception + mechanical/hardware).

> **How to read this file.** Each fact has a link to a page I opened (or a search result whose snippet confirmed it). Fit scores, engagement odds and "what they want to see" are **my estimates** unless a lab's own page says it. Personal e-mails and phone numbers are left out on purpose. Use the linked official pages.
>
> **Key timing point.** Every formal high-school research program I verified runs in **summer 2027**, after the March 1–2 paper deadline. Before March, a lab is realistic only as an **informal advisor**: a 15–20 minute call or written feedback on the experiment design or draft. Hosting the build in their lab before then is unlikely. Plan outreach on that basis. Summer programs are a follow-on (extend the paper, journal or workshop version, letters for college applications).
>
> **Research limits.** The shared web-search budget ran out partway through this task. A few items (e.g., RoMeLa join policy, USC SHINE 2027 status, UC Merced lab people page) could not be checked and are marked **UNVERIFIED**.

---

## Ranking table

| # | Lab | PI | Relevance to this project | HS evidence (verified) | Fit (1–10, est.) | Best way in |
|---|-----|----|---------------------------|------------------------|------------------|-------------|
| 1 | UC Santa Cruz, Autonomous Systems Lab (ASL) | Gabriel Elkaim | Very high. Low-cost Raspberry Pi + ROS 2 + Nav2 differential-drive robot; UGV navigation; lab's stated aim is cutting autonomy cost via open source | **Strong.** ASL-mentored projects in UCSC's HS Scholar Immersion Program (SIP) in 2024, 2025 and 2026 | **9** | SIP 2027 application (portal Jan 15 – Feb 26, 2027) plus a short note to Elkaim with your demo |
| 2 | UC Merced Robotics Lab | Stefano Carpin | Very high. Mobile/multi-robot planning; ROS 2 Nav2 for outdoor agriculture (ICRA 2024); CASE Best Paper 2018; RA-L associate editor; publishes at ICRA/IROS/CASE | None found (CV lists undergrad interns only) | **7.5** | Cold e-mail with a 60-s video + cost/measurement table; ask one concrete question about evaluation design for a CASE/ICRA-workshop paper |
| 3 | Santa Clara Univ. Robotic Systems Lab (RSL) | Christopher Kitts | High. Multi-robot land rovers, modular rover (IMECE 2023), agricultural robots, ultra-low-cost devices; undergraduate-staffed, education-focused lab | None found. SCU's free HS program (SES) excludes students with prior engineering exposure | **7.5** | Cold e-mail or ask to visit the lab (RSL page invites contact or visits); offer a demo |
| 4 | UCLA LEMUR (Laboratory for Embedded Machines and Ubiquitous Robots) | Ankur Mehta | High. Cheap, printable robots ("Towards One-Dollar Robots"); LiDAR odometry; multi-robot localization | None on lab pages (join page covers undergrad and grad only). UCLA's HS Summer Research Program (HSSRP) is documented (2017 paper) but its 2027 status is UNVERIFIED | **7.5** | Follow the lab's own join format (interests, past-project links, CV); ask for feedback, not a position |
| 5 | SJSU, Wencen Wu group (Computer Eng.) | Wencen Wu | Medium-high. Multi-robot / mobile sensor networks; small-scale autonomous parking vehicle (2021); NSF cooperative-perception project | Partial: her NSF project page lists K-12 engagement through an "Engineering Ambassadors" program | **7** | Cold e-mail referencing the autonomous-parking vehicle paper; ask for feedback on the localization/docking evaluation |
| 6 | UC Santa Cruz, other SIP robotics hosts | Nobby Kobayashi (UGV traversability), Ricardo Sanfelice (manipulator obstacle avoidance), Daniel Fremont (RL robustness for autonomy) | Medium–high (Kobayashi most relevant: off-road UGV) | **Strong:** listed as SIP 2026 faculty advisors | **7** | SIP 2027 (projects posted in 2027) |
| 7 | SJSU Robotics, Sensor & Machine Intelligence Lab (Mech. Eng.) | Winncy Du | Medium. Sensors, mechatronics, pipe-climbing and mobile sensing robots. Good match for the mechanical student | None specific (ASME Diversity & Outreach Award, 2004) | **6** | Cold e-mail focused on the hitch mechanism and sensor design |
| 8 | UCLA RoMeLa | Dennis Hong | Medium. Mechanisms, novel mobile locomotion; DARPA Urban Challenge history | UNVERIFIED (site blocks automated access) | **5.5** | Low odds; only if you have a standout mechanism video |
| 9 | USC Viterbi SHINE (program) | Various USC faculty | Medium (robotics is one listed field) | Historically strong (7-week HS lab immersion), but **not listed** on USC Viterbi K-12's 2026 summer page, so 2027 status is UNVERIFIED | **5** | Check in Dec 2026 whether SHINE runs in 2027 |
| 10 | UCSD REHS (San Diego Supercomputer Center) | SDSC mentors | Low–medium (computational projects, not robot hardware) | **Strong:** 17th annual HS program in 2026 | **5** | Only if you live in Southern California (residency rule) |
| 11 | SF State engineering labs | Zhuwei Qin (edge DL on mobile devices), Sanchita Ghose (computer vision), David Quintero (wearable robots for people with limited mobility), Alyssa Kubota (HRI) | Low–medium. No mobile/outdoor robot lab found | None found. Their summer program (STARS) is for community-college students only | **4.5** | Qin or Ghose for perception-on-cheap-compute advice |
| 12 | UC COSMOS (program, 6 UC campuses incl. UCSC, UCLA, UC Merced) | — | Low (course-based, not lab placement) | Strong (CA HS program) | **4** | Application Jan 6 – Feb 5, 2027 (clashes with the build crunch) |
| 13 | UC Davis Young Scholars Program | — | Low (biological, agricultural and environmental sciences) | Strong (≈40 HS students, 6 weeks) | **3** | Not recommended for this project |
| 14 | UC Irvine (St. Margaret's–Samueli internship) | e.g., David Reinkensmeyer (MAE) | Low | Yes, but tied to one partner school | **2** | Not open to outside students as described |

**National notes (verified, lower priority):** MIT Beaver Works Summer Institute (rising seniors, nationwide, AI and autonomy topics). Yale Social Robotics Lab has a dedicated HS-intern page but says "not offered in 2026." UW Human-Centered Robotics Lab hosted an HS intern in 2015. Univ. of Maryland Robotics Center "Pathways" program listed HS students but is "paused until further notice." Details are at the end.

---

## Per-lab sections

### 1. UC Santa Cruz: Autonomous Systems Lab (Prof. Gabriel Elkaim), through the Scholar Immersion Program (SIP)

**Relevant research**
- Lab page: https://asl.soe.ucsc.edu/home. Focus: guidance, navigation and control, path planning, computer vision and sensor fusion for autonomous systems. The site says a key objective is reducing autonomous-system costs through open-source development, which matches the "cheaper and proven" theme. Platforms include the Autoboat (solar autonomous surface vessel) and Overbot (2005 DARPA Grand Challenge vehicle) (https://asl.soe.ucsc.edu/research).
- Current work, shown through SIP project listings (more current than the lab's own publication page, whose listings are mostly older):
  - **SIP 2026, CSE-11:** "Embedded AI and Navigation on a Differential-Drive Robot using Raspberry Pi, ROS 2, and Docker." Interns evaluate Raspberry Pi AI HAT+ / AI HAT+2 accelerators and build a Nav2 navigation workflow on a real differential-drive robot. Faculty advisor: Gabriel Hugh Elkaim. 3 interns. https://sip.ucsc.edu/2026-research-projects/
  - **SIP 2024, ELE-05:** "A Unified Guidance Navigation and Control (GNC) Framework for Autonomous Ground Vehicle Navigation in Unstructured Environments." UCSC faculty contact: Prof. Gabriel Elkaim. 6 interns. https://sip.ucsc.edu/2024-research-projects/
  - **SIP 2025, CSE-04:** "Graph-Based SLAM Simulation in Python for Differential Drive Robots" (lab URL given: ASL). **SIP 2025, ELE-05:** autonomous ground vehicle mini-robot built with Python, RViz and Gazebo. https://sip.ucsc.edu/2025-research-projects/
- Representative peer-reviewed papers: the lab's bibliography page (https://asl.soe.ucsc.edu/biblio) lists mostly pre-2012 work, e.g., Choi, Curry, Elkaim, "Curvature-Continuous Trajectory Generation with Corridor Constraint for Autonomous Ground Vehicles," IEEE CDC 2010. I could not verify more recent ASL papers.

**Evidence of HS students:** **Strong.** ASL mentors ran SIP projects for high-school interns in 2024, 2025 and 2026 (links above). SIP is UCSC's HS research program, renamed from "Science Internship Program" to "Scholar Immersion Program" in August 2026 (https://sip.ucsc.edu/).

**How to approach**
- **Formal:** SIP 2027 (https://sip.ucsc.edu/applying-to-sip/). Eligibility: ages 14–17 during the program and not yet graduated by summer 2027. Portal opens **Jan 15, 2027**; deadline **Feb 26, 2027 (noon PT)**; references due Mar 5; rolling admissions from Apr 9. Online research week Jun 14–17; in person Jun 21 – Aug 6, 2027. Application fee $68 (waivers available). Tuition to be posted by Dec 2026. Need-based scholarships cover 25–100%; no stipend mentioned. 2027 projects will be posted in 2027 (https://sip.ucsc.edu/2027-research-projects/). The site also has an interest form.
- Some SIP projects require age 16+ for lab/field safety (seen on a 2026 project listing).
- **Direct:** a brief note to Prof. Elkaim through his official UCSC page / ASL site. Say you plan to apply to SIP and ask whether a short feedback call on your Nav2/Pi-based design is possible before March.

**What they'd want to see** (SIP's stated criteria: interest level, motivation, analytical thinking and **programming experience** for computational projects; preference for returning students and full-time 8-week commitment). For ASL specifically (my inference from the 2026 project): ROS 2 / Nav2 familiarity, Raspberry Pi + Docker, and a cost-vs-performance table for an embedded perception pipeline. Your robot is essentially the same stack, which is a strong match.

**Fit: 9/10. Engagement likelihood:** medium-high for summer 2027 through SIP; low-to-medium for advice before March. **Why:** the stack and cost focus match closely, and the lab has three straight years of HS mentoring. The risk is that SIP comes after your paper deadline and the lab's public site is not actively maintained.

---

### 2. UC Merced Robotics Lab (Prof. Stefano Carpin)

**Relevant research**
- Lab: https://robotics.ucmerced.edu/ (blocks automated fetch; an archived copy from May 2026, http://web.archive.org/web/20260514143154/https://robotics.ucmerced.edu/, confirms it was established in 2007 by Carpin, works on multi-robot systems and robot algorithms, is part of the NSF IoT4Ag precision-agriculture center, and that "each summer undergraduate students intern in the robotics lab").
- Bio: https://sites.ucmerced.edu/scarpin/bio. Professor of CSE, founder and director of the lab; IEEE Senior Member; CASE 2018 Best Paper; associate editor for IEEE RA-L (previously T-RO and T-ASE); regular ICRA/IROS/CASE committee member.
- Representative recent papers (from his CV, https://sites.ucmerced.edu/files/scarpin/files/documents/carpincvonline.pdf):
  - E. Sani, A. Sgorbissa, S. Carpin, "Improving the ROS 2 navigation stack with real-time local costmap updates for agricultural applications," ICRA 2024, pp. 17701–17707. *Directly relevant: Nav2 in outdoor, unstructured settings.*
  - A. Shamshirgaran, S. Carpin, "Environmental map learning with multiple-robots," ICRA 2025.
  - Several IEEE CASE 2025 papers (e.g., Zuzuárregui & Carpin, GNN-powered MCTS for stochastic orienteering). **CASE is one of your candidate venues.**

**Evidence of HS students:** **No evidence found.** The CV lists undergraduate, MS, PhD and visiting students, plus NASA Swarmathon undergrad teams, but no high-school students.

**How to approach:** no formal HS program found at the lab. UC Merced is a COSMOS campus (https://cosmos-ucop.ucdavis.edu/app/main), but COSMOS is course-based, not a placement in this lab. Use direct contact through the official bio page or lab site. Keep it short, name his ICRA 2024 Nav2 paper, and ask one precise question (e.g., "Is success rate over N trials across surface/slope/lighting conditions plus a cost breakdown a credible evaluation for CASE?"). Do not ask for lab space.

**What they'd want to see (inferred):** a robot that already moves, rigorous trial counts, a clear baseline, and evidence that you understand Nav2 costmaps and localization limits outdoors. Short video + one-page results table.

**Fit: 7.5/10. Engagement likelihood:** low-to-medium. **Why:** his topics and venues fit best of any PI here (outdoor Nav2, CASE/ICRA). But he is an Associate Dean with a large PhD group, there is no HS track record, and Merced may be far from you.

---

### 3. Santa Clara University: Robotic Systems Laboratory (Prof. Christopher Kitts)

**Relevant research**
- Lab: https://www.scu.edu/engineering/labs--research/labs/robotic-systems-lab/. Field robotics for scientific discovery, technology validation and **engineering education**. 100+ undergrad and grad students per year. Current projects include the **ultra-low-cost** Jaipur prosthetic hand, agricultural robots (four modular robots with precision spraying), a robotic workcell, NASA ACS3 solar-sail mission operations, and marine profilers. The page invites interested people to "contact the director or visit the lab."
- Faculty page: https://www.scu.edu/engineering/academic-programs/department-of-mechanical-engineering/faculty-and-staff/faculty-by-research-area/kitts.html. Underwater vehicles, **clusters of land rovers**, aircraft, spacecraft; multi-robot coordination; model-based anomaly management.
- Representative papers:
  - S. Hart, J. Kamenetsky, C. Kitts, "Dynamic Elliptical Shaping Control for Swarm Robots," *IEEE Access* 11, 2023; S. Hart, C. Kitts, "Unifying Control Architecture for Reactive Particle Swarms," *IEEE/ASME T-Mech* 2022. Both from https://www.scu.edu/engineering/labs--research/labs/robotic-systems-lab/research--publications/
  - Sharma & Kitts, "Modular and Reconfigurable Multiple Drive-Unit Based Rover – Design and Control," IMECE 2023 (published Feb 2024): https://asmedigitalcollection.asme.org/IMECE/proceedings/IMECE2023/87592/V002T02A002/1195567 . *Relevant to a modular, cheap drive base.*

**Evidence of HS students:** **No evidence found** for the lab. SCU's Summer Engineering Seminar (https://www.scu.edu/engineering/beyond-the-classroom/outreach/summer-engineering-seminar-ses/) is free and residential for sophomores and juniors (2026 sessions in July; deadline Mar 31, 2026). It targets students with limited resources who have **not** been exposed to engineering, so this team likely does not qualify, and it is not a lab placement anyway.

**How to approach:** direct contact through the faculty/lab page, which explicitly invites contact or visits. Ask to show a 5-minute demo or to get feedback on hitch/drive-base design from a student team member.

**What they'd want to see (inferred from lab culture):** working hardware, field-test video, practical engineering trade-offs, and a cost-per-capability table. They value low-cost humanitarian and field systems.

**Fit: 7.5/10. Engagement likelihood:** medium. **Why:** an education-focused, hands-on, undergrad-staffed field-robotics lab with low-cost and humanitarian work is a natural friendly reviewer. There is no HS track record, and Kitts is also an associate dean.

---

### 4. UCLA: LEMUR (Prof. Ankur Mehta, Electrical & Computer Engineering), plus the UCLA HSSRP program

**Relevant research**
- Lab: https://uclalemur.com/. Printable robotics, rapid design and fabrication, affordable and accessible robots. Open-source "paperbot" designs. People: https://uclalemur.com/people (Mehta: Associate Professor and Samueli Fellow).
- Representative papers (https://uclalemur.com/publications):
  - W. Yan, A. Mehta, "Towards One-Dollar Robots: An Integrated Design and Fabrication Strategy for Electromechanical Systems," *Robotica*, 2020. *Strongly matches the "cheaper" thesis.*
  - K. Chen, B. T. Lopez, A. Agha-mohammadi, A. Mehta, "Direct LiDAR Odometry: Fast Localization With Dense Point Clouds," *IEEE RA-L*, 2022.
  - T.-K. Chang, K. Chen, A. Mehta, "Resilient and Consistent Multirobot Cooperative Localization With Covariance Intersection," *IEEE T-RO*, 2022.

**Evidence of HS students:** **None found on lab pages.** The people page has "Undergrads and summer students" but no HS students are identified. At UCLA level, the **High School Summer Research Program (HSSRP)** is documented in Kittur, Shaw, Herrera, *Journal of STEM Education* 18(4), 2017 (https://jstem.org/jstem/index.php/JSTEM/article/download/2183/1881/7494). It was 8 weeks for **rising seniors** placed in labs across all seven UCLA engineering departments, including Mechanical & Aerospace and Electrical Engineering. It was free except optional housing, with small stipends for low-income students. Selection used transcript, personal statement, recommendation letters and department ranking, and faculty pick from a pre-selected pool. UCLA engineering's HS outreach page (https://www.seasoasa.ucla.edu/high-school-1/) still links an HSSRP page (esc.seas.ucla.edu), but that page returned HTTP 403 when fetched, so **2027 status is UNVERIFIED**.

**How to approach:** LEMUR's join page (https://uclalemur.com/people/join) is for undergrads. It asks for an e-mail with academic/career interests, **links to or descriptions of past projects**, a CV (PDF) and an informal transcript. Mirror that format but ask for feedback, not membership. For summer, check in Dec 2026 – Jan 2027 whether HSSRP runs.

**What they'd want to see (from join page + inference):** links to past projects (GitHub, video), a CV, and a crisp cost-vs-performance claim. A "dollar-per-function" breakdown of your hitch and drive base fits their interests.

**Fit: 7.5/10. Engagement likelihood:** low-to-medium. **Why:** the thesis match ("one-dollar robots") is strong, but there is no HS evidence and the lab is large and busy.

**Also at UCLA:** **RoMeLa (Prof. Dennis Hong)**, https://romela.org/ and https://www.mae.ucla.edu/laboratories/. Humanoids and novel mobile locomotion; DARPA Urban Challenge 3rd place. HS policy UNVERIFIED (the site blocks automated access). Low odds unless your mechanism is visually striking. Fit 5.5.

---

### 5. San José State University: Prof. Wencen Wu (Computer Engineering)

**Relevant research**
- Official page: https://www.sjsu.edu/people/wencen.wu/. Professor (Computer Engineering); robotics + ML + estimation + control in cyber-physical systems. Group site: https://sites.google.com/sjsu.edu/wencen/research. Projects include **Swarming Cyber-Physical Systems** (NSF CPS, multi-robot), **Distributed Parameter Systems with Mobile Sensors** (NSF CMMI), and **NSF RINGS cooperative perception** for autonomous vehicles at intersections.
- Representative papers (https://sites.google.com/sjsu.edu/wencen/publications):
  - T. Yu, W. Lu, Y. Luo, C. Niu, W. Wu, "Design and Implementation of a Small-scale Autonomous Vehicle for Autonomous Parking," IEEE CACRE 2021. *Close to your docking/parking problem.*
  - Z. Zhang, S. T. Mayberry, W. Wu, F. Zhang, "Distributed Cooperative Kalman Filter … for Mobile Sensor Networks," *Frontiers in Robotics and AI*, 2023.

**Evidence of HS students:** **Partial.** Her research page says the NSF CMMI mobile-sensor project included **K-12 engagement through an Engineering Ambassadors program**. I found no HS lab members or HS co-authors.

**How to approach:** direct contact through her official SJSU page. Cite the autonomous-parking paper. Ask for feedback on how to evaluate the "drive into and latch onto the bin" maneuver (pose error, success rate), which is close to automated parking.

**What they'd want to see (inferred):** a clear estimation/control formulation (e.g., how you estimate bin pose and close the loop), quantitative error metrics, and clean code.

**Fit: 7/10. Engagement likelihood:** medium. **Why:** relevant small-vehicle autonomy work, a teaching-focused CSU campus in the Bay Area, and documented K-12 outreach. Less outdoor-field focus than Carpin or Kitts.

---

### 6. UC Santa Cruz: other SIP robotics hosts

- **Nobby Kobayashi:** faculty advisor, SIP 2026 ECE-08 "Unmanned Autonomous Ground Vehicle Terrain Traversability for Unstructured Environments" (traversability, SLAM uncertainty, slip/slope) (https://sip.ucsc.edu/2026-research-projects/). Relevant to driveway slopes and curb transitions.
- **Ricardo Sanfelice:** faculty advisor, SIP 2026 ECE-04 "Obstacle Avoidance for Robotic Manipulators" (same page).
- **Daniel Fremont:** faculty advisor, SIP 2026 CSE-04 on RL robustness for autonomous agents (same page).
- **HS evidence:** strong (all are SIP 2026 hosts). **Approach:** SIP 2027 only. **Fit: 7/10.**

---

### 7. San José State University: Prof. Winncy Du (Mechanical Engineering)

- **Research:** director of the Robotics, Sensor, and Machine Intelligence Laboratory. Sensors, robotics, mechatronics, automation and control, with emphasis on health care (https://www.sjsu.edu/people/winncy.du/index.html; bio: https://www.sjsu.edu/people/winncy.du/bio/index.html). Projects include an NSF-sponsored pipe-climbing inspection robot, a mobile sensory robot for hospital emergency rooms, and an aerial robotic sensor network (https://www.sjsu.edu/people/winncy.du/research/). Author of *Resistive, Capacitive, Inductive, and Magnetic Sensor Technologies* (CRC Press). Representative paper: Du et al., "Design of a GMR Sensor Array System for Robotic Pipe Inspection," IEEE Sensors 2010 (https://www.sjsu.edu/people/winncy.du/publications/; the list shown mostly ends around 2016).
- **HS evidence:** no direct evidence found. Received the International ASME Diversity & Outreach Award (2004) and repeated ASME student-section advisor awards (bio page).
- **Approach:** direct e-mail from the **mechanical student**, focused on the hitch/latch mechanism and its sensing (contact/force/limit switches, load measurement).
- **What they'd want to see (inferred):** mechanism drawings, sensor selection rationale, bench-test data.
- **Fit: 6/10. Likelihood:** medium for a mentoring conversation; low for co-authorship.

---

### 8. San Francisco State University

- **Labs** (https://engineering.sfsu.edu/research-labs-and-centers): CARE Lab (David Quintero; wearable robotic systems for people with limited mobility), PHAST Lab (Alyssa Kubota; HRI / assistive technology), ICE Lab (Xiaorong Zhang; embedded systems, human-machine interfaces), MIC Lab (Zhuwei Qin; deep-learning acceleration on mobile/edge devices), AI-LAMP (Sanchita Ghose; multimodal perception / computer vision), Rapid Prototyping Lab (Kwok-Siong Teh). **No mobile/outdoor robot lab found.**
- **HS evidence:** none found. The summer program **STARS** (https://engineering.sfsu.edu/2025-sf-state-university-summer-training-academy-research-scholars-stars-program) is for California **community-college** students aged 18+ ($4,000 stipend, 2026 cycle), not high schoolers.
- **Approach:** for perception-on-cheap-hardware advice only, contact Qin (MIC Lab) or Ghose (AI-LAMP).
- **Fit: 4.5/10.**

---

### 9. Other California programs (verified status)

| Program | What it is | Key facts (verified) | Fit |
|---|---|---|---|
| **UCSD REHS** (https://education.sdsc.edu/studenttech/rehs/) | Computational research with UCSD faculty/postdoc mentors | 2026 cycle: age ≥16 by Jun 15; finished 10th–12th grade; GPA ≥3.0; **Southern California residents**; Jun 8 – Jul 31, 2026; applications Feb 15 – Mar 15, 2026; $2,000 registration, need-based scholarships. 2027 dates not yet posted. | 5 |
| **USC Viterbi SHINE** | 7-week immersion in a USC professor's lab | A third-party review (https://www.lumiere-education.com/post/usc-viterbi-shine-2023-our-review) describes 7 weeks, freshmen–juniors, GPA ≥3.4, Feb deadline. **Not listed** on USC Viterbi K-12's 2026 summer-programs page (https://viterbik12.usc.edu/summer-programs-4/), so 2027 status is UNVERIFIED. | 5 |
| **UC COSMOS** (https://cosmos-ucop.ucdavis.edu/app/main) | 4-week residential STEM courses at UCD, UCI, UCLA, UC Merced, UCSD, UCSC | CA students finishing grades 8–12; GPA ≥3.5; **2027 application Jan 6 – Feb 5, 2027**. Course-based, not lab placement. | 4 |
| **UC Davis Young Scholars Program** (https://education.ucdavis.edu/young-scholars-program) | ~40 HS students, 6 weeks with research mentors | Focus: biological, agricultural, environmental, natural sciences; 2026 ran Jun 21 – Aug 1. Engineering/robotics not mentioned. | 3 |
| **UC Irvine St. Margaret's–Samueli internship** (https://engineering.uci.edu/news/2016/10/high-school-students-gain-research-experience-through-internship-program) | 6-week internships in UCI engineering labs (2016 article: 12th year) | Tied to one partner school; hosts included Reinkensmeyer (MAE). Not an open program. | 2 |

Stanford, UC Berkeley and Cal Poly: I **could not verify** a robotics-lab placement program for high-school students before the search budget ran out. The Stanford AI4ALL page linked by a third-party list returned "not found."

---

### 10. National notes (lower priority; verified status)

- **MIT Beaver Works Summer Institute** (https://bwsi.mit.edu/): for high-achieving students entering senior year, nationwide; AI, autonomy, radar, satellites and more. 2027 dates not posted.
- **Yale Social Robotics Lab** HS internship page (https://scazlab.yale.edu/prospective-students/prospective-high-school-interns): "Summer internship program not offered in 2026."
- **UW Human-Centered Robotics Lab** (https://hcrlab.cs.washington.edu/news/2015/08/summer-2015-interns/): a high-school intern built a prototype phone-repositioning arm in summer 2015 (old evidence).
- **Univ. of Maryland Robotics Center Pathways** (https://robotics.umd.edu/education/pathways-program): lists HS students, but the program is "currently paused until further notice."

---

## Outreach plan (Oct 2026 – Feb 2027)

**Principle:** ask for **advice on a specific question**, not for lab space or co-authorship. One e-mail per PI, one follow-up, then stop. Include a parent or teacher in the loop (you are minors, and many labs require 16+ and safety training for on-site work).

| When | Action | What to send |
|---|---|---|
| **Oct 6–17** | Prepare the assets once and reuse them | (1) One-page project brief (PDF): problem, cost target vs. existing approaches, planned measurements, baseline. (2) 30–60 s video of anything that moves: a teleop chassis pushing or towing a cart is enough. (3) Public GitHub/README with a bill of materials and cost table. (4) A one-line "specific question" tailored to each PI. |
| **Oct 20–31** | **Wave 1** cold e-mails: Carpin (UC Merced), Kitts (SCU), Wu (SJSU), Mehta (UCLA LEMUR) | Brief + video link + tailored question. LEMUR: follow their join format (interests, past-project links, CV). Fill out the UCSC SIP interest form. |
| **Nov 3–14** | One polite follow-up to non-responders (7–10 days later). **Wave 2:** Elkaim (UCSC ASL), Du (SJSU, from the mechanical student), optionally Qin/Ghose (SFSU) | Same assets, updated with any new progress |
| **Late Nov – early Dec** | Whoever replies: book a 15–20 min call. Before it, send your draft experiment design (trials, conditions, metrics, baseline). Afterwards, send a thank-you note with what you changed. | Experiment-design one-pager |
| **Dec (build starts)** | Short progress update to responsive mentors only (≤5 lines + 30 s clip) | First hitch/dock attempt video; first cost number |
| **Early–mid Jan** | Preliminary data update: success rate over N trials, localization error, cost breakdown. Ask one question about the analysis or ablation. **Apply to COSMOS (Jan 6 – Feb 5)** only if you want it; it clashes with the build. | Results table + plot |
| **Jan 15 – early Feb** | **Submit the SIP 2027 application early** (portal opens Jan 15; deadline Feb 26, noon PT). Request recommenders by mid-January (references due Mar 5). Check whether UCLA HSSRP and USC SHINE run in 2027. | SIP application; mention your bin-robot project and data |
| **~Feb 8–12** | Send the near-final draft to one responsive mentor with a two-week window, asking for "one round of comments." Credit them in the Acknowledgments. Co-authorship only if they make substantive intellectual contributions (IEEE authorship norms). | Draft PDF |
| **Mar 1–2** | Submit. Send a thank-you plus the submitted PDF to everyone who helped. | — |
| **Mar – May** | Follow up with SIP / summer-program hosts using the submitted paper as your credential | Paper + demo video |

### Cold e-mail outline (no personal data; keep it under ~150 words)

1. **Subject:** "HS robotics project: question on [specific topic] (low-cost bin-to-curb robot)"
2. **Greeting:** "Dear Prof. [Last name],"
3. **Who (1 sentence):** "We are two high-school students at [school, city] building a low-cost robot that moves unmodified 64/96-gallon trash carts from garage to curb."
4. **Claim (1–2 sentences):** what is cheaper than existing approaches and how you will measure it (target cost, success rate over N trials, positioning error at the curb).
5. **Why them (1 sentence):** name **one specific paper or project** of theirs and the link to your problem (e.g., Carpin: ROS 2 costmaps outdoors, ICRA 2024; Wu: small-scale autonomous parking, CACRE 2021; Mehta: "Towards One-Dollar Robots"; Elkaim: Raspberry Pi + Nav2 SIP robot).
6. **The ask (1 sentence):** one concrete question, plus "Would you or a student in your group have 15 minutes for feedback, or be willing to reply by e-mail?"
7. **Links (not attachments):** 1-page brief, 60-s video, GitHub README.
8. **Logistics (1 sentence):** "Our [teacher/parent] is aware of the project; we are submitting to [venue] by March 1, 2027."
9. **Close:** thank them and give your names and school. Use a school or project e-mail address. Do not include phone numbers or home addresses.

---

## Bottom line

- **Best HS-ready match:** UCSC ASL (Elkaim) through SIP 2027. It has a verified three-year record of HS projects on almost exactly your stack (Raspberry Pi + ROS 2 + Nav2 differential-drive robot, UGV navigation).
- **Best topical advisors for the paper itself:** Carpin (UC Merced; outdoor Nav2, CASE/ICRA) and Kitts (SCU; low-cost field rovers, education-focused). Neither shows HS evidence, so pitch a short, specific feedback request.
- **Thesis-aligned long shot:** Mehta (UCLA LEMUR, "one-dollar robots"). Check UCLA HSSRP's 2027 status in December.
- **Accessible Bay Area option:** Wencen Wu (SJSU). Small autonomous-vehicle work and K-12 outreach history.

---

### Removed during verification

None. Every entry could be verified.

### Link verification (2026-10-03)

- **URLs checked:** 44 unique URLs (plus 1 archive link added as a correction).
- **OK:** 43. Five returned 403/406/timeouts to plain curl and were confirmed another way: ASME IMECE paper (DOI 10.1115/imece2023-112155 resolves to that URL; Crossref confirms title, authors Sharma & Kitts, published online Feb 5, 2024), robotics.ucmerced.edu (Wayback snapshot, May 2026), viterbik12.usc.edu (WebFetch), jstem.org PDF and romela.org (retry with browser headers). Content of every paper, program and central claim was checked against the page.
- **Fixed:** 1 broken link (Wencen Wu SJSU faculty page, 404, replaced with her official SJSU people page). Text corrections: Wu's rank is Professor, not Associate Professor; CARE Lab description changed to match the SFSU page ("low-cost" was not stated); the UC Merced lab claim is now backed by an archived copy rather than a search snippet.
- **Removed:** 0.
- **Confirmed only via search snippet:** 0.
