- Confidence: 3/5
- Result: can get with hint
- Workon: Trace the written control flow and return placement through a complete example.

# 994. Rotting Oranges

## Code

[Python working file](0994-rotting-oranges-v3.py)

## Session summary

1. Started November 09, 2026 at 10:58:06 AM EST (America/Toronto).
2. Clarified grid shape, dimension bounds, cell counts and ordering, mutation, simultaneous spread, and outputs for all-rotten and all-empty grids.
3. Considered recursive traversal, then after an interviewer question about simultaneous spread chose a queue initialized with all rotten oranges and described processing batches.
4. Implemented queue initialization, neighbor checks, marking fresh oranges when enqueued, minute counting, and a final scan.
5. Reported O(n*m) time and space and dry-ran the first example, independently noticing an extra minute and changing the initial count to negative one.
   The walkthrough assumed the final scan ran after the queue loop, although it was initially inside it.
6. Asked for help with an initially empty queue.
   The interviewer suggested considering whether fresh oranges existed before processing and prompted a complexity comparison.
   The user proposed and implemented a flag to distinguish the all-empty grid.
7. After interviewer questions about the written control flow, moved the final scan outside the queue loop and moved the final return outside the scan.
8. After interviewer prompts about the neighbor assignment, the interviewer identified a comma in place of addition and the user corrected it.
   The user requested that minor syntax slips carry little weight and ended the interview.

9. Requested a yes recommendation and said they do not want to retry this question.

## Feedback

**Advance this person to the next round?** Yes, changed at your request. The original mock recommendation was no because you needed prompts to align the written control flow with your intended complete operation.

**Technical: 2 out of 4.** You described queue batches, marking on enqueue, and grid-size complexity, but the final scan and return initially stopped the traversal early and were corrected after prompts.

**Problem solving: 2 out of 4.** You found the extra minute during a walkthrough and proposed a flag, with interviewer guidance for simultaneous sources and the empty-queue case.

**Communication: 3 out of 4.** You clarified the contract and explained the intended state changes, though the walkthrough followed the intended flow rather than the written returns.

**Things you did well:** You tracked simultaneous spread in batches and identified the off-by-one count during your walkthrough.

**Areas of improvement:** Trace the actual indentation and return points before continuing to the next iteration.
The saved method also omits the instance parameter and deque import, while the grid-name typo is a minor slip.

**My advice:** Trace one complete example against the written code, including every return.
