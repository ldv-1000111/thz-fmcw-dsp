.. _phase1_ci:

GitHub Actions — Phase 1
=========================

.. code-block:: yaml
   :caption: .github/workflows/phase1-ci.yml

   name: Phase 1 CI

   on: [push, pull_request]

   jobs:
     build-and-test:
       runs-on: ubuntu-24.04
       steps:
         - uses: actions/checkout@v4
         - name: Install dependencies
           run: sudo apt-get install -y cmake ninja-build g++-12 python3-pip
                && pip install numpy matplotlib
         - name: CMake configure
           run: cmake --preset release
         - name: Build
           run: cmake --build build --parallel
         - name: Catch2 tests
           run: ctest --test-dir build --output-on-failure
         - name: Python validation
           run: ./build/radar_sim && python3 scripts/plot_if.py

Push procedure
--------------

.. code-block:: bash

   git checkout -b phase-1/physics-engine
   git add CMakeLists.txt include/ src/ tests/ scripts/ docs/ .github/
   git commit -m "feat(phase1): IF physics engine, tests, CI"
   git push -u origin phase-1/physics-engine
   # Wait for CI green, then:
   git checkout main && git merge --no-ff phase-1/physics-engine
   git tag -a v0.1.0 -m "Phase 1 complete" && git push origin main --tags
