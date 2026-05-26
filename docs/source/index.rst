.. _index:

fmcw-thz-radar-sim
==================

| **Author:** Luis Viveros
| **Date:** May 2026
| **Repository:** `github.com/ldv-1000111/fmcw-thz-radar-sim <https://github.com/ldv-1000111/fmcw-thz-radar-sim>`_
| **Documentation:** `fmcw-terahertz-radar-simulation.readthedocs.io <https://fmcw-terahertz-radar-simulation.readthedocs.io>`_

----

.. admonition:: Licence & Copyright

   © 2026 Luis Viveros. Released under the **MIT Licence** — permission is
   granted, free of charge, to any person obtaining a copy of this
   documentation and associated software to use, copy, modify, merge, publish,
   distribute, sublicense, and/or sell copies, subject to the condition that
   the above copyright notice and this permission notice appear in all copies.

   DSP theory references: Smith, S.W. (1997) *The Scientist and Engineer's
   Guide to Digital Signal Processing*, California Technical Publishing —
   used under fair use for educational and research purposes.
   Simulation design basis: Schasler et al. (2021), *IEEE Journal of
   Microwaves*, DOI 10.1109/JMW.2021.3104722.

   **This documentation is provided "as is", without warranty of any kind.**

----

A C++ simulation engine for **300 GHz THz FMCW radar** — physics-level IF
signal generation, 2D Range-Doppler processing with FFTW3, CA-CFAR detection,
and Yocto cross-compilation for automotive ADAS targets.

.. list-table::
   :widths: 30 70
   :stub-columns: 1

   * - **Phase 1 — v0.1.0**
     - IF physics engine, micro-Doppler, Catch2 tests, CI ✅
   * - **Phase 2 — v0.2.0**
     - Range-Doppler pipeline (FFTW3), CA-CFAR, 16 tests, 66,232 assertions ✅
   * - **Phase 3 — in progress**
     - Yocto deployment: NXP S32G, Renesas R-Car, Raspberry Pi 5

.. toctree::
   :maxdepth: 2
   :caption: Getting Started

   introduction
   sensor_landscape

.. toctree::
   :maxdepth: 3
   :caption: Phase 1 — IF Physics Engine

   phase1/overview
   phase1/fmcw_theory
   phase1/cpp_implementation
   phase1/cmake_build
   phase1/testing
   phase1/python_validation
   phase1/github_workflow

.. toctree::
   :maxdepth: 3
   :caption: Phase 2 — Signal Processing

   phase2/overview
   phase2/data_cube
   phase2/range_doppler
   phase2/cfar
   phase2/embedded_opt
   phase2/github_workflow

.. toctree::
   :maxdepth: 3
   :caption: Phase 3 — Yocto Deployment

   phase3/overview
   phase3/meta_layer
   phase3/bitbake_recipe
   phase3/build_workflow
   phase3/github_workflow

.. toctree::
   :maxdepth: 2
   :caption: Reference

   reference/formulas
   reference/smith_chapters
   reference/bibliography
