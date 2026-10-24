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
