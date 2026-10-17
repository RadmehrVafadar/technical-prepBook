- Confidence: 4/5
- Result: clean
- Workon: Derive recursive time and space costs from branching and maximum active depth before stating complexity.

# 79. Word Search

## Users Own notes

## Code

```python
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        word_len = len(word)

        def dfs(r, c, i, visited):
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != word[i] or (r,c) in visited:
                return
            visited.add((r, c))
            if i == word_len-1:
                return True

            if (dfs(r - 1, c, i+1, visited) or dfs(r + 1, c, i+1, visited) or dfs(r, c + 1, i+1, visited) or dfs(r, c - 1, i+1, visited)):
                return True

            visited.remove((r,c))

        visited = set()
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0, visited): return True
        return False
```

## Session summary

- Attempt started October 17, 2026 at 4:12:53 PM EDT (America/Toronto).
- Shared the problem screenshot with Python 3 selected and an empty method body.
- Requested interview mode before discussing an approach.
- Restated the input as a 2D letter matrix and a string, and described matching the word in order through left, right, up, or down adjacency. Described the letters as lowercase; did not yet address cell reuse.
- Independently proposed scanning the matrix for a match to the first character, then using DFS through valid horizontal and vertical neighbors to seek a path matching the remaining characters in order.
- Said each DFS call needs the current cell value and the string index for comparison; a matching character continues the search, while a mismatch ends that branch.
- Explained that success means finding cells matching the entire string in order, and failure means finishing the scan of the board without finding a match.
- Asked whether a board containing only `A B` could form `ABA` by reusing a cell. The interviewer clarified that each cell may be used at most once in a path, so this example is false.
- After that clarification, independently proposed a visited set to track cells used during DFS.
- Reported checking the constraints and confirming that neither the matrix nor the string can be empty, so planned to omit empty-input handling.
- Submitted an implementation that checks boundaries, character matches, and visited membership; adds matching cells to the shared set; searches four neighbors; removes cells after unsuccessful exploration; and tries every starting cell.
- Initially questioned whether a dry run was necessary. When asked to choose a case that could expose a mistake, dry-ran the supplied board with `ABCB` and predicted false. Described following the first `A` through `B` and `C`, backing out, and rejecting the other `A` because it has no neighboring `B`. Said no adjacent cell matched the final character, without explicitly explaining that the neighboring `B` is already visited.
- When asked to explain the rejections at the first `C`, correctly clarified that the `B` to its left is already visited and the other neighboring cells do not match `B`.
- Initially responded to the shared-set safety question with “why would it not be.” After the interviewer focused the question on state left by failed branches, explained that failed branches remove their added cell and invalid cells are never added.
- Claimed worst-case time `O(nm+s)` and auxiliary space `O(nm)`, defining `m` as rows, `n` as columns, and `s` as word length. Reasoned that the board is scanned and a DFS searches up to the word length from each cell; cited the visited set potentially containing the entire board for space.
- When asked for the worst-case number of DFS calls from one starting cell as a function of `s`, answered `s^2` without a derivation yet.
- When asked to derive that estimate from the recursive calls, revised total worst-case time to `O(nm * 3^s)`, explaining that after the start there are at most three possible directions to continue.
- When asked about recursion depth and simultaneous visited cells, identified word length as the bound and revised auxiliary space to `O(s)`.

## Feedback

**Advance this person to the next round?**
Yes. At the intern level, you completed a correct implementation and explained the key path constraints. Complexity analysis needed follow-up questions; the algorithm itself required no solution hints.

**Technical: 3 out of 4.**
You completed a working solution with correct boundary checks, character matching, visited-cell handling, and restoration after failed branches. You verbally dry-ran a negative case. Your initial complexity estimates were incorrect; after questions, you revised them to `O(nm * 3^s)` time and `O(s)` auxiliary space, including recursion depth.

**Problem solving: 3 out of 4.**
You independently chose a board scan with DFS and added visited tracking after clarifying the no-reuse rule. You explained failed-branch cleanup when prompted. Your main gap was deriving the search cost: you first treated the work as additive, then estimated quadratic calls before identifying exponential branching.

**Communication: 3 out of 4.**
Your approach and stopping conditions were understandable. Your dry run initially omitted the reason the neighboring B was rejected, but you clarified it correctly. Answering justification questions directly would make your explanation more convincing than responding “why would it not be.”

**Things you did well:**

- Asked a concrete cell-reuse question and incorporated the answer into your state design.
- Implemented failed-branch restoration correctly without implementation hints.
- Correctly explained why the previously visited B cannot complete ABCB.

**Areas of improvement:**

- Derive complexity before stating it: distinguish the number of starting cells, branching within each search, and maximum active depth.
- Treat verification as part of completing the solution. You initially called it unnecessary and demonstrated only a negative dry run.
- State the visited-set guarantee directly: it holds the cells of the current candidate path, and failed calls restore the prior state.

**My advice:**

- Highest priority: on your next three recursive problems, write the branching factor, maximum depth, and work per call before giving time complexity.
- Before finishing, choose one successful path, one failed search, and one case targeting state restoration; predict each result and explain the state changes.
- Practice a variation that counts valid paths to check whether you understand the effect of early returns and cleanup.
