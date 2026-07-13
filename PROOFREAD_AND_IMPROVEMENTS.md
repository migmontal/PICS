# Proofread & improvement report — PICS systematic review

**Manuscript:** `scrip post-ICU syndrome.docx` · **Reviewed:** 2026-07-13
**Scope:** copy-edit (grammar/typos/consistency) + structural/methodological improvement + resolution of the 7 tracked comments by M. Á. Montero.

Fixes are ordered **must-fix → should-fix → nice-to-have**. Each gives the *location* and an exact *find → replace* where possible so edits can be applied directly in Word.

---

## A. Resolution of the supervisor's 7 comments (comments in Spanish)

| # | Comment (MM) | Resolution |
|---|---|---|
| 10 | *"Nunca se mete el año actual, hasta 2025. Si hay alguna de 2026 meter en la discusión. Además en el resumen se dice hasta 2025."* | **Keep the range as 2015–2025 everywhere.** Delete the tracked "2026" in both the Methods and the Objectives (see B1). The abstract already says 2025 — leave it. No included study is dated 2026, so nothing needs moving to the Discussion. (Refs 2, 7 in the list carry 2025-epub/2026-print dates — cite them normally; the *search window* stays 2015–2025.) |
| 11 | *"Este párrafo lo he metido yo, revisa el inglés… la referencia, no sé si le corresponde la 40… las referencias ni están por orden alfabético ni de aparición."* | (a) English of the inserted PRISMA/flow-diagram paragraph is edited in C. (b) The PRISMA citation **is** Page et al. 2020 — that is the correct source, but it should be number-matched to its position, not hard-coded as "[40]", and the bracket style must match the rest (parentheses). (c) **References must be renumbered by order of first appearance** (Vancouver) — this is a real defect, see F. |
| 12 | *"No se dice nada de esta tabla… citarla en ese texto. Revisar el inglés."* | Table 1 is now cited in the Incidence text (see D3). English of the surrounding sentence edited. |
| 13 | *"Revisar el gráfico, pone n=23 en el título y el n es 22."* | **Figure 2 caption/label must read n = 22**, not 23 (see B4). Confirm the plotted bars are also 22 studies. |
| 14 | *"Citar la tabla 1 en el texto, como hice con las figuras."* | Done — Table 1 call-out added (D3). |
| 15 | *"Citar en el texto."* (Table 3/4 region) | Table call-outs added for every table (D3). |
| 16 | *"Citar en el texto. Poner todos los encabezados/títulos de las tablas de la misma forma. Todas citadas en el texto."* | All five tables now (a) cited in text and (b) given a **uniform caption format** — see D3/D4 for the standard template. |

---

## B. Must-fix (a referee/editor will bounce these)

**B1. Tracked-change leftovers — two numbers sit side by side.**
- Methods: `between 2015 and 2025 2026` → **`between 2015 and 2025`** (2 occurrences: Methods intro + search-terms sentence).
- Objectives: `2015 and 2025 2026` → **`2015 and 2025`**.
- Methods: `Although 33 32 articles initially met` → **`Although 32 articles initially met`** (12+5+14+1 = 32 across databases; keep 32).
- Table 5 title: `the 15 22 articles considered most relevant` → **`the 22 studies included`** (the table lists 22).

**B2. Untranslated Spanish line with a typo (in the Tools section, after "Pain domain").**
Current: *"Variables más utilizadas: 5Q-5D-5L (calidad de vida relacionada con la salud), VAS (dolor), HADS (ansiedad y depresión), MoCA (cognitivo), IES-R (evaluación trauma)."*
- `5Q-5D-5L` is a typo for **EQ-5D-5L**.
- The line is Spanish in an English manuscript **and** names *VAS* for pain, but your Pain-domain text and Table 4 use *BPI* and *DN4*, not VAS — an internal inconsistency.
- **Replace with:** *"The most frequently used instruments across the included studies were the EQ-5D-5L (health-related quality of life), HADS (anxiety and depression), MoCA (cognition), IES-R (post-traumatic stress), and, for pain, the BPI and DN4."*

**B3. Duplicate reference entry (Sánchez-García).** The Sánchez-García reference appears **twice, concatenated** in the list (2023 *Int J Med Sci* 20(1):1-10 … then again "2022 Dec 19 … 20(1):1–10"). Same paper, two dates. **Delete the duplicate**, keep the version with the PMID/PMCID, and confirm the year (the DOI 10.7150/ijms.77792 is a 2023 article — use **2023**, matching Table 5 and the data).

**B4. Figure 2 (STROBE) says n = 23 but 22 studies were included.** Correct the caption to **n = 22** and verify the figure shows 22 bars.

**B5. STROBE is a reporting checklist, not a risk-of-bias tool.** Methods says *"Methodological quality and risk of bias were assessed using the STROBE guidelines."* STROBE assesses **reporting completeness**, not risk of bias. For cohort studies a referee will expect **Newcastle–Ottawa Scale** or **ROBINS-I**. Two clean options:
  - Reword to *"reporting quality was appraised with the STROBE checklist"* and drop the "risk of bias" claim; **or**
  - Add a proper risk-of-bias appraisal (NOS) alongside STROBE. Recommend the first if you don't want to re-score.

**B6. STROBE itself is uncited.** Add the STROBE reference (von Elm E, et al. *Lancet* 2007;370:1453-7) and cite it where STROBE is introduced.

**B7. Author↔citation-number drift in the Discussion (spot-check the whole section).** Example: *"Yamamoto et al. found that 47% of sepsis survivors still had physical disabilities a year later (18)"* — Yamamoto (ref for the COVID/IMV cohort) did **not** study sepsis; the 47 % sepsis figure and ref (18) point to a different (sepsis) study. The name and the number disagree. This class of error recurs (see also the delirium/cognition attributions). **Action:** after renumbering (F), re-verify every author-name ↔ number pairing in the Discussion against the reference list.

---

## C. Grammar, spelling, phrasing (find → replace)

| Location | Find | Replace |
|---|---|---|
| Intro §1 | `life threatening conditions` | `life-threatening conditions` |
| Intro §2 (Scope) | `the first-year post-survival` | `the first year after ICU discharge` |
| Intro §2 (Scope) | `adults in risk of becoming fragile` | `adults at risk of becoming frail` |
| Header (Current State) | `Current State of Knowledge on PICS Post-Intensive Care Syndrome in Adult Survivors` | `Current State of Knowledge on PICS in Adult Survivors` |
| Methods (search) | `key terms:` list ok, but | ensure Boolean operators and quotation marks render consistently |
| Table 5 (Nakamura row) | `r = -0.25, p = 0.011$)` | `r = −0.25, p = 0.011)` (delete stray `$`) |
| Discussion (Rehab para) | `improved quality of lifelong term` | `improved quality of life over the long term` |
| Discussion (Psych para) | `PTS)` on first use | define once: `post-traumatic stress (PTS)` or standardise to **PTSD** throughout |
| Throughout | mixed `MOCA` / `MoCA` | use **MoCA** everywhere |
| Throughout | `6-min walking test`, `6MWT`, `6-Minute Walk Test` | pick one (**6MWT**, defined once) |
| Discussion | `Ayenew et al.` pooled `54.35%` | fine, but note it is a *meta-analysis cited for context*; make explicit it was **not** an included study (you excluded meta-analyses) |
| Abstract | `PICS incidence ranged from 30% to 80%` | body Table 1 shows up to **90%** (COVID). Reconcile to `30% to 90%` or state the 80% refers to non-COVID cohorts |
| Abstract | `physical impairments in nearly 50%` | body reports physical up to **83%** (Nanwani). Clarify which population "nearly 50%" describes (sepsis) or raise the figure |

**Spacing/citation formatting** — many in-text citation clusters are malformed (stray spaces, a period used as a separator, digits fused). Clean all of these:
- `(21,13. 24)` → `(13, 21, 24)`
- `(22, 23,13,4, 29, 30,31)` → `(4, 13, 22, 23, 29, 30, 31)`
- `(13,4 , 29, 35)` → `(4, 13, 29, 35)`
- `(27,9)` → `(9, 27)`
- `(28,31)` → `(28, 31)`
- `( 4 ,10, 13, 22)` → `(4, 10, 13, 22)`
- `(25)` for the HABC-M "systematic screening" sentence — verify it points to Narváez-Martínez (the HABC-M validation), not Flaws.
- General rule: **one space after each comma, numbers ascending, no periods inside a citation group.** (This will largely resolve once references are renumbered, F.)

---

## D. Consistency & cross-referencing (tables/figures)

**D1. Reference-style consistency.** In-text uses parenthetical numerals `(1)`, `(2, 7)`. The PRISMA call-out uses square brackets `[40]`. **Standardise to parentheses** (or to the target journal's style) everywhere.

**D2. Reference-list style is mixed.** Some entries are full Vancouver with `PMID/PMCID`; others carry `[Internet]`, `[cited …]`, and abbreviated fields. **Harmonise to one style** (recommend journal-standard Vancouver: Authors. Title. Journal. Year;Vol(Issue):pages. doi.). Decide whether to keep PMIDs — keep or drop, but do so uniformly.

**D3. Every table must be called out in the text (comments 12/14/15/16).** Insert a citing sentence before each:
- **Table 1** — end of the Incidence paragraph: *"Table 1 summarises the reported prevalence of cognitive, psychological, and physical impairment by patient category."*
- **Table 2** — end of the Risk-factors intro: *"Table 2 details the principal risk factors and their proposed mechanisms."*
- **Table 3** — end of the Prevention intro: *"Table 3 synthesises the evidence-based preventive strategies."*
- **Table 4** — Tools section: *"Table 4 lists the standardised instruments used across domains."*
- **Table 5** — Treatment/synthesis: *"Table 5 presents the characteristics and key findings of the 22 included studies."*

**D4. Uniform table-caption format (comment 16).** Apply this template to all five:
> **Table N.** *[Descriptive title in sentence case].*
- Currently Table 4 and Table 5 use a colon (`Table 4:`) while Tables 1–3 use a period (`Table 1.`). Use **`Table N.`** (period) for all, sentence-case title, no trailing period inside the title.

**D5. Figure captions.** Same treatment: `Figure 1.` / `Figure 2.`, sentence case; ensure both are cited in text (Fig. 1 is, Fig. 2 add: *"Figure 2 shows the proportion of STROBE items met by each study."* — already present, keep).

**D6. Database-count arithmetic — state it adds up.** PubMed 12 + WOS 5 + Scopus 14 + CINAHL 1 = **32**; after de-duplication/full-text = **22**. Add a one-line reconciliation so the reader can follow 32 → 22 (duplicates + full-text exclusions = 10). This mirrors the PRISMA diagram.

---

## E. Substantive / structural improvements

**E1. Add the meta-analysis (biggest upgrade).** You have extractable continuous data for 10 domains and it has already been analysed (see `META_ANALYSIS.md`). Adding it:
- upgrades the paper from a narrative review to a **systematic review and meta-analysis** — retitle accordingly;
- gives quotable pooled numbers (6MWT 406 m; EQ-5D 0.79; HADS-A 4.7; HADS-D 4.9);
- directly evidences your central thesis (measurement is not standardised) via the high I².
- **Prerequisite:** fix the three data-quality blockers in `META_ANALYSIS.md` §4 (Cognition scale mix, Barthel outlier, ventilation units) first.

**E2. PROSPERO / protocol registration.** Reviewers of systematic reviews expect a registered protocol. State the PROSPERO ID or explicitly say the review was not registered (and why).

**E3. PRISMA 2020 checklist.** You cite PRISMA — add the completed PRISMA 2020 checklist as a supplement and reference it.

**E4. Selection reproducibility.** Methods say a *"multidisciplinary team of six"* screened. State **how many reviewers screened each record independently** and **how disagreements were resolved** (e.g., "two independent reviewers, third-party adjudication"). This is a PRISMA item and a common reviewer question.

**E5. Inclusion age threshold.** `≥19 years` is unusual (adult is typically ≥18). If 19 is deliberate (a specific guideline), justify it in one clause; otherwise use ≥18.

**E6. Objectives are broad.** Four objectives (tools, risk factors, prevention, awareness) is a lot for one review; the meta-analysis lets you foreground the **assessment-tools** objective as primary and frame the rest as secondary — which the current text already gestures at. Tighten the abstract Objectives to match.

**E7. Limitations paragraph — add the meta-analysis caveats.** Fold in: single-arm pooling (no comparator), high heterogeneity, median→mean conversion assumptions (Wan 2014), and instrument non-comparability within domains. This pre-empts the referee.

**E8. Discussion length / signposting.** The Discussion is a strong narrative but long; the subsection headers help. Ensure each subsection ends with a one-line "so what" that connects to a clinical or research recommendation (most already do).

---

## F. Reference list overhaul (comment 11 — the biggest editorial defect)

The in-text style is numeric-sequential `(1), (2)…`, which **requires references to be listed in order of first appearance**. They currently are not (neither appearance order nor alphabetical), and the list mixes styles and contains a duplicate. Do this:

1. **Renumber by order of first appearance** in the text. Every `(n)` in the body must equal the position of that source in the list.
2. **Re-verify each in-text number** after renumbering — especially the Discussion (see B7).
3. **Remove the duplicate** Sánchez-García entry (B3).
4. **Add** the missing methodological citations: **STROBE** (von Elm 2007), **Wan 2014** (median→mean), and confirm **PRISMA/Page 2020** is numbered in sequence (not hard-coded 40).
5. **Harmonise style** (D2).
6. Cross-check names that differ between the data workbook and the reference list: `Appel` (not "Apple"), `Narváez-Martínez` (not "Narvaez-Rojas"), and the single spelling `González`.

> **Tip:** once the manuscript is stable, `/validate-bib --semantic` (or a reference manager set to the target journal's Vancouver style) will re-sequence and flag any remaining missing/unused/duplicate entries automatically.

---

## G. Quick-win checklist (apply in this order)

1. [ ] Delete the doubled year/count leftovers — B1
2. [ ] Translate & fix the EQ-5D-5L Spanish line — B2
3. [ ] Remove duplicate Sánchez-García ref — B3
4. [ ] Fix Figure 2 caption to n = 22 — B4
5. [ ] Reword STROBE claim (+ cite STROBE) — B5/B6
6. [ ] Add the five table call-outs + uniform captions — D3/D4
7. [ ] Standardise citation brackets to parentheses — D1
8. [ ] Clean malformed in-text citation clusters — C
9. [ ] Renumber references by appearance; re-verify pairings — F/B7
10. [ ] Decide on and integrate the meta-analysis; retitle — E1
