- Confidence: 3/5
- Result: need review
- Workon: Independently audit stopping conditions and derive complexity from all changing state variables.

# 39. Combination Sum

## Code

[Python working file](0039-combination-sum-v3.py)

## Session summary

1. Attempt started October 26, 2026 at 2:50 PM EDT.
2. You agreed to retry after questioning the repeated problem selection.
3. You independently clarified sorting, candidate and target bounds, unreachable targets and their output, mutation, uniqueness, reuse, distinct candidates, and candidate count.
4. You proposed recursion and independently explained that positive candidates make overshoot terminal.
5. Your initial advancing branch also added the next candidate.
   An interviewer-requested trace of the existing single-seven example prompted you to revise it to advance without adding; branch labels briefly switched during the explanation.
6. You independently chose recursive index, temporary list, and sum state, copied successful combinations to avoid shared-reference mutation, and restored the temporary list after the take branch.
7. You narrated part of the example traversal and explained that nondecreasing indices prevent reordered duplicates.
   You declined a complete manual traversal because of its length.
8. Saved-code review prompted an index-exhaustion guard and a return after recording success; you supplied both corrections after focused questions.
9. You independently created a class, named method, parameters, helper initialization, and result return.
   Interviewer guidance corrected indentation and a script-level return to print; repeated explanations and stale-read communication caused avoidable confusion.
10. Your initial bounds used only the target.
    Interviewer guidance and an interviewer-supplied target-one, thirty-candidate example exposed stack growth from skips.
    You then stated auxiliary space O(T + N), a loose recursive-call bound O(2^(T + N)), and included copying to state time O(T * 2^(T + N)).
    These revised bounds were assisted; auxiliary space excludes returned combinations.
11. You selected candidates [2] with target 7 and correctly expected no combinations.
    For candidates [2, 4, 8] and target 8, you initially listed uniform combinations and added [2, 2, 4] after an interviewer prompt about mixed values.
    You reported adding the mixed case to your expectations.

## Feedback

1. **Advance this person to the next round? Yes, narrowly.** The final implementation is coherent and you independently handled copying, restoration, positivity, and uniqueness, with meaningful help on stopping conditions and complexity.
   This is an internship-level mock recommendation, not a hiring prediction.
2. **Technical: 3 out of 4.** The final saved implementation supports reuse, skips, pruning, copied results, and restoration, while boundary checks and successful termination required prompts.
3. **Problem solving: 2 out of 4.** You derived the main recursive approach independently, but branch precision, complete state-based complexity, and exhaustive expected output needed guidance.
4. **Communication: 3 out of 4.** You drove relevant clarifications and explained positivity and uniqueness, although switching branch labels made transitions harder to follow.
5. **Things you did well:** Independently recognized list aliasing, restored shared state, and justified why forward-only indices avoid reordered duplicates.
6. **Areas of improvement:** Audit every stopping condition, distinguish stack depth from returned-output size, and include all independent state variables in complexity reasoning.
   Mechanical Python issues receive little weight; interviewer read-status confusion is not counted against you.
7. **My advice:** Before tracing, state each helper variable, both exact transitions, and every stopping condition.
8. **Session summary:** See the numbered chronology above.
