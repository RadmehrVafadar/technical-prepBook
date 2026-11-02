- Confidence: 3/5
- Result: can get with hint
- Workon: Derive and trace search boundary updates directly from the saved statements.

# 981. Time Based Key-Value Store

## Code

[Python working file](0981-time-based-key-value-store-v1.py)

## Session summary

1. Started October 31, 2026 at 7:04:39 PM EDT (America/Toronto).
2. You clarified types, bounds, key independence, and call limits; at your request, the interviewer suggested asking about timestamp order and call counts.
3. You proposed a direct timeline array, identified its cost, and developed a linked list of stored values with constant-time insertion and a linear worst-case lookup.
4. The interviewer asked about repeated early lookups and access to the middle of linked nodes; you proposed a sorted list and binary search.
5. An interviewer-supplied search example exposed the last-midpoint issue and a second example ruled out subtracting one; prompted to track a candidate, you developed the eligible timestamp and boundary rules.
6. You explained logarithmic lookup, then after prompts identified the number of stored entries as the relevant input size and constant-time insertion under the ordering guarantee.
7. At your request, the interviewer suggested storing timestamps and values together in list entries; you implemented that representation.
8. You dry-ran examples, independently noticed a missing midpoint operator, and corrected the right boundary after the interviewer asked for pointer values on an earlier timestamp.
9. You requested feedback after describing the example results and declining the need for additional execution.

## Feedback

**Advance this person to the next round?** Yes, for this mock. You developed a sound approach and implemented its central logic, with prompts needed for boundary reasoning and representation.

**Technical: 3 out of 4.** Your saved search and insertion logic express the intended behavior and you explained operation costs; an indentation error in your dry-run notes prevents the saved file from running as written.

**Problem solving: 3 out of 4.** You developed a sparse baseline and proposed binary search, then derived candidate and boundary rules after interviewer-supplied examples and prompts.

**Communication: 3 out of 4.** You clarified constraints and explained your reasoning and corrections, though pointer and timestamp descriptions sometimes needed clarification.

**Things you did well:** You recognized the cost of a dense timeline, used timestamp ordering, and corrected the midpoint and boundary issues during your walkthrough.

**Areas of improvement:** State the search invariant and trace the written pointer updates; distinguish the number of stored entries from the timestamp range.

**My advice:** Before coding a boundary search, state what makes a candidate valid and what remains in the search interval.
