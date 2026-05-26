.. _phase2_embedded:

Embedded Optimisation Notes
============================

For Phase 3 real-time deployment the key constraint is processing one CPI
(256 chirps × 5000 samples = 1.28 M samples) within the CPI duration of
256 × 100 µs = 25.6 ms.

FFTW3 WISDOM plan
------------------

Generate an optimal plan once and save it:

.. code-block:: bash

   fftwf-wisdom -o wisdom.fftw -n 5000   # range FFT plan
   fftwf-wisdom -o wisdom.fftw -n 256    # doppler FFT plan

Load at startup: ``fftwf_import_wisdom_from_filename("wisdom.fftw")``.
This typically reduces plan execution time by 30–40% on ARM NEON.

Double-buffering
-----------------

The ADC fills one buffer while the processor computes on the other (ping-pong).
See :ref:`phase3_overview` for the embedded implementation.
