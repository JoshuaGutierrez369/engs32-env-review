## ENGS 32 — Environmental Science Reviewer (`github.io` pattern)

**Live site (after Pages build):** **[https://joshuagutierrez369.github.io/engs32-env-review/](https://joshuagutierrez369.github.io/engs32-env-review/)**

**Repository:** [JoshuaGutierrez369/engs32-env-review](https://github.com/JoshuaGutierrez369/engs32-env-review)

**Your GitHub Pages domain:** [https://joshuagutierrez369.github.io/](https://joshuagutierrez369.github.io/)

**Recommended live URL for this app** (after you create a repository named `engs32-env-review` on account **joshuagutierrez369** and enable Pages):

**→ [https://joshuagutierrez369.github.io/engs32-env-review/](https://joshuagutierrez369.github.io/engs32-env-review/)**

*If you instead put these files in your user site repo `joshuagutierrez369.github.io` at the **root**, the app would be at `https://joshuagutierrez369.github.io/` (or in a subfolder e.g. `https://joshuagutierrez369.github.io/env/`).*

---

Standalone static site matching the CA3 examiner flow:

- Landing overlay → **Reviewer** (full bank, expandable rationale + references) or **Quiz Bee** (pick LO topics, shuffle, timer).
- **`questions.js`** — **LO5W** (Lec 5.2 water) and **LO5A** (Lec 5.3 air) each have **23** MCQ/T‑F items, matching the LO7 deck size, plus **LO7–LO13** (`window.ENVS_QB`). Rebuild pollution topics: `python scripts/merge_pollution_topics.py` (sources in `scripts/engs_pollution_bank.py`). Quiz “# Questions” caps to the loaded bank size on open.
- **PWA-lite**: `manifest.json` + `sw.js` caches `index.html`, `questions.js`, icons (open once online for offline reuse).
- **Answer grounding**: [`MATERIALS.md`](./MATERIALS.md) lists the six lecture PDFs that define keyed answers; [`SOURCES.md`](./SOURCES.md) notes optional cross-checks (Lawphil, UNDP, etc.). Quiz keys follow the **slides** (e.g. RA 9003 enacted **16 February 2001** on Lec 5.4).

### Deploy to GitHub Pages (account: **joshuagutierrez369**)

1. On GitHub, create repo **`engs32-env-review`** under **https://github.com/joshuagutierrez369** (Public is fine).
2. Push this entire folder (`index.html`, `questions.js`, `manifest.json`, `sw.js`, `icon.svg`, `SOURCES.md`, `README.md`) to the repo **root** on branch `main` (or serve from **`/docs`** if you prefer that layout).
3. **Settings → Pages → Build and deployment**: Source **Deploy from a branch**, folder **`/ (root)`** or **`/docs`**, matching where your `index.html` lives.
4. Open **`https://joshuagutierrez369.github.io/engs32-env-review/`** (GitHub may take 1–2 minutes after the first workflow/build).
5. Reload once online so **`sw.js`** registers for offline caching.

### Filename note

Pages often serves `index.html` as the directory default — keep **`index.html`** as entry (same idea as CA3 Pages deploy).

Optional: generate PNG icons (192/512) and add entries to `manifest.json` using your preferred favicon toolchain for better Android install banners.
