# Personal notes (preserved)

# # Need to remember how we create unqique combinations (dp with one branch moving the window of candidate and one branch not) and going untill reach the base cases where either the window is larger then the candidates list of total sum is higher or equal.

# User-submitted solution, sourced from a YouTube video (assisted).

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
