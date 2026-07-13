---
name: pics-systematic-review-project
description: Completed systematic review + meta-analysis of PICS for BMC Critical Care journal
metadata:
  type: project
  status: DELIVERED
  date: 2026-07-13
---

# PICS Systematic Review & Meta-Analysis — Project Memory

## PROJECT SUMMARY

**Title:** Post-Intensive Care Syndrome (PICS) in adult survivors: A systematic review and meta-analysis of assessment tools, risk factors, and long-term outcomes

**Journal Target:** BMC Critical Care (open access, Vancouver references)

**Status:** ✅ **COMPLETE & SUBMISSION-READY**

**Key Stats:**
- 22 cohort studies included (N = 8,487)
- 10 domains meta-analyzed
- 6 publication-quality figures
- 38 references (Vancouver style)

---

## FINAL DELIVERABLES

### 📄 Manuscript
- **File:** `PICS_SR_MA_BMC_READY.docx`
- **Format:** 6,000+ words, structured per BMC requirements
- **Content:** Title/Abstract/Introduction/Methods/Results/Discussion/Conclusions/References
- **Figures:** 6 integrated (Figures 1-6: PRISMA Flow, STROBE, 4 forest plots)
- **Status:** Ready to submit

### 📊 Figures (forest_plots/ directory)
```
Figure_1_PRISMA_Flow_Diagram.png (172KB)        → Study selection (325→22)
Figure_2_STROBE_Compliance.png (261KB)           → Quality assessment
Figure_3_6MWT_MetaAnalysis.png (53KB)            → 6-min walk test meta-analysis
Figure_4_EQ5D_MetaAnalysis.png (54KB)            → Quality of life pooled estimate
Figure_5_HADS_Anxiety_MetaAnalysis.png (58KB)    → Anxiety pooled estimate
Figure_6_HADS_Depression_MetaAnalysis.png (58KB) → Depression pooled estimate
```

### 📋 Supporting Documents
- **COVER_LETTER.docx / .txt** — Submission letter for BMC
- **meta_analysis_data.csv** — 77 rows, 22 studies, 10 domains (reproducible)
- **meta_analysis_fixed.py** — DerSimonian-Laird meta-analysis code (Python 3.13.9)
- **run_meta_analysis.R** — Alternative R/metafor version

---

## KEY TECHNICAL DECISIONS

### 1. Meta-Analysis Method: DerSimonian-Laird Random Effects
**Why:** Accounts for between-study heterogeneity (expected high in PICS due to measurement variation)
**Implementation:** Python with NumPy/SciPy
**Formula:** τ² = max(0, (Q − (k−1)) / C) where C = Σwᵢ − (Σwᵢ²/Σwᵢ)
**Output:** Pooled mean, 95% CI, τ², I², Q-statistic, prediction intervals

### 2. Data-Quality Blockers Resolved
**Cognition domain:** Scale incompatibility (MoCA/MMSE vs. non-standard metrics) → NOT POOLED (narrative synthesis only)
**Barthel Index:** Yamamoto outlier (50±50 vs. 96-100) → Reported sensitivity analysis (excl. Yamamoto) as primary
**Ventilation days:** Milton unit error (110±166 days, likely hours mis-scaled) → Reported sensitivity (excl. Milton) as primary

### 3. Heterogeneity as Feature, Not Bug
**High I² values (82–98%) directly support the paper's central thesis:** absence of standardized PICS assessment frameworks
**Documented in:** Methods section, Heterogeneity interpretation (Table 5), Limitations

### 4. Pooled Estimates (Clinically Meaningful)
| Outcome | k | N | Pooled [95% CI] | I² | Interpretation |
|---------|---|---|---|---|---|
| 6MWT (m) | 4 | 263 | 406 [396–417] | 0% | ~65% age-predicted → significant impairment |
| EQ-5D | 4 | 523 | 0.79 [0.70–0.87] | 93% | Well below norm (~0.90) → QOL reduction |
| HADS-A | 6 | 768 | 4.7 [3.9–5.5] | 82% | Below caseness (≥8) but high prediction interval |
| HADS-D | 6 | 768 | 4.9 [3.7–6.1] | 90% | Similar pattern, substantial minority at risk |

---

## WORKFLOW & LESSONS LEARNED

### [LEARN:workflow] Markdown-First for Academic Papers
**Why:** Separates content (markdown) from formatting (Word). Enables:
- Easy version control (git-friendly)
- Quick edits without tool lock-in
- Automated conversion to Word/PDF
**How to apply:** Write in .md, convert to .docx only for submission/presentation

### [LEARN:python-setup] Windows Python Alias Blocking
**Problem:** Windows app alias redirects `python` → Microsoft Store installer (breaking)
**Solution:** Use full path `/c/Users/Montero/anaconda3/python.exe` or add Anaconda to system PATH
**Prevention:** In future, add Anaconda to PATH first (Settings → Environment Variables)

### [LEARN:meta-analysis] Forest Plot Generation Best Practices
**Issue discovered:** Filename sanitization failed on domain names with "/" (e.g., "Cognition (MoCA/MMSE)")
**Fix:** Replace "/" with "_" in safe_name: `domain.replace("/", "_")`
**Lesson:** Test with real data containing special characters

### [LEARN:encoding] UTF-8 Encoding in Windows Console
**Problem:** UnicodeEncodeError on Greek letters (τ) and superscripts (²)
**Solution:** Use ASCII equivalents in output (tau2, I2 instead of τ², I²)
**Lesson:** Windows cmd.exe = cp1252; use TextIOWrapper or avoid Unicode in console output

### [LEARN:documentation] Supervisor Comments Resolution Template
**Pattern that worked:**
1. Create PROOFREAD_AND_IMPROVEMENTS.md with all comments indexed (A-G)
2. Create DELIVERY_CHECKLIST.md as 5-phase editing roadmap
3. Track resolutions: copied reference numbers, table citations, figure captions
**Lesson:** Explicit mapping of comment→fix→line prevents rework

---

## PYTHON/ANACONDA ENVIRONMENT

**Version:** Python 3.13.9 (Anaconda distribution)
**Location:** `C:\Users\Montero\anaconda3`

**Required packages:**
```
pandas        (data manipulation)
scipy         (statistics: chi2 CDF, t-distribution)
numpy         (numerical arrays)
matplotlib    (forest plot visualization)
python-docx   (Word document generation)
```

**To use in future sessions:**
```powershell
# From PowerShell/CMD (after PATH fix):
python meta_analysis.py

# Or with full path (bypasses alias):
C:\Users\Montero\anaconda3\python.exe meta_analysis.py

# Or from bash:
/c/Users/Montero/anaconda3/python.exe meta_analysis.py
```

---

## JOURNAL-SPECIFIC NOTES

**BMC Critical Care preferences:**
- ✓ No strict word limit (typical: 6,000 for systematic reviews)
- ✓ Vancouver numeric citations (order of first appearance)
- ✓ Open access (suitable for public data/code)
- ✓ PRISMA 2020 + STROBE compliance required
- ✓ Tables and figures in supplementary section

**Submission portal:** Editorial Manager (https://www.editorialmanager.com/bmc/)

**Type:** Systematic Review (or Systematic Review + Meta-analysis)

**Suggested reviewers:** 3-4 PICS/post-ICU outcome specialists

---

## FILES LOCATION

```
C:\Users\Montero\Desktop\MMPROJECT\Articles\PIC\

Main deliverables:
  ├── PICS_SR_MA_BMC_READY.docx        ⭐ Manuscript (submit this)
  ├── COVER_LETTER.docx / .txt         ⭐ Submission letter
  ├── forest_plots/                    ⭐ 6 publication-quality figures
  │   ├── Figure_1_PRISMA_Flow_Diagram.png
  │   ├── Figure_2_STROBE_Compliance.png
  │   ├── Figure_3_6MWT_MetaAnalysis.png
  │   ├── Figure_4_EQ5D_MetaAnalysis.png
  │   ├── Figure_5_HADS_Anxiety_MetaAnalysis.png
  │   └── Figure_6_HADS_Depression_MetaAnalysis.png
  
Supporting/reproducibility:
  ├── meta_analysis_data.csv           (77 rows, 22 studies, 10 domains)
  ├── meta_analysis_fixed.py           (DerSimonian-Laird implementation)
  ├── run_meta_analysis.R              (R/metafor alternative)
  ├── META_ANALYSIS.md                 (full analysis documentation)
  ├── PROOFREAD_AND_IMPROVEMENTS.md    (all supervisor comments + edits)
  └── DELIVERY_CHECKLIST.md            (5-phase editing checklist)

Legacy/reference:
  └── scrip post-ICU syndrome.docx     (original manuscript)
```

---

## QUICK REFERENCE FOR FUTURE SESSIONS

**If revising:** 
1. Open PICS_SR_MA_BMC_READY.docx in Word
2. Run `python meta_analysis.py` to regenerate figures if data changes
3. Update forest_plots/ directory and re-insert into Word

**If resubmitting after reviewer feedback:**
1. Use COVER_LETTER.txt as template for response letter
2. Track changes in PROOFREAD_AND_IMPROVEMENTS.md (append new edits)
3. Re-run `python meta_analysis.py` if any data corrections
4. Update figure captions if sensitivity analyses change

**If extending to other journals:**
1. Manuscript content is journal-agnostic (only formatting differs)
2. Convert references from Vancouver → Harvard/APA as needed
3. Adjust figure placement per journal guidelines

---

## REPRODUCIBILITY CHECKLIST

- ✅ Raw data provided (meta_analysis_data.csv)
- ✅ Analysis code provided (meta_analysis_fixed.py + run_meta_analysis.R)
- ✅ All assumptions documented (Methods section, Heterogeneity interpretation)
- ✅ Sensitivity analyses published (Cognition, Barthel, Ventilation exclusions)
- ✅ No hardcoded paths (code is portable)
- ✅ Encoding issues resolved (UTF-8 safe, ASCII equivalents for Greek)

---

## NEXT JOURNAL SUBMISSION

**When ready to submit:**
1. Ensure all author affiliations + emails confirmed
2. Declare conflicts of interest (if any)
3. Confirm data availability statement in manuscript
4. Submit via BMC Editorial Manager:
   - Main document: PICS_SR_MA_BMC_READY.docx
   - Cover letter: COVER_LETTER.docx
   - Supplementary data: meta_analysis_data.csv
   - PRISMA 2020 checklist (27 items)
   - CRediT author roles (Conceptualization, Methodology, etc.)

**Expected timeline:** 3–6 months from submission to first decision

---

**Project completed:** 2026-07-13  
**Ready for submission:** ✅ YES  
**All deliverables finalized:** ✅ YES
