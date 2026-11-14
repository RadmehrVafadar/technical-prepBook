"""
Given a 2 x n grid where each row has the numbers 1 through n, we define a valid config as one where
the numbers in the rows are all unique and also in all the columns. Given that you can swap numbers
between columns, how many possible valid configs are there?

1 4 2 3
3 2 1 4

3 2 1 4
1 4 2 3

=> 2

1 2 3 4
2 1 4 3

2 2 3 4
1 1 4 3

=> 1

"""

"""
Questions:
input: 2D array of int
output: int

range of rows? always 2
range of columb? 2-20 (inclusive)

duplicates per row? no
range of grid[i]? 1-n
modify? yes
ordered? no columbs will be the same

target contraint? no, as long as it works within input

already valid? yes
"""

"""
Appraoch (brute force):

Time: O(n * 2^n)
Space: O(n)

"""

class Solution:
    def __init__(self, grid):
        self.grid = grid
        self.ROWS = 2
        self.COLS = len(grid[0])

    def numValidConfigs(self):
        i = 0
        totalValid = 0

        self.backtracking(i, )

    def backtracking(self, i):
        grid = self.grid
        if i == len(grid):
            return isThisValid(grid)

        # does not flip
        backtracking(i + 1)

        temp = grid[0][i]
        grid[0][i] = grid[1][i]
        grid[1][i] = temp

        # does flip
        backtracking(i + 1)

        # returns it back
        temp = grid[0][i]
        grid[0][i] = grid[1][i]
        grid[1][i] = temp

    def isThisValid(self):
        grid = self.grid

        row1 = set()
        row2 = set()
        for col in range(COLS):
            if grid[0][col] in row1:
                return False

            if grid[1][col] in row2:
                return False

            row1.add(grid[0][col])
            row2.add(grid[1][col])

        return True
