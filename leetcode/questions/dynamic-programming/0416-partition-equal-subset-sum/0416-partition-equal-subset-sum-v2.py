# Given an integer array nums, return whether its elements can be split
# into two subsets with equal sums.
#
# nums = [1, 5, 11, 5] -> True
# nums = [1, 2, 3, 5] -> False
"""
list of ints? yes
range nums[i]? 1-100 (inclusive)
range len(nums)? 1-200 (inclusive)
can sum be odd? yes, return False
are nums given in any order? no
modify? yes
is there a required target? no
each number used once? yes
duplicates? yes
"""
"""
Appraoch: include or not include
Time: O(2^n)
Space: O(1) # if we count the cl stack O(n)
"""
"""
Approach #2:
Time: O(n)
Space: O(1) # call stack is O(n)

"""

class Solution:
  def twoGroupsSum(self, nums):
    totalSum = sum(nums)
    if (sum(nums) % 2) == 1:
      return False
    target  = totalSum // 2
    
     self.equalsTarget(index, curSum) 
    
    
