- Confidence: 3/5
- Result: can get with hint
- Workon: Trace the saved entry point through a case with both upward and downward moves.

# 2096. Step-By-Step Directions From a Binary Tree Node to Another

## Code

[Python working file](2096-step-by-step-directions-from-a-binary-tree-node-to-another-v2.py)

## Session summary

1. Started November 26, 2026 at 5:03:24 PM EST (America/Toronto).

2. You traced both opening examples and clarified ordering, balance, height, value range, uniqueness, endpoint guarantees, input and output types, node fields, and the absence of a stated complexity target.
3. You independently proposed storing parent links and child directions, walking upward from the start to record distances, and stopping the destination walk at the first shared ancestor.
   You explained linear time and space and chose iterative BFS to avoid recursion depth limits.
4. You implemented the two walks and independently noted that reversing the collected child directions yields the order needed for the downward part of the result.
5. During review, interviewer questions surfaced the child lookups on the queue, the late nested helper definition, and the discarded helper result.
   You updated the saved child lookups, helper placement, and return.
6. You chose the two-node case from the prompt and traced the saved logic to L.
   You declined a second trace involving both upward and downward moves because you were out of time.

## Feedback

- **Advance this person to the next round? Yes.** Pass recorded at your request. You independently derived a viable approach and traced the two-node case after prompted fixes.
- **Technical: 2 out of 4.** You corrected the child lookup, helper placement, and return, then traced the two-node case through the corrected logic.
- **Problem solving: 3 out of 4.** You independently derived the parent map, both ancestor walks, the direction reversal, and the linear bounds.
- **Communication: 3 out of 4.** You clarified the contract and walked through the queue, maps, and returned string on your chosen example.
- **Things you did well:** You chose an iterative traversal based on the maximum depth.
- **Areas of improvement:** Your example exercised a single downward move, leaving the combination of upward moves and reversed downward directions unverified in your walkthrough.
- **My advice:** Trace the saved entry point with a path that goes up and then takes two different downward turns.
