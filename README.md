## ENGS 32 — Environmental Science Reviewer (`github.io` pattern)

**Your GitHub Pages domain:** [https://joshuagutierrez369.github.io/](https://joshuagutierrez369.github.io/)

**Recommended live URL for this app** (after you create a repository named `engs32-env-review` on account **joshuagutierrez369** and enable Pages):

**→ [https://joshuagutierrez369.github.io/engs32-env-review/](https://joshuagutierrez369.github.io/engs32-env-review/)**

*If you instead put these files in your user site repo `joshuagutierrez369.github.io` at the **root**, the app would be at `https://joshuagutierrez369.github.io/` (or in a subfolder e.g. `https://joshuagutierrez369.github.io/env/`).*

---

Standalone static site matching the CA3 examiner flow:

- Landing overlay → **Reviewer** (full bank, expandable rationale + references) or **Quiz Bee** (pick LO topics, shuffle, timer).
- **`questions.js`** — question bank keyed by LO7–LO13; editable without touching markup.
- **PWA-lite**: `manifest.json` + `sw.js` caches `index.html`, `questions.js`, icons (open once online for offline reuse).
- **Verification notes**: [`SOURCES.md`](./SOURCES.md) lists primary statutes and UN/IPCC portals used to justify keyed answers (e.g. **RA 9003 approved 26 January 2001 on Lawphil**, not the Feb 16 typo some slides repeat).

### Deploy to GitHub Pages (account: **joshuagutierrez369**)

1. On GitHub, create repo **`engs32-env-review`** under **https://github.com/joshuagutierrez369** (Public is fine).
2. Push this entire folder (`index.html`, `questions.js`, `manifest.json`, `sw.js`, `icon.svg`, `SOURCES.md`, `README.md`) to the repo **root** on branch `main` (or serve from **`/docs`** if you prefer that layout).
3. **Settings → Pages → Build and deployment**: Source **Deploy from a branch**, folder **`/ (root)`** or **`/docs`**, matching where your `index.html` lives.
4. Open **`https://joshuagutierrez369.github.io/engs32-env-review/`** (GitHub may take 1–2 minutes after the first workflow/build).
5. Reload once online so **`sw.js`** registers for offline caching.

### Filename note

Pages often serves `index.html` as the directory default — keep **`index.html`** as entry (same idea as CA3 Pages deploy).

Optional: generate PNG icons (192/512) and add entries to `manifest.json` using your preferred favicon toolchain for better Android install banners.
