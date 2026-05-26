.. _reference_smith:

Smith Chapter Map
==================

Every DSP concept in the engine traces back to a chapter in Smith's
*The Scientist and Engineer's Guide to Digital Signal Processing*
(available free at `dspguide.com <http://www.dspguide.com>`_).

.. list-table::
   :header-rows: 1
   :widths: 12 28 60

   * - Chapter
     - Title
     - Engine connection
   * - Ch. 3
     - ADC and DAC
     - σ_q = LSB/√12; Nyquist: R_max = 93.75 m; anti-alias
   * - Ch. 5
     - Linear Systems
     - Additivity justifies multi-target superposition
   * - Ch. 7
     - Properties of Convolution
     - Mixer = matched filter; optimum SNR = 2E/N₀
   * - Ch. 8
     - The DFT
     - Range bin extraction; range bin = 1334 at R=50 m
   * - Ch. 10
     - Fourier Transform Properties
     - Time-shift → phase slope (beat frequency); Δφ_vib
   * - Ch. 11
     - Fourier Transform Pairs
     - Pulse compression; ΔR = c/(2B) = 3.75 cm
   * - Ch. 12
     - The FFT
     - O(N log N); FFTW3 mixed-radix for N=5000
   * - Ch. 13
     - Continuous Signal Processing
     - Chirp waveform; convolution integral
   * - Ch. 16
     - Windowed-Sinc Filters
     - Hann window in compute_range_doppler(); upgrade to Blackman
   * - Ch. 17
     - Custom Filters
     - Matched filter SNR = 2E/N₀; Wiener filter = CFAR upper bound
   * - Ch. 24
     - Linear Image Processing
     - Separable 2D PSF: range FFT × Doppler FFT independent
   * - Ch. 25
     - Special Imaging Techniques
     - MTF/FWHM for THz MIMO angular resolution
   * - Ch. 26
     - Neural Networks (and more!)
     - ROC curve; CFAR α = N·(P_FA^(−1/N)−1)
   * - Ch. 28
     - Digital Signal Processors
     - MAC operation; circular buffer; 46 µs / 1024-pt FFT
   * - Ch. 31
     - The Complex Fourier Transform
     - IQ output; complex DFT resolves Doppler sign
