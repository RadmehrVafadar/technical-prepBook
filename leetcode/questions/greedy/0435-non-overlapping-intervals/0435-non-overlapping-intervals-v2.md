- Confidence: 2/5
- Result: incorrect
- Workon: Trace every branch that discards an interval and check that each changes the returned count.

# 435. Non-overlapping Intervals

## Code

[Python working file](0435-non-overlapping-intervals-v2.py)

## Session summary

1. Started November 26, 2026 at 5:57:27 p.m. EST (America/Toronto).

2. You clarified input shape, both input bounds, ordering, duplicates, overlap, and the removal-only contract.
3. You proposed enumerating subsets and tracking the minimum removals.
   After a question about checking overlaps in unsorted subsets, you accounted for sorting at each leaf and identified subset enumeration as the bottleneck.
4. You proposed removing the interval with the most overlaps.
   The interviewer supplied a five-interval chain and pointed out that removing the middle first needs three removals, while removing the second and fourth needs two.
5. With the interviewer's prompt to consider which interval leaves room for later intervals, you explored choosing by length and supplied a duplicate-containing example.
   The interviewer flagged the remaining duplicate overlap, clarified a misleading acknowledgment about length, and identified the end time as the relevant comparison.
6. You proposed sorting by start, checking for overlap against the retained interval, and discarding the interval with the later end on a conflict.

7. You explained that sorting dominates the runtime and implemented a list of retained intervals with a removal counter.
   The interviewer clarified Python's default list ordering and the distinction between in-place sorting and making a sorted copy.
8. The interviewer asked you to trace two identical intervals through the saved code.
   Your trace initially counted a pop despite the strict comparison, and you considered including equality after the interviewer pointed to the condition.
   You asked to wrap up before submitting a correction.

## Feedback

- **Advance this person to the next round? No.** You reached a viable selection rule with guidance, but the submission undercounted removals and the defect remained at wrap-up.
- **Technical: 2 out of 4.** The saved implementation handles the replacement branch but omits the count when it skips an interval, and its method name differs from the required interface.
- **Problem solving: 2 out of 4.** You identified the exponential bottleneck and formulated a workable scan after guidance on which endpoint to compare.
- **Communication: 3 out of 4.** You clarified both input scales and explained your choices, but your duplicate trace followed the intended result instead of the written condition.
- **Things you did well:** You asked about the input bounds and used your own example to challenge the length heuristic.
- **Areas of improvement:** Count a removal whenever two intervals conflict, then use the end comparison to decide which interval stays.
- **My advice:** Dry-run both conflict branches against the saved code and say when the counter changes.

## Post-interview feedback

After receiving feedback, you proposed counting once per overlap and asked to apply that correction.
The corrected loop counts both discarding the current interval and replacing the retained interval.
The assisted correction resolves the counting defect, and the original mock assessment reflects the submission at wrap-up.
The method still needs the required platform name, and the scan only needs the last retained end and a count.
