# thz-fmcw-dsp

**DSP reference documentation for 300 GHz THz FMCW radar simulation**

Author: Luis Viveros · May 2026  
Repository: [thz-fmcw-dsp](https://github.com/ldv-1000111/thz-fmcw-dsp)  
Simulation engine: [fmcw-thz-radar-sim](https://github.com/ldv-1000111/fmcw-thz-radar-sim)  
Live docs: [thz-fmcw-dsp.readthedocs.io](https://thz-fmcw-dsp.readthedocs.io)

---

## Scope

This repository contains the **documentation source** for the `fmcw-thz-radar-sim`
C++ simulation engine — a physics-level 300 GHz THz FMCW radar simulator covering
IF signal generation, 2D Range-Doppler processing, CA-CFAR detection, and Yocto
cross-compilation for automotive ADAS targets.

The documentation is grounded in all 34 chapters of Smith's
*The Scientist and Engineer's Guide to Digital Signal Processing* (dspguide.com),
with every equation and design decision traced back to a specific chapter and page.
Every DSP concept maps to a concrete function, struct field, or test assertion in
the simulation engine.

This is a **documentation-only repository**. It does not contain C++ source code.
For the simulation engine itself, see
[fmcw-thz-radar-sim](https://github.com/ldv-1000111/fmcw-thz-radar-sim).

---

## What is covered

| Section | Content |
|---------|---------|
| **Phase 1 — IF Physics Engine** | `generate_chirp_if()` signal model, THz micro-Doppler theory, beat frequency derivation, ADC constraints, Catch2 test documentation, Python validation |
| **Phase 2 — Signal Processing** | `compute_range_doppler()` FFTW3 pipeline, Hann windowing, range-Doppler map, CA-CFAR detection, embedded optimisation notes |
| **Phase 3 — Yocto Deployment** | Yocto meta-layer, BitBake recipe, NXP S32G / Renesas R-Car / Raspberry Pi 5 targets, ARM64 CI, on-target profiling |
| **Reference** | Complete formula table, Smith chapter map (all 34 chapters), bibliography |

---

## Why THz?

| Property | 77 GHz radar | **300 GHz THz** |
|----------|-------------|-----------------|
| Wavelength λ | 3.9 mm | **1.0 mm** |
| Range resolution | ~4 cm | **3.75 cm** (at B = 4 GHz) |
| Micro-Doppler phase (0.2 mm vib.) | 0.64 rad | **2.51 rad** — 3.9× more sensitive |
| Doppler resolution (M=256, Tc=100 µs) | 0.76 mm/s | **0.195 mm/s** |
| Angular resolution (same aperture) | baseline | **3.9× finer** |
| All-weather penetration | ✅ | ✅ |

THz sensors detect sub-millimetre mechanical vibrations that are invisible to
conventional automotive radar — enabling engine fault detection, pedestrian
micro-Doppler classification, and structural health monitoring at short range.

---

## Engine parameters (canonical)

```cpp
// fmcw-thz-radar-sim · src/main.cpp
const RadarParams p {
    300e9,   // f0         → λ = 1 mm
    4e9,     // bandwidth  → ΔR = 3.75 cm
    100e-6,  // chirp_time → κ = 4×10¹³ Hz/s
    50e6,    // fs         → R_max = 93.75 m
    5000,    // num_samples (= fs × chirp_time)
    256      // num_chirps  (Phase 2 data cube)
};

const Target tgt {
    50.0,    // range    → expected range bin 1334
    0.0,     // velocity → no Doppler shift
    1.0,     // rcs      → unit reflectivity
    0.0002,  // vib_amp  → 0.2 mm engine idle vibration
    200.0    // vib_freq → 200 Hz
};
```

---

## Repository structure

```
thz-fmcw-dsp/
├── README.md
├── LICENSE
└── docs/
    ├── .readthedocs.yaml        ← RTD build config (Python 3.12, ubuntu-24.04)
    ├── requirements.txt         ← sphinx 7.4.7, sphinx-rtd-theme 3.0.2
    └── source/
        ├── conf.py              ← Sphinx config, HPE dark theme
        ├── index.rst            ← Master toctree + licence notice
        ├── introduction.rst
        ├── sensor_landscape.rst
        ├── _static/
        │   └── custom.css       ← HPE Server Docs theme overrides
        ├── phase1/              ← 7 pages: IF physics engine
        ├── phase2/              ← 6 pages: signal processing pipeline
        ├── phase3/              ← 5 pages: Yocto deployment
        └── reference/           ← 3 pages: formulas, Smith map, bibliography
```

---

## Building locally

```bash
pip install sphinx sphinx-rtd-theme sphinx-copybutton myst-parser

sphinx-build -b html docs/source docs/_build/html
open docs/_build/html/index.html
```

---

## DSP foundation

All theory is grounded in:

> Smith, S.W. (1997). *The Scientist and Engineer's Guide to Digital Signal
> Processing*. California Technical Publishing. Available free at
> [dspguide.com](http://www.dspguide.com).

Key chapters: Ch. 3 (ADC), Ch. 5 (Linear Systems), Ch. 7 (Matched Filtering),
Ch. 10 (Fourier Properties / Doppler), Ch. 11 (Pulse Compression / Chirp),
Ch. 12 (FFT), Ch. 16 (Windowing), Ch. 17 (Wiener/Matched Filter), Ch. 26 (CFAR).

---

## Simulation basis

> Schasler, C. et al. (2021). A Realistic Radar Ray Tracing Simulator for Large
> MIMO-Arrays in Automotive Environments. *IEEE Journal of Microwaves*, 1(4),
> 962–974. DOI: [10.1109/JMW.2021.3104722](https://doi.org/10.1109/JMW.2021.3104722)

Justifies IF-domain simulation: generating the beat signal directly rather than
sampling at the 600 GHz carrier frequency.

---

## Licence

MIT Licence — see [LICENSE](LICENSE).  
© 2026 Luis Viveros.
