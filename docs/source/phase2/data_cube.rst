.. _phase2_data_cube:

Data Cube Architecture
=======================

Phase 2 builds a 2D data cube ``cube[num_chirps][num_samples]`` and processes
it with two separable FFT stages (Smith Ch. 24).

.. list-table::
   :header-rows: 1
   :widths: 20 20 20 40

   * - Axis
     - Dimension
     - After FFT
     - Encodes
   * - Fast-time
     - N = 5000 samples/chirp
     - Range FFT
     - Target distance (ΔR = 3.75 cm/bin)
   * - Slow-time
     - M = 256 chirps/CPI
     - Doppler FFT
     - Radial velocity (Δv = 0.195 mm/s/bin)

Three-target scenario
----------------------

Phase 2 superimposes three ``generate_chirp_if()`` calls:

.. code-block:: cpp

   // Targets: R = 20 m, 50 m, 80 m  (velocity = 0 in Phase 2 baseline)
   for (const auto& tgt : targets)
       for (int c = 0; c < num_chirps; ++c) {
           generate_chirp_if(p, tgt, c, tmp);
           for (int s = 0; s < num_samples; ++s) cube[c][s] += tmp[s];
       }

Valid by Smith Ch. 5 additivity — the range FFT separates the three peaks
independently.
