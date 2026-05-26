.. _phase2_ci:

GitHub Actions — Phase 2
=========================

.. code-block:: yaml
   :caption: .github/workflows/phase2-ci.yml (key steps)

   - name: Install FFTW3
     run: sudo apt-get install -y libfftw3-dev pkg-config

   - name: CMake configure
     run: cmake --preset release

   - name: Build
     run: cmake --build build --parallel

   - name: Catch2 tests (16 cases, 66232 assertions)
     run: ctest --test-dir build --output-on-failure

   - name: Python Range-Doppler validation
     run: ./build/radar_sim && python3 scripts/plot_range_doppler.py

Push procedure
--------------

.. code-block:: bash

   git checkout -b phase-2/signal-processing
   git add src/ include/ tests/ scripts/ CMakeLists.txt .github/
   git commit -m "feat(phase2): Range-Doppler pipeline, CA-CFAR, FFTW3, 16 tests"
   git push -u origin phase-2/signal-processing
   # Wait for CI green, then merge and tag v0.2.0
