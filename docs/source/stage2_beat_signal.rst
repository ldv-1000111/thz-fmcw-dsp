.. _stage2:

Stage 2 — Beat Signal Formation
================================

*Smith Ch. 6, 7, 13, 31 · Engine:* ``generate_chirp_if()`` output

The channel as an impulse response (Smith Ch. 7, p. 2)
---------------------------------------------------------

.. admonition:: Smith Ch. 7, p. 2

   "Enemy aircraft are detected with radar by analyzing a measured impulse
   response… Reflections from the target appear as peaks in this impulse
   response, with the time delay indicating the distance."

For K targets the channel impulse response is:

.. math::

   h[n] = \sum_k a_k\,\delta[n - n_k], \quad n_k = \text{round}\!\left(\frac{2R_k}{c}\cdot f_s\right)

The engine's Phase 1 target (R = 50 m): n₁ = round(2×50/3×10⁸ × 50×10⁶) = **bin 1334**.

The mixer as a matched filter (Smith Ch. 7, pp. 8–10)
-------------------------------------------------------

.. admonition:: Smith Ch. 7, p. 9

   "Correlation is the *optimal* technique for detecting a known waveform
   in random noise. No other linear filter can produce a higher SNR at the
   peak of the output."

The engine output ``exp(j·2π·f_beat·t)`` is the result of mixing the received
echo with the reference chirp — mathematically a cross-correlation, which is
the matched filter. Peak SNR = 2E/N₀ where E = N/fs = **100 µs**.

IQ output — unambiguous Doppler (Smith Ch. 30–31)
---------------------------------------------------

The engine generates ``std::complex<float>`` output. Smith Ch. 31, Eq. 31-4:
a real sinusoid = two complex exponentials at ±f. The engine's complex output
eliminates this ambiguity — the complex DFT in ``compute_range_doppler()``
places approaching targets at positive frequency bins, receding targets at
negative bins.

.. math::

   \text{out}[i] = I(t) + j\,Q(t) = A\,e^{\,j\,(2\pi f_{\text{beat}}\,t + \phi_0)}

Multi-target superposition — Phase 2 (Smith Ch. 5)
----------------------------------------------------

Phase 2 sums three ``generate_chirp_if()`` calls. Valid by Smith Ch. 5
additivity: each target's beat tone superimposes independently; the range
FFT separates them.

End effects and the guard interval (Smith Ch. 6, p. 5)
--------------------------------------------------------

Convolving an N-point signal with an M-point IF filter kernel produces N+M−1
output points. The first M−1 samples are corrupted end effects and must be
discarded — this defines the minimum detectable range R_min = c·(M−1)/(2·fs).
