.. _stage4:

Stage 4 — Noise, SNR & CA-CFAR Detection
==========================================

*Smith Ch. 2, 7, 9, 17, 26 · Engine:* ``cfar_detect()``

THz noise taxonomy (Smith Ch. 2; Ch. 9, Fig. 9-2)
---------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Noise type
     - FMCW relevance
   * - Thermal (white)
     - Flat PSD. Gaussian model (CLT, Ch. 2). Absent in Phase 1–2 simulation; present in Phase 3 hardware. The 61.1 dB coherent gain is the headroom budget.
   * - 1/f (flicker)
     - VCO phase noise. Worse at 300 GHz than at 77 GHz due to higher multiplication chain. Manifests as spectral broadening of range peaks.
   * - Atmospheric absorption
     - THz-specific: ~5 dB/km at 300 GHz in humid air. Negligible at ADAS ranges (50–100 m: < 0.5 dB).
   * - Quantization
     - σ_q = LSB/√12 (Ch. 3). Engine uses float64 — absent in simulation.

Matched filter sensitivity (Smith Ch. 17)
------------------------------------------

.. math::

   \text{SNR}_{\text{peak}} = \frac{2E}{N_0},
   \quad E = \frac{N}{f_s} = \frac{5000}{50\times10^6} = 100\;\mu\text{s}

Peak SNR depends only on signal energy, not waveform shape. The 100 µs THz
chirp achieves the same sensitivity as a 1 µs pulse at 100× peak power.

Wiener filter (Smith Ch. 17, Eq. 17-1)
----------------------------------------

.. math::

   H[f] = \frac{S[f]^2}{S[f]^2 + N[f]^2}

The theoretical CFAR upper bound. CA-CFAR approximates N[f] from training
cell averages.

CA-CFAR — cfar_detect() (Smith Ch. 26)
----------------------------------------

.. code-block:: cpp

   float noise = 0.0f; int count = 0;
   for (int k = cell - guard_cells - train_cells;
            k <= cell + guard_cells + train_cells; ++k) {
       if (std::abs(k - cell) <= guard_cells) continue;
       noise += rd_map[row][k]; ++count;
   }
   return rd_map[row][cell] > alpha * (noise / count);

CFAR threshold:

.. math::

   \alpha = N_{\text{train}}\,\left(P_{FA}^{-1/N_{\text{train}}} - 1\right)

For P_FA = 10⁻⁶, N_train = 16: α ≈ 41.6 → threshold ≈ **16.4 dB** above
local noise floor.

ROC curve (Smith Ch. 26, Fig. 26-2)
--------------------------------------

The Phase 2 test suite implicitly validates P_D = 1.0, P_FA → 0 — achievable
in simulation with zero additive noise. Phase 3 hardware validation will
operate at the design point (P_D ≥ 0.9 at P_FA ≤ 10⁻⁶).
