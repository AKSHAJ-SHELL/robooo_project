"""Cluster-aware power simulation for E1.v2 (all effect sizes are ASSUMPTIONS, to be
re-estimated from the Dec pilot).

H1 (primary, open-loop): per-frame policy-output divergence D (waypoint L2 between policy on
real frame and policy on twin render at the same pose) is larger for human-height twins (T_H)
than robot-height twins (T_R).  Data: frames nested in drives, routes, sites.

C1 (confirmatory, closed-loop): the |twin - real| gap in a continuous closed-loop outcome is
larger for T_H than T_R.  Compares the v1 design (8 routes x 3 starts, no retest) with the
v2 design (16 routes at 8 sites x 1 start x 2 real repeats).

Run: python3 e1v2_power.py
"""
import numpy as np
from scipy import stats

rng = np.random.default_rng(7)
NSIM = 2000


def sites_for(n_routes, n_sites):
    return np.arange(n_routes) % n_sites


def site_perm_p(diff_by_site, nperm=2000):
    """Sign-flip permutation test at the SITE level (clusters = sites)."""
    obs = diff_by_site.mean()
    k = len(diff_by_site)
    if k <= 12:  # exact enumeration
        signs = np.array(np.meshgrid(*[[-1, 1]] * k)).reshape(k, -1).T
    else:
        signs = rng.choice([-1, 1], size=(nperm, k))
    null = (signs * diff_by_site).mean(1)
    return (np.sum(null >= obs) + 1) / (len(null) + 1)  # one-sided (pre-registered direction)


# ---------------- H1: open-loop divergence ----------------
def sim_h1(delta, n_routes=14, n_sites=6, n_pol=2, n_frames=200, rho=0.9,
           s_site=0.3, s_route=0.3, s_rc=0.15, s_sc=0.10, s_f=0.6):
    """log D model. delta = log ratio D_TH / D_TR (true height effect).
    s_rc: route-specific variation of the height effect; s_sc: site-specific variation."""
    site = sites_for(n_routes, n_sites)
    site_eff = rng.normal(0, s_site, n_sites)
    site_c = rng.normal(0, s_sc, n_sites)
    route_eff = rng.normal(0, s_route, n_routes)
    route_c = rng.normal(0, s_rc, n_routes)
    # AR(1) frame noise for each route x policy x capture
    shape = (n_routes, n_pol, 2, n_frames)
    e = np.empty(shape)
    e[..., 0] = rng.normal(0, s_f, shape[:-1])
    innov = rng.normal(0, s_f * np.sqrt(1 - rho ** 2), shape)
    for t in range(1, n_frames):
        e[..., t] = rho * e[..., t - 1] + innov[..., t]
    pol = np.array([0.0, 0.4])[:n_pol]
    c = np.array([0.0, 1.0])  # 0 = T_R, 1 = T_H
    logD = (site_eff[site][:, None, None, None] + route_eff[:, None, None, None]
            + pol[None, :, None, None]
            + c[None, None, :, None] * (delta + route_c[:, None, None, None]
                                        + site_c[site][:, None, None, None])
            + e)
    # naive frame-level Welch t (wrong: ignores clustering)
    p_naive = stats.ttest_ind(logD[:, :, 1].ravel(), logD[:, :, 0].ravel(),
                              alternative="greater").pvalue
    # route-level paired t (averages frames and policies within route)
    rd = (logD[:, :, 1].mean(-1) - logD[:, :, 0].mean(-1)).mean(1)
    p_route = stats.ttest_1samp(rd, 0, alternative="greater").pvalue
    # site-level sign-flip permutation (most conservative; matches pre-registration)
    sd = np.array([rd[site == s].mean() for s in range(n_sites)])
    p_site = site_perm_p(sd)
    # per-policy route-level test (both policies must show it for a "general" claim)
    rd_p = logD[:, :, 1].mean(-1) - logD[:, :, 0].mean(-1)
    p_pol = [stats.ttest_1samp(rd_p[:, k], 0, alternative="greater").pvalue
             for k in range(n_pol)]
    return p_naive, p_route, p_site, max(p_pol)


def run_h1():
    print("H1 open-loop divergence: one-sided alpha=0.05, 2 policies, frames AR(1) rho=0.9")
    print("delta=log(D_TH/D_TR). Assumed s_rc=0.15, s_sc=0.10 (heterogeneity of the height effect)")
    for n_routes, n_sites in [(8, 4), (14, 6), (16, 8)]:
        for delta in [0.0, 0.10, 0.15, 0.20, 0.30]:
            res = np.array([sim_h1(delta, n_routes, n_sites) for _ in range(NSIM)])
            rej = (res < 0.05).mean(0)
            print(f"  routes={n_routes:2d} sites={n_sites} ratio={np.exp(delta):.2f}: "
                  f"naive-frame={rej[0]:.2f} route-t={rej[1]:.2f} site-perm={rej[2]:.2f} "
                  f"both-policies(route-t)={rej[3]:.2f}")


# ---------------- C1: closed-loop gap ----------------
def sim_c1(design, delta_sd, n_sites=8, s_noise=0.10, s_R=0.10, s_cell=0.15):
    """Outcome y = route progress / trajectory score on a continuous scale (SD of cell means
    ~ s_cell).  Real run noise s_noise (test-retest).  Twin discrepancy SD s_R for T_R and
    s_R + delta_sd for T_H (cell-level, shared across starts in the same route x policy).
    Twin rollouts are deterministic (deterministic policies), so twin reliability = 1."""
    if design == "v1":
        n_routes, n_starts, n_rep = 8, 3, 1
        n_sites = 4
    else:
        n_routes, n_starts, n_rep = 16, 1, 2
    n_pol = 2
    site = sites_for(n_routes, n_sites)
    cell = rng.normal(0, s_cell, (n_routes, n_pol))
    start_eff = rng.normal(0, 0.05, (n_routes, n_pol, n_starts))
    truth = cell[..., None] + start_eff
    disc_R = rng.normal(0, s_R, (n_routes, n_pol))[..., None] + rng.normal(0, 0.03, truth.shape)
    disc_H = rng.normal(0, s_R + delta_sd, (n_routes, n_pol))[..., None] + rng.normal(0, 0.03, truth.shape)
    real = truth[..., None] + rng.normal(0, s_noise, truth.shape + (n_rep,))
    real_m = real.mean(-1)
    gapR = np.abs(truth + disc_R - real_m)
    gapH = np.abs(truth + disc_H - real_m)
    rd = (gapH - gapR).mean((1, 2))
    p_route = stats.ttest_1samp(rd, 0, alternative="greater").pvalue
    # naive episode-level paired t (ignores route clustering)
    p_naive = stats.ttest_1samp((gapH - gapR).ravel(), 0, alternative="greater").pvalue
    # SRCC-style correlation (cells), with attenuation correction when retest exists
    tw = (truth + disc_R).mean(-1).ravel()
    rm = real_m.mean(-1).ravel()
    r = np.corrcoef(tw, rm)[0, 1]
    rel = np.nan
    if n_rep == 2:
        a, b = real[..., 0].mean(-1).ravel(), real[..., 1].mean(-1).ravel()
        r_tt = np.corrcoef(a, b)[0, 1]
        rel = 2 * r_tt / (1 + r_tt)  # Spearman-Brown for the 2-run mean
    return p_naive, p_route, r, rel


def run_c1():
    print("\nC1 closed-loop |twin-real| gap, T_H vs T_R (route-clustered paired t, one-sided 0.05)")
    for design in ["v1", "v2"]:
        for d in [0.0, 0.05, 0.10, 0.15]:
            res = np.array([sim_c1(design, d) for _ in range(NSIM)])
            rej = (res[:, :2] < 0.05).mean(0)
            r = res[:, 2]
            lo, hi = np.percentile(r, [2.5, 97.5])
            extra = ""
            if design == "v2":
                extra = f" median reliability of 2-run real mean={np.nanmedian(res[:, 3]):.2f}"
            print(f"  {design} extra-SD(T_H)={d:.2f}: naive-episode={rej[0]:.2f} "
                  f"route-clustered={rej[1]:.2f}  SRCC(T_R) 95% range=[{lo:.2f},{hi:.2f}]{extra}")


if __name__ == "__main__":
    run_h1()
    run_c1()
