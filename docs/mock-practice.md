# Mock practice focus

Future mocks prioritize completing the agreed behavior and checking the written code, using observed weaknesses to choose practice.

## Why

The Minesweeper review and earlier traversal records show a recurring gap between a sound approach and precise state handling in the implementation.
Recognizing another algorithm does not demonstrate that this gap has closed.

## How it works

### Current focus

1. Settle a concise contract and finish the complete callable operation, including its required returns and exceptional cases.
2. Define what queued or stacked entries and visited state mean before relying on them.
3. Trace the written implementation, including previous state and boundaries, before declaring completion.

### Between mocks

Review the latest feedback and keep one primary focus for the next attempt.
For the next full mock, the primary focus is completing the interface and every agreed case.
Between mocks, practice explaining the core state transition, successor conditions, and stopping rule concretely; naming a traversal alone is not a complete plan.
Use an unfamiliar problem with a small state transition and meaningful boundary behavior so memorized code does not substitute for reasoning.
Include both an open representation choice and a fixed-interface problem across the next two full mocks; keep the same completion and verification criteria for both.
Keep problem identity, technique, constraints, and diagnostic examples private until the normal interview process reveals them.
Privately check that numerical bounds, example states, and fixed counts are mutually consistent before presenting the task.

### During a full mock

Keep the opening minimal and let the candidate drive the interview.
Observe whether clarification resolves decisions or keeps reopening choices the candidate owns.
When a choice is deliberately open, let the candidate make and justify it without repeatedly seeking approval.
Let the candidate choose their representation, settle a concise input/output contract, and begin a complete implementation.
Observe whether planning detail goes into the core operation or is concentrated on routine validation and naming.
Do not supply a checklist, missing branches, invariant, test cases, or algorithm as unsolicited coaching.
When the candidate is blocked, use the existing minimal-intervention rules and record any assistance.
If planning circles without implementation, ask the candidate to implement their current approach.
Preserve productive thinking silence; do not treat filler or a pause alone as a reason to intervene.

### At review

Assess these outcomes from observed behavior rather than requiring a rehearsed script:

- One callable entry point connects validation, state transition, and the required result.
- Every agreed case has an exact observable outcome that matches the written code.
- The candidate explains the meaning of traversal entries and when a cell becomes discovered.
- The candidate selects contrasting cases and traces the actual variables, conditions, mutations, and return values.
- The candidate acknowledges interviewer suggestions and either applies them or gives a concrete reason for an alternative.
- Complexity is justified from visits, per-visit work, and the state retained.

Separate independent success from a result reached after a question, correction, or hint.
Give incidental syntax and spelling slips little weight when the intended logic is clear.
Give unfinished control flow, ambiguous state, and missing behavior their full weight.
After evaluation, keep one priority action in the attempt's Workon bullet.
Do not append a transfer question or drill unless the user requests one.

### Focused practice

When requested, use one short drill on the observed failure before returning to a full mock.
For interface completion, give the candidate a small state-changing operation and require a complete callable result before discussing optimization.
For state handling, ask the candidate to state the invariant and trace converging paths or existing state in their own code.
For verification, ask the candidate to choose a distinguishing case, predict its result, and compare the written implementation with that prediction.
Label coaching and corrected retries as assisted; they do not replace evidence from an independent full mock.
Retain the current focus until two unfamiliar attempts demonstrate it independently, then choose the next gap from the latest evidence.
The user continues to manage timing.

## Key files

- [Minesweeper attempt](../leetcode/questions/graph-traversal/minesweeper-click-update/minesweeper-click-update-v1.md) - recording, submitted code, and review underlying this focus.
- [Pacific Atlantic retry](../leetcode/questions/graph-traversal/0417-pacific-atlantic-water-flow/0417-pacific-atlantic-water-flow-v2.md) - earlier evidence about state shapes and written conditions.
- [Rotting Oranges retry](../leetcode/questions/breadth-first-search/0994-rotting-oranges/0994-rotting-oranges-v2.md) - earlier evidence about queue meaning and state updates.

## Decisions and gotchas

This plan changes problem selection and review emphasis while preserving the existing interview format.
Do not generalize a weakness beyond the saved evidence or infer an unobserved explanation from hesitation.
Do not repair or replace historical user code to make an attempt look complete.

## Related

- [Interview sessions](interview-sessions.md)
- [Attempt records](attempt-records.md)
