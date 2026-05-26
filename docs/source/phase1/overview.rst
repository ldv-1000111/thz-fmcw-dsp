.. _phase1_overview:

Phase 1 Overview
================

.. list-table::
   :widths: 30 70
   :stub-columns: 1

   * - **Git tag**
     - ``v0.1.0``
   * - **Status**
     - Complete — CI green on ``main``
   * - **Tests**
     - 7 Catch2 test cases, 607 assertions, 100% passing
   * - **Python validation**
     - ``plot_if.py``: PASS — peak at 49.99 m (bin 1334)

Phase 1 delivers the core physics engine: ``generate_chirp_if()`` produces
the complex analytic IF beat signal for one chirp, including THz micro-Doppler.

.. toctree::
   :maxdepth: 1

   fmcw_theory
   cpp_implementation
   cmake_build
   testing
   python_validation
   github_workflow
