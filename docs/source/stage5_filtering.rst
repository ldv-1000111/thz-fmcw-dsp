.. _stage5:

Stage 5 — Filtering
====================

*Smith Ch. 14–21, 26, 33 · Engine:* ``signal_processing.cpp``, ``cfar.cpp``

What the engine currently uses
--------------------------------

.. list-table::
   :header-rows: 1
   :widths: 30 30 40

   * - Engine stage
     - Filter
     - Smith basis
   * - Range FFT pre-weighting
     - Hann window (−44 dB)
     - Ch. 16, Eq. 16-1
   * - IF low-pass (implicit)
     - ADC Nyquist brick-wall
     - Ch. 3 anti-alias
   * - CFAR threshold
     - CA-CFAR moving average
     - Ch. 15 (moving avg); Ch. 26
   * - Doppler axis
     - None (Phase 3 upgrade)
     - Ch. 16 upgrade path

FIR design — windowed-sinc (Smith Ch. 16)
-------------------------------------------

.. math::

   w_{\text{Hann}}[i] &= 0.5\,(1 - \cos(2\pi i/M)) \\
   w_{\text{Blackman}}[i] &= 0.42 - 0.5\cos(2\pi i/M) + 0.08\cos(4\pi i/M) \\
   h[i] &= w[i]\cdot\frac{\sin(2\pi f_c(i-M/2))}{\pi(i-M/2)}, \quad
   M \approx \frac{4}{BW}

IIR DC block for Phase 3 clutter (Smith Ch. 19)
-------------------------------------------------

.. code-block:: cpp

   // Apply to each range bin's slow-time series before Doppler FFT
   y[n] = x[n] - x[n-1] + alpha * y[n-1];   // alpha = 0.99

At f₀ = 300 GHz with λ = 1 mm, α = 0.99 rejects velocities below
32·λ/2 = 16 mm/s — all static clutter — while preserving pedestrians
(v > 0.5 m/s) and all vehicles.

z-domain IIR stability (Smith Ch. 33)
---------------------------------------

All IIR poles must satisfy |z| < 1 (inside the unit circle). The frequency
axis runs 0 to π around the unit circle = 0 to fs/2 in Hz.

.. warning::

   Smith Ch. 20: 4-pole and 6-pole Chebyshev filters with fc ≤ 0.025·fs
   are unstable in single precision. Use double precision for coefficient
   computation for narrow Doppler notch filters.

Real-time streaming — overlap-add (Smith Ch. 18)
--------------------------------------------------

Phase 3 uses overlap-add for real-time FIR filtering::

   1. Pre-compute H[k] = FFT(h[n], L)  — once at startup
   2. Per chirp segment: X[k] = FFT(segment)
   3. Y[k] = X[k] · H[k]
   4. y[n] = IFFT(Y[k])
   5. Overlap-add last M−1 samples

Speed crossover at ~60 taps (Ch. 18, Fig. 18-3). The Hann kernel is
pre-computed once and reused for all chirps.

VCO nonlinearity correction (Smith Ch. 17, Ch. 22)
----------------------------------------------------

The THz VCO multiplication chain introduces phase nonlinearity that broadens
range peaks. Two correction approaches:

- **Deconvolution** (Ch. 17, pp. 7–9): inverse filter cancels the blurring kernel.
- **Cepstral analysis** (Ch. 22, pp. 19–21): the cepstrum separates the nonlinearity signature (short quefrency) from the target response (longer quefrency). Planned for Phase 3 factory calibration.
