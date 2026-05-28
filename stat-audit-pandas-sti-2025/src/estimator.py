import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy import stats

prs    = pd.read_csv("prs_clean.csv")
issues = pd.read_csv("issues_per_day.csv")

is_merged    = prs["is_merged"].values          
issues_count = issues["issues_count"].values    

n_pr    = len(is_merged)
k_merge = is_merged.sum()
p_mle   = k_merge / n_pr

print("=" * 55)
print("1. MLE BERNOULLI - Probabilitas PR di-merge")
print("=" * 55)
print(f"   Total PR          : {n_pr}")
print(f"   PR yang di-merge  : {k_merge}")
print(f"   PR tidak di-merge : {n_pr - k_merge}")
print(f"   p_hat (MLE)       : {p_mle:.4f}  ({p_mle*100:.2f}%)")
print()

se_p  = np.sqrt(p_mle * (1 - p_mle) / n_pr)
ci_lo = p_mle - 1.96 * se_p
ci_hi = p_mle + 1.96 * se_p
print(f"   SE(p_hat)         : {se_p:.4f}")
print(f"   95% CI            : [{ci_lo:.4f}, {ci_hi:.4f}]")
print()

n_days  = len(issues_count)
lam_mle = issues_count.mean()

print("=" * 55)
print("2. MLE POISSON - Rata-rata issue masuk per hari")
print("=" * 55)
print(f"   Jumlah hari       : {n_days}")
print(f"   Total issue       : {issues_count.sum()}")
print(f"   lambda_hat (MLE)  : {lam_mle:.4f} issue/hari")
print()

se_lam  = np.sqrt(lam_mle / n_days)
ci_lo_l = lam_mle - 1.96 * se_lam
ci_hi_l = lam_mle + 1.96 * se_lam
print(f"   SE(lambda_hat)    : {se_lam:.4f}")
print(f"   95% CI            : [{ci_lo_l:.4f}, {ci_hi_l:.4f}]")
print()

max_k    = issues_count.max()
obs_freq = np.bincount(issues_count, minlength=max_k + 1)
exp_freq = stats.poisson.pmf(np.arange(max_k + 1), lam_mle) * n_days

exp_scaled = exp_freq * (obs_freq.sum() / exp_freq.sum())
chi2_stat, chi2_p = stats.chisquare(obs_freq, f_exp=exp_scaled)
print(f"   Chi-square GoF    : chi2 = {chi2_stat:.2f}, p = {chi2_p:.4f}")
print()

alpha_prior = 12    
beta_prior  = 8 

alpha_post = alpha_prior + k_merge
beta_post  = beta_prior  + (n_pr - k_merge)

post_mean = alpha_post / (alpha_post + beta_post)
post_mode = (alpha_post - 1) / (alpha_post + beta_post - 2)
post_var  = (alpha_post * beta_post) / \
            ((alpha_post + beta_post)**2 * (alpha_post + beta_post + 1))
post_std  = np.sqrt(post_var)
hdi_lo, hdi_hi = stats.beta.ppf([0.025, 0.975], alpha_post, beta_post)

print("=" * 55)
print("3. BETA POSTERIOR - Gabungan Prior + Data")
print("=" * 55)
print(f"   Prior             : Beta(alpha={alpha_prior}, beta={beta_prior})")
print(f"   Prior mean        : {alpha_prior/(alpha_prior+beta_prior):.4f}")
print(f"   Likelihood        : Binomial(n={n_pr}, k={k_merge})")
print(f"   Posterior         : Beta(alpha={alpha_post}, beta={beta_post})")
print()
print(f"   Posterior mean    : {post_mean:.4f}  ({post_mean*100:.2f}%)")
print(f"   Posterior mode    : {post_mode:.4f}  ({post_mode*100:.2f}%)")
print(f"   Posterior std     : {post_std:.4f}")
print(f"   95% Credible Int  : [{hdi_lo:.4f}, {hdi_hi:.4f}]")
print()

print("-" * 55)
print("  RINGKASAN PERBANDINGAN")
print("-" * 55)
print(f"  {'Metode':<25} {'Estimasi p':>12}")
print(f"  {'MLE (Frekuentis)':<25} {p_mle:>12.4f}")
print(f"  {'Prior mean (Bayes)':<25} {alpha_prior/(alpha_prior+beta_prior):>12.4f}")
print(f"  {'Posterior mean (Bayes)':<25} {post_mean:>12.4f}")
print("-" * 55)

fig = plt.figure(figsize=(16, 10))
fig.suptitle("MLE Bernoulli - MLE Poisson - Beta Posterior", fontsize=14,
             fontweight="bold", y=0.98)
gs = gridspec.GridSpec(2, 3, figure=fig, hspace=0.45, wspace=0.35)

colors = {
    "prior"      : "#4e79a7",
    "likelihood" : "#f28e2b",
    "posterior"  : "#59a14f",
    "bar"        : "#76b7b2"
}

ax1 = fig.add_subplot(gs[0, 0])
counts = [n_pr - k_merge, k_merge]
labels = ["Not Merged", "Merged"]
bars   = ax1.bar(labels, counts, color=["#e15759", "#59a14f"],
                 edgecolor="white", width=0.5)
for bar, cnt in zip(bars, counts):
    ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 30,
             f"{cnt}\n({cnt/n_pr*100:.1f}%)", ha="center", va="bottom", fontsize=10)
ax1.set_title("Distribusi PR Status", fontweight="bold")
ax1.set_ylabel("Jumlah PR")
ax1.set_ylim(0, max(counts) * 1.2)
ax1.spines[["top", "right"]].set_visible(False)

ax2 = fig.add_subplot(gs[0, 1])
p_vals  = np.linspace(0.001, 0.999, 500)
ll_bern = k_merge * np.log(p_vals) + (n_pr - k_merge) * np.log(1 - p_vals)
ax2.plot(p_vals, ll_bern, color=colors["likelihood"], lw=2)
ax2.axvline(p_mle, color="#e15759", ls="--", lw=1.5,
            label=f"p_hat = {p_mle:.4f}")
ax2.set_title("Log-Likelihood Bernoulli", fontweight="bold")
ax2.set_xlabel("p")
ax2.set_ylabel("log L(p)")
ax2.legend(fontsize=9)
ax2.spines[["top", "right"]].set_visible(False)

ax3 = fig.add_subplot(gs[0, 2])
max_show = min(max_k, 35)
x_range  = np.arange(0, max_show + 1)
ax3.bar(x_range,
        np.bincount(issues_count, minlength=max_show + 1)[:max_show + 1],
        color=colors["bar"], edgecolor="white", alpha=0.8, label="Observasi")
ax3.plot(x_range, stats.poisson.pmf(x_range, lam_mle) * n_days,
         "o-", color="#e15759", ms=5, lw=1.5,
         label=f"Poisson(lambda={lam_mle:.2f})")
ax3.set_title("Issue per Hari vs Poisson Fit", fontweight="bold")
ax3.set_xlabel("Jumlah Issue")
ax3.set_ylabel("Frekuensi")
ax3.legend(fontsize=9)
ax3.spines[["top", "right"]].set_visible(False)

ax4 = fig.add_subplot(gs[1, 0])
lam_vals = np.linspace(max(0.01, lam_mle - 3), lam_mle + 3, 400)
ll_pois  = (issues_count.sum() * np.log(lam_vals)
            - n_days * lam_vals)    # konstanta diabaikan
ax4.plot(lam_vals, ll_pois, color=colors["likelihood"], lw=2)
ax4.axvline(lam_mle, color="#e15759", ls="--", lw=1.5,
            label=f"lambda_hat = {lam_mle:.4f}")
ax4.set_title("Log-Likelihood Poisson", fontweight="bold")
ax4.set_xlabel("lambda")
ax4.set_ylabel("log L(lambda)")
ax4.legend(fontsize=9)
ax4.spines[["top", "right"]].set_visible(False)

ax5 = fig.add_subplot(gs[1, 1:])
p_plot    = np.linspace(0.3, 0.9, 600)
prior_pdf = stats.beta.pdf(p_plot, alpha_prior, beta_prior)
post_pdf  = stats.beta.pdf(p_plot, alpha_post,  beta_post)

prior_mean = alpha_prior / (alpha_prior + beta_prior)

ax5.fill_between(p_plot, prior_pdf, alpha=0.25, color=colors["prior"])
ax5.plot(p_plot, prior_pdf, color=colors["prior"], lw=2,
         label=f"Prior  Beta({alpha_prior}, {beta_prior})  mean={prior_mean:.3f}")

ax5.fill_between(p_plot, post_pdf, alpha=0.25, color=colors["posterior"])
ax5.plot(p_plot, post_pdf, color=colors["posterior"], lw=2,
         label=f"Posterior Beta({alpha_post}, {beta_post})  mean={post_mean:.4f}")

ax5.axvline(p_mle, color=colors["likelihood"], ls="--", lw=1.5,
            label=f"MLE p_hat = {p_mle:.4f}")
ax5.axvspan(hdi_lo, hdi_hi, alpha=0.10, color=colors["posterior"],
            label=f"95% Credible Interval [{hdi_lo:.3f}, {hdi_hi:.3f}]")

ax5.set_title("Beta Prior vs Posterior (Conjugate Update)", fontweight="bold")
ax5.set_xlabel("p (probabilitas PR di-merge)")
ax5.set_ylabel("Densitas")
ax5.legend(fontsize=9, loc="upper left")
ax5.spines[["top", "right"]].set_visible(False)

plt.savefig("bayesian_analysis.png", dpi=150, bbox_inches="tight")
plt.show()
print("Plot disimpan ke bayesian_analysis.png")