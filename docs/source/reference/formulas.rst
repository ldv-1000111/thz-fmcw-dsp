.. _reference_formulas:

Formula Quick Reference
========================

All formulas use engine parameter names.

.. list-table::
   :header-rows: 1
   :widths: 30 40 30

   * - Quantity
     - Formula
     - Engine value
   * - Wavelength λ
     - c / p.f0
     - **1.0 mm**
   * - Range resolution ΔR
     - c / (2·p.bandwidth)
     - **3.75 cm**
   * - Max range R_max
     - c·p.fs·p.chirp_time / (4·p.bandwidth)
     - **93.75 m**
   * - Beat freq at R
     - 2·p.bandwidth·R / (c·p.chirp_time)
     - 13.33 MHz at R=50 m
   * - Range bin at R
     - round(f_beat · N / p.fs)
     - **bin 1334** at R=50 m
   * - Micro-Doppler phase
     - 4π·tgt.vib_amp·p.f0 / c
     - **2.51 rad** (0.2 mm)
   * - Velocity resolution Δv
     - λ / (2·M·p.chirp_time)
     - **0.195 mm/s/bin**
   * - Max velocity v_max
     - λ / (4·p.chirp_time)
     - **2.5 m/s**
   * - Range FFT gain
     - 10·log₁₀(N)
     - **37.0 dB** (N=5000)
   * - Doppler FFT gain
     - 10·log₁₀(M)
     - **24.1 dB** (M=256)
   * - Total CPI gain
     - 10·log₁₀(N·M)
     - **61.1 dB**
