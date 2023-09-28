
> *"In the land of lost Carcosa, under the Hydra's gaze, these dice rumble with the might of altered realities. Beware, mortal, for the thrill of fortune comes at a cost..."*

**Effect:**

When you use this artifact, you may choose to roll any number of dice when you would normally roll one, taking the highest result as your outcome.

However, each additional die you roll inflicts sanity damage on you. The amount of sanity damage is equal to the difference between the average result of rolling one die, and the average result of rolling the number of dice you choose to roll.

**Sanity Damage Calculation:**
- If you choose to roll `m` dice, each with `n` faces, the sanity damage you take is 
- `⌈0 - n/2 + (m * n)/(1 + m)⌉`

Rolling 'm' dice with advantage can be analogously represented in a mathematical space with 'm'+1 dimensions, where each dimension corresponds to the outcome of one die and the additional dimension signifies the probability or frequency of each outcome. Every additional roll is performing an integration over this multi-dimensional outcome space, with the domain of integration expanding as 'm' increases. This models the amplified potential for higher results, analogous to an accumulating integral over a larger region. The formula serves as an estimate for this multidimensional integration in the context of 'm' 'n'-sided dice, which has diminishing returns as 'm' approaches infinity due to the fractional term m/(m+1).

| # of dice | d4 | d6 | d8 | d10 | d12 | d20 |
|---|---|---|---|---|---|---|
| 1  |  0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| 2  |  1.00 | 1.00 | 2.00 | 2.00 | 2.00 | 4.00 |
| 3  |  1.00 | 2.00 | 2.00 | 3.00 | 3.00 | 5.00 |
| 4  |  2.00 | 2.00 | 3.00 | 3.00 | 4.00 | 6.00 |
| 5  |  2.00 | 2.00 | 3.00 | 4.00 | 4.00 | 7.00 |
| 6  |  2.00 | 3.00 | 3.00 | 4.00 | 5.00 | 8.00 |
| 7  |  2.00 | 3.00 | 3.00 | 4.00 | 5.00 | 8.00 |
| 8  |  2.00 | 3.00 | 4.00 | 4.00 | 5.00 | 8.00 |
| 9  |  2.00 | 3.00 | 4.00 | 4.00 | 5.00 | 8.00 |
| 10  |  2.00 | 3.00 | 4.00 | 5.00 | 5.00 | 9.00 |

