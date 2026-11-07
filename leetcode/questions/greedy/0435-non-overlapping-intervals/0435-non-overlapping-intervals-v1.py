# Each interval is a pair [start, end].
# What is the fewest intervals you can remove so that the remaining intervals do not overlap?
#
# Input: [[1, 4], [2, 5], [6, 8]]
# Output: 1
#
# Input: [[1, 2], [4, 5]]
# Output: 0
"""
Questions:
1. range of len(intervals) = 1-100,000 (inclusive)
2. range of intervals[i] = -50,000/+50,000 (inclusive)
3. Could we be given intervals that dont overlap? yes
4. could we be given all overlapping intervals? yes
5. inherit contraint? no
6. they can be given in any order
7. do they overlapp on the same? no
8. modfit? yes
"""

"""
Approach (brute force):
1. go though intervals
2. pick if we keep interval or not 
3. check if the intervals are overlapping 
4. if not keep track of the minimum not keeps we had to do
5. if not overlapping the we stop that branch


Time: O(2^n^2)
Space: O(k)


Approach (removing overlapping):
1. sort the array start then end
2. go though the array and check if it is overlapping
3. if it is overlapping then remove the interval with the largest ending
4. minus the starting length with the ending length and return that result

Time: O(nlogn) # sorting
Space: O(n)

Invariance: 
- we remove the intervals that we need ro have non-overlapping and return the diffirence
"""

class Solution:
  def giveMinNonOverlap(intervals):
    intervals.sort()
    
    stk = []
"""
Intervals = [[1, 8],  [6, 8]]
# Output: 1

stk = [[1,8]]
start = 6
end = 8
preStart = 1
preEnd = 8
""" 
    for start, end in intervals:
      if not stk:
        stk.append([start, end])
        continue
      
      preStart, preEnd = stk.pop()
      
      if preEnd > start:
        if preEnd < end:
          stk.append([preStart, preEnd])
        else:
          stk.append([start, end])
      else:
        stk.append([preStart, preEnd])
        stk.append([start, end])
    return (len(intervals) - len(stk))
        
        
        
      
  

