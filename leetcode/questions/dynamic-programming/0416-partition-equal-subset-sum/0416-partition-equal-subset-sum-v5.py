# Given a list of integers, return True if you can split its elements into
# two groups with equal sums. Return False otherwise.
#
# [1, 5, 11, 5] -> True
# [1, 2, 3, 5] -> False

"""
Questions:
input: list of integers
output: boolean

range len(nums)? 1-200 (inclusive)
range of nums[i]? 1-100 (inclusive)
duplicates? yes
modify? yes
sorted? no
"""

class Solution:
  def twoGroupsSum(self, nums):
    totalSum = sum(nums)
    if (totalSum % 2):
      return False
      
    target = totalSum/2
    
    def dfs(self, i, curSum):
      if curSum == target:
        return True
      if len(self.nums)-1 < i or  target < curSum:
        return False
    
      if (dfs(i+1, curSum + nums[i]) or dfs(i + 1, curSum)):
        return True
    
     return dfs(0, 0)
     
     
# ----------------
class Solution:
  def twoGroupSum(self, nums):
    
    value = set()
    
    for num in nums:
      temp_values = value.copy()
      for val in value:
        value.add(num)
        temp_values.add(val + num)
      
      value = temp_values      
        
    

    
    