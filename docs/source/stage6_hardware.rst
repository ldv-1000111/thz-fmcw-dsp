.. _stage6:

Stage 6 — Hardware & Embedded Implementation
=============================================

*Smith Ch. 3, 4, 18, 28, 29 · Phase 3 targets: NXP S32G, Renesas R-Car, RPi 5*

Phase 3 deployment targets
----------------------------

.. list-table::
   :header-rows: 1
   :widths: 25 35 40

   * - Target
     - Processor
     - Key constraint
   * - NXP S32G
     - Cortex-A53 @ 1 GHz + LLCE/RTU
     - ASIL-D functional safety; CAN/Ethernet I/O
   * - Renesas R-Car
     - Cortex-A57 @ 1.5 GHz + IMP-X5
     - Vision + radar sensor fusion; low latency
   * - Raspberry Pi 5
     - Cortex-A76 @ 2.4 GHz
     - NEON SIMD; fastest iteration; development target

Real-time throughput budget (Smith Ch. 28)
--------------------------------------------

One CPI = 256 chirps × 5000 samples = 1.28 M samples in 25.6 ms.

.. list-table::
   :header-rows: 1

   * - Operation
     - Cost
     - Result
   * - Range FFTs (256 × O(5000 log 5000))
     - ~15.7 M ops
     - ~2 ms on RPi 5 (NEON)
   * - Doppler FFTs (5000 × O(256 log 256))
     - ~10.2 M ops
     - ~1.5 ms on RPi 5
   * - CA-CFAR
     - 5000×256 comparisons
     - ~0.5 ms
   * - **Total**
     - **~26 M ops**
     - **Target < 20 ms (20% margin)**

Double-buffer architecture (Smith Ch. 28–29)
----------------------------------------------

.. code-block:: cpp

   std::complex<float> buf[2][N_CHIRP][N_SAMP];
   volatile int active = 0;

   void adc_dma_isr(std::complex<float> sample) {
       int fill = 1 - active;
       buf[fill][write_chirp][write_samp++] = sample;
       if (write_samp == N_SAMP) {
           write_samp = 0;
           if (++write_chirp == N_CHIRP) {
               write_chirp = 0;
               active = fill;
               fftw_trigger(buf[active]);
           }
       }
   }

ADC selection (Smith Ch. 3)
-----------------------------

If analog SNR at ADC input is 60 dB, 12-bit ADC (σ_q ≈ V_FS/16,000) keeps
quantization below thermal noise. Engine uses float64 — quantization is absent
in simulation; real hardware ADC selection follows the Ch. 3 two-question rule.

Fixed-point vs. floating-point (Smith Ch. 4)
---------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Arithmetic
     - Dynamic range
     - FMCW use
   * - 16-bit integer
     - 96 dB
     - ADC sample storage; scale by ½ before each FFT butterfly stage
   * - 32-bit float
     - ~150 dB
     - Engine default; window multiplication; filter coefficients
   * - 64-bit double
     - ~300 dB
     - Chebyshev coefficient computation only (Ch. 20 instability)

Data reduction (Smith Ch. 27)
-------------------------------

Raw ADC: 256 × 5000 × 2 bytes = **2.5 MB/CPI**.
Detection list: ~10 targets × 5 parameters × 4 bytes = **~200 bytes/CPI** — 12,500:1 compression.
