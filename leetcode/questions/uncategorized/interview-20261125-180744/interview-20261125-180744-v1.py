# Given a list of integers nums and an integer k, return the maximum of each
# contiguous subarray of length k, in order from left to right.
#
# nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3 -> [3, 3, 5, 5, 6, 7]
         [5, 6, 7]
# nums = [1], k = 1 -> [1]
"""
Questions:
input: list of ints
output: list of ints


range len(nums)? 1-100,000 (inclusive)
range nums[i]? -10,000/10,000 (inclusive)

range of k? 1-len(nums) (inclusive)

sorted? no
modify? yes
duplicates? yes

target contraint? no
"""


"""
Approach:
Time: O(n-k * k)
Space: O(n)
"""

class Solution:
  def maxValKIntervals(self, nums, k):
    l = 0
    r = k-1
    res = []
    
    """
    nums = [3, 3, 5, 5] #4 k=2 #ouput: [3, 5, 5]
                     l  r
    res = [3, 5, 5]
    maxVal = 5
    
    """
    while r < len(nums):
      maxVal = float('-inf')
      for i in range(l, r+1):
        maxVal = max(maxVal, nums[i])
      res.append(maxVal)
      l += 1
      r += 1
    return res
        
      
    


