- Confidence: 2/5
- Result: need review
- Workon: Write precise recursive state and branch transitions, then distinguish recursion depth from total calls when deriving bounds.

# 39. Combination Sum

## Code

[Python working file](0039-combination-sum-v2.py)

## Session summary

1. Attempt started October 24, 2026 at 5:52:33 PM EDT (America/Toronto).
2. You independently clarified that sorting is not guaranteed, mutation is allowed, candidates are distinct, reuse is allowed, and the target can be unreachable.
   The interviewer prematurely volunteered the empty-result behavior; you objected and later separately asked what to return, so that return behavior was not a fresh independent discovery.
3. You independently asked about target positivity and its maximum of 40, candidate count up to 30, and later the exclusion of zero and negatives and the full candidate range of 2 through 40.
   You connected the small bounds with willingness to enumerate possibilities.
4. You explored brute force and a recursive two-choice tree, initially changing the branch definitions and allowing an empty-list path that did not progress.
   Focused interviewer questions exposed the nonprogress; the interviewer highlighted your earlier index rules and requested implementation.
5. You implemented skip with an advancing index and take with an unchanged index, overshoot and index guards, and an equality case that records a result.
6. The interviewer asked what `append` returns; you believed it returned the list, and the interviewer corrected this to `None`.
   You then independently changed to append before the recursive call and pop afterward.
7. When prompted about storing a reference to the working list, you identified shared-list mutation and chose to store a copy.
   You explained that nondecreasing index progression prevents reordered duplicates and allows reuse until advancing past a candidate.
8. You initially proposed quadratic time, then self-corrected to `2^n` with `n` as candidate count.
   Substantial repeated interviewer guidance distinguished a skip/take path from the whole tree, target dependence, and active stack from total calls.
   You did not independently establish complete time or auxiliary-space bounds; your final stack answer used only the target before the interviewer supplied the index contribution.
9. You proposed an unreachable target and ordinary and boundary cases.
   No concrete execution results were reported by you; interviewer-supplied cases are not credited as your testing evidence.
10. You ended the session by requesting assessment and explicitly requested syntax, class, and function review.

## Feedback

1. **Advance this person to the next round? No.** Your observed internship-level performance showed useful input discovery and an emerging branch structure, but the recursive model and complexity reasoning required substantial guidance.
   This is a mock recommendation, not a hiring prediction.
2. **Technical: 2 out of 4.** Your latest saved code expresses the intended skip/take structure, result copying, and append/call/pop behavior.
   The requested interface review found hardcoded class attributes rather than a callable public method accepting candidates and target, `dfs` without `self`, bare `myList`, `target`, and `res` names that do not resolve through the class's lexical scope, bare recursive `dfs` calls, and an invalid class-body `return`.
   These are repairable packaging, scope, and interface issues and receive limited weight compared with the unresolved complexity reasoning and guidance required.
   Your testing discussion supplied candidate cases, without concrete user-reported execution outcomes.
3. **Problem solving: 2 out of 4.** You independently discovered relevant input properties and used small bounds to consider enumeration.
   Branch semantics and progress were initially inconsistent, and the final structure, mutable-list handling, and complexity discussion involved meaningful interviewer assistance.
   Complete time and auxiliary-space bounds were not independently established.
4. **Communication: 2 out of 4.** You asked relevant clarifications and explained positivity and index-based uniqueness, but repeatedly changing branch definitions made the state transitions difficult to follow.
   The improvement is precision about state and transitions, not greater verbosity or less productive silence.
5. **Things you did well:** You connected input discovery to feasibility, developed the intended branch skeleton, explained aliasing after a focused prompt, and articulated why index progression avoids reordered duplicates.
6. **Areas of improvement:** Define each recursive state and branch consistently, show why every path progresses, and separate tree height, total calls, and active stack when discussing complexity.
   Complete the callable interface and Python scope structure during your final code review.
7. **My advice:** Before tracing, write the state, both transitions, and stopping conditions precisely.
   Separately practice distinguishing tree height from node count and active stack.
8. **Session summary:** See the numbered chronology above for independent decisions, interviewer assistance, corrections, and your testing discussion.
