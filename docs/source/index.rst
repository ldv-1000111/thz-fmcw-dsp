.. _index:

THz FMCW DSP — Complete Reference
===================================

| **Author:** Luis Viveros
| **Date:** May 2026
| **Simulation engine:** `fmcw-thz-radar-sim <https://github.com/ldv-1000111/fmcw-thz-radar-sim>`_
| **This repo:** `thz-fmcw-dsp <https://github.com/ldv-1000111/thz-fmcw-dsp>`_

----

.. admonition:: Licence & Copyright

   © 2026 Luis Viveros. Released under the **MIT Licence**.
   DSP theory: Smith, S.W. (1997) *The Scientist and Engineer's Guide to
   Digital Signal Processing*, California Technical Publishing — cited under
   fair use for educational and research purposes.
   Simulation basis: Schasler et al. (2021), *IEEE Journal of Microwaves*,
   DOI `10.1109/JMW.2021.3104722 <https://doi.org/10.1109/JMW.2021.3104722>`_.
   **Provided "as is", without warranty of any kind.**

----

DSP theory grounded in all 34 chapters of Smith's
*The Scientist and Engineer's Guide to Digital Signal Processing*,
tied directly to the ``fmcw-thz-radar-sim`` C++ engine.
Every equation maps to a struct field, a function, or a test assertion
in the codebase. All worked examples use the engine's canonical
300 GHz parameters: **f0 = 300 GHz, B = 4 GHz, Tc = 100 µs,
fs = 50 MHz, N = 5000, M = 256**.

.. toctree::
   :maxdepth: 2
   :caption: DSP Reference

   overview
   stage1_chirp
   stage2_beat_signal
   stage3_range_velocity
   stage4_noise_detection
   stage5_filtering
   stage6_hardware
   stage7_mimo_angle
   reference
