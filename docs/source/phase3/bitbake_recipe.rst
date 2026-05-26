.. _phase3_recipe:

BitBake Recipe
==============

.. code-block:: bitbake
   :caption: fmcw-thz-radar-sim_0.3.0.bb

   SUMMARY = "300 GHz THz FMCW radar simulation engine"
   AUTHOR  = "Luis Viveros"
   LICENSE = "MIT"
   LIC_FILES_CHKSUM = "file://LICENSE;md5=..."

   SRC_URI = "git://github.com/ldv-1000111/fmcw-thz-radar-sim.git;branch=main"
   SRCREV  = "\${AUTOREV}"

   DEPENDS = "fftw"

   inherit cmake

   EXTRA_OECMAKE = "-DCMAKE_BUILD_TYPE=Release"

   do_install() {
       install -d \${D}\${bindir}
       install -m 0755 \${B}/radar_sim \${D}\${bindir}/
   }
