# Given a string s, return its longest contiguous substring that reads the same
# forwards and backwards.
#
# Input: s = "babad"
# Output: "bab" ("aba" is also valid)
#
# Input: s = "cbbd"
# Output: "bb"
"""
Questions:
- special characters? No
- Spaces? No
-     lowercase? both upper and lower case (treat as distinct)
- 0-9, ints or strings? Yes
- Constraints of s: 1-1,000
- Theere is no order
- If there are multiple longest palindromes which one would i return? return any one of them
"""

"""
Brute force

cbccdg
- grab the slice from the list at the end by storing where the pointers had the longest length
- going though each iteration and checking if its a valid palindrome (left and right)
"""

class Solution:
  def longestPalindrome(s):
    res = [] # left, right
    cur_max = -1
    for i in range(len(s)):
    
      
      # odd
      l, r = i, i
      while l >= 0 and r < len(s) and s[l] == s[r]:        
        if (r-l) > cur_max:
          cur_max = (r-l)
          res = [l, r]
        
        l -= 1
        r += 1
      
      
      # even
      l, r = i, i+1
      while l >= 0 and r < len(s) and s[l] == s[r]:
        if (r-l) > cur_max:
          cur_max = (r-l)
          res = [l, r]
        
        l -= 1
        r += 1
    
    l, r = res
    return s[l:r+1]
    
    
if __name__=="__main__":
  s = 'abba'
  # output: 'abba'
  print(Solution.longestPalindrome(s))



