.. _sensor_landscape:

Sensor Landscape
================

The simulation engine is motivated by a concrete gap in the automotive
sensing stack: no existing production sensor combines all-weather robustness
with sub-centimetre range resolution and micro-Doppler sensitivity.

THz advantages for ADAS
------------------------

- **λ = 1 mm** — 3.9× shorter than 77 GHz, giving 3.9× finer angular
  resolution for the same aperture, or equal angular resolution in a
  3.9× smaller antenna array.
- **Micro-Doppler phase depth** — a 0.2 mm engine vibration at 300 GHz
  produces Δφ = 2.51 rad per cycle; at 77 GHz the same vibration gives
  only 0.64 rad — barely detectable.
- **Weather penetration** — THz wavelengths (1 mm) are large compared to
  fog droplets (~100 µm), placing scattering in the Rayleigh regime where
  attenuation ∝ (d/λ)⁴. Practical attenuation at 300 GHz in dense fog:
  < 3 dB over 100 m.

Simulation scope
----------------

The engine covers three phases:

1. **Phase 1**: single-target IF signal generation with THz micro-Doppler
2. **Phase 2**: multi-target Range-Doppler map via FFTW3 + CA-CFAR detection
3. **Phase 3**: Yocto cross-compilation for NXP S32G, R-Car, RPi 5
