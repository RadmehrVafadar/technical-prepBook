- Confidence: 2/5
- Result: need review
- Workon: Define active-path and completed states and explain why every prerequisite branch must succeed.

# 207. Course Schedule

## Code

[Python working file](0207-course-schedule-v1.py)

## Session summary

1. Independently restated prerequisite direction and identified cycles as the obstacle.
2. Initially assumed one prerequisite per course; corrected that assumption and changed the map values to lists.
3. Proposed following prerequisite chains recursively and identified revisiting a course on the current branch as a cycle.
4. Initially treated one successful branch as sufficient; needed guidance that all prerequisites must be completable.
5. Needed repeated help distinguishing unchecked, currently exploring, and completed states; the transition explanation remained unresolved during voice practice.
6. Correctly argued that a course without prerequisites can be marked safe immediately, prompting correction of the coach's earlier advice.
7. Watched a solution video and submitted the recorded implementation; independent explanation reconstruction was deferred.
8. Requested a future revisit and other approaches.

## Feedback

**Advance this person to the next round?**
Insufficient evidence. Formal evaluation was deferred until your interview-ready explanation; scores were not assigned.

**Technical: Not enough evidence.**

You supplied the recorded recursive implementation after watching a solution video. Independent reconstruction of its full explanation was deferred.

**Problem solving: Not enough evidence.**

You independently connected impossible prerequisites to cycles. Distinguishing active-path visits from completed work and requiring every prerequisite branch needed guidance. The final solution followed a video; independent reconstruction is pending.

**Communication: Not enough evidence.**

The state-transition explanation remained unresolved during voice practice. Your final explanation was deferred.

**Things you did well:**

- You independently identified cycles as the obstruction.
- You correctly challenged the advice that courses without prerequisites could not be marked safe.

**Areas of improvement:**

- Clearly define the active path and when a course becomes safe.
- Explain why one failing required branch makes the course impossible.

**My advice:**

- Main demonstrated strength: independently connected impossible prerequisites to cycles and correctly challenged the claim that no-prerequisite courses must remain unvisited.
- Main learning gap: distinguishing active-path state from completed work and combining all required branches correctly.
- Completion is assisted; independent mastery has not yet been demonstrated.
- User explicitly wants to revisit this problem and learn other approaches.
- Next step: explain in the user's own words what visited means, why removal is necessary, and why clearing preMap[crs] is safe.
- Revisit from a blank editor without the video or notes; justify the invariant before implementing.
- Compare this implementation with DFS using a separate three-state array so prerequisite data remains intact.
- Learn a queue-based approach using counts of unfinished prerequisites (Kahn's topological sort); derive why processing fewer than V courses proves a cycle.
- Explore iterative DFS as an alternative that avoids Python recursion depth limits.
- Targeted review cases: a shared prerequisite across branches; one safe branch and one cyclic branch; a cycle in a disconnected component; no prerequisites; a long chain. Predict and dry-run results before execution.
