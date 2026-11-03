# Given a list of integers nums and an integer k, return the element
# at position k when the list is ordered from largest to smallest.
#
# Input: nums = [3, 2, 1, 5, 6, 4], k = 2
# Output: 5
#
# Input: nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
# Output: 4
"""
Questions:
- what is the new order? Largest to smallest
- is nums sorted? no
- nums[i] range? -10,000 <= x <= 10,000 (inclusive)
- k range? 1-len(nums) (inclusive)
- len of the nums array? 1-100,000 (inclusive)
- is there a default time and space complexity? no
- could there be duplicate values? Yes
- is k the index? no it is one based (count)
- are allowed to modify the nums? yes
- are duplicates sepirae posisiton? Yes
"""

"""
Approach:
1. sort the array largetst -> smallest
2. convert the k to index value by minusing it by one 
3. go to the k-1 index and return that value

time: O(nlogn)
space: O(1)
Invariance: We sort first. We will always have the value in the list that is properly sorted in that position.

Approach: #2 (monotonic stack)
1. create a stack
2. make its maximum be k
3. only add to the list if the value cur at is larger then the top of the stack
4. return the value at the top
"""

class Solution:
  def kth_largest(nums, k):
    nums.sort(reverse=True)
    return nums[k-1]

if __name__ == "__main__":
  nums = [3, 2, 1, 5, 6, 4]
  k = 2
  # Output: 5
  print(Solution.kth_largest(nums, k))

















