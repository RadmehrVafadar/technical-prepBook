- Confidence: 2/5
- Result: incorrect
- Workon: Finish and dry-run a valid insert and a query at each endpoint before optimizing.

# Union of Ranges

## Code

[Python working file](union-of-ranges-v1.py)

## Session summary

1. Round one started November 17, 2026 at 2:26:48 PM EST (America/Toronto), using the recording start time.
2. You clarified how often each operation was called, the integer bounds, input ordering and validity, overlap, and the excluded right endpoint.
   The interviewer confirmed that inserts happen one at a time and can be interleaved with queries.
3. You explored merging with a stack.
   The interviewer pointed out that an overlapping interval could be deeper in the stack and prompted you to compare sorting at query time with a linear scan.
4. You implemented append and scan for the insert-heavy workload, then added validation after the interviewer revisited malformed inputs.
   You offered a dry run, and the interviewer deferred it to move on to the follow-up.
5. For a query-heavy workload, you proposed sorted insertion and binary search.
   The interviewer prompted for a nested-interval counterexample, explained why the search could skip a covering interval, and narrowed the implementation to disjoint ranges.
6. You sketched the indexed lookup and revised sorted-list insertion to O(n).
   The interview moved to candidate questions before the lookup correctly checked coverage.

## Feedback

1. **Advance you to the next round? Lean no on this round's evidence.**
   Your baseline design fit the workload, but the saved insert fails on valid input and the simplified follow-up remained incorrect.
2. **Technical: 2 out of 4.**
   Your linear scan uses the correct half-open comparison, but the validator call and type check prevent valid insertion, and a binary-search index alone does not establish membership.
3. **Problem solving: 2 out of 4.**
   You recognized the workload tradeoff and corrected the list insertion cost, while the overlap failure and search invariant needed interviewer guidance.
4. **Communication: 2 out of 4.**
   You surfaced important constraints, but the clarification and design discussion left little time for a successful trace.
5. **Things you did well.**
   You asked about operation frequency and carried the excluded endpoint into the baseline code.
6. **Areas of improvement.**
   Trace the public methods together and state exactly what the chosen search index represents.
7. **My advice.**
   Insert `(2, 5)` and trace queries at `2` and `5` before moving on to the faster lookup.
