# Given an integer array nums, return whether its elements can be divided into
# two subsets with equal sums, using every element exactly once.
#
# Input: nums = [1, 5, 11, 5]
#
# Input: nums = [1, 2, 3, 5]
# Output: False

"""
Quesitons:
- are the groups squential? no, you can put any element in the group as long as every element ends up in a group.
- how many groups? two
- duplicates? yes
- is it int array? yes
- the range of nums[i]? 1-100 (inclusive)
- the range of len(nums)? 1-200 (inclusive)
- is the list sorted? no
- modify input? yes
- if its 1 element only? return False
- is there an inherit contraint? no
- each elemnt use once? yes
"""

"""
Approach: (siling window) X
1. sort nums
2. what is the total sum of the values in nums
3. a window where if the total_sum - cur_window_value == cur_window_value return true
4. if we go though the entire array and it does not equal then return False

Time:  O(nlogn)
Space: O(n) or O(1) Auxillay

Invariance:
- always return if we have two groups (our window and total-window aka 2nd group) would equal each other, same thing as having two groups that sum would equal. Therefore we would always return True in the proper case.

Approach: (dynamic programming)
1. get a target by divding the total sum of the nums by two
2. create a set that would incluse the sums starting from the sum of zero since we can always never add any values
3. go through our nums and add new unique totals to our set
4. because we cant iterate and modify at the same time. would would iterate though a master set and add its values and the new values to a temp set
5. once we add all new values we would make the master set equal the temp set.
6. if at any point when we are adding the set will have a value that equals target, return True
7. if we go though entire list and it does not return false


time: O(n * sum(nums))
space O(n)
"""


"""
Dry Run:
  nums = [1, 5, 11, 5]
  # output: True
  
  total = 22 
  target = 11
  dp = (0, 5, 1, 6)
  num = 11
  temp_dp = ()
  t = 0 + 1
  # returns True since it finds at index 2 is 11 and is equal to target
  
  
  Dry run #2:
  Input: nums = [1, 2, 3, 8]
  # Output: False
  
  sum = 14
  
  target = 7
  num = 8
  t= 0
  temp_dp = (0, 8, 2, 10, 5, 13, 1,  9, 4, 12, 3, 11, 6, 14)
  dp = (0, 8, 2, 10, 5, 13, 1,  9, 4, 12, 3, 11, 6, 14)
  
  since we finished all num in nums and did not get a value equal to target we return False
  
  
  
"""
class Solution:
  def canSplitEqualGroups(nums):
    total = sum(nums)
    if total % 2:
      return False
    
    target = sum(nums) // 2
    dp = set()
    dp.add(0)
    
    for num in nums:
      if num == target:
        return True
      temp_dp = set()
      for t in dp:
        if (t + num) == target:
          return True
        temp_dp.add(t)
        temp_dp.add(t + num)
      dp = temp_dp
    
    return False
    

if __name__ == "__main__":
  nums = [1, 5, 11, 5]
  print(Solution.canSplitEqualGroups(nums))  
  




