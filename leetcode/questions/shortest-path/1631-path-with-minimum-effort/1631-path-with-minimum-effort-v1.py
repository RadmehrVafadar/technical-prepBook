# Given a rectangular grid of heights, travel from the top-left cell to the
# bottom-right cell, moving up, down, left, or right.
# A route's effort is the largest absolute height difference between consecutive
# cells on that route. Return the smallest possible effort.
#
# Input: heights = [[1, 2, 2], 
#                   [3, 8, 2],
#                   [5, 3, 5]]
# Output: 2
#
# Input: heights = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
# Output: 1

"""
Questions:
- square or ractangle? ractangle
- range of n? 1-100 (inclusive)
- range of m? 1-100 (inclusive)
- modify? yes
- it is sorted? no
- range of heights[i]? 1-10^6 (inclusive)
- starts and ends at the same zell? return zero for a one cell grid
- is there an inherit contraint? no
"""


"""
Approach: (greedy?) X
1. start from the top right cell
2. if the cur cell is the bottom right cell return 0 (because cell size is 1
3. otherwise, out of all of the possible directions that are legal go to the one with the smallest value
4. while you are traversing, keep track of the largest cel lvalue you had to traverse
5. once you reach the bottom right, return the max value you had to traverse to get here

Invariance: 
- we always pick the smallest value to go to (it will always try and keep the max value small) and keep track of the largest out of those values we had to traverse, meaning we would always get the largest value we had to cover in our smallest max path.

Time: O(4^(n * m))
Space: O(1) # only if we modify cells we already visited to be the largest value possible


Approach #2 (dikstras):
1. make a min heap and add the top left cell
2. make a visited set
3. make a directions set for left right top and bottom of a cell
4. while you have values in your min heap keep searching
5. pop the top of the min heap, getting the path with the smallest maximum effort and add it to the visited set
6. check if the current value has been visited before, if not keep going otherwise dont consider it and grab the next value top of the minheap
7. check if that path you had poped had reached the bottom right if so return the dist
8. if not the end and not visited before skip all of its neightbors in the left right top bottom directions that would not be in the nums array (invalid) or if those new ones are already in the new list
9. add them to the min heap but update the new dist value (the maximum effort till that point) to be the larger one of either what has already been explored or the current poped cells height minus the new neightbors that being addeds height's absolute value


Invariance: we would always return the path that had the least largest effort's maximum effort it took for that path

Time: O(n * m * ) #idk
Space: O(n * m)
"""


class Solution:
  def mineffort(heights):
    ROWS, COLS = len(heights), len(heights[0])
    
    minheap = [[0,0,0]]
    visited = set()
    distance = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    
    while minheap: 
      dist, r, c = heapq.heappop(minheap)
      
      if (r,c) in visited:
        continue
      visited.add((r, c))
      if r == ROWS-1 and c == COLS-1:
        return dist
      
      for dr, dc in distance:
        newR, newC = (r + dr), (c + dc)
        
        if (newR < 0 or newC < 0 or 
            newR == ROWS or newC == COLS or 
            (newR, newC) in visited):
          continue
        newD = max(dist, abs(heights[r][c] - heights[newR][newC]))
        heapq.heappush(minheap, [newD, newR, newC])


if __name__ == "__main__":
  heights = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
  # Output: 1
  print(Solution.mineffort(heights))
  
          
        
      
        
      
      
      









