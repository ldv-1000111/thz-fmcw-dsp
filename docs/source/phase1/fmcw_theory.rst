.. _phase1_fmcw_theory:

FMCW Theory — 300 GHz THz
==========================

All equations are tied to engine parameter names (``p.*`` and ``tgt.*``).

Chirp waveform (Smith Ch. 13)
-------------------------------

.. math::

   s_{TX}(t) = A \cos\!\left(2\pi\left[f_0 t + \frac{B}{2T_c} t^2\right]\right)

- ``p.f0`` = 300 GHz, ``p.bandwidth`` = 4 GHz, ``p.chirp_time`` = 100 µs

Range resolution (Smith Ch. 11)
---------------------------------

.. math::

   \Delta R = \frac{c}{2B} = \frac{3\times10^8}{2\times4\times10^9} = 3.75\;\text{cm}

IF beat signal model (Smith Ch. 7, 10, 11)
--------------------------------------------

Instantaneous range including THz micro-Doppler:

.. math::

   R(t) = \underbrace{R_0}_{\text{tgt.range}}
        + \underbrace{v(t_{\text{slow}}+t)}_{\text{tgt.velocity}}
        + \underbrace{A\sin(2\pi f_v(t_{\text{slow}}+t))}_{\text{vib\_amp / vib\_freq}}

Beat frequency:

.. math::

   f_{\text{beat}} = \frac{B}{T_c}\cdot\frac{2R(t)}{c} + \frac{2f_0 v}{c}

Complex IF output per sample (Smith Ch. 31):

.. math::

   \text{out}[i] = e^{j2\pi f_{\text{beat}}\cdot t}, \quad t = i/f_s

Why THz makes micro-Doppler visible (Smith Ch. 10)
----------------------------------------------------

.. math::

   \Delta\phi_{\text{vib}} = \frac{4\pi A f_0}{c}

For A = 0.2 mm at 300 GHz: **2.51 rad** — clearly resolved FM sidebands.
The same vibration at 77 GHz gives only 0.64 rad.

Maximum unambiguous range (Smith Ch. 3)
-----------------------------------------

.. math::

   R_{\text{max}} = \frac{c\cdot f_s\cdot T_c}{4B} = 93.75\;\text{m}

.. warning::

   The Phase 1 validation target (50 m) is safely within this limit.
   Targets at R > 93.75 m will alias to a wrong range bin.
