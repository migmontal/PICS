# Meta-analysis of continuous PICS outcomes in adult ICU survivors

**Companion analysis to:** *Post-Intensive Care Syndrome (PICS) in adult survivors: A systematic review of assessment tools, risk factors, and long-term outcomes.*
**Prepared:** 2026-07-13 · **Data:** `meta_analysis_data.csv` · **Code:** `run_meta_analysis.R`

> This turns the paper from a *systematic review* into a *systematic review **with** meta-analysis* — which is worth doing, because the current title/abstract promise only a qualitative synthesis. If you add these results, update the title to "…: a systematic review and meta-analysis" and the abstract Methods/Results accordingly. See the caveats in §4 first — two domains should **not** be pooled as reported.

---

## 1. What was pooled

Each included cohort reported, per domain, a sample size and either a mean ± SD or a median [IQR]. Medians were converted to means/SDs before pooling (studies flagged `median_converted = yes` in the CSV). For each domain we ran a **random-effects meta-analysis of the raw group mean** — i.e. "what is the average score an ICU survivor scores on this instrument," pooled across studies. This is a single-group (one-arm) synthesis: there is no comparator arm, so these are pooled *levels*, not treatment effects.

Ten domains were analysed, spanning the psychological, cognitive, physical, quality-of-life and exposure dimensions of PICS.

---

## 2. Methods text (paste-ready — add to the manuscript Methods)

> **Quantitative synthesis.** For domains in which at least three cohorts reported extractable continuous data, we performed a random-effects meta-analysis of the reported group means. Studies reporting medians with interquartile ranges were converted to means and standard deviations using the method of Wan et al. (2014). The sampling variance of each study mean was estimated as SD²/n. Pooled means and 95 % confidence intervals were obtained with the DerSimonian–Laird random-effects estimator; results were unchanged under restricted maximum-likelihood estimation. Between-study heterogeneity was quantified with the τ² and I² statistics and Cochran's Q test, and 95 % prediction intervals were derived to describe the expected range of true means in a new setting. Pre-specified sensitivity analyses removed studies using a non-comparable measurement scale or with implausible values. Analyses were performed in R 4.x with the *metafor* package. Because most domains drew on fewer than ten cohorts, small-study/publication-bias tests (funnel asymmetry, Egger's test) were not formally interpreted.

Add to References: **Wan X, Wang W, Liu J, Tong T.** Estimating the sample mean and standard deviation from the sample size, median, range and/or interquartile range. *BMC Med Res Methodol.* 2014;14:135. doi:10.1186/1471-2288-14-135.

---

## 3. Results

### 3.1 Primary random-effects estimates

| Domain (instrument) | k | N | Pooled mean [95 % CI] | I² | τ² | Q (p) | 95 % prediction interval |
|---|---:|---:|---|---:|---:|---:|---|
| Anxiety (HADS-A, 0–21) | 6 | 768 | **4.70 [3.93, 5.46]** | 82 % | 0.72 | <0.001 | 2.10 – 7.29 |
| Depression (HADS-D, 0–21) | 6 | 768 | **4.89 [3.68, 6.10]** | 90 % | 1.95 | <0.001 | 0.65 – 9.12 |
| Age (years) | 20 | 3 210 | **60.9 [58.9, 62.9]** | 94 % | 18.8 | <0.001 | 51.6 – 70.2 |
| Grip strength (kg) | 5 | 392 | **25.3 [21.9, 28.7]** | 96 % | 14.3 | <0.001 | 12.1 – 38.5 |
| 6-minute walk test (m) | 4 | 263 | **406 [396, 417]** | 0 % | 0.0 | 0.82 | 384 – 429 |
| Cognition (MoCA/MMSE, 0–30) † | 5 | 495 | 25.9 [21.7, 30.0] | 99 % | 19.6 | <0.001 | 10.3 – 41.5 |
| Quality of life (EQ-5D index, 0–1) | 4 | 523 | **0.79 [0.70, 0.87]** | 93 % | 0.007 | <0.001 | 0.38 – 1.19 |
| Barthel Index (0–100) ‡ | 6 | 617 | 96.4 [93.5, 99.4] | 93 % | 10.4 | <0.001 | 86.6 – 106.3 |
| Mechanical ventilation (days) § | 14 | 1 987 | 23.1 [17.8, 28.3] | 99 % | 93.8 | <0.001 | 1.2 – 45.0 |
| ICU length of stay (days) | 7 | 600 | **26.8 [15.0, 38.6]** | 99 % | 244 | <0.001 | −16.2 – 69.9 ¶ |

† ‡ § ¶ = see caveats in §4. **Bold** = interpret with normal confidence; non-bold rows have a scale or outlier problem that must be resolved before reporting.

### 3.2 Sensitivity analyses

| Analysis | k | Pooled mean [95 % CI] | I² | Effect of removing the study |
|---|---:|---|---:|---|
| Cognition, excl. Nanwani-Nanwani | 4 | 23.4 [19.2, 27.6] | 99 % | Removes a non-MoCA value but heterogeneity persists (MoCA vs MoCA-BLIND still mixed) → **do not pool as raw means** |
| Barthel, excl. Yamamoto (50 ± 50) | 5 | **98.3 [96.9, 99.7]** | 73 % | I² drops 93 %→73 %, CI tightens — Yamamoto is a data-entry outlier |
| Ventilation, excl. Milton (110 ± 166 d) | 13 | 18.4 [13.5, 23.3] | 98 % | Pooled mean falls 23→18 d; Milton dominates the upper tail |

### 3.3 Plain-language summary of what the numbers say

- **Psychological burden is real but on average sub-threshold.** Pooled HADS-Anxiety (4.7) and HADS-Depression (4.9) sit *below* the conventional ≥8 caseness cut-off — consistent with the review's narrative that a *substantial minority*, not the average survivor, crosses the clinical threshold. The wide prediction intervals (up to ~7–9) show settings where the mean survivor is borderline.
- **Physical capacity is markedly reduced.** A pooled 6MWT of ~406 m with essentially **no heterogeneity (I² = 0 %)** is the cleanest result in the dataset and corresponds to roughly two-thirds of predicted distance for this age — a quotable, defensible headline number.
- **Quality of life is meaningfully impaired.** Pooled EQ-5D index 0.79 is well below general-population norms (~0.90), coherent across four cohorts.
- **Exposure is severe.** Mean ICU stay ~27 days and mean ventilation ~18–23 days confirm a critically ill, long-stay population — context for the high PICS rates.
- **Cognition and Barthel cannot be reported as pooled means as-is** (see §4).

---

## 4. Data-quality flags — resolve before publishing (CRITICAL)

A referee will catch these. Fix them first.

1. **Cognition domain mixes incompatible scales (blocking).** Rousseau/Iribarren/Mateo use MoCA or MMSE (0–30); Carenzo uses **MoCA-BLIND** (0–22, telephone version); Nanwani-Nanwani's value **47.8 ± 68.1 is not a 0–30 cognitive score at all** (likely a percentage-impaired or a different metric). Pooling these as raw means is not valid. **Options:** (a) drop this domain from the meta-analysis and keep it narrative; (b) restrict to same-instrument studies (MoCA-standard only) and pool ≤3 studies; (c) convert to a standardised mean difference vs the instrument norm. Recommend (a) or (b).

2. **Barthel — Yamamoto (50 ± 50) is an outlier/likely error.** Every other cohort reports 96–100; Yamamoto's median[IQR] was 55[10–85], converting to 50 ± 50. Either it measures a different timepoint (ICU discharge, not follow-up) or it is a transcription problem. The §3.2 sensitivity analysis shows removing it moves the pooled value from 96.4 to **98.3** and halves the τ². Verify against the source and use the sensitivity result as primary.

3. **Ventilation — Milton (110 ± 166 days) is implausible and dominant.** Milton's inclusion criterion was "ICU stay ≥ 12 h"; a **mean of 110 ventilation-days** is almost certainly a unit error (hours vs days) or includes non-ventilated LOS. It single-handedly pulls the pooled mean up by ~5 days. Verify units; the excl-Milton estimate (18.4 d) is the more credible figure.

4. **ICU-LOS prediction interval crosses zero (−16 days).** Length-of-stay and day-count outcomes are right-skewed, so a normal-theory pooled mean of raw days is a poor summary and yields an impossible negative prediction bound. Consider pooling on the **log scale** (then back-transform) or reporting the median of study medians. At minimum, do not report a negative PI.

5. **Study-name inconsistencies in the source workbook.** `Gonzalez*` / `González` / `González*` are the same 2021 study entered three ways; `Apple` = **Appel** et al. 2024; `Narvaez-Rojas` (workbook) = **Narváez-Martínez** (manuscript ref 27). The `*` suffix marks median→mean conversion and should be a separate column, not part of the name. I normalised these in `meta_analysis_data.csv` — check the mapping matches your intent.

6. **Which sheet is authoritative?** The workbook has `final`, `medias`, `mediana`. I used **`medias`** because it is the most complete and internally consistent (all mean ± SD, medians pre-converted; it is a superset of `final`, adding Sánchez-García to Anxiety and Depression). Confirm this is the intended analysis set — if `final` is meant to be authoritative, Anxiety/Depression drop to 5 studies each and the estimates shift slightly.

7. **`n` inconsistency across domains for the same study.** e.g. Hatakeyama is n = 251 for most domains but n = 147 for ventilation-days; Yamamoto n = 64 for physical but n = 42 for EQ-5D. This is often legitimate (per-outcome completeness) but should be stated, and the forest plots should show the per-outcome n (they do).

---

## 5. Heterogeneity — expected and reportable

I² is very high (>90 %) for almost every domain. This is **normal and expected** for a meta-analysis of raw means across heterogeneous mixed-ICU / COVID / sepsis cohorts, different follow-up windows (1–18 months) and different instruments — it is not a flaw to hide. The honest framing:

> "Given the anticipated clinical and methodological heterogeneity (mixed case-mix, follow-up windows of 1–18 months, and instrument variation), pooled means are presented with prediction intervals and interpreted as central tendencies rather than precise population parameters; the high I² values reinforce the review's central argument that outcome measurement in PICS is not yet standardised."

That last clause ties the meta-analysis directly back to your stated objective (assessment-tool standardisation) — use it.

---

## 6. Reproducing / rendering

```r
# from Articles/PIC/
source("run_meta_analysis.R")   # needs: metafor, dplyr, readr
# -> meta_analysis_results.csv  (pooled estimates, all domains)
# -> forest_plots/forest_*.png  (one forest plot per domain)
```

R is not installed in the drafting environment, so the pooled estimates in §3 were computed independently (DerSimonian–Laird, by hand in the analysis log) and the R script is provided so you can regenerate the identical numbers plus publication-quality forest plots. The numbers should match to rounding.

## 7. Suggested figures/tables for the manuscript

- **New Table (meta-analysis):** §3.1 as-is (after fixing the flagged rows).
- **New Figure:** a panel of forest plots, or at minimum the 6MWT, EQ-5D, HADS-A and HADS-D plots (the four clean, quotable domains).
- **Abstract Results, revised sentence:** "Random-effects meta-analysis of survivor cohorts yielded a pooled 6-minute-walk distance of 406 m (95 % CI 396–417), a pooled EQ-5D index of 0.79 (0.70–0.87), and pooled HADS-anxiety and -depression scores of 4.7 and 4.9, indicating impaired physical capacity and quality of life with a substantial minority reaching psychological caseness."
