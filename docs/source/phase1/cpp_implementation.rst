.. _phase1_cpp:

C++ Implementation
==================

``include/fmcw_generator.hpp``
--------------------------------

.. code-block:: cpp
   :caption: include/fmcw_generator.hpp
   :linenos:

   #pragma once
   #include <complex>
   #include <vector>
   #include <cmath>

   struct RadarParams {
       double f0;          // Start frequency (Hz)  e.g. 300e9
       double bandwidth;   // Sweep bandwidth (Hz)  e.g. 4e9 -> 3.75 cm ΔR
       double chirp_time;  // Chirp duration (s)    e.g. 100e-6
       double fs;          // IF sample rate (Hz)   e.g. 50e6
       int    num_samples; // Samples per chirp     e.g. 5000
       int    num_chirps;  // Chirps per CPI        e.g. 256
   };

   struct Target {
       double range;      // Initial range (m)
       double velocity;   // Radial velocity (m/s)
       double rcs;        // Radar cross-section (m²)
       double vib_amp;    // Vibration amplitude (m)  e.g. 0.0002 = 0.2 mm
       double vib_freq;   // Vibration frequency (Hz) e.g. 200.0
   };

   // Physics: beat_freq = (B/Tc)*tau + 2*f0*v/c
   //          tau(t) = 2*(R + v*t + A*sin(2*pi*fv*t)) / c
   //          out[i] = exp(j * 2*pi * beat_freq * t)
   void generate_chirp_if(
       const RadarParams& p, const Target& tgt,
       int chirp_idx,
       std::vector<std::complex<float>>& out  // pre-allocated, size = num_samples
   );

``src/main.cpp`` — canonical 300 GHz configuration
----------------------------------------------------

.. code-block:: cpp
   :caption: src/main.cpp (key parameters)

   const RadarParams p {
       300e9,   // f0         -> lambda = 1 mm
       4e9,     // bandwidth  -> ΔR = 3.75 cm
       100e-6,  // chirp_time
       50e6,    // fs         -> Nyquist limit = 25 MHz -> R_max = 93.75 m
       5000,    // num_samples (= fs * chirp_time)
       256      // num_chirps  (Phase 2 data cube)
   };

   const Target tgt {
       50.0,    // range    -> expected bin 1334
       0.0,     // velocity -> no Doppler shift
       1.0,     // rcs      -> unit reflectivity
       0.0002,  // vib_amp  -> 0.2 mm engine micro-Doppler
       200.0    // vib_freq -> 200 Hz idle vibration
   };

Expected output
---------------

.. code-block:: text

   Phase 1: wrote 5000 samples -> build/if_signal.csv
            f0=300 GHz  B=4 GHz  Tc=100 us  fs=50 MHz
            target: R=50.0 m  v=0.0 m/s  vib=0.200 mm @ 200 Hz
