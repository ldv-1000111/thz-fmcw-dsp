# thz-fmcw-dsp

**THz FMCW DSP — Complete Reference**

Author: Luis Viveros · May 2026
Repository: [thz-fmcw-dsp](https://github.com/ldv-1000111/thz-fmcw-dsp)
Simulation engine: [fmcw-thz-radar-sim](https://github.com/ldv-1000111/fmcw-thz-radar-sim)
Live docs: [thz-fmcw-dsp.readthedocs.io](https://thz-fmcw-dsp.readthedocs.io)

---

## Scope

DSP theory reference grounded in all 34 chapters of Smith's
*The Scientist and Engineer's Guide to Digital Signal Processing*,
tied directly to the `fmcw-thz-radar-sim` C++ engine.
Every equation maps to a struct field, function, or test assertion
in the codebase. All worked examples use the engine's canonical
300 GHz parameters.

**This is a documentation-only repository.**
For the simulation engine, see
[fmcw-thz-radar-sim](https://github.com/ldv-1000111/fmcw-thz-radar-sim).

---

## Contents

| Page | Smith chapters | Content |
|------|---------------|---------|
| Overview | Ch. 3, 8, 10, 11, 16 | Engine parameters, core formulas, window reference |
| Stage 1 — Chirp & IF Model | Ch. 5, 11, 13, 30–32 | `generate_chirp_if()` signal model, THz micro-Doppler |
| Stage 2 — Beat Signal | Ch. 6, 7, 13, 31 | Channel impulse response, matched filtering, IQ |
| Stage 3 — Range & Velocity | Ch. 8, 9, 10, 12, 16, 24 | Range FFT, Doppler FFT, FFTW3, Hann window |
| Stage 4 — Noise & CFAR | Ch. 2, 7, 9, 17, 26 | `cfar_detect()`, Wiener filter, ROC curve |
| Stage 5 — Filtering | Ch. 14–21, 26, 33 | Hann/Blackman, IIR DC block, overlap-add |
| Stage 6 — Hardware | Ch. 3, 4, 18, 28, 29 | Phase 3 targets, double-buffer, throughput budget |
| Stage 7 — MIMO & Angle | Ch. 8, 10, 12, 24, 25 | Virtual aperture, spatial FFT, MTF, SAR |
| Reference | All 34 Ch. | Engine ↔ Smith map, bibliography |

---

## Building locally

```bash
pip install sphinx sphinx-rtd-theme sphinx-copybutton myst-parser
sphinx-build -b html docs/source docs/_build/html
open docs/_build/html/index.html
```

---

## Licence

MIT Licence — see [LICENSE](LICENSE).
© 2026 Luis Viveros.
