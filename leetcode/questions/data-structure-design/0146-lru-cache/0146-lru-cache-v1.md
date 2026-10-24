- Confidence: 1/5
- Result: incorrect
- Workon: Make node construction consistent, then explain and reconstruct the cache operations without the video.

# 146. LRU Cache

## Code

[Python working file](0146-lru-cache-v1.py)

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
