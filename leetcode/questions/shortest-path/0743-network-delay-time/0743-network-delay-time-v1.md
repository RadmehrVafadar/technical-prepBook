- Confidence: 4/5
- Result: clean
- Workon: Explain why a node's shortest distance is final when it is first removed from the min-heap.

# 743. Network Delay Time

## Code

[Python working file](0743-network-delay-time-v1.py)

## Session summary

- Tracking began October 13, 2026 at 12:14:46 EDT (America/Toronto). The earlier attempt start time was not captured.
- You shared the problem statement with Python 3 selected and no solution implementation shown.
- You identified `n` as the number of nodes labeled `1..n`, each entry in `times` as a start node, end node, and weight, and `k` as the starting node.
- You described the output as the time needed for every node to receive the signal starting from `k`.
- You asked whether the signal spreads simultaneously. After clarification that nodes 1 and 3 receive it at time 1 from node 2, you correctly stated that node 4 receives it at time 2.
- For the same edges starting from node 1, you correctly answered `-1` because not all nodes can be reached regardless of how long we wait.
- You asked about node labels beyond `n`, cycles, a starting node with no outgoing edges, edge direction, and whether `n` or the number of edges could be zero; the coach clarified these input guarantees.

- On October 15, 2026 at 15:15:41 EDT (America/Toronto), tracking resumed with your submitted solution; the start time of this coding work was not captured.
- You supplied a Python implementation using an adjacency list, a min-heap of cumulative travel times, and a dictionary of finalized distances. You returned the maximum recorded distance, or `-1` if any node was unreachable.
- Your docstring explained that the longest of the minimum arrival times determines when every node receives the signal. No algorithmic hints were given for this submitted implementation in this exchange.

- You explained that the min-heap selects the shortest queued route and that `visited` skips later entries for an already finalized node. You also suggested tracking known distances before pushing entries to reduce heap clutter. Your explanation has not yet justified why a route discovered later cannot improve a finalized distance.

- When asked which edge-weight property prevents a later route from improving a finalized distance, you answered that the weights are positive. The coach clarified that nonnegative weights, including zero, are sufficient.

- You gave time complexity as `O((V+E) log V)`, attributing heap operations to each node and traversal to nodes and edges. The coach clarified that this implementation can queue multiple entries per node, so heap size and operation count can depend on `E`; you asked why the logarithm uses `E` and why the bound included `+1`.
- You correctly gave auxiliary space as `O(V+E)`, citing the adjacency structure and visited storage. You referred to `res` and `visited` as lists; the coach clarified that `res` is a scalar, `visited` is a dictionary, and the heap also contributes space.

## Feedback
