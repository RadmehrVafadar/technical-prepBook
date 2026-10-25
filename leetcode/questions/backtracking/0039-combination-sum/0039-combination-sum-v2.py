# Given a list of candidate numbers and a target, return all unique
# combinations of candidates whose sum equals the target.
# You may choose a candidate more than once.
# Combinations that differ only in order count as the same combination.
#
# Input: candidates = [2, 3, 6, 7], target = 7
# Output: [[2, 2, 3], [7]]

"""
Questions:
- Is sorted? No
- Can array be modified? Yes
- Duplicates? No
- Re-use values? Yes
- Can nothing sum to the target? Yes
- If nothing sums to the target we return empty list
- candidate always positive. only 2-40
- up to 30 numbers
"""

"""
Input [2, 3, 6, 7] target = 7


[2,3,6,7]
     i  
                                    [  ]
                       []                           [2]
           []                   [3]
         []   [6]            [3,3] [3,6]
       []  [7] [6,6] [6,7]
     
           
           
output: [[2, 2, 3], [7]]
"""


class FindTarget:
    target = 7
    myList = [2, 3, 6, 7]
    res = []

    def dfs(cur_list, i, cur_sum):
      if i > len(myList)-1 or cur_sum > target:
        return
      if cur_sum == target:
        res.append(cur_list.copy())
        return
      
      dfs(cur_list, i+1, cur_sum)
      cur_list.append(myList[i])
      dfs(cur_list, i, cur_sum+myList[i])
      cur_list.pop()
    
    dfs([], 0, 0)
    return res
      