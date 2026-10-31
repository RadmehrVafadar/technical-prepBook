# Given a grid, 0 means empty, 1 means a fresh orange, and 2 means a rotten orange.
# Each minute, fresh oranges adjacent horizontally or vertically to rotten oranges
# become rotten simultaneously.
# Return the minimum minutes until no fresh oranges remain, or -1 if impossible.
#
# Input: grid = [[2,1,1],
#                [1,1,0],
#               [0,1,1]]
# Output: 4
#
# Input: grid = [[2,1,1],
#                [0,1,1],
#                [1,0,1]]
# Output: -1
"""
Questions:
1. our grid is m by n grid
2. contraint of m? 1-10 (inclusive)
3. contrainst of n? 1-10 (inclusive)
4. spread up down left right  
5. has to be 0, 1, 2 for grid[i][j]? no other values then the ones mentioned
6. is it able to be modified? Yes
7. are the numbers ordered in any way? No
8. limit of how many oranges we can start out with? each can appear 0-n*m times
9. grid of all zeros? zero minutes since nothing is there to rot
"""


"""
Approach:
1. Go though the grid
2. Add ever rotten orange to a queue 
3. we pop it from the queue and then add whatever oranges are adjacent to the popedd orange (not rotten oranges)
4. after the pop the orange we change its value in the grid to be rotten (keep track for the checking if we have been able to rot all oranges)
4. once we have popped all of the rotten oranges and added their adjacent values, we would increment a minutes counter by one
5. we would keep doing this loop of adding to the queue and dequeueing once the original queu was dequeued and we increment our value of minutes by one and replace its place in the grid with a rotten fruit
6. go though the grid again after we finish with our queue and check if there are any oranges, if there are return -1 otherwise we return our minutes value

Time: O(n*m)
Space: O(n*m)
Invariance: our grid and the minutes counter the grid would always end with all of the oranges that can be rotten turned rotten and minutes would always refrect the time it would take to get t othat point. 

- only count minutes after we have added the origional rotten oranges
"""

class Solution:
  def rottenOranges(self, grid):
  
"""
# Input: grid = [[2,2,2], n=3, m=3
#                [2,2,0],
#               [0,2,2]]
# Output: 4

q = [0]
minutes = 5
x = 0
y = 0
"""
  
    minutes = 0
    q = dequeue()
    n = len(grid)
    m = len(grid[0])
    # if there is rotten fruit. Add it to our queue
    for i in range(n):
      for j in range(m):
        if grid[i][j] == 2:
          q.append([i, j])
    offsets = [[1, 0], [-1, 0], [0,1], [0, -1]]
    
    # if the first orange is rotten be able to not add minutes 
    while q:
      for orange in range(len(q)):
        x, y = q.popleft()
        
        for v, b in offsets:
          new_x = x + v
          new_y = y + b
          if new_x => 0 and new_x < n and new_y => 0 and new_y < m and grid[new_x][new_y] == 1:
            q.append([new_x, new_y])
            grid[new_x][new_y] == 2
      if q:
        minutes += 1
         
    
    for i in range(n):
      for j in range(m):
        if grid[i][j] == 1:
          return -1
    
    return minutes 

if __name__ == "__main__":
  grid = [[2,1,1],[0,1,1],[1,0,1]
  # output: -1
  
  # Input: grid = [[2,2,2],
  #                [0,2,2],
  #                [1,0,2]]
  # Output: -1
  print(Solution().rottenOranges(grid))
  
  
  
  
  
  
  
  
  