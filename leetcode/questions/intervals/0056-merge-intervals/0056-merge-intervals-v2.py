# Given a list of intervals [start, end], combine overlapping intervals.
# Return non-overlapping intervals covering exactly the same values.
#
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
"""
Questions:
- Is it sorted? Not
- Is is wellformed (start be less or equal to the end)? Yes
- Interval of one single point: [1,1] 
- are they integers? All integers
- what is the range of the values = 0-10,000 (inclusive)
- what it the range of the number intervals= 1-10,00 (inclusive)
- can we modify input? yes
- can there be intervals with the same start? Multiple intervals can have same starting value 
- what do we do if the interval of on is the same as the other? [1, 3] [3, 10] YES overlapping? [1,2] [3,10] NO
- could there be an inteval that covers all intervals? Yes
"""

"""
Approach:
1. Sorting the list by [start then finish]
2. check if the last values ending is larger then the current ones stating 
3. If it is we remove the current one in result and replace it with one where out of the two it has smallest start and largest end
4. Once we do that for the entire input we can return our res
Time: O(nlogn)
Space: O(n)
"""

class Solution:
  def mergeIntervals(intervals):
    intervals.sort()
    stk = []
    
    for start, end in intervals:
      if not stk:
        stk.append([start, end])
        continue
      
      if stk[-1][1] >= start:
        prev_start, prev_end = stk.pop() 
        
        new_start = min(prev_start, start)
        new_end = max(prev_end, end)
        stk.append([new_start, new_end])
        
      else:
        stk.append([start, end])
      
    return stk
    
if __name__ == "__main__":
  intervals = [[1, 3], [2, 4]] #output = [[1,4]]
  print(Solution.mergeIntervals(intervals))    
      
      




















