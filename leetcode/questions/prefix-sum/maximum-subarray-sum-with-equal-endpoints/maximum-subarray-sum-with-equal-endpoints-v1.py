# Given a nonempty list of integers, return zero-based indices i <= j with
# nums[i] == nums[j] that maximize the sum of nums[i:j + 1].
# Example: [1, 2, 3, 2, 5] -> (1, 3)

# Questions:
# input: list of int (nums)
# ouput: tow ints i, j
# range len(nums)? 1-inf
# range nums[i]? -inf/inf
# duplicates? yes
# the same number would for i and j the sum is counted once
# modify? yes
# sorted? no

# Approach (sliding window)
# if l == num[r]
# Time: O(n^3)
# Space: O(1)

# Input: [1, 2, 3, 2, 5]
# Prefix sums: [1, 3, 6, 8, 13]
# Output: i = 1, j = 3
# l = 1
# r = 3
# curSum = 5
# maxSum = 5
# max_i = 1
# max_j = 3

# Approach #2
# Time: O(n^2)
# O(n)


class Solution:
  def largetSetSum(self, nums):
     sumAtPoint = []

     curSum = 0
     for num in nums:
       curSum += num
       sumAtPoint.append(curSum)

       maxSum = 0
       max_i = 0
       max_j = 0

     for l in range(len(nums)):
       for r in range(l, len(nums)):
         if nums[l] == nums[r]:

            curSum = (sumAtPoint[r] - sumAtPoint[l]) + nums[l]

            if curSum > maxSum:
               maxSum = curSum
               max_i = l
               max_j = r
     return max_i, max_j


# hashmap = value : (1, 2, )
#                   l  r
# nums = [1, 2, , 2 ,2 ]
# O(n^2)
