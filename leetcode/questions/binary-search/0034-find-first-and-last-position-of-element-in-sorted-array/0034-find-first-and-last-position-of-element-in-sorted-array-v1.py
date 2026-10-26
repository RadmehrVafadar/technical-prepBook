# Given an integer array nums sorted in nondecreasing order and a target,
# return the zero-based indices of its first and last occurrence.
# Return [-1, -1] if the target is absent.
#
# Input: nums = [5, 7, 7, 8, 8, 10], target = 8
# Output: [3, 4]
#
# Input: nums = [5, 7, 7, 8, 8, 10], target = 6
# Output: [-1, -1]


"""
Questions: 
- The nums[i] can be -10^9-10^9
- Target can be -10^9-10^9
- Length can be 0-100,000
- If empty return pair of -1's
- can have duplicates
- array is sorted non-decreasing (meaning the values can be the same not just increasing)
- can you modify the arary? Yes
- is there a constraint limit? O(logn) n is the array length
-  No limit to the number of values
"""


"""
Binary Serach:

[-1,1,1,1,1,2]
target = 1
"""

class Intervals:
  def getIntervals(nums, target):
      res = [-1, -1]
      l, r = 0, len(nums)-1
      
      while l <= r:
        middle = l + ((r-l)//2) # centure
        
        if nums[middle] == target:
          lower = self.getlowerBound(l, middle-1)
          higher = self.getupperBound(middle+1, r)
          res = [lower, higher]
          break
              
        elif nums[middle] > target:
          r = middle - 1
        else:
          l = middle + 1
          
      return res
      
  def getlowerBound(self, l, r):
      res = r + 1
      while l <= r:
        middle = l + ((r-l)//2)
        
        if nums[middle] == target:
           res = middle 
           r = middle - 1      
        else:
          l = middle + 1
      return res
    
  
  def getupperBound(self, l, r):
      res = l - 1
      while l <= r:
        middle = l + ((r-l)//2)
        
        if nums[middle] == target:
           res = middle 
           l = middle + 1      
        else:
          r = middle - 1
      return res
    

if __name__ == "__main__":
  nums = [1,1,1,1]
  target = 1
  # output = [0,3] 
  print(Intervals().getIntervals(nums,target)
