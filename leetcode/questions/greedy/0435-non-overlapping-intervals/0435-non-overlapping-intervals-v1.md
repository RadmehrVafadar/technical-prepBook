- Confidence: 3/5
- Result: need review
- Workon: Justify the interval choice by explaining why it preserves options for all later intervals.

# 435. Non-overlapping Intervals

## Code

[Python working file](0435-non-overlapping-intervals-v1.py)

## Session summary

1. Started November 7, 2026 at 11:03:15 AM EST (America/Toronto).
2. Clarified input size, endpoint bounds, overlap possibilities, ordering, modification, and performance requirements.
   The interviewer suggested asking about touching endpoints.
3. Proposed a keep-or-remove search and recognized its poor scaling.
   The interviewer suggested ordering the intervals, then prompted comparison of overlapping intervals by their endpoints.
4. Chose to retain the interval with the earlier end, described a sorted scan, and corrected the time complexity to include sorting after a prompt.
5. Wrote the scan and traced both supplied examples and a self-selected equal-end case.
   After an interviewer prompt about the method definition, corrected a parameter spelling.
6. Explained the earlier-ending choice as reducing future overlap.
   The user specified that instance binding was outside the exercise.

## Feedback

**Advance this person to the next round?** No for this mock, because the central interval choice needed substantial guidance and its justification remained informal.

**Technical: 3 out of 4.** Your scan handles the observed overlap cases and returns the removal count, and you corrected the sorting cost after a prompt; the saved file has an indentation issue around the dry-run notes.

**Problem solving: 2 out of 4.** You identified the exponential baseline and implemented the guided choice, but needed hints for ordering and which interval to retain.

**Communication: 3 out of 4.** You clarified the contract and traced the written state clearly, while the correctness rationale would benefit from a more exact explanation.

**Things you did well:** You identified the input scale as a problem for exhaustive search and traced both overlap and non-overlap branches.

**Areas of improvement:** Explain why an earlier end preserves every future option available after a later end, and account for sorting when stating complexity.

**My advice:** Practice justifying a local choice by comparing the future options it leaves with those of the alternative.
