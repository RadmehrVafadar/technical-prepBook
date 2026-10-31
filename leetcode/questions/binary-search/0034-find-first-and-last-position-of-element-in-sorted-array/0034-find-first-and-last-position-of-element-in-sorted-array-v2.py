# Given an integer array nums sorted in non-decreasing order and an integer
# target, return the indices of its first and last occurrence.
# Return [-1, -1] if target is absent.
#
# Input: nums = [5, 7, 7, 8, 8, 10], target = 8
# Output: [3, 4]
#
# Input: nums = [5, 7, 7, 8, 8, 10], target = 6
# Output: [-1, -1]

"""
Question:
- if there is only one match both are at the same index
- if it is not in the nums list it would return -1, -1
- contraints of the nums[i]? -10^9/10^9
- contraint of target? -10^9/10^9
- contraint of the length of nums? 0-100,000 (inclusive)
- there will always be a target value? Yes
- is the numbers in nums a list of integers? Yes ints
- is target an integer? Yes
- are we able to modify the array? Yes
- is there a time contraint? O(logn)
- is the output integers? Yes
"""


"""
Approach:
1. do a binary search to find if the number exists in the nums array, if not return [-1,-1]
2. if it is then add it as the starting and ending index in the interval
3. do a binary search on its left side and check if it is there in the less section if it is update the starting
4. do a binary serach on its right side and check if it is in the more section if so update the ending 
5. return the left most and right most values for the target interval


Invariance: 
the starting and ending location of the target in the nums list

Time: O(logn)
Space: O (1)
"""

class Solution:
  def findInterval(self, nums, target):
    
    l, r = 0, len(nums)-1
  """
    Input: nums = [5, 7, 7, 8, 8, 10], target = 8
                                r  lc
      l = 5    r = 4   c = ~
      
    self.findStarting(nums, 4)
    target = 8
    highest = 4
    l = 0    r = 3
    
    start = 3
    end = 4
    return [3, 4]
    
            
       
                      
    Output: [3, 4]
  """
    while l <= r:
      c = l + (r-l)//2
      
      if nums[c] == target:
        start = self.findStarting(nums, c)
        end = self.findEnding(nums, c)
        return [start, end]
      
      elif nums[c] > target:
        r = c - 1
      else:
        l = c + 1
    
    return [-1, -1]
        
        
  def findStarting(self, nums, lowest):
    target = nums[lowest]
    
    l, r = 0, lowest -1
    while l <= r:
      c = l + (r-l)//2
      if nums[c] == target:
        lowest = c
        r = c - 1
      else:
        l = c + 1
    return lowest
        

  def findEnding(self, nums, highest):
    target = nums[highest]
    
    l, r = highest+1, len(nums)-1
    while l <= r:
      c = l + (r-l)//2
      if nums[c] == target:
        highest = c
        l = c + 1
      else:
        r = c - 1
    return highest
        
if __name__ == "__main__":
  nums = [5, 7, 7, 8, 8, 10]
  target = 8
  # Output: [3, 4]
  # Input: nums = [5, 7, 7, 8, 8, 10], target = 6
  # Output: [-1, -1]
  print(Solution().findInterval(nums, target))
















