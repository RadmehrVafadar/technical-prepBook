# Two linked lists encode integers, with the ones digit first.
# Return a linked list encoding their sum in the same order.
#
# Input: l1 = [2, 4, 3], l2 = [5, 6, 4]
# Output: [7, 0, 8]
"""
[2 11 40 ]

2 1's 
4 10's 
3 100's

342

5 1's
6 10's
4 100's

465

465 + 342 = 807
7 0 8

""" 

""" 
Questions:
1. Range of length: 1-100
2. Range of values in nodes is a digit: 0-9
3. Inputs values: l1 and it points to the next one
class Node:
  def __init__(self,val,next)
    self.val = val
    self.next = Null
 None at the end. No prev pointer
 4. Given the head of each linked list
 5. returning the head of the new linked list that represents the sum starting from the ones digit
 6. No required complexity
 Needed to ask if we can modify the existing nodes
 7. The two nodes can have sepirate lengths 
Mistake: Did not ask if the linked listst are modifiable
""" 

"""

[2, 4, 3]
2 x 10^0 = 2
4 x 10^1 = 42
3 x 10^2 = 342 


[2, 4, 3]
2 x 10^0 = 2
4 x 10^1 = 42
3 x 10^2 = 342 

684
| | | 
4 -> 8 -> 6 -> Null

Time: O(l1 + l2)
Space: O(1)
"""

class Solution:
  def sumNodes(l1, l2):
    dummy = Node()
    cur = dummy
    carry = 0
    while l1 or l2 or carry:

      val_l1 = l1.val if l1 else 0 
      val_l2 = l2.val if l2 else 0
      
      cur_sum = val_l1 + val_l2 + carry
      
      carry = cur_sum // 10
      cur_sum = cur_sum % 10 
      cur.next = Node(cur_sum)
      
      cur = cur.next
      l1 = l1.next if l1 else None
      l2 = l2.next if l2 else None
      
    return dummy.next


 if __name__ == "__main__":
 # assume the linked lists are given
   print(Solution.sumNodes(l1, l2))
 
 
 
 