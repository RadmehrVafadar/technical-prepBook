- Confidence: 1/5
- Result: need review
- Workon: Explain how the two recursive choices allow reuse while preventing different orderings of the same combination.

# 39. Combination Sum

## Users Own notes

## Code

User-submitted solution, sourced from a YouTube video (assisted).

```python
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        
        """
        res = []
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            cur.append(candidates[i])
            dfs(i, cur, total+candidates[i])
            cur.pop()
            dfs(i+1, cur, total)

        dfs(0, [], 0)
        return res
```

## Session summary

- Attempt started October 17, 2026 at 2:33:06 PM EDT (America/Toronto).
- Shared the problem statement and an empty Python 3 method stub.
- Restated the task as finding all combinations of positive candidate integers that sum to the target, returning an empty array when none exist.
- Explained that `[2, 2, 3]` and `[3, 2, 2]` count as one because the task asks for unique combinations, not unique permutations.
- Requested a switch to interview mode before discussing an algorithm.
- Proposed backtracking with memoization: subtract each candidate from the remaining target, recursively find combinations for the remainder, and return chosen values when the remainder reaches zero. Used candidates `[2, 3, 5]` and target `7` to illustrate reducing to `5` after choosing `2`.
- Suggested caching combinations for a remainder such as `dp[5]` to avoid recomputation, mentioning a set as possible storage. Also mentioned a similar bottom-up alternative without detailing it.
- When asked how different orderings would be excluded, claimed that computing each value only once would prevent adding the same combination twice; did not yet explain how ordering is handled when combining cached results.
- Switched back to coaching mode and reported using a YouTube solution because they could not remember the backtracking solution properly. Submitted the code above and requested an explanation derived from it.
- The coach explained the recursive state, the use-or-skip branches, restoring the current list, the stopping conditions, copying a result, and the distinction between memoization and preventing reordered duplicates.
- Correctly explained that advancing the index in the use branch would prevent reusing the same candidate.
- Explained that sequential index progression prevents generating `[3, 2, 2]` for `[2, 3, 5]`, describing the result as never having an unsorted sum. The distinction between index order and numeric order remains to be clarified.
- After the coach distinguished candidate index order from numerical order, correctly predicted `[3, 2, 2]` for candidates `[3, 2, 5]` and target `7`.
- Correctly explained that `cur.pop()` removes the value added for the use branch so the skip branch starts without that choice.
- Could not initially explain why results require `cur.copy()`. After the coach explained list references with a small append-and-pop example, correctly predicted that the stored list would change to `[2, 2]` and that all saved references would ultimately contain empty lists as backtracking finishes.
- Asked how to derive edge cases in an interview. The coach suggested deriving cases from success, failure, reuse, and multiple-answer behavior, then invited a failure-case trace.
- Ended the session before attempting the edge-case trace or giving a final independent explanation and complexity analysis.

## Feedback
