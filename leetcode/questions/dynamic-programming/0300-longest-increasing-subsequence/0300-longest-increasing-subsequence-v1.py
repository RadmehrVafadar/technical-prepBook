# Given an integer list nums, return the length of its longest strictly increasing
# subsequence. A subsequence preserves order but may skip elements.
#
# Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]                 
#              
# Output: 4
#
# Input: nums = [0, 1, 0, 3, 2, 3]
# Output: 4
"""
Questions: 
range of len(nums)? 1-2,500 (inclusive)
range of nums[i]? -10,000/10,000 (inclusive)
can we modify nums? yes
what if it is the same value? does not count in the subsequence must be increasing
is there a required complexity? No time or space
is the array give in any order? no, they can be in any order
"""

"""
# Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]                 
#                2   2  4  3  3  2   1    1   
# Output: 4

# nums [1, 5, 2, 3, 4]
# output: 4


Approach: #1
1. start from the first value
2. create a stack, add that value 
3. go though the list and add numbers of they are larger then the stack
4. when you reach the end of the stack keep track of the largest length stack
5. do this for every number in nums
6. return the largest value kept

Invariance:
- Go though array while keeping track of the largest possibel strictly increasing subsequence

Time: O(n^2)
Space: O(n) 


Approach: #2
1. start with a LIS list and a max length value
2. add the firt number in nums (we have to have a comparison)
3. as we go though the list if the value is smaller then the final value we would
4. go though the LIS untill we reach a index i where that value is no longer larger then our cur value
5. we would replace the cur value with the value our i stopped at
6. if the top of the lists value is smalelr then the cur, we would add it to the top of the list and increase our max value by 1

Time: O(n^2) # with binary search O(nlogn)
Space: O(n)

Invariance:
- We would always get the largest incereaing subsequence length because our length would always increase if the values are increasing and since we ensure that for each of the values in the list we pick the smallest at that length we would always end up with the list length that represents the most/highest length list we can have. 
"""

"""
Dry runs:
Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]                 
# Output: 4
LIST= [2, 3, 7, 18]
max_length = 4
nums = ~
i = 3



Dry run #2:
# nums [1, 5, 2, 3, 4]
# output: 4

LIS= [1, 2, 3, 4]
max_length = 4
num = 4
index = 0

num = [3, 7, 7]
# output: 2
LIS = [3, 7]
max_length = 2



l = 1
r = 0
c = 1

index = 0
"""
class Solution:
  def LongestIncreasingSubsequence(nums):
    LIS = [nums[0]]
    max_length = 1
    
    for num in nums[1:]:
      if num > LIS[-1]:
        LIS.append(num)
        max_length += 1
      else:
        # i = 0
        # while i < len(nums) and LIS[i] < num:
        #   i += 1
        # LIS[i] = num
        l, r = 0, len(LIS)-1
        index = l
        while l <= r:
          c = l + (r-l)//2
          if LIS[c] >= num:
            index = c
            r = c - 1
          else:
            l = c  + 1
        LIS[index] = num
          
    return max_length
    
    
if __name__ == "__main__":
  nums = [10, 9, 2, 5, 3, 7, 101, 18]
  # output: 4
  print(Solution.LongestIncreasingSubsequence(nums))    
      
         
      
    









