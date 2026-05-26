.. _introduction:

Introduction
============

This tutorial builds a high-fidelity **300 GHz THz FMCW radar simulation
pipeline** in modern C++17, deployed on embedded Linux with the Yocto Project.

Why THz?
--------

.. list-table::
   :header-rows: 1
   :widths: 25 15 15 15 15 15

   * - Sensor
     - Range res.
     - Weather
     - Micro-Doppler
     - λ
     - ADAS status
   * - Camera
     - px-limited
     - ❌ fog/rain
     - ❌
     - 0.5 µm
     - L1–L2
   * - LiDAR
     - ~3 cm
     - ❌ fog
     - ❌
     - 905 nm
     - L3
   * - 77 GHz radar
     - ~4 cm
     - ✅
     - limited
     - 3.9 mm
     - L2–L3
   * - **300 GHz THz**
     - **3.75 cm**
     - **✅**
     - **✅ 0.2 mm visible**
     - **1.0 mm**
     - emerging

Why simulate in the IF domain?
-------------------------------

Simulating the THz carrier directly would require ADC sampling at >600 GHz —
computationally prohibitive. The engine generates the **IF beat signal**
instead, which is what hardware produces after the mixer. This approach
(established by Schasler et al., 2021) is numerically identical to real
hardware output.

.. note::

   All DSP theory in this documentation traces back to Smith's
   *The Scientist and Engineer's Guide to Digital Signal Processing*
   (dspguide.com). Chapter references are given throughout.
