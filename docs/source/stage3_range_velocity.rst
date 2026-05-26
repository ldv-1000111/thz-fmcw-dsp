.. _stage3:

Stage 3 — Range & Velocity Estimation
======================================

*Smith Ch. 8, 9, 10, 11, 12, 15, 16 · Engine:* ``compute_range_doppler()``

Range bin extraction (Smith Ch. 8)
------------------------------------

.. math::

   X[k] = \frac{1}{N}\sum_{n=0}^{N-1} x[n]\,e^{-j2\pi kn/N}

Range bin k maps to beat frequency f_k = k·fs/N and range R_k = k·c·fs·Tc/(2BN).

Beat frequency at R = 50 m:

.. math::

   f_{\text{beat}} = \frac{2\times4\times10^9\times50}{3\times10^8\times100\times10^{-6}}
                   = 13.33\;\text{MHz}
   \quad\Rightarrow\quad k = \text{round}\!\left(\frac{13.33\times10^6}{50\times10^6/5000}\right) = \mathbf{1334}

This matches the Phase 1 Catch2 test assertion ``REQUIRE(peak_bin == 1334)``.

Time-shift → beat frequency (Smith Ch. 10, p. 2)
--------------------------------------------------

A range delay of d samples multiplies the DFT by a linear phase ramp
e^(−j2πkd/N). The beat frequency is the slope of this ramp — the precise
mathematical mechanism by which FMCW encodes range as frequency.

Processing gain — Parseval's relation (Smith Ch. 10, Eq. 10-3)
----------------------------------------------------------------

.. math::

   \sum_n|x[n]|^2 = N\sum_k|X[k]|^2

White noise distributes equally across N bins → noise power/bin = σ²/N.

.. math::

   G_R = 10\log_{10}(N) = 10\log_{10}(5000) = \mathbf{37.0\;\text{dB}}

   G_D = 10\log_{10}(M) = 10\log_{10}(256) = \mathbf{24.1\;\text{dB}}

   G_{\text{total}} = 10\log_{10}(N\cdot M) = 10\log_{10}(1{,}280{,}000) = \mathbf{61.1\;\text{dB}}

FFTW3 and Smith Ch. 12
-----------------------

Smith Ch. 12 derives O(N log N) FFT complexity. The engine uses FFTW3 which
achieves the theoretical minimum constant factor via SIMD plans. N = 5000 is
not a power of 2 (= 2³×5⁴) — FFTW3 handles this via mixed-radix
decomposition. Smith's power-of-2 recommendation applies to simple FFT
implementations, not FFTW3.

Windowing (Smith Ch. 9, 16)
-----------------------------

``compute_range_doppler()`` applies a **Hann window** before the range FFT:

.. code-block:: cpp

   float w = 0.5f * (1.0f - std::cos(2.0f*M_PI*s/(num_samples-1)));
   cube[c][s] *= w;

Upgrade to Blackman (−74 dB) by replacing with:
``0.42 - 0.5*cos(x) + 0.08*cos(2x)`` (Smith Ch. 16, Eq. 16-2).

THz Doppler resolution
-----------------------

.. math::

   \Delta v = \frac{\lambda}{2\,M\,T_c}
             = \frac{1\;\text{mm}}{2\times256\times100\;\mu\text{s}}
             = \mathbf{0.195\;\text{mm/s}}

The engine's Phase 2 Doppler FFT resolves the 200 Hz engine vibration
(velocity amplitude = 2π×200×0.0002 = 251 mm/s) as two sidebands at
±200 Hz around the carrier Doppler bin.

Range-Doppler map — separable 2D processing (Smith Ch. 24)
-----------------------------------------------------------

The processing is separable: range FFT along fast-time (N=5000) and Doppler
FFT along slow-time (M=256) operate independently. Smith Ch. 24: a separable
2D PSF reduces to two sequential 1D convolutions.
