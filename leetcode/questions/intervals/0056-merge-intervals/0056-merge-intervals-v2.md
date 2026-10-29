- Confidence: 3/5
- Result: can get with hint
- Workon: Trace both overlap and separation branches and explain why sorted order makes the last result sufficient.

# 56. Merge Intervals

## Code

[Python working file](0056-merge-intervals-v2.py)

## Session summary

1. Attempt started October 29, 2026 at 5:58:49 PM EDT (America/Toronto).
2. Clarified ordering, endpoint validity and bounds, input size, mutation, duplicate starts, inclusive overlap, and containment.
3. Proposed sorting by start and scanning, using the larger end for overlaps after an interviewer question about containment.
4. Confirmed equal endpoints overlap after an interviewer prompt distinguishing overlap from maximum selection.
5. Derived O(n log n) time after independently including sorting and O(n) result space.
6. Implemented the scan and dry-ran an overlapping pair; an interviewer request for a separate-interval case prompted adding the missing branch.
7. Corrected comparison syntax after a review prompt and identified the instance parameter after an interviewer question; the saved method remains callable directly on the class.
8. Attributed comparison with only the last result to sorting, without explaining why earlier results cannot overlap.

## Feedback

**Advance this person to the next round?** No for this mock: the approach is viable, but the separation branch required a prompt and the correctness justification was incomplete.

**Technical: 3 out of 4.** Your saved scan handles overlap and separation on inspection, and you accounted for sorting and result space, but the separation branch needed a prompt.

**Problem solving: 2 out of 4.** You proposed sorting and scanning, but needed prompts for containment and separation and did not justify why earlier results cannot overlap.

**Communication: 3 out of 4.** You clarified relevant constraints and traced the overlapping case clearly, though the final correctness argument stopped at sorted order.

**Things you did well:** You clarified inclusive endpoints and input bounds, tracked containment using the maximum end, and independently included sorting in the runtime.

**Areas of improvement:** Test both branches and explain the invariant connecting sorted starts to completed result intervals.

**My advice:** Before coding, state why a separated interval cannot overlap any earlier result and trace both branches against that rule.
