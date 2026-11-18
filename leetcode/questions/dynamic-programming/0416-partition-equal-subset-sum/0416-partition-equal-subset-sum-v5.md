- Confidence: 2/5
- Result: not finished
- Workon: Trace the first state update and the Boolean return through the written method before calling it complete.

# 416. Partition Equal Subset Sum

## Code

[Python working file](0416-partition-equal-subset-sum-v5.py)

## Session summary

1. Started November 18, 2026 at 6:07:53 PM EST (America/Toronto).
2. You clarified the input bounds, duplicates, ordering, mutation, and input validity, then independently reduced the task to finding a subset with half the total sum after rejecting odd totals.
3. You proposed an include-or-skip search and identified its exponential complexity.
   When prompted to apply the maximum list length, you computed the worst-case scale and corrected your initial assessment that it would be practical.
4. You implemented the recursive baseline and, after a focused question, clarified that exceeding the target must return `False` because the remaining values are positive.
5. On request, you chose `[2, 2]` and traced the include branch reaching the target and returning `True` in the intended control flow.
   The interviewer then asked you to check how the arguments at the initial call bind to the saved helper's parameters.
6. You declined another dry run because of time and moved to optimization with the saved baseline's call unresolved.
   The interviewer corrected an earlier misreading of the call, and you explained why the existing guard lets the last element participate before stopping past it.
7. After a question about nonadjacent selections, you set aside prefix sums and proposed retaining a set of reachable totals, checking for the target as new totals are added.
   With follow-up questions about reusing an element, you described taking a snapshot before each update and traced the first three elements of the opening example.
8. You initially counted the list scan and the sum updates additively, then corrected the time bound after an interviewer example illustrated repeated scans.
   You accepted that the distinct reachable totals also bound the set and its copy without a separate term for the original list length.
9. While coding the set approach, you recognized that adding the current element before reading the old state could let you reuse it.
   You saved a second method and asked to wrap up.

## Feedback

- **Advance this person to the next round? No.** You found a viable optimization, but neither saved method delivered a callable Boolean result at the end of the mock.
- **Technical: 1 out of 4.** The recursive draft has an indentation error and a helper argument mismatch, and the set draft leaves the initial set empty because the only insertions are inside its loop and the method has no Boolean return.
- **Problem solving: 3 out of 4.** You independently reduced the task to a half-sum search and proposed tracking reachable totals, then needed prompting to pin down the snapshot and account for repeated scans.
- **Communication: 3 out of 4.** You clarified both input scales, explained the last-index guard, and traced a success path, though the trace followed your intended flow and missed the saved call mismatch.
- **Things you did well:** You used positivity to justify stopping an overshooting branch and spotted the risk of counting the same element twice while drafting the set method.
- **Areas of improvement:** Keep the snapshot and destination separate in the update and wire the target decision through to the public method's return.
  The saved set draft places an insertion into the iterated set, so a nonempty iteration could also mutate that set.
- **My advice:** Trace the first state update and the Boolean return through the written method before calling it complete.
