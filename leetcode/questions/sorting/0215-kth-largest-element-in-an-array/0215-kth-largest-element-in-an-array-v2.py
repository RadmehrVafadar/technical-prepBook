# Given a list of integers nums and an integer k, return the value
# occupying position k when the values are ordered from largest to smallest.
#
# Input: nums = [3, 2, 1, 5, 6, 4], k = 2
# Output: 5
#
# Input: nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
#           
# Output: 4

"""
Questions:
- range of the len(nums)? 1-100,000 (inclusive)
- range of the k? 1-len(nums) (inclusive)
- range of nums[i]? -10,000/10,000
- modify nums? yes
- is nums sorted? no
- will we always have a result? yes
- is there a required time or space? no, but try not to have O(nlogn)
- is k the index? no, it is the number of letter (it is 1 based)
- the resulting should be sorted from largest to smallest
-------
- is there duplicate values?
"""


"""
Approach #1:
- sort nums from largest to smallest
- return the value at k-1 index in nums

Time: O(nlogn) # for sorting n is the size of the nums
Space: O(1) 

Invariance:
- Beacuse we sort the array we will always have the proper order of largest to smallest as such the k-1th value will be the kth largest


Approach #2:
1. Create a min heap of size k
2. Go though entire nums array and add to heap and remove if it goes over k
3. by the end return the value at the kth / bottom of the heap

Invariance: 
- Our heap will always keep the kth largest values so when we go though all of nums we will have the kth largest and we would return the last value in that heap.

Time: O(nlogk)
Space: O(k)
"""


class Solution:
  def kthLargest(nums, k)
    nums.sort(reverse=True)
    return nums[k-1]


if __name__ == "__main__":
  nums = [3, 2, 1, 5, 6, 4]
  k = 2
  # Output: 5
  print(Solution.kthLargest(nums, k))











