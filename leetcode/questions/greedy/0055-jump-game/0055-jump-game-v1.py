# Given a list nums, start at index 0.
# Each value is the maximum number of positions you may jump forward from there.
# Return whether you can reach the final index.
#
# Input: nums = [2, 0, 1, 0]              
# Output: True
#
# Input: nums = [1, 0, 2]      
# Output: False


# [2, 2, 2, 1, 0, 0]
# dfs(1)



"""
Questions:
- is the nums sorted? No
- value of nums[i]? 0-100,000 (inclusive)
- what is the contraint of length nums? 1-10,000 (inclusive)
- are we able to modfiy? yes
- is the value the max jum or mamimum jumps you can take? You can jump up to that value
- start and ending? index 0, len(list)-1? Yes
- what if the size of the nums list is one? always return True
- is it a list of integers? Yes
- is there a default contraint? no explicit time or space requirement
"""

"""
Approach: (recursion)

1. traverse the paths that our cur index allows us to go
3. we do this by adding cur index position and up to its value so if index 0 and value 2 we would serach dfs(0+1) and dfs(0+2)
3. if at any point the index is equal to the len(nums)-1 we return true
4. if we finish our serach with an empty stack, we would return False

Time: O(n^2)
Space: O(n)
# where n is the legnth of the nums

Invariance:
- I seraches all of the paths it is allowed to and only returns True if any of those paths lead to the end
""" 


"""
Approach: (greedy) 
1. go though the list
2. as we are going though we wil keep track of the maximum we can reach
3. if the cur index is larger then the maximum we can reach we would return False, because we can not reach that index and not reach the end
4. if the max is less then the cur index we would check to see if from that index we can go further and if we can we update our max.
5. if our max can reach or surpass the length-1 of the list we can return True

Time: O(n)
Space: O(1)

Invariance:
- because we always keep track of the maxium index we can reach we will be able to tell if we can reach the end as we are going though the list
"""
# Input: nums = [1, 0, 2]      
# Output: False
# maxReach = 2
# i = 3
class Solution:
  def canReachEnd(nums):
    maxReach = 0
    
    for i in range(len(nums)):
      if i > maxReach:
        return False
      
      maxReach = max(maxReach, i + nums[i])
      
      if maxReach >= len(nums)-1:
        return True
      
    return True

if __name__ == "__main__":
  nums = [2, 0, 1, 0]
  # output: True
  print(Solution.canReachEnd(nums))















