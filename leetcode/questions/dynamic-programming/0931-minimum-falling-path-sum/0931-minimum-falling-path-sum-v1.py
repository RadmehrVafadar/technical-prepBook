# Given a square matrix of integers, return the smallest sum of a path
# from the top row to the bottom row. Start in any column.
# At each step, move down one row and stay in the same column or move
# one column left or right, staying inside the matrix.
#
# [[2, 1, 3], 
#  [6, 5, 4], 
#  [7, 8, 9]] -> 13
# ---
# [[14, 13, 15], 
#  [13, 12, 12], 
#  [7, 8, 9]] -> 13




# [[-19, 57], 
#  [-40, -5]] -> -59


"""
Questions:
input: 2D list of ints
output: int

if return and starting row is the same return that single cells value
grid? n*n
range of n? 1-100 (inclusive) total 100*100 = 10,000
range of grid[n]? int: -100/100 (inclusive)
modify? yes
target complexity? no
duplicates? no
"""


"""
Approach (burte force backtracking)
Time: O(n * 3^n)
Space: O(n) # for the callstack
"""

"""
Appraoch (start from bottom keep track of smallesst path in a pathSum grid)
Time: O(n^2)
Space: O(n^2)
"""

class Solution:
  def __init__(self, grid):
    self.n= len(grid)
    self.grid = grid
  
  
  def createPath(self, row, col, grid, gridSum):
    if row == self.n-1:
      gridSum[row][col] = grid[row][col]
    
    directions = [(-1, 0), (-1, -1), (-1, 1)]
    
    for dr, dc in directions:
# [[2, 1, 3], 
#  [6, 5, 4], 
#  [7, 8, 9]] -> 13
# ---
# [[14, 13, 15], 
#  [13, 12, 12] 
#  [7, 8, 9]] -> 13    
    
      newR, newC = (row+ dr), (col+ dc)
      if (0 <= newR < self.n and 0 <= newC < self.n):
        newValue = (gridSum[row][col] + grid[newR][newC])
        if gridSum[newR][newC] == None or gridSum[newR][newC] > newValue:
          gridSum[newR][newC] = newValue
          
        
  
  def smallestSumPath(self):
    grid = self.grid
    
    gridSum = [[None for _ in range(self.n)] for _ in range(self.n)]
    
    for row in range(self.n-1, -1, -1):
      
      for col in range(self.n):
        self.createPath(row, col, grid, gridSum)
    
    
    return min(gridSum[0])
      
    
    