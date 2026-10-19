- Confidence: 1/5
- Result: incorrect
- Workon: Make node construction consistent, then explain and reconstruct the cache operations without the video.

# 146. LRU Cache

## Users Own notes

New to this double   linked list way of representing cache. First time making it / using it.

## Code

Submitted after watching a solution video.

```python
class dll:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_map = {}

        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1

        node = self.node_map[key]
        self._remove(node)
        self._add(node)
        return node.value

    def _add(self, node):
        prev_end = self.tail.prev
        prev_end.next = node
        node.prev = prev_end
        node.next = self.tail
        self.tail.prev = node

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            old_node = self.node_map[key]
            self._remove(old_node)
        new_node = dll(key, value)
        self._add(new_node)
        self.node_map[key] = new_node

        if (len(self.node_map)) > self.capacity:
            least_used = self.head.next
            self._remove(least_used)
            del self.node_map[least_used.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```

## Session summary

- Attempt started October 18, 2026 at 10:44:39 AM EDT (America/Toronto).
- Shared the problem screenshot with Python 3 selected and an empty implementation skeleton.
- Reported watching a solution video and submitted the implementation above; independent derivation was not observed.
- Asked to finish the interview and save the note about first using this representation.
- Coach identified the mismatch between the defined `dll` class and sentinel construction using `ListNode`; no corrected submission followed before the evaluation.

## Feedback

**Advance this person to the next round?**
Insufficient evidence.

At the intern level, this assisted submission does not establish independent problem solving. You submitted a complete implementation, but a constructor naming defect remains unresolved. This is a mock-interview assessment, not a hiring prediction.

**Technical: 2 out of 4.**
Your pointer updates, recency updates, and eviction logic are coherent on inspection. However, you define `dll` and construct the sentinels with `ListNode`. As submitted, the code does not provide a working constructor: `ListNode` is undefined in the supplied code. Use the same node class consistently. You did not report test results or provide complexity analysis.

**Problem solving: Not enough evidence.**
You disclosed watching a solution video. No baseline, derivation, correctness explanation, or response to counterexamples was observed, so independent understanding cannot be assessed.

**Communication: Not enough evidence.**
You clearly disclosed the assistance and your unfamiliarity with the representation, but did not explain the algorithm or its tradeoffs.

**Things you did well:**

- You separated insertion and removal into helpers, making the pointer changes easier to inspect.
- Your submitted code refreshes recency on successful reads and updates, and removes the evicted key from the map.
- You identified that this representation is new to you, giving us a concrete review target.

**Areas of improvement:**

- Node construction is inconsistent; the submitted class cannot initialize as written. Check constructor references before considering an implementation complete.
- Reproducing a video solution does not demonstrate why it works. You still need to explain the relationship between the map, list order, and eviction choice in your own words.
- Complexity analysis and user-led verification were not observed; these remain assessment gaps.

**My advice:**

- Highest priority: fix the node-class mismatch, then reconstruct the implementation from a blank editor without the video.
- Before coding, state what each end of the list represents and how the map and list remain consistent after each operation.
- Dry-run a capacity-one cache and an update to an existing key, predicting the map contents and list order after every operation.
- Review target: independently implement the cache, justify each operation, and explain its average time and auxiliary-space costs.
