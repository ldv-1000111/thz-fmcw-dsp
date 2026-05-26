.. _stage7:

Stage 7 — MIMO & Angle Estimation
===================================

*Smith Ch. 8, 10, 12, 24, 25 · Phase 3+ extension*

Spatial phase and angular resolution
--------------------------------------

For a uniform linear array (ULA) with element spacing d, a target at angle θ
induces a phase shift between adjacent receive elements (Smith Ch. 10):

.. math::

   \Delta\phi_{\text{spatial}} = \frac{2\pi\,d\,\sin\theta}{\lambda}
                                  = \frac{2\pi\,d\,\sin\theta\,f_0}{c}

This is the spatial analogue of the Doppler phase advance Δφ = 4πvTc/λ.
The same DFT machinery (Smith Ch. 8) resolves spatial frequencies as angles.

MIMO virtual aperture (Smith Ch. 24)
--------------------------------------

N_TX transmit × N_RX receive = N_TX × N_RX virtual elements.

.. math::

   \Delta\theta \approx \frac{\lambda}{N_{TX}\cdot N_{RX}\cdot d}

At 300 GHz with N_TX=3, N_RX=4, d = λ/2 = 0.5 mm:

.. math::

   \Delta\theta = \frac{1\;\text{mm}}{12\times0.5\;\text{mm}} = 0.167\;\text{rad} = 9.6^\circ

The same 12-element virtual aperture at 77 GHz requires a 23.4 mm antenna
array; at 300 GHz the same aperture fits in **6 mm**.

Separable 3D processing (Smith Ch. 24)
-----------------------------------------

The full 3D pipeline is separable — all three axes process independently:

1. **Range FFT** (fast-time, N=5000): ``compute_range_doppler()`` Step 1
2. **Doppler FFT** (slow-time, M=256): ``compute_range_doppler()`` Step 2
3. **Spatial FFT** (N_rx elements): new Phase 3+ function

MTF and resolution (Smith Ch. 25)
------------------------------------

- **FWHM**: beam width at −6 dB. With Hann window and N_virt=12, d=0.5 mm: FWHM ≈ 1.44×λ/(N_virt·d) = **13.8°**.
- **MTF** (Modulation Transfer Function): 2D Fourier transform of the beam pattern. Characterises how the THz sensor blurs point targets in the range-azimuth plane (Smith Ch. 25).

Fourier slice theorem — connection to SAR (Smith Ch. 25, pp. 20–27)
---------------------------------------------------------------------

Each aperture position provides a 1D range profile whose spectrum is a radial
slice of the 2D scene spectrum (Fourier slice theorem, Smith Ch. 25, Fig. 25-18).
Collecting profiles at multiple angles fills the 2D spectrum — inverse 2D FFT
reconstructs the scene image. This is the SAR image formation algorithm;
its ramp filter H[f] = |f| (Smith Ch. 25, Eq. 25-2) corrects the 1/f spectral
density bias of radial sampling.
