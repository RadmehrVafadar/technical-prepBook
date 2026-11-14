# In a grid, 1 is land and 0 is water. You can move between land cells
# that share an edge and step off the grid from any land cell on its boundary.
# Return the number of land cells from which you cannot step off the grid.
#
# [[0, 0, 0, 0], 
#  [1, 0, 1, 0], 
#  [0, 1, 1, 0], 
#  [0, 0, 0, 0]] -> 3

# [[0, 1, 1, 0], 
#  [0, 0, 1, 0], 
#  [0, 0, 1, 0], 
#  [0, 0, 0, 0]] -> 0
"""
Question:
input: grid 2D list of ints, with 0's and 1's 
output: int

range of n? 1-500 (inclusive)
range of m? 1-500 (inclusive)
total: 500*500 = 250,000


target complexity? no
modify? yes

what are directions? up, down, left, right
are the number placements random? yes
"""
"""
Approach (iterative bfs or dfs)
Time: O(n*m)
Space: O(n*m)
"""

class Solution:
  def __init__(self, grid):
    self.ROWS =  len(grid)
    self.COLS = len(grid[0])
    self.grid = grid
    self.stk = []
    
  def countEnclosedLandCells(self):
    grid = self.grid
    stk = self.stk
    
    # top row
    for col in range(self.COLS):
      cell = grid[0][col]
      if cell == 1:
        stk.append((0, col))
        grid[0][col] = 0
    
    # bottom row
    for col in range(self.COLS):
      cell = grid[self.ROWS-1][col]
      if cell == 1:
        stk.append((self.ROWS-1, col))
        grid[self.ROWS-1][col] = 0
        
    # left columb
    for row in range(self.ROWS):
      cell = grid[row][0]
      if cell == 1:
        stk.append((row, 0))
        grid[row][0] = 0
    
    # right columb
    for row in range(self.ROWS):
      cell = grid[row][self.COLS-1]
      if cell == 1:
        stk.append((row, self.COLS-1))
        grid[row][self.COLS-1] = 0
    
    self.dfs(stk)
    
    numLandCells = 0
    for row in range(self.ROWS):
      for col in range(self.COLS):
        if grid[row][col] == 1:
          numLandCells += 1
    
    return numLandCells 
    
    
  def dfs(self, stk):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while stk:
      r, c = stk.pop()    
      for dr, dc in directions:
        newR, newC = (r + dr), (c + dc)
        if (0 <= newR < self.ROWS and 0 <= newC < self.COLS and self.grid[newR][newC] == 1):
          stk.append((newR, newC))
          self.grid[newR][newC] = 0
    
    
    
