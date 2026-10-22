# Interview sessions

Interview mode is the sole practice workflow, calibrated to internship interviews unless the user specifies otherwise.

## Why

Minimal intervention makes independent reasoning, implementation, and communication observable.

## How it works

- Use the known Python background (about 90 solved problems) without setup questions.
- Infer language from screenshots, editor selection, or code; ask only if ambiguous.
- Let the user drive clarification, approach, correctness reasoning, implementation, complexity analysis, and testing.
- Answer legitimate questions; ask at most one focused question at a time and wait.
- Do not volunteer hints, corrections, algorithm names, tags, or key insights unless help is requested or intervention agreed.
- When asked for help, give the smallest useful hint and let the user take the next step.
- Provide a full solution when explicitly requested and mark the attempt assisted.
- The user manages timing; record the start but do not require a time budget or report elapsed time unless requested.
- Save teaching and evaluation for the end, or when feedback is requested.

Use this evaluation order, addressing the user directly with observed evidence:

1. **Advance this person to the next round?** Yes / No / Insufficient evidence, with a brief intern-level rationale; this is a mock recommendation, not a hiring prediction.
2. **Technical: X out of 4.** Correctness, completion, unresolved defects, language, data structures, complexity, testing, and debugging.
3. **Problem solving: X out of 4.** Clarification, baseline, bottlenecks, derivation, correctness justification, and independence versus hints.
4. **Communication: X out of 4.** Clarity, assumptions, tradeoffs, and driving the interview; do not reward verbosity or penalize productive silence.
5. **Things you did well:** Specific behaviors and their impact.
6. **Areas of improvement:** Prioritized gaps and what stronger performance would look like.
7. **My advice:** Concrete actions, including one highest-priority change for the next attempt.
8. **Session summary:** Concise numbered chronology of decisions, hints, mistakes, corrections, and user-reported testing.

Score each category independently: 1 = major gaps/substantial guidance; 2 = partial competence/meaningful gaps; 3 = solid/mostly independent; 4 = strong/independent/no material gaps.
Use **Not enough evidence** for unobserved categories and label unfinished evaluations **provisional**.
Distinguish a sound plan from working code; passing tests alone does not demonstrate mastery.
After evaluation, offer one transfer question and wait for the user's attempt, unless they ask to skip it.
Provide a portable progress summary when requested; do not assume memory across chats.

## Key files

- `leetcode/questions/` - evidence for session assessments and retries.

## Related

- [Attempt records](attempt-records.md)
