# You start at index 0 of an integer list. Each element gives the maximum
# distance you can jump forward from that index. Return the fewest jumps
# needed to reach the last index.
#
# [2, 3, 1, 1, 4] -> 2
# [2, 3, 0, 1, 4] -> 2

"""
Questions:
input: list of ints
output: int

range of len(nums)? 1-10,000 (inclusive)
range of nums[i]? 0-1,000 (inclusive)

duplicates? yes
sorted? no
modify? yes

if len(nums) == 1? zero jumps because we are already at the last index

will always reach last index? yes


"""



class Solution:
  def twoSumTwo(self, nums):

  # [2, 3, 1, 1, 4] -> 2 #5
  # l = 3
  # r = 4
  # furthest = 4
  # res = 2

    if len(nums) == 1:
      return 0
    res = 0
    l = r = 0
    furthest = 0
    while r < len(nums)-1:
      for index in range(l, r + 1):
        furthest = max(furthest, index + nums[index])

      l = r + 1
      r = furthest
      res += 1

    return res
