# Given a list of [start, end] intervals, return the fewest intervals you
# must remove so that the remaining intervals do not overlap.
# Intervals that share only an endpoint can both remain.
#
# [[1, 2], [2, 3], [3, 4], [1, 3]] -> 1
# [[1, 2], [1, 2], [1, 2]] -> 2
"""
input: list of list of ints
output: int

always a pair? yes
can they be the same? no start < end

range of len(ranges)? 1-100,000 (inclusive)
range of len(ranges[interval][i])? -50,000/50,000 (inclusive)

is ranges list sorted? no
all overlaps and no overlaps
duplicates? yes

if the same value, not overlapping

target complexity? no
"""

"""
Approach:
Time: O(nlogn * 2^n)
Space: O(n)
"""


"""
Approach:
Time: O(nlogn)
Space: O(n)
"""


class Solution:
  def minOverLapping(self, intervals):
    intervals.sort()
    
    res = []
    counter = 0
    for inter in intervals:
      if not res:
        res.append(inter)
        continue
     
      if inter[0] < res[-1][1]:
        if inter[1] < res[-1][1]:
          res.pop()
          res.append(inter)
        counter += 1
      else:
        res.append(inter)
    
    return counter
      
      
    
      
      
      