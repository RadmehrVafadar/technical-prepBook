# A row of trees is represented by fruits, where each value is a fruit type.
# You have two baskets, each holding any amount of one fruit type.
# Start at any tree and move right, picking one fruit from every tree.
# Stop when the next fruit cannot fit in either basket.
# Return the maximum number of fruits you can collect.
#
# Input: fruits = [1, 2, 1]
# Output: 3
#
# Input: fruits = [0, 1, 2, 2]
# Output: 3
""" 
Questions: 
- Input: arr of ints? Yes
- Output: int? Yes 

- are we able to modify? Yes
- is the given input sorted? No
- contrainst of fruits[i]: 0-len(arr)-1
- constraint of len frutis: 1-100,000 (inclusive)

- Never enough diff types of fruit, what to? give the value only one basket has
"""

"""
 Input: fruits = [0, 1, 2, 2]
                     |     |         
              
Approach: 
1. Go though list 
2. we would pick a starting point
3. from that starting point, we would continue going right as long as the right value can be put in our baskets
 - The cur fruit is a type that is already in basket ( increase count) 
 - The cur fruit is a new type and basket has space for a new type
4. Stop if the baskets are full and we have a diff type. (or end of list)
5. sum up the frequencies of all the values in our baskets and compare to keep the largest one (count the number of fruits in baskets)
5. start from the next starting point (reset the baskets) 


Invariance: 
We would be keeping track of the maximum value

Time: O(n^2) # n would be length of list of fruits
Space: O(1) 

Approach #2:

1. start at the begining of the list with a left and right pointer
2. As we are moving right our right pointer would keep going as long as the condiitons:
  - no more than 2 types
  - the cur tree is a type that is in the basket
3. While its growing r is increasing, check the invariance (the number of fruits in our basket) 
4. Update the maximum number as we are going to increase (invariance)
5. if the conditions are no longer be able to be met. reset by increasing the left pointer and reducing the value in the basket or if there is one value we will remove from the hashmap/basket
6. after going though the entire trees array we will return the invariance (maximum value) 

Invariance:
- Keeping track of the longest value as our window increases.

Time: O(n) # legnth of our trees input
Space: O(1) 

"""
 # fruits = [1] 
 #           lr 
 # l = 0
 # r = 1
 # basket= {1:1}
 # res = 1
class Solution:
  def mostFruits(self, fruits):
    l = r = 0
    basket = {}
    res = 1
    
    while r < len(fruits):
      if fruits[r] in basket:
        basket[fruits[r]] += 1
      else:
        while len(basket) == 2:
          if basket[fruits[l]] == 1:
            del basket[fruits[l]]
          else:
            basket[fruits[l]] -= 1
          l += 1
      
        basket[fruits[r]] = 1
      
      cur_sum = 0
      for fruit in basket:
        cur_sum += basket[fruit]
      
      res = max(res, cur_sum)
      r += 1
    
    return res
    

if __name__ == '__main__':
  fruits = [0, 1, 2, 2]
  # output: 3
  
  fruits = [1]
  # output: 1
  
  print(Solution().mostFruits(fruits))
        
        
        








