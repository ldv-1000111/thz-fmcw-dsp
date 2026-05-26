.. _phase3_ci:

GitHub Actions — Phase 3
=========================

Phase 3 CI validates that the Yocto recipe parses and that the CMake cross-
compilation (ARM64) succeeds.

.. code-block:: yaml
   :caption: .github/workflows/phase3-ci.yml

   - name: Install ARM64 cross-compiler
     run: sudo apt-get install -y gcc-aarch64-linux-gnu g++-aarch64-linux-gnu

   - name: CMake cross-compile
     run: |
       cmake -B build-arm64 \
         -DCMAKE_TOOLCHAIN_FILE=cmake/aarch64-toolchain.cmake \
         -DCMAKE_BUILD_TYPE=Release
       cmake --build build-arm64 --parallel

   - name: Verify binary is ARM64
     run: file build-arm64/radar_sim | grep aarch64

.. todo::

   Full Yocto build CI is pending — Yocto builds take 2–4 hours and
   require a self-hosted runner with 50 GB free disk space.
