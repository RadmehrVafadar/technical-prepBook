# Given a list of integers, return True if you can split its elements
# into two groups with equal sums, and False otherwise.
#
# [1, 5, 11, 5] -> True
# [1, 2, 3, 5] -> False
"""
Questions:
- list of ints? yes
- range of len(list)? 1-200 (inclusive)
- range of list[1]? 1-100  (inclusive)
- modify? yes
- is it sorted? no
- target complexity? no
"""

"""
Appraoch (brute force)
1. go though array
2. decide to keep or not keep
3. if we keep a sum that is equal to half of the total sum of the array we return True
4. if we go over we stop exapnding on that branch
5. if it equals to our target (half of total sum), return True
6. if we go though the entire array and we do not find it, we return False

time: O(2^n)
space: O(n)
"""


"""
Approach (dynamic programming):

Time: O(n*sum(nums))
Space: O(sum(nums))
"""

class Solution:
  
  def twoGroupSum(self, nums):
    total = sum(nums)
    if (total % 2):
      return False
# [1, 5, 11, 5] -> True 22//2  = 11
# dp = (0, 1, 5, 6, 11, 12, 16, 17, 10, 21, 22)
# num = 5
# dp_temp = (0, 1, 5, 6, 11, 12, 16, 17, 10, 21, 22)
#  [1, 2, 3, 5] -> False
# dp = (0)
# num = 5
# dp_temp = (0, 1,2,3,4,5,6,7,8,9,10)


    target = total // 2
    dp = set()
    dp.add(0)
    for num in nums:
      dp_temp = dp.copy()
      for value in dp:
        dp_temp.add(num)
        dp_temp.add((num + value))
      dp = dp_temp
    
    return True if target in dp else False
        
    
    

