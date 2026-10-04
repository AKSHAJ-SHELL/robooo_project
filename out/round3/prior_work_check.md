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

## 3. Wanderland (arXiv 2511.20620 v2, CVPR 2026), read in full

**What it does.** Captures 530 indoor/outdoor urban scenes (NYC, Jersey City) with a handheld MetaCam scanner: Livox Mid-360 lidar, IMU, RTK-GNSS and two fisheye cameras at 1 FPS. LIV-SLAM gives metric poses and point clouds; 3DGS is initialized from the point cloud and trained with a depth loss; collision meshes come from the lidar cloud; everything runs in Isaac Sim. It shows that vision-only pipelines (Vid2Sim, GaussGym, COLMAP, VGGT and others) give worse poses, meshes and novel views, and that policies trained or evaluated in Vid2Sim-style environments behave differently from ones in Wanderland environments.

**The key question: did it run a real robot? No.** Every navigation result (Tables 4–5, Fig. 7) is in simulation. "Evaluation reliability" is argued by comparing two simulators to each other: all policies score lower success and more interventions in Vid2Sim-built environments than in Wanderland's. There is no real-robot ground truth, no sim-vs-real correlation and no SRCC, even though it cites Kadian et al. [61]. Which simulator is closer to reality is never measured.

**Other facts relevant to E1.v2:**
- **Camera/capture height is never varied or discussed.** The scanner is handheld (roughly human height). The paper doesn't state the simulated agent's camera height; the released code puts it at about 1.1 m (checked earlier).
- **Extrapolated views degrade.** The paper's own motivation is that rendering quality drops for viewpoints away from the capture path, and it holds out "extrapolation trajectories" to measure this. But its extrapolation views come from the same handheld device. A 30 cm robot camera is exactly this kind of extrapolation, in the vertical direction, which the paper doesn't test.
- **Image metrics disagree with each other.** On extrapolated views (Table 3), Vid2Sim has *better* LPIPS than Wanderland (0.371 vs 0.445) but worse PSNR (16.49 vs 17.92). Fig. 6 then argues qualitatively that Vid2Sim's DINOv3 features diverge from the real image, which "can confuse end-to-end navigation policies that rely on DINO features" such as CityWalker. That is an untested claim, and it's exactly E1's co-primary question: do image metrics predict how much the policy's output moves?
- **Same policies as E1.** It benchmarks CityWalker and MBRA (the LogoNav paper) zero-shot. Outdoor success is low (SR 0.21 and 0.22, Table 5). Warning for E1: expect weak closed-loop performance, which is why the open-loop divergence D is the primary result and the October floor check matters.

## Net effect on E1.v2 after all three papers

- **E1's central gap is confirmed.** None of the three papers runs a real robot against a splat twin for navigation, varies capture height, or tests image metrics against policy-output divergence. Wanderland, the closest navigation paper, argues reliability only sim-vs-sim.
- **Sharper pitch for the paper:** "Wanderland shows that phone/video twins and lidar-grounded twins give different navigation scores, but never checks either against a real robot. The Kaedim study checks against a real robot, for manipulation, changing everything at once. We test one factor, capture height, for a 30 cm navigation robot, against real runs, and ask whether the image metrics these papers report (PSNR/SSIM/LPIPS/DINO) predict policy-output divergence."
- **Use Wanderland's own numbers as motivation:** its LPIPS-vs-PSNR disagreement on extrapolated views and its untested DINOv3 claim.
- **No remaining "verify before you commit" papers.** Residual risk is only papers published after these; repeat a Scholar search for "real-to-sim navigation evaluation Gaussian splatting real robot" before submission.
