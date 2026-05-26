.. _phase3_meta:

Yocto Meta-Layer Structure
===========================

.. code-block:: text

   meta-fmcw-thz/
   ├── conf/
   │   └── layer.conf
   ├── recipes-radar/
   │   └── fmcw-thz-radar-sim/
   │       └── fmcw-thz-radar-sim_0.3.0.bb
   └── recipes-support/
       └── fftw/
           └── fftw_%.bbappend     <- enables single-precision (libfftw3f)

``layer.conf``
--------------

.. code-block:: bash

   BBPATH  .= ":\${LAYERDIR}"
   BBFILES += "\${LAYERDIR}/recipes-*/*/*.bb"
   LAYERSERIES_COMPAT_meta-fmcw-thz = "scarthgap"
