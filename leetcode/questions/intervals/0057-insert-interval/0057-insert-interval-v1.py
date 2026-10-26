# Given non-overlapping intervals sorted by start, insert one new interval.
# Merge overlaps and return the resulting intervals in sorted order.
#
# Input: intervals = [[1, 3], [6, 9]], new_interval = [2, 5]
# Output: [[1, 5], [6, 9]]
#
# Input: intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], new_interval = [4, 8]
# Output: [[1, 2], [3, 10], [12, 16]]


"""
Questions: 
- How is the interval ordered (ordered by the start position)
- Is the input ordered? Yes, by the start position
- Add multiple intervals? No, only one
- Can interval values be negative? Non negative 0-100,000 (inclusive)
- Garanteed one new interval
- up to 10,000 existing intervals
- Modify input array? Yes
- Endpoint sharing is overlapping.
- The current interval can cover all intervals
brute force dry-run:

0, 1, 2, 3, 4, 5, 6, 7, 8, 9..Value of Max Interval
O(Max_mimum interval lengt) -- > 100,000
O(Maximum interval Langth) --> 100, 000

Example 2:
[[1, 3], [3, 9]], [1, 9] 
[[1,3], [1,9], [3,9]]
res = [[1,9]]
 


[[1, 3],[3,4] [7, 9]] | [3,4]
"""

class Intervals:

  def insertInterval(self, intervals, new_interval):
      if not intervals:
        intervals.append(new_interval)
        return
  
      new_start, new_end = new_interval
      
      l, r = 0, len(intervals)-1
      while l <= r:
        centure = l + ((r-l)//2)
        
        if intervals[centure][0] == new_start:
              break
  
        elif intervals[centure][0] > new_start:
          r = centure - 1 
        else:
          l = centure + 1
      
      if intervals[centure][0] < new_start:
        intervals.insert(centure+1, new_interval)
      else:
        intervals.insert(centure, new_interval)
  
  def mergeIntervals(self, intervals):
#     [[1, 3]] 
    res = []
    for interval in intervals:
      if not res or interval[0] > res[-1][-1]:
        res.append(interval)
      else:
        prev_start, prev_end = res.pop()
        
        merged_start = min(prev_start, interval[0])
        merged_end = max(prev_end, interval[1])
        
        res.append([merged_start, merged_end])
    return res

  def main(self, intervals, new_intervals):
      self.insertInterval(intervals, new_intervals)
      return self.mergeIntervals(intervals)
      
if __name__=='__main__':
  intervals [[1,3],[3,4]]
  new_intervals = [7,9]
  return Intervals().main(intervals, new_intervals)
      
  
  
  
  



