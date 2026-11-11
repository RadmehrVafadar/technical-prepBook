- Confidence: 3/5
- Result: can get with hint
- Workon: Trace the first loop iteration on a boundary case before submitting.

# 236. Lowest Common Ancestor of a Binary Tree

## Code

[Python working file](0236-lowest-common-ancestor-of-a-binary-tree-v4.py)

## Session summary

1. Started November 11, 2026 at 05:44:09 p.m. EST (America/Toronto).

2. Clarified size, ordering, uniqueness, balance, target existence, ancestor behavior, the node interface, and the return type.
3. Identified recursion depth as a risk on skewed trees and independently proposed an iterative traversal to build parent links, then walking both paths toward the root to find the first intersection.
4. After a membership-cost question, chose a set for the first path and explained linear time and auxiliary space.
5. Implemented the parent map and both walks in a callable method.
6. The interviewer asked which node the second walk checks first, then pointed out that it checks the parent and asked what happens if the starting node is the answer.
   You identified the required change and moved the membership check before the parent lookup.

7. Chose the opening example and traced the parent map, ancestor set, and return value.
   After a focused follow-up, corrected the stack pop order.
8. Explained that advancing before checking membership would skip the original second target if it was already on the first target's path.

## Feedback

1. **Advance this person to the next round?** Yes.
   You independently developed a scalable approach and completed a correct callable method after a targeted boundary prompt.
2. **Technical: 3 out of 4.** Your final method returns the existing node and handles deep trees iteratively, but the original loop skipped the starting node and your first dry run misstated stack order.
3. **Problem solving: 3 out of 4.** You independently derived the parent-link approach and first-intersection rule, then clarified membership cost and corrected the loop after interviewer questions.
4. **Communication: 3 out of 4.** You clarified the contract, connected the depth bound to Python's recursion limit, and explained why the first shared node is the answer.
5. **Things you did well.** You used the lack of parent pointers to motivate the map and explained the time and space bounds.
6. **Areas of improvement.** Follow the actual order of pushes, pops, membership checks, and pointer updates in the written code.
7. **My advice.** Dry-run the first loop iteration on an input where the starting node is already the answer.
