.. _phase2_cfar:

CA-CFAR Detection
==================

``cfar_detect()`` in ``cfar.cpp`` implements Cell-Averaging CFAR.

.. code-block:: cpp
   :caption: src/cfar.cpp (threshold computation)

   float noise = 0.0f; int count = 0;
   for (int k = cell - guard_cells - train_cells;
            k <= cell + guard_cells + train_cells; ++k) {
       if (k < 0 || k >= N) continue;
       if (std::abs(k - cell) <= guard_cells) continue;
       noise += rd_map[row][k]; ++count;
   }
   const float threshold = alpha * (noise / count);
   return rd_map[row][cell] > threshold;

Threshold derivation (Smith Ch. 26)
-------------------------------------

.. math::

   \alpha = N_{\text{train}} \cdot \left( P_{FA}^{-1/N_{\text{train}}} - 1 \right)

For P_FA = 10⁻⁶, N_train = 16:  α ≈ 41.6 → threshold ≈ 16.4 dB above noise.

.. tip::

   The Wiener filter (Smith Ch. 17, Eq. 17-1) is the theoretical upper bound
   for CFAR detection: H[f] = S[f]² / (S[f]² + N[f]²). CA-CFAR approximates
   the denominator N[f] from training cell averages.
