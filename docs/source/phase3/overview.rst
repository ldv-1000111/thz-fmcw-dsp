.. _phase3_overview:

Phase 3 Overview
================

.. list-table::
   :widths: 30 70
   :stub-columns: 1

   * - **Prerequisite**
     - Phase 2 tag ``v0.2.0``
   * - **Git tag**
     - ``v0.3.0`` (in progress)
   * - **Targets**
     - NXP S32G, Renesas R-Car, Raspberry Pi 5
   * - **Build system**
     - Yocto Project (meta-fmcw-thz)

Phase 3 cross-compiles the engine for embedded automotive Linux targets,
adds the real-time double-buffer ADC architecture, and runs on-target
profiling to confirm the 25.6 ms per CPI budget is met.

.. toctree::
   :maxdepth: 1

   meta_layer
   bitbake_recipe
   build_workflow
   github_workflow
