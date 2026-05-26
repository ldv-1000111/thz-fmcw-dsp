.. _stage1:

Stage 1 — Chirp Generation & the IF Signal Model
==================================================

*Smith Ch. 1, 3, 5, 11, 13, 30–32 · Engine:* ``generate_chirp_if()``

Why simulate in the IF domain
-------------------------------

At f₀ = 300 GHz, satisfying Nyquist on the carrier requires ADC sampling at
>600 GHz. The engine generates the IF beat signal instead — what hardware
produces after the mixer. This is numerically identical to real hardware output
(Schasler et al., 2021) and allows simulation at 50 MHz sample rate.

Linearity foundations (Smith Ch. 5)
-------------------------------------

The simulation is valid because the FMCW receive chain is a linear system:

- **Homogeneity** (p. 89): k·x[n] → k·y[n]. Scaling ``tgt.rcs`` scales output linearly.
- **Additivity** (p. 90): x₁+x₂ → y₁+y₂. Phase 2 superimposes three ``generate_chirp_if()`` calls — valid because beat tones from separate targets superpose independently.
- **Sinusoidal fidelity** (p. 94): each target produces exactly one beat tone. The DFT decomposes them cleanly.

Pulse compression (Smith Ch. 11, pp. 7–8)
-------------------------------------------

.. admonition:: Smith Ch. 11, p. 8

   "This allows the portions of the system that measure distance to see
   *short pulses*, while the power handling circuits see *long duration
   signals*. This type of waveshaping is a fundamental part of modern
   radar systems."

.. math::

   \Delta R = \frac{c}{2B} = \frac{3\times10^8}{2\times4\times10^9} = 3.75\;\text{cm}

Range resolution depends only on bandwidth, independent of chirp duration.
Matched-filter peak SNR = 2E/N₀ depends only on signal energy — a 100 µs
chirp achieves the same sensitivity as a 1 µs pulse at 100× lower peak power.

The complete IF signal model
------------------------------

For chirp index ``chirp_idx``, sample ``i`` (Smith Ch. 11, 13):

.. math::

   R(t) = \underbrace{R_0}_{\text{tgt.range}}
        + \underbrace{v\,(t_{\text{slow}}+t)}_{\text{tgt.velocity}}
        + \underbrace{A\sin(2\pi f_v(t_{\text{slow}}+t))}_{\text{vib\_amp / vib\_freq}}

.. math::

   f_{\text{beat}} = \frac{B}{T_c}\cdot\frac{2R(t)}{c}
                    + \frac{2\,f_0\,v}{c}

.. math::

   \text{out}[i] = e^{\,j\,2\pi\,f_{\text{beat}}\,t}, \quad t = i/f_s

Why THz makes micro-Doppler visible (Smith Ch. 10)
----------------------------------------------------

.. math::

   \Delta\phi_{\text{vib}} = \frac{4\pi\,A\,f_0}{c}

For A = 0.2 mm, f₀ = 300 GHz: **Δφ = 2.51 rad** — clearly resolved FM
sidebands in the IF spectrum. The same vibration at 77 GHz gives only
0.64 rad (3.9× less sensitive).

ADC constraint — max unambiguous range (Smith Ch. 3)
------------------------------------------------------

.. math::

   R_{\text{max}} = \frac{c\cdot f_s\cdot T_c}{4B}
               = \frac{3\times10^8\times50\times10^6\times100\times10^{-6}}
                       {4\times4\times10^9} = 93.75\;\text{m}

.. warning::

   The Phase 1 validation target (50 m, bin 1334) is safely within this
   limit. Targets beyond 93.75 m alias to a wrong range bin.
