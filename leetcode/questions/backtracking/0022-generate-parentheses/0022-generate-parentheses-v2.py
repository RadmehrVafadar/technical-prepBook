# Given n pairs of parentheses, return all distinct well-formed strings
# containing exactly n pairs.
#
# Input: n = 3
# Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]
#
# Input: n = 1
# Output: ["()"]

"""
Questions:
- Contraints of n: 1-8 (inclusive)
- only round paranthesise
- output can be in any order
- expect an iterative or recursive solution
- duplicates? no
"""

"""
n=2
          []
['(' ')' ')']

Time: O(4^n)
Space: O(n)
"""


"""
2
[()()] [(())]



res = [(())] [()()]
opening = 2
closing = 2
dfs(1, 0, [])

"""

class Parantheses:
  def combinationPra(n):
      res = []
      
      def dfs(opening, closing, cur_arry):
        if opening == n and opening == closing:
          res.append(''.join(cur_arry))
          return
          
        if opening < n:
          cur_arry.append('(')
          dfs(opening+1, closing, cur_arry)
          cur_arry.pop()
        if opening > closing:
          cur_arry.append(')')
          dfs(opening, closing+1, cur_arry)
          cur_arry.pop()
        
      dfs(0, 0, [])
      return res
      
if __name__ == "__main__":
  n = 2
  print(Parantheses.combinationPra(n))  
        
      
      
      
      
      
      