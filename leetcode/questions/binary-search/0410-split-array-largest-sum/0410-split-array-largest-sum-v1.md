- Confidence: 1/5
- Result: not finished
- Workon: Describe how to enumerate all legal cut placements before implementing the baseline.

# 410. Split Array Largest Sum

## Code

[Python working file](0410-split-array-largest-sum-v1.py)

## Session summary

1. Started November 28, 2026 at 12:43:55 PM EST (America/Toronto).
2. You clarified the order, size and value bounds, duplicates, and whether the array could be modified.
   The interviewer prompted you to ask about the range of k, and you independently identified the result when every part contains one element.
3. You proposed using the average part sum as a threshold and traced a case where the rule gave the expected result.
   The interviewer supplied [4, 4, 1, 1] with k = 2 and showed that cutting after the first element gives a largest sum of 6, below the rule's result of 8.
4. You suggested prefix sums and, after a focused question, obtained the right part sum by subtracting the left part sum from the total.
   The interviewer prompted you to fix the first cut and consider positions for the second, and the general baseline remained unfinished.
5. You stopped before implementing and requested the problem link for independent review and a spaced retry.
   The earliest eligible retry is November 29, 2026 at 1:10:03 PM EST (America/Toronto), and at least 24 hours after any later solution review.

## Feedback
