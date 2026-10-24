# Personal notes (preserved)

# # either land or water (binary)
# # output: the number of islands
# # [ '1', '0' ]
# # [ '0', '1' ]
# # i,j : isVisited
# # i = 0
# # j = 0

# Saved final implementation; imports and formatting added for standalone use.

from typing import List
import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # either land or water (binary)
        # output: the number of islands
        # [ '1', '0' ]
        # [ '0', '1' ]
        # i,j : isVisited
        # i = 0
        # j = 0

        visited = set()
        island_nums = 0
        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))

            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited and grid[r][c] == '1':
                        visited.add((r, c))
                        q.append((r, c))

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    island_nums += 1

        return island_nums
