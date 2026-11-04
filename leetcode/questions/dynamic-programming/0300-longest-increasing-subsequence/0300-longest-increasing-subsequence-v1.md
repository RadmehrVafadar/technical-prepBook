- Confidence: 3/5
- Result: need review (assisted; retry later)
- Workon: Test greedy decisions and binary search equality boundaries independently.

# 300. Longest Increasing Subsequence

## Code

[Python working file](0300-longest-increasing-subsequence-v1.py)

## Session summary

1. Started November 3, 2026 at 17:10 EST (America/Toronto).
2. Interviewer began to give a solution; user stopped the explanation and reported not hearing it.
3. Clarified subsequences, equality, input bounds, mutation, and complexity requirements; interviewer illustrated a supplied example on request.
4. Proposed scanning greedily from each starting position and dry-ran the original example.
5. After an interviewer prompt and counterexample, dry-ran that case and identified that choosing the first larger value can miss a longer subsequence.
6. Developed the smallest-ending-value approach and independently proposed binary search on the sorted working list.
7. After prompts about equality, refined the scan boundary; implemented a linear scan, then binary search.
8. Interviewer prompted checks of the replacement target and append name; user corrected both.
9. After prompts about equality in binary search and a duplicate beyond the first position, user dry-ran duplicates and corrected the comparison.
10. Added a direct class call and discussed its validity; no execution result was reported.

## Feedback

1. **Advance this person to the next round? Yes.** The completed approach and recovery from counterexamples show intern-level potential, though boundary checks needed guidance.
2. **Technical: 3 out of 4.** The saved binary-search implementation maintains the intended lengths with O(n log n) time and O(n) space, after prompted corrections to list names and equality handling.
3. **Problem solving: 3 out of 4.** You developed the smallest-ending-value idea and binary-search optimization, while interviewer-supplied cases and questions exposed gaps in the initial greedy rule and duplicate handling.
4. **Communication: 3 out of 4.** You explained the invariant, complexity, and dry runs, though more precise names and conditions would make your reasoning easier to follow.
5. **Things you did well:** You asked about input bounds and equality, revised your approach after a counterexample, and identified the sorted working list as an opportunity for binary search.
6. **Areas of improvement:** Challenge greedy choices with counterexamples and test equality and update targets before treating an implementation as complete.
7. **My advice:** For each binary search, state the exact boundary you seek and dry-run an equal value before coding.
