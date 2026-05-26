.. _phase1_cmake:

CMake Build
===========

Dependencies
------------

.. code-block:: bash

   # Ubuntu 22.04 / 24.04
   sudo apt install cmake ninja-build g++-12 python3-pip
   pip install numpy matplotlib

Build
-----

.. code-block:: bash

   git clone https://github.com/ldv-1000111/fmcw-thz-radar-sim.git
   cd fmcw-thz-radar-sim
   cmake --preset release          # or: cmake -B build -DCMAKE_BUILD_TYPE=Release
   cmake --build build --parallel
   ./build/radar_sim               # writes build/if_signal.csv

Run tests
---------

.. code-block:: bash

   ctest --test-dir build --output-on-failure
   # Expected: 7/7 test cases passed, 607 assertions
