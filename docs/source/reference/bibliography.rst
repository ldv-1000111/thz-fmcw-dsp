.. _reference_bibliography:

Bibliography
============

DSP foundation
--------------

Smith, S.W. (1997). *The Scientist and Engineer's Guide to Digital Signal
Processing*. California Technical Publishing. ISBN 0-9660176-3-3.
Available free at `dspguide.com <http://www.dspguide.com>`_.

Simulation design
------------------

Schasler, C., Hoffmann, M., Braunig, J., Ullmann, I., Ebelt, R., &
Vossiek, M. (2021). A Realistic Radar Ray Tracing Simulator for Large
MIMO-Arrays in Automotive Environments. *IEEE Journal of Microwaves*, 1(4),
962–974. https://doi.org/10.1109/JMW.2021.3104722

Justification for IF-domain simulation and the "simulate the beat signal,
not the carrier" design decision in ``fmcw_generator.cpp``.

Liu, G., Yang, W., Li, P., et al. (2022). MIMO Radar Parallel Simulation
System Based on CPU/GPU Architecture. *Sensors*, 22(1), 396.
https://doi.org/10.3390/s22010396

Data cube architecture and separable 2D processing.

FFTW3
------

Frigo, M., & Johnson, S.G. (2005). The Design and Implementation of FFTW3.
*Proceedings of the IEEE*, 93(2), 216–231.
https://doi.org/10.1109/JPROC.2003.823119

Used for range FFT and Doppler FFT in Phase 2 (``compute_range_doppler()``).
