- Confidence: 3/5
- Result: can get with hint
- Workon: Trace what each stored value must provide at the point where the paths meet.

# 2096. Step-By-Step Directions From a Binary Tree Node to Another

## Code

[Python working file](2096-step-by-step-directions-from-a-binary-tree-node-to-another-v1.py)

## Session summary

1. Started November 11, 2026 at 06:30:02 PM EST (America/Toronto).
2. You clarified the node count and value bounds, tree ordering and balance, the form and presence of the two target values, and the node fields.
   When you asked what else to clarify, the interviewer suggested asking whether the targets could coincide.
3. You independently proposed an iterative traversal to build a parent map with child directions, then walking from both targets to find their shared ancestor.
   You explained the linear time and space costs and chose an iterative depth-first traversal because the tree can be deep.
4. Focused interviewer questions led you to fix the target name in the first loop, move its update inside the loop, and give the root entry the same tuple shape as other entries.
5. An interviewer question about the first loop's output exposed excess up moves.
   After a hint to store the distance to each ancestor and build the up moves after finding the intersection, you implemented the distance map.
6. The interviewer pointed out that the destination loop assigned the parent to a different variable, and you corrected the assignment.
7. You traced the first example with the interviewer confirming the tree layout, identified the reversed order of the downward directions, and fixed it in code.
   You chose a two-node case with the destination above the start and traced the early return to a single up move.
8. When asked why the meeting point gives the shortest path, you identified it as the lowest common ancestor and explained that it is the closest shared ancestor.

## Feedback

1. **Advance this person to the next round?** No.
   You reached a correct solution for the agreed behavior, but needed a hint to carry the start-to-ancestor distance into the return value and prompts to get both walks advancing correctly.
2. **Technical: 2 out of 4.** Your final callable implements the agreed behavior in linear time and space, and your dry runs covered both return branches after the traversal fixes.
3. **Problem solving: 3 out of 4.** You independently devised the parent-map approach and explained the lowest common ancestor, then used a hint to represent the distance needed when the walks meet.
4. **Communication: 3 out of 4.** You clarified relevant input guarantees, explained your choice of iterative traversal, and traced concrete state through both return branches.
5. **Things you did well:** You accounted for deep trees and independently caught the order of the downward directions during your dry run.
6. **Areas of improvement:** Define what each entry needs to tell you when the walks meet, and check that each loop updates the variable its condition reads.
7. **My advice:** Before coding, trace a case where the walks meet below the root and write down the exact state the return expression needs.
