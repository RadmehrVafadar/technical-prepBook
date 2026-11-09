- Confidence: 1/5
- Result: not finished
- Workon: Implement the BFS baseline as a callable and trace its height calculation on a small tree.

# 310. Minimum Height Trees

## Code

[Python working file](0310-minimum-height-trees-v1.py)

## Session summary

1. Started November 08, 2026 at 11:19:23 AM EST (America/Toronto).

2. Asked about node and edge bounds and whether every node has an incident edge.
3. Proposed iterative BFS from each candidate root and tracking the best height and ties, with O(n^2) time and O(n) space.
4. Considered caching and explained that a height computed under one rooting can change after rerooting.
   The interviewer clarified the distinction between neighbors and children, then misread the caching concern as an edge traversal question until the user clarified it.
5. Requested a hint.
   The interviewer asked the user to compare a leaf and its neighbor as roots, then supplied a three-node path after the user said the heights were equal.
   The user counted two edges from the endpoint and ultimately reported zero from the middle.
   The interviewer asked how many edges lead from the middle to an endpoint.
6. Stopped to watch a video before implementing the approach.

## Feedback
