# A grid uses 0 for empty cells, 1 for fresh oranges, and 2 for rotten oranges.
# Each minute, fresh oranges next to a rotten orange horizontally or vertically
# turn rotten at the same time.
# Return how many minutes it takes until no fresh oranges remain, or -1 if impossible.
#
# Input: grid = [[2, 1, 1], 
#               [1, 1, 0], 
#               [0, 1, 1]]
# Output: 4
#
# Input: [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
# Output: -1 
"""
Questions:
grid size? it can be rectangalar
rows? n 
columbs? m
range of n? 1-10 (inclusive) 10*10 = 100
range of m? 1-10 
if whole grid is rotten? return zero
if the whole grid has no oranges? zero
if its not possible return -1
is there a restriction on fruits, rotten or normal? 0-n*m times
is there an order? no 
modify? yes
are the rotennesses doing the same time? yes
are we allowed to use a deque()
"""

"""
Approach: (iterative bfs) (know it should be reursive instead)
1. create a dfs by storing the number of oranges and its chilren
2. if the oranges in that layer are all removed form the stack then we would increase the conter by one
3. each time we remove the rotten oranges, we add its children, and change the grid so that it is  rotten at that location.

Time: O(n*m)
Space: O(n*m)
"""
# grid : list of ints
# output : int
class Solution:
  def rottenOranges(grid):
    minutes = -1
    q = deque()
    ROWS, COLS = len(grid), len(gird[0]) # 3, 3
# Input: grid = [[2, 2, 2], 
#               [2, 2, 0], 
#               [0, 2, 2]]
# Output: 4
# minutes = 5
# q = []
    # first time going, add to queue
    value = False
    for i in range(ROWS):
      for j in range(COLS):
        if grid[i][j] == 2:
          q.append((i, j))
        if grid[i][j] == 1:
          value = True
          
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    if not q and not value:
      return 0
        
    while q:
      for _ in range(len(q)):
        row, col = q.popleft()
        
        for dr, dc in directions:
          newR, newC = (dr + row), (dc + col)
          
          if (0 <= newR < ROWS and 0 <= newC < COLS and grid[newR][newC] == 1):
            q.append((newR, newC))
            grid[newR][newC] = 2
            
      minutes += 1
      
    for i in range(ROWS):
      for j in range(COLS):
        if grid[i][j] == 1:            
          return -1
      
    return minutes
            