# Given a rectangular matrix of integers, return its elements in clockwise
# spiral order, starting at the top-left corner and moving right first.
#
# Input: [[1, 2, 3], 
#         [4, 5, 6], 
#         [7, 8, 9]]
#
# Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
#
# Input: [[1, 2, 3,   4], 
#         [5, 6, 7,   8], 
#         [9, 10, 11, 12]]
# Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
"""
Questions:
- What is the dimensions: n*m
- Number values can be in any order
- Range of each number[i]: -100/+100 (inclusive) [have to be ints]
- Are we allowed to modify out input? Yes
- Range for n & m: 1-10 (inclusive) they could be diffirent
- result: a list of integers
- No preffrence of weather (recursive or iterative)
- Not ordered
"""


"""
Time: O(n x m)
Space: O(n x m)


# Input: [[1, 2, 3], 
#         [4, 5, 6], 
#         [7, 8, 9]]

top = 1
left = 1
right = 2    
bottom = 2    
res = [1, 2, 3, 6, 9, 8, 7, 4, 5]
"""

class Solution:
  def matrixSpiral(input):
    top = 0
    left = 0
    right = len(input[0])
    bottom = len(input)
    res = []
    
    while top < bottom and left < right:
      for num in range(left, right):
        res.append(input[top][num])
      top += 1
      
      if not top < bottom:
        break
        
      for num in range(top, bottom):
        res.append(input[num][right-1])
      right -= 1
    

      if not left < right:
        break    
      
      for num in range(right-1, left-1, -1):
        res.append(input[bottom-1][num])
      bottom -= 1
      
      if not top < bottom:
        break
    
      for num in range(bottom-1, top-1, -1):
        res.append(input[num][left])
      left += 1
      
      if not left < right:
        break
      
    return res
    












