# =============================================================================
# Meta-analysis of continuous PICS outcomes across post-ICU cohort studies
# Companion to: "Post-Intensive Care Syndrome (PICS) in adult survivors ..."
#
# Reproduces the pooled means, heterogeneity statistics and forest plots
# reported in META_ANALYSIS.md. Data: meta_analysis_data.csv
#
# Model:  random-effects meta-analysis of raw (untransformed) means.
#         DerSimonian-Laird tau^2 estimator to match the primary report;
#         REML shown as a robustness check.
# Studies reporting median [IQR] were converted to mean / SD with the
#         Wan et al. (2014) method before entry (median_converted == "yes").
# =============================================================================

## packages 
# install.packages(c("metafor", "dplyr", "readr"))
library(metafor)
library(dplyr)
library(readr)

## data 
dat <- read_csv("meta_analysis_data.csv", show_col_types = FALSE)

# sampling variance of a mean = sd^2 / n
dat <- dat %>%
  mutate(vi = sd^2 / n,
         sei = sqrt(vi))

domains <- unique(dat$domain)

## primary analysis: one random-effects model per domain 
run_domain <- function(d, method = "DL") {
  sub <- dat %>% filter(domain == d)
  m <- rma(yi = mean, vi = vi, data = sub, method = method,
           slab = paste0(study, " (", year, ")"))
  pi <- predict(m)                       # includes prediction interval
  tibble(
    domain   = d,
    k        = m$k,
    N        = sum(sub$n),
    pooled   = as.numeric(m$b),
    ci_lb    = m$ci.lb,
    ci_ub    = m$ci.ub,
    tau2     = m$tau2,
    I2       = m$I2,
    Q        = m$QE,
    Q_p      = m$QEp,
    pi_lb    = pi$pi.lb,
    pi_ub    = pi$pi.ub
  )
}

results <- bind_rows(lapply(domains, run_domain))
print(as.data.frame(results), digits = 3)
write_csv(results, "meta_analysis_results.csv")

## REML robustness check 
results_reml <- bind_rows(lapply(domains, run_domain, method = "REML"))
print(as.data.frame(results_reml), digits = 3)

## sensitivity analyses
# Cognition excluding Nanwani-Nanwani (47.8 +/- 68.1 is not a MoCA/MMSE score):
cog <- dat %>% filter(domain == "Cognition (MoCA/MMSE)",
                      !grepl("Nanwani", study))
print(rma(mean, vi, data = cog, method = "DL"))

# Barthel excluding Yamamoto (50 +/- 50 vs ~96-100 elsewhere -> data error/outlier):
bar <- dat %>% filter(domain == "Barthel Index", !grepl("Yamamoto", study))
print(rma(mean, vi, data = bar, method = "DL"))

# Ventilation excluding Milton (110 +/- 166 days, likely hours mis-scaled):
vent <- dat %>% filter(domain == "Ventilation (days)", !grepl("Milton", study))
print(rma(mean, vi, data = vent, method = "DL"))

## forest plots 
dir.create("forest_plots", showWarnings = FALSE)
for (d in domains) {
  sub <- dat %>% filter(domain == d)
  m <- rma(mean, vi, data = sub, method = "DL",
           slab = paste0(study, " (", year, ")"))
  png(file.path("forest_plots",
                paste0("forest_", gsub("[^A-Za-z0-9]+", "_", d), ".png")),
      width = 1400, height = 130 + 55 * m$k, res = 150)
  forest(m, header = c(d, "Mean [95% CI]"),
         xlab = "Pooled mean", addpred = TRUE, refline = coef(m))
  dev.off()
}

## optional: funnel / Egger for domains with k >= 10 
for (d in domains) {
  sub <- dat %>% filter(domain == d)
  if (nrow(sub) >= 10) {
    m <- rma(mean, vi, data = sub, method = "DL")
    cat("\n--- Egger test:", d, "---\n"); print(regtest(m))
  }
}

cat("\nDone. Pooled estimates -> meta_analysis_results.csv; plots -> forest_plots/\n")
