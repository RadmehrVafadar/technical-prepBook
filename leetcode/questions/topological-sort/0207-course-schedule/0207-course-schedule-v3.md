- Confidence: 4/5
- Result: can get with hint
- Workon: State why completed courses can be cached and include recursion depth in space analysis.

# 207. Course Schedule

## Code

[Python working file](0207-course-schedule-v3.py)

## Session summary

- Attempt started: October 20, 2026, 4:57:33 PM EDT (America/Toronto).
- You shared the Course Schedule statement with Python 3 selected and no implementation yet.

- You described course labels starting at 0, interpreted each pair as a course and its prerequisite, and stated that the result asks whether all courses can be completed. Your wording initially conflated the number of courses with the largest label, numCourses - 1.
- You independently identified circular prerequisites as the obstruction, illustrated by courses 0 and 1 requiring each other, and noted that a course can have multiple prerequisites.

- You proposed an adjacency list mapping each course to its prerequisites, following prerequisite chains, returning False for a repeated required course, and popping requirements once they can be completed. The meaning of a repeated course and the state needed to distinguish a loop from shared prerequisites remain to be clarified.

- After the coach presented shared prerequisites as a counterexample to treating every repeated encounter as a loop, you explained that a course leaves visited when its exploration finishes. You also proposed clearing its prerequisites to remember that it can be completed, avoiding a false loop when another course requires it.

- You stated that prerequisites must have no loop before clearing a course. The coach clarified that every prerequisite must itself be completable and invited implementation.
- You submitted a complete Python implementation with adjacency lists, a set for the active traversal chain, recursive failure propagation, removal on successful completion, and cleared prerequisite lists to remember completed work.

- You dry-ran the three-course cycle, built the correct adjacency list, identified the repeated active course 0, and explained how False propagates through recursive calls to the final result. Your written final visited state omitted course 2, which had also been added.
- You stated O(V + E) time and O(V + E) space, defining V as courses and E as prerequisite pairs; your space explanation covered the adjacency structure but did not explicitly mention the active set or recursion stack.

- The coach corrected the omitted course 2 in your trace and confirmed your complexity bounds, adding the active-set and recursion-stack costs. You requested no further dry runs.

## Feedback






**Advance this person to the next round?**
Yes

For an intern interview, you produced a correct implementation and explained cycle detection and failure propagation, with limited coaching to distinguish shared prerequisites from a loop.

**Technical: 3 out of 4.**
You completed a working algorithm and implementation. Your O(V + E) time and space bounds are correct. Your space explanation omitted the O(V) active set and recursion stack. Deep chains can encounter Python recursion limits.

**Problem solving: 3 out of 4.**
You independently identified circular dependencies and proposed adjacency lists and recursive exploration. A shared-prerequisite example prompted you to precisely distinguish the current chain from completed work. You then described both states correctly.

**Communication: 3 out of 4.**
Your explanation of failure propagation was clear. Your initial course-count wording and one omitted active course in the trace needed correction.

**Things you did well:**

- You identified circular prerequisites before receiving an algorithm hint.
- You translated your plan into code with correct cleanup and failure propagation.

**Areas of improvement:**

- Define the active-chain invariant precisely at the outset; your initial repeated-course rule was ambiguous.
- Explicitly account for recursion depth when explaining auxiliary space.

**My advice:**

- On your next attempt, state what membership in each tracking structure means before coding.
- Give a one-sentence justification for caching completed courses and include the recursion stack in your complexity explanation.
