# Given a grid of heights, return the coordinates from which water can reach
# both oceans. One ocean borders the top and left edges, and the other
# borders the bottom and right edges.
# Water can move up, down, left, or right to a cell of equal or lower height,
# and from a boundary cell into the ocean it touches.
#
# Input: heights = [[1, 2],
#                  [4, 3]]
# Output: [[0, 1], [1, 0], [1, 1]]

"""
Questions:
which ocean borders top,left? pacific, the other is atlantic
can it flow to equal height? yes
will it be populated? yes
is the population ints? yes
range of heights[i]? 0-100,000 (inclusive)
is the heights grid dimnesions? n*m
range of n? 1-200 (inclusive)
range of m? 1-200 (inclusive)
max size = 200 * 200 = 40,000
is the output order matter? no
modify? yes
is the heights ordered? no
inherit space or time? no 
are we allowed to use dequue()? yes
"""


"""
Brute force Appraoch (bfs iteratively): X
1. go though every single cell in our grid using bfs
2. have a visited set for that search
3. if cells are found in that visited set that are from both the oceans (we could have a set per ocean that goes along their respective orderes)
4. add that origional cell we seached from to our results
5. once done this for all cells in the 2D-array, we would return our results list

Time: O((n*m)^2)
Space: O(n*m)
"""


"""
Approach (bfs iteratively):
1. put in our queue all of the cells that one of the oceans starts from.
2. run bfs for that ocean and keep a visited set, such that you would know which cells you can reach
3. do this for the other ocean
4. compare the cells they could reach and return the cells that could reach both in a results list

Time: O(m*n)
Space: O(m*n)
"""

class Solution:
  def __init__(self):
    self.pacific = set()
    self.atlantic = set()
    
  def reachBothOceans(self, heights):
    ROWS, COLS = len(heights), len(heights[0])
    pacific = self.pacific
    atlantic = self.atlantic
    
    q = deque()
    
    # top - pacific 
    for col in range(COLS):
      q.append((0, col))
      pacific.add((0, col))
      
    # left - pacific
    for row in range(ROWS):
      q.append((row, 0))
      pacific.add((row, 0))
    
    self.bfs(q, pacific, heights)
    
    q = deque()
    # bottom - atlantic
    for col in range(COLS):
      q.append((ROWS-1, col))
      atlantic.add((ROWS-1, col))
      
    # right - atlantic
    for row in range(ROWS):
      q.append((row, COLS-1))
      atlantic.add((row, COLS-1))
      
    self.bfs(q, atlantic, heights)
    
    res = []
    if len(atlantic) > len(pacific):
      for cell in atlantic:
          if cell in pacific:
            rows, cols = cell
            res.append([rows, cols])
    return res
            
  def bfs(self, q, visited, heights):
    r, c= q.popleft()
    direcitons = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dr, dc in direcitons:
      newR, newC = (dr + r), (dc + c)
      
      if (0 <= newR < ROWS and 0 <= newC < COLS and [newR, newC] not in visited and heights[r][c] <= heights[newR][newC]):
        q.append((newR, newC))
        visited.add((newR, newC))
        
  
      
    
    
    
