.. _phase3_build:

Yocto Build Workflow
====================

.. code-block:: bash

   # Clone Poky + add meta-fmcw-thz
   git clone -b scarthgap https://github.com/yoctoproject/poky.git
   cd poky
   git clone https://github.com/ldv-1000111/meta-fmcw-thz.git

   source oe-init-build-env build-rpi5

   # Add layer
   bitbake-layers add-layer ../meta-fmcw-thz

   # Build for Raspberry Pi 5
   MACHINE=raspberrypi5 bitbake fmcw-thz-radar-sim

On-target profiling
--------------------

.. code-block:: bash

   # On RPi 5
   perf stat -e cycles,cache-misses ./radar_sim
   # Target: < 20 ms per CPI (25.6 ms budget - 20% margin)
