# Given a list of integers, return whether it can be split into two groups
# whose sums are equal. Each list element must belong to exactly one group.
#
# [1, 5, 11, 5] -> True
# [1, 2, 3, 5] -> False
"""
Questions:
input: list of ints
output: boolean

range of len(list)? 1-200 (inclusive)
range of list[i]? 1-100 (inclusive)

sorted? no
modify? yes
duplicates? no

target complexity? no
"""

"""
Approach:
Time: O(2^n)
Space: O(n)
"""

"""
Apprach:
Time: O(n * sum(n))
Space: O(sum(n))
"""

class Solution:
  def canTwoGroups(self, nums):
    sumation = sum(nums)
    if (sumation % 2):
      return False

    target = sumation/2
    sums = set()
    sums.add(0)
    # [1, 2, 7] 5 False
    # {0, 1, 2, 3, 7, 8, 9, 10}
    for num in nums:
      temp_sums = sums.copy()
      for value in sums:
        newVal = (num + value)
        if newVal == target:
          return True
        temp_sums.add(newVal)
      sums = temp_sums

    return True if target in sums else False
