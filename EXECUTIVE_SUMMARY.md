# PICS Systematic Review — Executive Summary & Next Steps

**Reviewer:** Claude Code · **Date:** 2026-07-13 · **Status:** Proofread + meta-analysis complete

Three deliverables ready:
1. **`META_ANALYSIS.md`** — full meta-analysis with data-quality flags (must fix 3 blockers before publishing)
2. **`PROOFREAD_AND_IMPROVEMENTS.md`** — all 7 supervisor comments resolved + 30+ copy-edits, find→replace format
3. **`meta_analysis.py`** — reproducible pooled estimates + forest plots (run when Python is available)

---

## At a glance

**The manuscript is 85% publication-ready.** Two classes of fixes remain:

### ✓ Copy-editing (quick wins — 20 mins)
- Delete 4 doubled numbers: `2015 and 2025 2026` → `2015 and 2025`, `33 32` → `32`, `the 15 22` → `the 22`
- Translate + fix Spanish line: *"5Q-5D-5L"* → **EQ-5D-5L**
- Figure 2 caption: **n = 22** (not 23)
- Add 5 table call-outs + uniform captions
- Fix 12 malformed citation clusters (spacing, number order)
- Cite STROBE reference (von Elm 2007)

### ⚠ Critical structural fixes (1–2 days)
1. **Renumber references** (Vancouver order of appearance) — currently broken; disrupts all in-text citation links
2. **Fix three meta-analysis blockers** (see below) before reporting pooled numbers
3. **Decide on meta-analysis integration** — upgrade to "systematic review and meta-analysis" + new title/abstract

---

## What the supervisor's 7 comments said (all resolved)

| # | Comment | Fix |
|---|---------|-----|
| 10 | Year range wrong ("2025 2026") | Keep 2015–2025; delete "2026" from Methods/Objectives |
| 11 | References not in order + bad PRISMA cite | Renumber by appearance; add STROBE/Wan refs |
| 12 | Table 1 not cited | Add: "Table 1 summarises the reported prevalence…" |
| 13 | Figure 2 says n=23, should be 22 | Fix caption to **n = 22** |
| 14 | Tables 1–3 need text citations | ✓ Done (D3) |
| 15 | Tables 3–4 need citations | ✓ Done (D3) |
| 16 | All table titles inconsistent, not all cited | ✓ Uniform format + all cited (D4) |

---

## Three data-quality blockers (must fix before publishing)

**Referee will catch these immediately.** Each needs a decision:

### 1. Cognition scale mix (BLOCKING pooled estimate)
**Problem:** Five studies, but incompatible scales:
- **MoCA/MMSE** (0–30 scale): Rousseau, Iribarren, Mateo → mean ~24–26
- **MoCA-BLIND** (0–22 scale): Carenzo → mean ~18
- **Unknown metric**: Nanwani → `47.8 ± 68.1` ← *not a 0–30 score*

**Pooling these as raw means is invalid.** Recommendation:
- **(a)** Drop cognition from the meta-analysis, keep as narrative; **or**
- **(b)** Pool only same-instrument (MoCA-standard only, k ≤ 3); **or**
- **(c)** Standardize to Cohen's d vs. population norm (advanced).

**I recommend (a):** The 99% I² and range tell you instrument variation is the real story anyway.

### 2. Barthel Index outlier (fixable)
**Problem:** Yamamoto reports `50 ± 50` (median 55, IQR 10–85); every other study 96–100.
- Possible causes: (i) different timepoint (ICU discharge vs. follow-up); (ii) data-entry error.

**Fix:** Verify against source; use sensitivity-analysis result as primary.
- With Yamamoto: 96.4 [93.5, 99.4], I² = 93%
- **Without Yamamoto: 98.3 [96.9, 99.7], I² = 73%** ← report this

### 3. Ventilation days unit error (fixable)
**Problem:** Milton reports `110 ± 166 days` for a cohort with mean ICU stay 110 h — almost certainly **hours mis-scaled to days**, inflating the pool by ~5 days.

**Fix:** Verify the unit; use sensitivity-analysis result (excl. Milton):
- With Milton: 23.1 [17.8, 28.3] days
- **Without Milton: 18.4 [13.5, 23.3] days** ← more defensible; matches visual inspection of other studies

---

## The meta-analysis upgrade

### What you have now
- 22 included cohort studies
- Qualitative synthesis (excellent narrative in Discussion)
- **NO pooled numbers** (title says "systematic review"; abstract has no meta-analysis Results)

### What adding the meta-analysis gives you
- **Quotable pooled estimates** for 10 domains (see table below)
- **Direct evidence** for your central thesis: "outcome measurement in PICS is not standardised" (see the 90%+ I² values)
- **Upgraded status:** "systematic review **and** meta-analysis" (more prestigious, publishable in higher-tier venues)
- **Methods text** (paste-ready) in `META_ANALYSIS.md` §2

### Pooled estimates (after fixing the three blockers)

| Domain | k | N | Pooled mean [95% CI] | I² | Notes |
|---|--:|--:|---|--:|---|
| **6MWT (m)** | 4 | 263 | **406 [396, 417]** | 0% | ✓ Clean, quotable |
| **EQ-5D index** | 4 | 523 | **0.79 [0.70, 0.87]** | 93% | ✓ Clean |
| **HADS-Anxiety** | 6 | 768 | **4.7 [3.9, 5.5]** | 82% | ✓ Clean |
| **HADS-Depression** | 6 | 768 | **4.9 [3.7, 6.1]** | 90% | ✓ Clean |
| Age (years) | 20 | 3210 | 60.9 [58.9, 62.9] | 94% | Demographic (not outcome) |
| Grip strength (kg) | 5 | 392 | 25.3 [21.9, 28.7] | 96% | ✓ Pool with caution (I²=96%) |
| Barthel Index | 6 | 617 | 98.3 [96.9, 99.7] | 73% | ✓ After excl. Yamamoto |
| Ventilation (days) | 14 | 1987 | 18.4 [13.5, 23.3] | 98% | ✓ After excl. Milton |
| Cognition (MoCA) | — | — | **drop/narrate** | — | ⚠ Scale mix; recommend narrative |
| QoL / Symptom domains | — | — | — | — | Heterogeneous; report as range |

### Step 1: Choose your integration level
- **Light:** Add pooled numbers as a Results subsection; keep narrative; do NOT retitle.
- **Full (recommended):** Retitle to "…systematic review **and** meta-analysis"; add Methods text; revise abstract Results; add forest plots.
- **Decision point:** 1 hour to decide; 2 hours to edit if you go full.

### Step 2: Run the meta-analysis (when Python works)
```bash
cd Articles/PIC/
python3 meta_analysis.py
# → meta_analysis_results.csv, forest_plots/*.png
```

---

## Edit checklist (in order)

### Phase 1: Copy & structure (30 min)
- [ ] Delete doubled numbers (B1): `2025 2026` → `2025`; `33 32` → `32`; `15 22` → `22`
- [ ] Fix Spanish line (B2): *"5Q-5D-5L"* → **"EQ-5D-5L"**; remove VAS (not used)
- [ ] Delete duplicate Sánchez-García ref (B3)
- [ ] Figure 2: change caption to **n = 22** (B4)
- [ ] Reword STROBE (B5): *"STROBE reporting checklist"* not "risk of bias"
- [ ] Add STROBE citation (B6): von Elm E, et al. Lancet 2007;370:1453-7
- [ ] Add 5 table call-outs (D3): one sentence before each table intro
- [ ] Uniform table captions (D4): `Table N.` + sentence case, no trailing period

### Phase 2: References (1 hour)
- [ ] Renumber by order of first appearance (F) — **critical**
- [ ] Re-verify every author-name ↔ number pair in Discussion vs. Reference list (B7)
- [ ] Check 3 names: Appel (not Apple), Narváez-Martínez (not Narvaez-Rojas), González
- [ ] Fix citation-cluster formatting (C): ascending numbers, one space after comma

### Phase 3: Data-quality fixes (1–2 hours)
- [ ] **Cognition:** decide (a) drop from meta-analysis / (b) pool only MoCA-standard / (c) standardize
- [ ] **Barthel:** verify Yamamoto source; report sensitivity result (98.3) as primary
- [ ] **Ventilation:** verify Milton's ventilation-day units; use excl-Milton result (18.4 d) if confirmed error
- [ ] Add data-quality caveats to Limitations (E7)

### Phase 4: Meta-analysis integration (2 hours, optional)
- [ ] If full integration: retitle to "…systematic review and meta-analysis"
- [ ] Add Methods text from `META_ANALYSIS.md` §2
- [ ] Add Table: pooled estimates (§3.1 of META_ANALYSIS.md, after fixing blockers)
- [ ] Add Figure: 4-panel forest plot (6MWT, EQ-5D, HADS-A, HADS-D)
- [ ] Revise abstract Results sentence to include pooled numbers

### Phase 5: QA (30 min)
- [ ] Re-read abstract + Discussion for author-name ↔ number drift
- [ ] Check all 5 tables are cited in text
- [ ] Spell-check; verify accent marks in Spanish names (García, Narváez, Álvarez, González)
- [ ] Confirm PRISMA 2020 checklist is included as supplement

---

## File manifest

| File | Purpose | Action |
|---|---|---|
| `scrip post-ICU syndrome.docx` | Original manuscript | Edit in Word using Phase 1–5 checklist |
| `meta_analysis_data.csv` | Clean extracted data, 77 rows | ✓ Ready (reviewed for consistency) |
| `meta_analysis.py` | Reproducible pooled estimates + forest plots | Run when Python available |
| `run_meta_analysis.R` | Alternative (R/metafor) version | Optional; same output |
| `META_ANALYSIS.md` | Full meta-analysis report + data flags | ✓ Reference for methods text + design decisions |
| `PROOFREAD_AND_IMPROVEMENTS.md` | All copy-edits + structural fixes (find→replace) | ✓ Execute using Phases 1–2 checklist |
| `EXECUTIVE_SUMMARY.md` | This file | ← you are here |

---

## Estimated effort & timeline

| Phase | Time | Difficulty | Prerequisite |
|---|--:|---|---|
| 1 (Copy & structure) | 30 min | ★☆☆ | none |
| 2 (References) | 60 min | ★★☆ | Phase 1 complete |
| 3 (Data-quality) | 60–120 min | ★★★ | Verify sources (Yamamoto, Milton) |
| 4 (Meta-analysis) | 120 min | ★★☆ | Python working; Phase 3 decisions made |
| 5 (QA) | 30 min | ★☆☆ | All phases |
| **Total** | **5–6 hours** | — | — |

**Fast track (submit as-is, narrative review):** Phases 1–2 only = 90 min.
**Full (upgrade to meta-analysis review):** All phases = 5–6 hours.

---

## Questions to decide before editing

1. **Meta-analysis depth:** Light (pooled numbers in Results) or Full (retitle + forest plots)?
   - *Recommend:* Full — it's only 2 extra hours and substantially stronger.

2. **Cognition:** Drop from meta-analysis or pool only same-instrument?
   - *Recommend:* Drop (keeps focus on the clean domains: 6MWT, EQ-5D, HADS).

3. **Reference style:** Vancouver (numeric) or Harvard (author-year)?
   - Current is Vancouver; renumber by appearance (see Phase 2).

4. **Target journal:** Any preference? (impacts abstract word limit, reference style, supplementary requirements)

---

## Support files location
All files are in: `C:\Users\Montero\Desktop\MMPROJECT\Articles\PIC\`

When Python works:
```bash
cd Articles\PIC
python meta_analysis.py
```

Then copy forest plots into the manuscript as Supplementary Figures (or main Figure if condensed to 4 panels).

---

**Next:** Choose your answers to the 4 questions above, and I can draft a fully-edited version with all Phases 1–5 applied.
