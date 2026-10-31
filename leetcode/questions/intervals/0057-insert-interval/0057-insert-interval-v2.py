# Given a list of intervals and one additional interval, add the new interval,
# merging overlaps as needed. Return the resulting intervals in order of start.
#
# Input: intervals = [[1, 3], [6, 9]], newInterval = [2, 5]
# Output: [[1, 5], [6, 9]]
#
# Input: intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval = [4, 8]
# Output: [[1, 2], [3, 10], [12, 16]]
"""
Questions:
- is intervals sorted? Yes
- number of intervals: 0-10,000 (inclusive)
- number of newIntervals: 1
- could no intervals be empty? no, always one
- Range of interval values: 0-100,000 (inclusive)
- list of int? Yes
- are intervals wellformed? Yes, less then or equal to end
- intervals of range 1? [1,1]
- is [1,3] and [3,4] overlapping? yes
- modfiy input? Yes
- Yes they are garanteed non-overlapping
- no required time or space complexity
"""

"""
Approach: 
1. insert the newInterval into the existing intervals at the right spot (binary search)
2. Once the newInterval is added to the spot it should be (for sorted)
3. Now merge the overlapping intervals starting at the new intervals placement minus one if that does not exist the no need to look at the left
4. returning the new non-overlapping intervals list

Time: O(n)    # n is length of intervals
Space: O(n) 

Invariance: 
- the resullt will always remain a non-overlapping list of intervals
"""


class Solution:
  def main(self, intervals, newInterval):
    self.insertInterval(intervals, newInterval)
    return self.mergeIntervals(intervals)


  def insertInterval(self, intervals, newInterval):
    if not intervals:
      intervals.append(newInterval)
      return
    # binary search  
    
    l, r = 0, len(intervals)-1
    while l <= r:
      c = l + ( (r-l)//2 )
      
      if newInterval[0] == intervals[c][0]:
        break
  
      elif newInterval[0] > intervals[c][0]:
        l = c + 1
      else:
        r = c - 1
    
    if intervals[c][0] < newInterval[0]:
         c += 1
       
    intervals.insert(c, newInterval])
    
  # intervals = [[1, 2], [3, 5], [4, 8], [6, 7], [8, 10], [12, 16]]
  #
  # stk = [[1,2], [3,10], [12, 16] ]
  def mergeIntervals(self, intervals):
    stk = []
    
    for start, end in intervals:
      if not stk:
        stk.append([start, end])
        continue
      
      if stk[-1][-1] => start:
        old_start, old_end = stk.pop()
        new_start = min(old_start, start)
        new_end = max(old_end, end)
        stk.append([new_start, new_end])
      else:
        stk.append([start, end])
    return stk
    
      

if __name__ == '__main__':
  intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval = [4, 8]
  # Output: [[1, 2], [3, 10], [12, 16]]
  
  intervals = [], newInterval = [4, 8]
  # output: [4,8]
  print(Solution().main(intervals, newInterval))










