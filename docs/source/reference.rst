.. _reference:

Reference
=========

Engine code ↔ Smith chapter map
---------------------------------

.. list-table::
   :header-rows: 1
   :widths: 35 12 53

   * - Engine symbol / file
     - Smith Ch.
     - Equation / concept
   * - ``p.f0 = 300e9`` → λ = 1 mm
     - Ch. 10
     - Δφ = 4πvTc/λ; λ governs all Doppler calculations
   * - ``p.bandwidth = 4e9`` → ΔR = 3.75 cm
     - Ch. 11, pp. 7–8
     - Pulse compression: ΔR = c/(2B)
   * - ``p.chirp_time = 100e-6``
     - Ch. 13
     - s_TX(t) = A·cos(2π[f₀t + (B/2Tc)t²])
   * - ``p.fs = 50e6``
     - Ch. 3, p. 8
     - Anti-alias Nyquist: R_max = c·fs·Tc/(4B) = 93.75 m
   * - ``p.num_samples = 5000``
     - Ch. 8; Ch. 12
     - DFT analysis equation; FFTW3 O(N log N); G_R = 37.0 dB
   * - ``p.num_chirps = 256``
     - Ch. 10; Ch. 15
     - Parseval: G_D = 24.1 dB; Δv = 0.195 mm/s
   * - ``generate_chirp_if()``
     - Ch. 5, 6, 7
     - Additivity; convolution; matched filtering; out[i]=exp(j·2π·f_beat·t)
   * - ``beat_freq = (B/Tc)·τ + 2·f0·v/c``
     - Ch. 11; Ch. 10
     - Chirp system dechirp; time-shift → beat frequency
   * - ``tgt.vib_amp·sin(2π·vib_freq·t)``
     - Ch. 10; Ch. 11
     - Δφ_vib = 4πAf₀/c = 2.51 rad (0.2 mm @ 300 GHz)
   * - ``std::complex<float>`` IQ output
     - Ch. 30, 31
     - Euler's relation; I+jQ resolves Doppler sign
   * - Hann window in ``compute_range_doppler()``
     - Ch. 16, Eq. 16-1
     - 0.5·(1−cos(2πi/M)); −44 dB sidelobes
   * - ``fftwf_execute(range_plan)``
     - Ch. 12
     - O(N log N); G_R = 37.0 dB; FFTW3 mixed-radix (N=5000)
   * - ``fftwf_execute(doppler_plan)``
     - Ch. 8, 10
     - Slow-time DFT; G_D = 24.1 dB; Δv = 0.195 mm/s
   * - ``cfar_detect()`` threshold
     - Ch. 26; Ch. 17
     - H₁/H₀; ROC curve; α = N·(P_FA^(−1/N)−1)
   * - Phase 3 double-buffer / DMA
     - Ch. 28, 29
     - MAC; ping-pong buffer; 25.6 ms CPI budget
   * - FFTW3 WISDOM plan
     - Ch. 18
     - Overlap-add; pre-computed H[k]; crossover ~60 taps
   * - IIR DC block (Phase 3)
     - Ch. 19, 33
     - y[n]=x[n]−x[n−1]+αy[n−1]; unit circle stability
   * - MIMO spatial FFT (Phase 3+)
     - Ch. 8, 10, 24, 25
     - Δθ = λ/(N_TX·N_RX·d); separable 3D; MTF/FWHM

Bibliography
-------------

Smith, S.W. (1997). *The Scientist and Engineer's Guide to Digital Signal
Processing*. California Technical Publishing. ISBN 0-9660176-3-3.
Available free at `dspguide.com <http://www.dspguide.com>`_.

Schasler, C. et al. (2021). A Realistic Radar Ray Tracing Simulator for Large
MIMO-Arrays in Automotive Environments. *IEEE Journal of Microwaves*, 1(4),
962–974. `DOI 10.1109/JMW.2021.3104722 <https://doi.org/10.1109/JMW.2021.3104722>`_.

Frigo, M. & Johnson, S.G. (2005). The Design and Implementation of FFTW3.
*Proceedings of the IEEE*, 93(2), 216–231.
`DOI 10.1109/JPROC.2003.823119 <https://doi.org/10.1109/JPROC.2003.823119>`_.
