- Confidence: 4/5
- Result: can get with hint
- Workon: Define what each table entry represents and use that definition to check the return and each dry-run update.

# 120. Triangle

## Code

[Python working file](0120-triangle-v1.py)

## Session summary

1. Started November 16, 2026 at 05:24:26 PM EST (America/Toronto).
2. You clarified the dimensions, value bounds, target complexity, and whether you could modify the input.
3. You developed a bottom-up approach that copies the bottom row, propagates candidate sums to valid parents, and keeps the smallest sum for each parent.
   A question about zero-based indexing prompted you to correct the final row index.
   The interviewer pointed out that edge cells can have only one valid parent, and you implemented bounds using the destination row.
4. A prompt contrasting the two tables led you to return the computed sum at the top.
5. You traced the negative singleton and the larger example, and the interviewer supplied a trace and corrected an intermediate sum.
   You fixed the remaining syntax issue and reported running both examples.

## Feedback

1. **Advance this person to the next round?** Yes.
   You independently developed the core recurrence and finished a working baseline after focused prompts.
2. **Technical: 3 out of 4.** The final code handles triangle boundaries and the singleton, and the full table gives quadratic time and extra space in the row count.
3. **Problem solving: 3 out of 4.** You derived the upward propagation independently and corrected the return after a prompt.
4. **Communication: 3 out of 4.** You explained the moves and bounds, with some confusion between input values and accumulated sums during the trace.
5. **Things you did well.** You set the column bound from the destination row and checked a negative single-cell example.
6. **Areas of improvement.** Keep the original cell value and the running path sum distinct during the walkthrough.
7. **My advice.** State what one stored sum means before coding, then use that definition to check the return.
