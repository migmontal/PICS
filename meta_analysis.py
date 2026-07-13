#!/usr/bin/env python3
"""
Meta-analysis of continuous PICS outcomes across post-ICU cohort studies.
Reproduces random-effects pooled estimates, forest plots, and sensitivity analyses.

Usage: python3 meta_analysis.py
Output: meta_analysis_results.csv, forest_plots/*.png
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy.stats import t as t_dist
import os
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# 1. Load data
# ============================================================================
df = pd.read_csv('meta_analysis_data.csv')
print(f"Loaded {len(df)} effect-size rows across {df['domain'].nunique()} domains")

# Compute sampling variance (se^2 / n) and standard error
df['vi'] = (df['sd'] ** 2) / df['n']
df['sei'] = np.sqrt(df['vi'])

# ============================================================================
# 2. Random-effects meta-analysis (DerSimonian-Laird)
# ============================================================================

def meta_analysis_de(domain_data):
    """DerSimonian-Laird random-effects meta-analysis of a single domain."""
    k = len(domain_data)
    yi = domain_data['mean'].values
    vi = domain_data['vi'].values
    n = domain_data['n'].values

    # Fixed-effects
    wi = 1 / vi
    theta_fe = np.sum(wi * yi) / np.sum(wi)

    # Q statistic
    Q = np.sum(wi * (yi - theta_fe) ** 2)

    # DL tau^2
    C = np.sum(wi) - np.sum(wi ** 2) / np.sum(wi)
    tau2 = max(0, (Q - (k - 1)) / C)

    # Random-effects
    wi_re = 1 / (vi + tau2)
    theta_re = np.sum(wi_re * yi) / np.sum(wi_re)
    se_re = np.sqrt(1 / np.sum(wi_re))

    # CI (95%, normal approximation)
    ci_lb = theta_re - 1.96 * se_re
    ci_ub = theta_re + 1.96 * se_re

    # Prediction interval (t on k-2 df)
    df_pred = max(1, k - 2)
    t_crit = t_dist.ppf(0.975, df_pred)
    se_pi = np.sqrt(tau2 + se_re ** 2)
    pi_lb = theta_re - t_crit * se_pi
    pi_ub = theta_re + t_crit * se_pi

    # I^2
    I2 = 100 * max(0, (Q - (k - 1)) / Q) if Q > k - 1 else 0

    # p-value (chi^2)
    from scipy.stats import chi2
    Q_p = 1 - chi2.cdf(Q, k - 1)

    # Total N
    N = domain_data['n'].sum()

    return {
        'domain': domain_data['domain'].iloc[0],
        'k': k,
        'N': N,
        'pooled_mean': theta_re,
        'ci_lb': ci_lb,
        'ci_ub': ci_ub,
        'tau2': tau2,
        'I2': I2,
        'Q': Q,
        'Q_p': Q_p,
        'se_re': se_re,
        'pi_lb': pi_lb,
        'pi_ub': pi_ub
    }

domains = df['domain'].unique()
results_list = []
for d in sorted(domains):
    domain_data = df[df['domain'] == d]
    res = meta_analysis_de(domain_data)
    results_list.append(res)
    print(f"{d:30s}  k={res['k']:2d}  pooled={res['pooled_mean']:7.3f}  95%CI [{res['ci_lb']:7.3f}, {res['ci_ub']:7.3f}]  I²={res['I2']:5.1f}%  τ²={res['tau2']:7.3f}")

results_df = pd.DataFrame(results_list)
results_df.to_csv('meta_analysis_results.csv', index=False)
print(f"\nResults saved to meta_analysis_results.csv")

# ============================================================================
# 3. Sensitivity analyses
# ============================================================================
print("\n" + "="*80)
print("SENSITIVITY ANALYSES")
print("="*80)

# Cognition excl. Nanwani
cog_data = df[(df['domain'] == 'Cognition (MoCA/MMSE)') & ~(df['study'].str.contains('Nanwani'))]
if len(cog_data) >= 3:
    res = meta_analysis_de(cog_data)
    print(f"Cognition excl. Nanwani: pooled={res['pooled_mean']:.3f} I²={res['I2']:.1f}%")

# Barthel excl. Yamamoto
bar_data = df[(df['domain'] == 'Barthel Index') & ~(df['study'].str.contains('Yamamoto'))]
if len(bar_data) >= 3:
    res = meta_analysis_de(bar_data)
    print(f"Barthel excl. Yamamoto: pooled={res['pooled_mean']:.3f} I²={res['I2']:.1f}%")

# Ventilation excl. Milton
vent_data = df[(df['domain'] == 'Ventilation (days)') & ~(df['study'].str.contains('Milton'))]
if len(vent_data) >= 3:
    res = meta_analysis_de(vent_data)
    print(f"Ventilation excl. Milton: pooled={res['pooled_mean']:.3f} I²={res['I2']:.1f}%")

# ============================================================================
# 4. Forest plots
# ============================================================================
os.makedirs('forest_plots', exist_ok=True)

def plot_forest(domain_name, df_sub, res_row):
    """Draw a forest plot for one domain."""
    # Sort by study year, then name
    df_sub = df_sub.sort_values(['year', 'study']).reset_index(drop=True)
    k = len(df_sub)

    # Compute each study's CI
    df_sub['ci_lb'] = df_sub['mean'] - 1.96 * df_sub['sei']
    df_sub['ci_ub'] = df_sub['mean'] + 1.96 * df_sub['sei']

    # Y positions (reversed so first study is at top)
    y_pos = np.arange(k, 0, -1)

    fig, ax = plt.subplots(figsize=(12, max(6, 0.4 * k)))

    # Plot study CIs (gray diamonds / error bars)
    for i, (idx, row) in enumerate(df_sub.iterrows()):
        y = y_pos[i]
        ax.plot([row['ci_lb'], row['ci_ub']], [y, y], 'o-', color='gray', linewidth=1, markersize=4)
        ax.plot(row['mean'], y, 'o', color='navy', markersize=6)

    # Plot pooled CI (red diamond)
    pooled_y = 0.5
    ax.plot([res_row['ci_lb'], res_row['ci_ub']], [pooled_y, pooled_y], 'D-', color='red', linewidth=2.5, markersize=10, label='Pooled')

    # Plot prediction interval as shaded region
    ax.axvspan(res_row['pi_lb'], res_row['pi_ub'], alpha=0.1, color='red', label='95% PI')

    # Vertical line at pooled estimate
    ax.axvline(res_row['pooled_mean'], color='red', linestyle='--', linewidth=1.5, alpha=0.7)

    # Labels and formatting
    ax.set_yticks(list(y_pos) + [pooled_y])
    ax.set_yticklabels([f"{s} ({int(y)})" for s, y in zip(df_sub['study'], df_sub['year'])] + ['POOLED'])
    ax.set_xlabel('Mean [95% CI]', fontsize=11, fontweight='bold')
    ax.set_title(f'{domain_name}\nk={res_row["k"]}, N={res_row["N"]}, I²={res_row["I2"]:.1f}%, Q_p={res_row["Q_p"]:.4f}',
                 fontsize=12, fontweight='bold')
    ax.grid(axis='x', alpha=0.3)
    ax.legend(loc='upper right', fontsize=9)

    plt.tight_layout()
    fname = f'forest_plots/forest_{domain_name.replace(" ", "_").replace("(", "").replace(")", "").lower()}.png'
    plt.savefig(fname, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  → {fname}")

print("\nGenerating forest plots...")
for _, res_row in results_df.iterrows():
    d = res_row['domain']
    df_sub = df[df['domain'] == d]
    plot_forest(d, df_sub, res_row)

print(f"\n✓ Done. Results in meta_analysis_results.csv and forest_plots/")
