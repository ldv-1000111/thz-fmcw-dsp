.. _phase1_python:

Python Validation
=================

``scripts/plot_if.py`` reads ``build/if_signal.csv`` and validates the range
peak position against the expected bin number.

.. code-block:: bash

   python3 scripts/plot_if.py

Expected output:

.. code-block:: text

   Range bin accuracy: PASS  peak @ 49.9904 m  (expected 50.0 m)

The script:

1. Reads the 5000-sample complex IF signal from CSV
2. Applies a Hann window (Smith Ch. 16)
3. Computes the range FFT (NumPy FFT — equivalent to FFTW3)
4. Converts peak bin to range: R = bin × c × Tc / (2 × B × N / fs)
5. Checks |R_measured − 50.0| < 0.1 m
