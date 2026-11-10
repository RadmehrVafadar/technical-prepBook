- Confidence: 3/5
- Result: can get with hint
- Workon: Justify the selection order and relate runtime to each input scale.

# Maximum value from unit-weight items

## Code

[Python working file](maximum-value-unit-weight-items-v1.py)

## Session summary

1. Started November 09, 2026 at 06:04:47 PM EST (America/Toronto).
2. Requested a recent Google intern interview question, and received a question from an October candidate report.
3. Clarified input types, bounds, sorting, mutation, zero capacity, and duplicate values and counts.
4. Proposed choosing the highest-value available items and traced the provided example.
5. After a scale question about processing individual copies, independently proposed processing a type's copies together.
6. Implemented a heap-based approach and, after asking how to inspect its root, received the index.
7. Traced the provided example and independently corrected the sign of the returned sum.
8. After a prompt, corrected the heap variable name in the insertion call.
9. Discussed zero capacity and an empty heap, and requested evaluation.

## Feedback

**Advance this person to the next round?** Yes for this mock: you completed a sound approach and traced it, deriving batch processing after a scale prompt.

**Technical: 3 out of 4.** You completed the algorithm, traced the example, and stated appropriate time and space complexity; the missing import and insertion function name are minor slips.

**Problem solving: 3 out of 4.** You selected higher-value items, then derived batch processing after a question about per-copy iteration at the input limits.

**Communication: 3 out of 4.** You clarified input bounds and explained the example and state changes, correcting the sign during your trace.

**Things you did well:** You recognized the importance of input scale and derived a batch operation, and your trace caught the negative return value.

**Areas of improvement:** Justify why selecting higher-value copies first maximizes the total, and identify the cost of per-copy processing across the input bounds.

**My advice:** Connect each loop to the input quantities it can iterate over when assessing runtime.
