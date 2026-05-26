.. _overview:

Overview
========

The simulation engine operates in the IF (intermediate frequency) domain —
the dechirped beat signal — not at the THz carrier. Simulating the carrier
at 300 GHz would require ADC sampling at >600 GHz; simulating the IF beat
signal at 50 MHz is computationally tractable and numerically identical to
what real hardware produces after the mixer (Schasler et al., 2021).

Canonical engine parameters
-----------------------------

.. list-table::
   :header-rows: 1
   :widths: 25 25 25 25

   * - Field
     - Value
     - Derived quantity
     - Smith basis
   * - ``p.f0 = 300e9``
     - 300 GHz
     - λ = 1.0 mm
     - Ch. 10 (Doppler phase)
   * - ``p.bandwidth = 4e9``
     - 4 GHz
     - ΔR = 3.75 cm
     - Ch. 11 (pulse compression)
   * - ``p.chirp_time = 100e-6``
     - 100 µs
     - κ = 4×10¹³ Hz/s
     - Ch. 13 (chirp waveform)
   * - ``p.fs = 50e6``
     - 50 MHz
     - R_max = 93.75 m
     - Ch. 3 (Nyquist)
   * - ``p.num_samples = 5000``
     - 5000 samples/chirp
     - Bin width = 3.75 cm
     - Ch. 8 (DFT)
   * - ``p.num_chirps = 256``
     - 256 chirps/CPI
     - Δv = 0.195 mm/s
     - Ch. 10 (Doppler)
   * - ``tgt.vib_amp = 0.0002``
     - 0.2 mm
     - Δφ_vib = 2.51 rad
     - Ch. 10 (micro-Doppler)
   * - ``tgt.vib_freq = 200.0``
     - 200 Hz
     - ±200 Hz IF sidebands
     - Ch. 11 (FM sidebands)

Core formulas
--------------

.. list-table::
   :header-rows: 1
   :widths: 35 40 25

   * - Quantity
     - Formula
     - Engine value
   * - Range resolution
     - ΔR = c / (2·B)
     - **3.75 cm**
   * - Max unambiguous range
     - R_max = c·fs·Tc / (4·B)
     - **93.75 m**
   * - Beat frequency at R
     - f_beat = 2·B·R / (c·Tc)
     - 13.33 MHz at R=50 m
   * - Doppler phase/chirp
     - Δφ = 4π·v·Tc / λ
     - 2.51 rad for 0.2 mm vib
   * - Velocity resolution
     - Δv = λ / (2·M·Tc)
     - **0.195 mm/s**
   * - Max velocity
     - v_max = λ / (4·Tc)
     - **2.5 m/s**
   * - Total CPI gain
     - G = 10·log₁₀(N·M)
     - **61.1 dB**

Window function reference
--------------------------

.. list-table::
   :header-rows: 1
   :widths: 20 40 15 25

   * - Window
     - Equation (Smith Ch. 16)
     - Sidelobes
     - FMCW use
   * - Rectangular
     - w[i] = 1
     - −21 dB
     - Never — inadequate dynamic range
   * - Hamming
     - 0.54 − 0.46·cos(2πi/M)
     - −53 dB
     - General purpose
   * - Blackman
     - 0.42 − 0.5·cos(2πi/M) + 0.08·cos(4πi/M)
     - −74 dB
     - **Recommended default**
   * - Blackman²
     - Self-convolve kernel
     - −148 dB
     - High dynamic range
