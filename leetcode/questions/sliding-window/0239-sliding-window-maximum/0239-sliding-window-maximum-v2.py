# Given a list of integers and a window size k, return the maximum
# of each contiguous window of length k, in left-to-right order.
#
# Input: nums = [4, 2, 5, 1], k = 2
# Output: [4, 5, 5]

# nums = [5, 2, 1], k = 2
#                l  r
# monotonic deque
# q = [2, 3]
# res =[5, 2, 1] 

class Solution:
  def maxNumInWindow(self, nums, k):
    q = deque()
    res = []
    
    r = l = 0
    
    while r < len(nums):
      # pop if new value is larger
      while q and nums[q[-1]] < nums[r]:
        q.pop()
      q.append(r)
      
      
      
      # remove from window if it is beyond it
      while q and q[0] < l:
        q.popleft()
      
      if r >= k-1:
        res.append(nums[q[0]])
        l += 1
      r += 1
    
    return res    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    