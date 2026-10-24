# A row of trees is represented by integers indicating fruit types.
# Choose any starting tree and move right, collecting one fruit per tree.
# You have two baskets, each holding only one fruit type, with unlimited capacity.
# Stop when the next fruit cannot fit. Return the most fruits you can collect.
#
# Input: [1, 2, 1]
# Output: 3
#
# Input: [0, 1, 2, 2]
# Output: 3
"""
 Question
 - You can change but it has to reflect orgional tree order
 - constaints:
 - minimum array length = 1
 - if one then you return arrays length
 - the result has to reflect the origional order
 - from zero up to the aray length minus one
 - complexity of lenght and values in the list would remain the same
 - the array is not ordered
 
 Dry-run:
 Input: [1, 2, 1]
 output: 3        
basket = (1)
temp_counter = 1
res = max(temp_counter, res) = 3
Time O(n^2)
Space: O(1)

Dry run 2.0:
Input: [0, 1, 2, 1]
              
hashmap = {2:1 1:2} # fruit: count
Time O(n)
space: O(1)


cur_total = 0
for tree, freq in hashmap:
  cur_total += freq
res = max(res, cur_total)

Output: 3
"""


"""
Input: [0, 1, 2, 1] # len=4
           l     r
Output: 3

basket = {1:2, 2:1}
temp_count = 3
res = 3
l = 1
r = 4

"""
class PickingFruits:
      def fruitbasket(myList):
          res = 0
          basket = {}
          l = r = 0
          while r < len(myList):
                if myList[r] in basket:
                      basket[myList[r]] += 1
                else:
                    if len(basket) < 2:
                      basket[myList[r]] = 1
                    else:
                      while len(basket) == 2:
                          if basket[myList[l]] == 1:
                            del basket[myList[l]]
                          else:
                            basket[myList[l]] -= 1
                          l += 1
                    
                    basket[myList[r]] = 1
                      
                temp_count = 0
                for key in basket:
                  temp_count += basket[key]
                
                res = max(temp_count, res)
                r += 1
            return res      
           
      if __name__ == "__main__":
           return fruitbasket(myList)