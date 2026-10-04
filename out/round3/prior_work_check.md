# Prior-work check for E1.v2 (papers supplied by the user, 2026-10-04)

Two of the three "verify before you commit" papers were read in full from text the user pasted.

## 1. Kaedim reconstruction-fidelity paper (very likely arXiv 2610.00731, "Measuring Asset and Scene Reconstruction Effects in Real-to-Sim Robot Evaluation"; the pasted text has no title, so the ID match is by content)

**What it does.** One bimanual manipulation cell (I2RT YAM), 5 tasks × 2 policies (π0.5, MolmoAct2) = 10 cells, 20 sim trials per cell per reconstruction, 200 real trials graded by a third party (Robocurve). Two reconstructions built from the same photos and video: "authored" (metric-scale object geometry from a ChArUco board, per-object physics, their own 3DGS scene) vs "default" (TRELLIS single-image meshes, PhysX default physics, PolaRiS-style 2DGS scene). Authored: r = 0.90, score error 6.97 pp. Default: r = 0.51, score error 17.54 pp. Only score error and progress disagreement separate significantly; correlation does not (CI on the difference includes zero with 10 cells).

**Overlap with E1.v2.** Same broad question: does how you reconstruct the twin change how well sim tracks real? It is the closest prior work found and must be cited.

**What it does not do (E1.v2 stays open):**
- Manipulation, indoor, one fixed robot cell. E1 is outdoor sidewalk navigation.
- Nothing about **camera or capture height**. Its camera heights (0.72/0.88 m) are matched between sim and real.
- No comparison of **policy outputs on paired real vs rendered frames** (E1's divergence D), no image metrics vs agreement (E1's S1), no **real-vs-real test-retest floor**.
- All factors change at once (geometry, scale, physics, scene). The authors list this as their first limitation and propose one-factor-at-a-time follow-up. E1 changes exactly one factor (capture height). Use this as a selling point.
- Industry-funded, authors' own pipeline vs a baseline they built themselves (they disclose this).

**What to take from it:**
- Its agreement measures (score error on cell means, progress disagreement, failure-stage TVD) and its paired-on-cell bootstrap are a ready template for E1's closed-loop C1 analysis.
- Its finding that 10 cells cannot separate correlations is direct evidence for E1's choice to make the open-loop D analysis primary and to cluster by site/route.
- Its configuration gate (reject any run whose camera height, step budget, etc. drifted) is worth copying: it caught 6 runs rendered at the wrong camera height.
- New references to cite: SimFoundry (arXiv 2606.28276), Wang et al. "A Practical Recipe Towards Improving Sim-and-Real Correlation for VLA Evaluation" (arXiv 2606.10366), SIMPLER (2405.05941) and its MMRV metric.

## 2. NavDP (arXiv 2505.08712 v3)

**What it does.** A navigation diffusion policy trained only in simulation (BlenderProc renders of 3,000 indoor scenes), RGB-D input, point-goal and no-goal tasks. Camera height is **randomized from 0.25 to 1.25 m** during training. Real-world tests: 10 episodes per robot per task on TurtleBot4, Go2, G1.

**The claim we were checking.** A reviewer's snippet said NavDP's real-to-sim evaluation is "consistent with real-world evaluation". **That sentence is not in the v3 text.** v3 has no real-to-sim (splat) evaluation and no sim-vs-real correlation at all. The claim may come from a different version or a project page, but it should not be cited from this paper.

**Relevance to E1.v2:**
- Supports the motivation: NavDP's own ablation (Q5) shows camera height matters. A model trained only on low cameras (< 0.5 m) dropped from 90% to 20% success on the tall robot. Height is a known factor for policies; E1 asks whether it is also a factor for **twin capture**, which NavDP does not touch.
- NavDP would be an interesting third policy, as a height-robust contrast to CityWalker (human-height training data). But it needs depth input, which E1's RGB-only robot camera and splat renders would have to supply, and its license (CC-BY-NC-SA) and availability were flagged earlier. **Keep it out of the core study**; mention it as future work.

## Net effect on E1.v2

- The narrow claims (capture-height manipulation at 30 cm; policy-output divergence vs image metrics against a real-vs-real floor; SRCC for sidewalk navigation models with test-retest) are **still open** after both papers.
- Framing must change: E1 is no longer the only "reconstruction choices affect sim-real agreement" study. Position it as the **single-factor, navigation, low-viewpoint** counterpart to the Kaedim study's all-at-once manipulation comparison.
- Still unread: the **Wanderland** paper PDF (does it include real-robot runs?).
