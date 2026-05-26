.. _phase2_overview:

Phase 2 Overview
================

.. list-table::
   :widths: 30 70
   :stub-columns: 1

   * - **Prerequisite**
     - Phase 1 tag ``v0.1.0`` — CI green on ``main``
   * - **Git tag**
     - ``v0.2.0``
   * - **Tests**
     - 16 Catch2 test cases, 66,232 assertions, 100% passing
   * - **New dependency**
     - FFTW3 (``libfftw3f``)
   * - **Python validation**
     - ``plot_range_doppler.py``: PASS all 3 targets (SNR 8.4 / 942.0 / 325.5)

.. toctree::
   :maxdepth: 1

   data_cube
   range_doppler
   cfar
   embedded_opt
   github_workflow
