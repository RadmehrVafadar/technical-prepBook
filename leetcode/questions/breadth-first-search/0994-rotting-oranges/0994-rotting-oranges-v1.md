- Confidence: 2/5
- Result: need review
- Workon: Explain what each fixed queue batch represents and why newly reached oranges wait for the next minute.

# 994. Rotting Oranges

## Code

[Python working file](0994-rotting-oranges-v1.py)

## Session summary

1. Restated cell meanings and the minimum-time objective, then proposed scanning for rotten oranges and exploring neighbors.
2. Received guidance on collecting all initial sources and counting time by levels.
3. Initially counted queue iterations on [2,1,1], then corrected the elapsed time to two minutes after tracing grid states.
4. Independently proposed marking fresh cells in the input instead of using a visited set.
5. Recognized on [1,2,1] that two processed neighbors represent one minute, and on [2,1,0,2,1] that separate sources spread simultaneously.
6. Considered independent island searches, then rejected sequential source processing using [2,1,1,2].
7. Reported watching a solution video, then proposed a fresh count and fixed-length batches containing all initial rotten coordinates.
8. Submitted code and explained that expanding the current queue batch completes one minute; requested code-specific feedback.
9. Independently suggested moving directions outside the loops; a revised implementation and personal complexity analysis were not provided.

## Feedback

**Advance this person to the next round?**
Insufficient evidence. You requested code-specific feedback rather than a general evaluation.

**Technical: Not enough evidence.**

You supplied the recorded implementation after watching a solution video. You explained batch processing as expanding the current rotten oranges for one minute and independently suggested moving directions outside the loops. Your own complexity analysis was not yet provided. You requested code-specific feedback rather than a general evaluation.

**Problem solving: Not enough evidence.**

You independently recognized that counting oranges or independent source searches overcounts simultaneous spread. Initial multi-source queue and level timing were supplied as assistance; later structure followed a video.

**Communication: Not enough evidence.**

You explained batch expansion as one minute. A precise queue invariant and your own complexity analysis were still pending.

**Things you did well:**

- You used [1,2,1] to distinguish processed oranges from elapsed minutes.
- You rejected sequential source processing on [2,1,1,2].
- You proposed marking cells in the input to avoid separate visited tracking.

**Areas of improvement:**

- Explain what the queue contains at the start of a minute and why new entries wait.
- Derive runtime from total cell processing and queue space from peak occupancy.

**My advice:**

- Highest priority on a revisit: explain the fixed-batch invariant before implementing.
- Predict no-fresh, unreachable-fresh, and multiple-source cases before execution.
