# Given n pairs of parentheses, return all well-formed strings using those pairs.
#
# Input: n = 3
# Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]
#
# Input: n = 1
# Output: ["()"]
"""
Questions:
- n values 1-8 (inclusive)
- Paranthesise have to be wellformed. 
- Wellformed paranthesise pairs have to equal the number
"""


"""
n=2
                                  ['(','(']
            ['(', '(']                                               ['(', ')']
                 ['(', '(', ')']                   ['(', ')', '(']                ['(', ')']
            []            ['(','(',')',')']                  ['(', ')', '(', ')']


output: ['()()', '(())']
Time: O(2^2n) = (2^2)^n = 4^n = O(n^4)
Space: O(n) 
number of open prantheise
number of closed pranthesise 
"""

class Sol
  def wellformedParen(self, n):
    res = []
    
    def dfs(open_number, closed_number, cur_list):
      if open_number == closed_number and open_number == n:
        res.append(''.join(cur_list.copy())) 
        return
      2
      [[ (),() ], [ (()) ]]
      
      ['(', '(', ')', ')']
      l = 2
      r = 2
      
      
      """
      n=2
      
      [ ]
      l = 2
      r = 0
      res = ['()()', "(())"]
      """
      if open_number < n:
        cur_list.append('(')
        dfs(open_number+1, closed_number, cur_list) 
        cur_list.pop()
      
      if closed_number < open_nummber:
        cur_list.append(")")
        dfs(open_number, closed_number+1, cur_list)
        cur_list.pop()
    
    dfs(0,0,[]) 
    return res
  
return sol.welformed(n)
      
  
  
  
  
  
  
  