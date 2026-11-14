# Mock practice focus

Future mocks prioritize completing the agreed behavior and checking the written code, using observed weaknesses to choose practice.

## Why

The grid configurations and Minesweeper reviews show a recurring gap between identifying a sound baseline and delivering a complete operation.
In the grid interview, the interviewer emphasized getting the backtracking baseline working quickly enough to spend time on verification and follow-ups.

## How it works

### Current focus

1. Settle the input/output contract and reconcile examples that disagree with it before coding.
2. Define the core state's meaning, stopping condition, and result, then connect them through one complete callable baseline.
3. Trace the written implementation through a distinguishing case before discussing optimization.

### Between mocks

For the next mock, use [416. Partition Equal Subset Sum](../leetcode/questions/dynamic-programming/0416-partition-equal-subset-sum/), explicitly requested after the November 10 unfinished retry.
This user-selected retry takes priority over automatic question selection and the deferred Minimum Height Trees retry.

Review the latest feedback and keep one primary focus for the next attempt.
For the next full mock, the primary focus is completing and tracing a callable baseline before the follow-up.
Between mocks, rehearse a small counting backtracking problem from a blank file and state what the helper returns before writing it.
Trace one accepted branch and one rejected branch through the leaf, return, and state restoration.
For a larger-input follow-up, change one decision in a small example and trace which other choices it forces.
Check the latest saved evaluation's advance recommendation before selecting a retry.
Exclude problems with a latest recommendation of Yes unless the user explicitly requests that problem or a passed-problem review.
A hint, review flag, confidence score, or tracker status does not override that pass.
Among problems not yet passed, prioritize an independent retry when the latest attempt was unfinished, incorrect, or needed a hint, solution, or video.
Use the tracker schedule and the latest saved feedback to choose among those problems.
For new mocks, wait at least 24 hours after the most recent known attempt, solve, or solution review before offering the same problem again.
When the user asks to defer a retry, record its earliest eligible time in the session summary and prioritize it in a later eligible mock.
After a clean retry, use an unfamiliar problem with a small state transition and meaningful boundary behavior to check whether the skill transfers.
Practice both open representation choices and fixed interfaces, with the same completion and verification criteria for both.
Keep problem identity, technique, constraints, and diagnostic examples private until the normal interview process reveals them.
Privately check that numerical bounds, example states, and fixed counts are mutually consistent before presenting the task.

### During a full mock

Keep the opening minimal and let the candidate drive the interview.
Observe whether clarification resolves decisions or keeps reopening choices the candidate owns.
When a choice is deliberately open, let the candidate make and justify it without repeatedly seeking approval.
Let the candidate choose their representation, settle a concise input/output contract, and begin a complete implementation.
Observe whether planning detail goes into the core operation or is concentrated on routine validation and naming.
Do not supply a checklist, missing branches, invariant, test cases, or algorithm as unsolicited coaching.
When a material error appears, use the focused intervention rules in [Interview sessions](interview-sessions.md#during-the-interview) and record any assistance.
If planning circles without implementation, ask the candidate to implement their current approach.
Preserve productive thinking silence; do not treat filler or a pause alone as a reason to intervene.

### At review

Assess these outcomes from observed behavior rather than requiring a rehearsed script:

- One callable entry point connects validation, state transition, and the required result.
- Every agreed case has an exact observable outcome that matches the written code.
- The candidate explains what each helper call or work item represents and how it contributes to the final result.
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

- [Valid grid configurations attempt](../leetcode/questions/backtracking/valid-grid-configurations/valid-grid-configurations-v1.md) - evidence about recursive returns, completing the baseline, and working through follow-ups.
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
