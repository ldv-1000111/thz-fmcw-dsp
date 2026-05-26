.. _phase1_testing:

Testing — Phase 1
=================

The test suite uses **Catch2** with two test files.

.. list-table::
   :header-rows: 1
   :widths: 40 20 40

   * - Test file
     - Assertions
     - What it validates
   * - ``test_if_signal.cpp``
     - 430
     - Beat frequency, range bin accuracy, unit magnitude
   * - ``test_micro_doppler.cpp``
     - 177
     - Phase diffs variance, amplitude scaling, sideband structure

Running the tests
-----------------

.. code-block:: bash

   cd build && ctest --output-on-failure

Expected output:

.. code-block:: text

   Test project /path/to/build
       Start 1: test_if_signal
   1/2 Test #1: test_if_signal ..........   Passed    0.05 sec
       Start 2: test_micro_doppler
   2/2 Test #2: test_micro_doppler ......   Passed    0.02 sec

   100% tests passed, 0 tests failed out of 2
