# Given an integer array and a target, return every unique combination of
# values from the array whose sum equals the target.
#
# Input: candidates = [2, 3, 6, 7], target = 7
# Output: [[2, 2, 3], [7]]
"""
Questions:
- is sorted? No
- range of candidates: 2-40 (inclusive)
- range of target: 1-40 (inclusive)
- What to return if can't equal target: If none sum to target return empty list
- can we modify input? Yes
- the lists have to be unique
- can candidates list be empty: 1-30
- Can there be duplicate candidates? No
"""


"""
recursion: 
Time: O(2^(t+n) * t)
Space: O(t + n)




[2, 3, 6, 7] target = 7

res = []

dfs(0,[], 0)
[2]
dfs(1, [2,2,,1], 6)

"""
class TargetSum:
  def targetCombonations(self, candidates, target):
      res = []
      def dfs(i, temp_arr, cur_sum):
          if i > len(candidates)-1 or cur_sum > target:
            return
      
          if cur_sum == target:
            res.append(temp_arr.copy())
            return
      
          temp_arr.append(candidates[i])
          dfs(i, temp_arr, (cur_sum+candidates[i]) )
          temp_arr.pop()
          dfs(i+1, temp_arr, cur_sum)
  
      dfs(0, [], 0)
      return res
  
if __name__ == '__main__':
  candidates = [2,3,4] 
  target = 4
  print(TargetSum().targetCombonations(candidates, target ))
  
  
  
  

