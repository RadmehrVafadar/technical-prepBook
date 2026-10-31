# Given a rectangular grid of land heights, return the coordinates of cells
# from which water can reach both oceans.
# The Pacific touches the top and left edges; the Atlantic touches the bottom
# and right edges.
# Water moves up, down, left, or right to a cell of equal or lower height.
# Water can flow directly from an ocean-bordering cell into that ocean.
#
# Input: heights = [[1, 2, 1], 
#                   [2, 1, 2]]
#
# Output: [[0, 1], [0, 2], [1, 0], [1, 2]]
#
# Input: heights = [[1]]
# Output: [[0, 0]]

# Good to know: Python recursiion limit is 1,000 calls so anything after that might be better to be iterativ
"""
Questions:
- modify input? yes
- is there a height requiremnt to go from edge to the ocean? no
- contraint of the heights[i]?  0-100,000 (inclusive)
- rows n and cloumbs m? yes, 1-200 (inclusive) so max 200*200 = 40,000
- can water flow between equal heights? yes
- can water flow back to a prevous visited cell? Yes
- can there be an empty result? 
- water can only flow, left, right, top, bottom.
- recursive or iterative? iterative
- order of result matter? no
"""


"""
Approach:
- Go though every cell in grid
- for each cell do dfs to see if it can reach both the oceans
- add that cell to the result list if it can. move on if otherwise

Time: O( (m*n )^2 )
Space: O(m*n)


Approach #2:
1. do DFS on all of the cells that connect to a border (all top cells, all bottom cells, left and right) 
2. we would run dfs for both oceans sepirately, keep track of the cells they can reach 
3. the dfs would be oppsite of flowing down. it would go to the adjacent cells that are equal to or higher then the current one
4. if a cell can be reached by both the oceans dfs() we would add those cells to our result list 
5. return the results list

 Time: O(n*m)
 Space: O(n*m)
 
Invariance: 
- our results will always be the cells that our dfs could reach for both oceans so it would only include cells that flow to both 
"""

"""
 heights = [
            [1, 2, 1], 
            [2, 1, 2]]
ROWS = 2
COLS = 3
pacific = ([0, 0], [0,1], [1,0], [0,2], [1,2])
atlantic = ([1,0], [1,1], [0,1], [1,2], [0,2])
stk []
res = [[0,1], [1,0], [0,2], [1,2]]
# Output: [[0, 1], [0, 2], [1, 0], [1, 2]]
"""
class Solution:
  def bothOceanCells(self, heights):
    ROW, COLS = len(heights), len(heights[0])
    pacific, atlantic = set(), set()
    
    def dfs(r, c, visited):
      if (r,c) in visited: 
        return 
      
      stk = [(r, c, heights[r][c])]
      
      while stk:
        cur_cell = stk.pop()
        row, columb, height = cur_cell
        visited.add((row, columb))
        delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for change in delta:
          pr = cur_cell[0] + change[0]
          pc = cur_cell[1] + change[1]
      
          if pr >= 0 and pr < ROWS and pc >= 0 and pc < COLS and (pr, pc) not in visited and heights[pr][pc] >= cur_cell[2]:
            stk.append((pr, pc, heights[pr][pc]))
    
    for c in range(COL):
      dfs(0, c, pacific)
      dfs(ROWS-1, c, atlantic)
    
    for r in range(ROW):
      dfs(r, 0, pacific)
      dfs(r, COL-1, atlantic)
      
    if len(atlantic) > len(pacific):
      for cell in atlantic:
        if cell in pacific:
          i, j = cell
          res.append([i, j])
    else:
      for cell in pacific:
        if cell in atlantic:
          r, c, h = cell
            res.append([r, c])
    
    return res
    

if __name__ == "__main__":
  heights = [[1]]
  # Output: [[0, 0]]
  print(Solution().bothOceanCells(self, heights))













