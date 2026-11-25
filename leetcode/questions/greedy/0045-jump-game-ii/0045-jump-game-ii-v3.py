# You start at index 0 in an integer array.
# Each value is the maximum number of positions you can jump forward from that index.
# Return the fewest jumps needed to reach the last index.

# nums = [2, 3, 0, 1, 4] -> 2
# nums = [1, 2, 1, 0] -> 2
"""
Questions:
always reach the end? yes
if length is 1? zero jumps

input: list of ints
outputs: int

range len(nums)? 1-10,000 (inclusive)
range nums[i]? 0-1,000 (inclusive)
ordered? no
modify? yes
duplicates? yes

target compelxity? no
"""

"""
Appraoch:
Time: O(n)
Space: O(1)
"""

class Solution:
  def minNumberJumps(self, nums):
    l = r = 0
    count = 0
    """
    nums = [1, 2, 1, 0] -> 2 #4
                  l  r
    count = 2
    newR = 3
    newL = 2
    """
    while r < len(nums)-1:
      newR = r
      newL = r+1
      for index in range(l, r+1):
        newR = max(newR, index + nums[index])
      count += 1
      r = newR
      l = newL
      
    return count
      


