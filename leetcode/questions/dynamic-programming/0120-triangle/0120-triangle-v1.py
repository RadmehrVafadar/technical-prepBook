# Given a triangle of integers, find the smallest sum along a path from
# the top to the bottom. From index i in one row, you can move to index i
# or i + 1 in the next row.
#
# [   [2], 
#    [3, 4], 
#   [6, 5, 7], 
# [4, 1, 8, 3]] -> 11
# [[-10]] -> -10
"""
Questions:
range of rows? 1-200 (inclusive) 200*200 = 20,100
range of cols? 1-200
range of pyramid[i]? -10,000/10,000 (inclusive)

target contraint? no
modify? yes
"""


"""
Approach: (pathSum + pyramid starts?)
Time: O( (r * (r+1)) / 2) )
Space: O( (r * (r+1) / 2) )
"""

class Solution:
  def __init__(self, pyramid):
    self.ROWS = len(pyramid)
    self.pyramid = pyramid
    infinity = float('inf')
    self.pyramidSum = [[infinity for _ in range(col)] for col in range(1, self.ROWS+1)]
    
## [   [2], 
#    [3, 4], 
#   [6, 5, 7], 
# [4, 1, 8, 3]] -> 11
# ROWS = 4
# pyramidSum = 
# [   [11], 
#    [9, 10], 
#   [7, 6, 10], 
# [4, 1, 8, 3]]
# 
#
    

  def smallestPath(self):
    pyramid = self.pyramid
    pyramidSum = self.pyramidSum
    
    for col in range(len(pyramid[self.ROWS-1])):
      pyramidSum[self.ROWS-1][col] = pyramid[self.ROWS-1][col]
    
    directions = [(-1, 0), (-1, -1)]
    
    for row in range(self.ROWS-1, -1, -1):
      for col in range(len(pyramid[row])):
        for dr, dc in directions:
          newR, newC = (dr + row), (dc + col)
          if (0 <= newR < self.ROWS and 0 <= newC < len(pyramid[newR])):
            pyramidSum[newR][newC] = min(pyramidSum[newR][newC], pyramidSum[row][col] + pyramid[newR][newC])
      
    return pyramidSum[0][0]  
      
    




