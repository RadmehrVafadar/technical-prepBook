- Confidence: 3/5
- Result: can get with hint
- Workon: Translate the traversal into executable code and verify state updates.

# 994. Rotting Oranges

## Code

[Python working file](0994-rotting-oranges-v2.py)

## Session summary

1. Started October 31, 2026 at 11:06:37 AM EDT (America/Toronto).
2. You clarified dimensions, bounds, adjacency, values, mutation, counts, and the all-empty case.
3. You proposed collecting initial rotten cells, processing queue batches, marking cells, scanning for fresh cells, and explained time and space bounds.
4. The interviewer suggested direction offsets; you developed the offset pairs and neighbor checks.
5. In a successful dry run, you identified an extra minute; prompted with the empty-grid case, you rejected unconditional subtraction.
6. After an interviewer hint to examine the queue after a batch, you revised the minute increment.
7. You walked through an unreachable-fresh case and requested feedback.
8. The interviewer incorrectly claimed the increment was not assigned and then corrected that feedback.
9. You asked to disregard minor syntax errors in the evaluation; the assessment was revised to reflect your clearly stated intent.

## Feedback

**Advance this person to the next round?** Yes. Your traversal, bounds, and dry runs show solid intern-level reasoning, with a limited hint for minute counting.

**Technical: 3 out of 4.** You described marking cells on enqueue, reasoned about batch timing and linear grid bounds, and walked through successful and unreachable cases.

**Problem solving: 3 out of 4.** You independently described the simultaneous traversal and found the extra minute in a dry run; the final timing condition followed an interviewer hint.

**Communication: 3 out of 4.** You explained your queue batches, clarified constraints, and walked through cases, though the minute invariant needed a more precise statement.

**Things you did well:** You identified the simultaneous sources and reasoned about the final unreachable-cell check.

**Areas of improvement:** State precisely what each queue batch represents and check that written statements match the intended state updates.

**My advice:** State the queue invariant and explain when the minute counter changes.
