# Personal notes (preserved)

# [ [1, 2, 1]
#           [2, 1, 2]
#         ]
#         [[1, 0], [2, 0], [1, 0]]
#         Time: O( (m x n)^2 )
#         Space O(m x n)
#         bfs(0,0)
#
# Corrected coordinates:
#
# [[0, 1], [0, 2], [1, 0], [1, 2]]

# Final submitted solution:

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        """
        Cells that flow up, down, left, right
        0 is allowed
        no empty matrix
        never have an emptry result
        heights are always integers

        [ [1, 2, 1]
          [2, 1, 2]
        ]
        [[0, 1], [0, 2], [1, 0], [1, 2]]
        Time: O((m x n))
        Space O(m x n)
        bfs(0,0)
        """

        res = []

        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, ocean, preValue):
            if r > ROWS-1 or r < 0 or c > COLS-1 or c < 0 or heights[r][c] < preValue or (r,c) in ocean:
                return
            cur_height = heights[r][c]

            ocean.add((r, c))

            dfs(r-1, c, ocean, cur_height)
            dfs(r+1, c, ocean, cur_height)
            dfs(r, c-1, ocean, cur_height)
            dfs(r, c+1, ocean, cur_height)


        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res
