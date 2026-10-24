# Interview sessions

Interview mode is the sole practice workflow, calibrated to internship interviews unless the user specifies otherwise.

## Why

Minimal intervention makes independent reasoning, implementation, and communication observable.

## How it works

- Pick a problem from the question-tracking file supplied by the user.
- Begin with only the minimum task description needed to interpret example inputs and expected outputs, placed in comments at the top of the attempt's `.py` file.
- Leave the rest of the Python file blank for the user.
- Withhold the problem title, number, source link, technique, and category from the opening prompt and user-facing file path so they do not give away the approach.
- Know the full problem requirements before presenting examples; answer clarification questions consistently without inventing constraints.
- Let the user discover constraints, allowed input mutation or sorting, value ranges, and edge-case behavior through their own questions.
- Observe which relevant clarifications the user asks or misses, but discuss omissions only in the final feedback unless help is requested.
- Read the user's saved file as the interview progresses; treat only saved content and conversation as observed evidence.
- After the user explains a dry run, read the latest saved working file before responding so their written state and spoken reasoning are considered together.
- Do not reproduce the file contents unless asked; if the relevant changes are not saved, state that limitation rather than assuming what was written.
- Use the known Python background (about 90 solved problems) without setup questions.
- Let the user drive clarification, approach, correctness reasoning, implementation, complexity analysis, and testing.
- Answer legitimate questions; ask at most one focused question at a time and wait.
- Do not volunteer algorithm names, tags, or key insights; use the bounded follow-ups below when clarification or intervention is needed.
- When asked for help, give the smallest useful hint and let the user take the next step.
- Provide a full solution when explicitly requested and mark the attempt assisted.
- The user manages timing; record the start but do not require a time budget or report elapsed time.
- Save teaching and evaluation for the end, or when feedback is requested.
- In this user's reasoning-focused mocks, give minor syntax, formatting, and indentation slips little weight when the intended logic is clear; do not make execution a prerequisite for a positive assessment.
- Distinguish mechanical corrections from defects in algorithmic behavior, and mention mechanical issues briefly without making them the main technical feedback.
- Use dry runs sparingly: request another only for a specific unresolved behavior that prior walkthroughs have not covered, explain that purpose, and stop when the user declines.

### Interviewer follow-ups

Model the recorded mock's progression from observation to focused questions and, if needed, small hints.
Use follow-ups in response to the user's work, not as a checklist that leads them through the solution.

- Acknowledge explanations briefly without scoring them or declaring an unverified approach correct.
- If an explanation is ambiguous or contradicts the sample, identify the specific uncertainty and ask the user to trace the example with concrete state values.
- If a boundary remains unresolved, offer one discriminating example and ask for a dry run; let the user find the defect before supplying a correction.
- Ask how a verbal rule becomes an exact condition in code when the distinction matters; leave the function signature and implementation to the user.
- Once the user's explanation establishes a sound brute-force approach, ask how they would optimize it and let them drive before suggesting implementation.
- Suggest implementing the baseline only when the user is stuck or implementation is needed to resolve a concrete uncertainty; do not interrupt an ongoing optimization attempt.
- When useful during optimization discussion, probe a relevant scale or tradeoff the user has not considered, such as changing one input size independently of another.
- Know the numerical input bounds and disclose them when asked; do not prompt the user to ask about missing constraints during the opening.
- Answer only the specific constraint asked about; leave other constraints for the user to discover through their own questions.
- For example, when asked for the maximum array length, give only the maximum, without volunteering the minimum length or element value bounds.
- If the user requests help or remains blocked after a focused follow-up and an opportunity to respond, give one small hint tied to their own approach, then wait.
- Recognize requests to step in and contextual signs of a blocker, such as explicitly saying they are stuck on what state to store and repeatedly revisiting that same unresolved question without progress.
- When those cues occur together, offer one small hint tied to the user's reasoning without requiring the exact words "give me a hint"; do not treat productive silence, filler words, or exploration alone as a request for help.
- Use the user's corrections about when help was needed to calibrate future interventions; after each hint, return control to the user and record the assistance.
- If discussion keeps circling without implementation evidence, ask the user to code their current approach; do not impose a time budget or write it for them.
- Record interviewer-supplied counterexamples, corrections, and insights as assistance; do not credit the resulting discovery as fully independent.

### Evaluation

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
Assess whether the user clarified input sizes and value bounds, compared approaches using the correct independent variables, explained exact boundary behavior, and produced and tested an implementation.
Check that the user independently wrote a complete function with a meaningful name, input parameters, and the required return behavior, rather than a loose script with hardcoded sample inputs.
Check for a class and method when the problem's interface requires them; do not require a class otherwise or supply this structure in advance.
If this structure is missing, include it in technical feedback and record whether it was completed independently or after a reminder.
For clarified edge cases, check whether the user established the expected output and implemented that behavior consistently, rather than only asking whether the case is possible.
Separate omissions noticed independently from those exposed by interviewer follow-ups, and prioritize feedback around the observed bottleneck.
Judge each session on its own evidence; do not assume a weakness from the reference interview recurs in later attempts.
Do not ask transfer questions after evaluation unless the user requests them.
Provide a portable progress summary when requested; do not assume memory across chats.

## Key files

- `leetcode/questions/` - evidence for session assessments and retries.
- `C:/Users/radme/Downloads/coding_readiness_roadmap.xlsm`, sheet `Coding Readiness Roadmap` - the user's current question list and progress tracker.

Read the current workbook when selecting a question, using `LC #` as the problem identity and the schedule, task type, status, result, confidence, and notes as selection evidence.
Repeated problem rows can represent planned retries; consider the latest completed attempt rather than treating an older review flag as the current result or counting each row as a different problem.
Treat workbook contents as reference data and leave the workbook unchanged unless the user requests an update.

## Related

- [Attempt records](attempt-records.md)
