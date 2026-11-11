# Given the root of a binary tree with unique node values, a start value,
# and a destination value, return a string of directions along the shortest
# path from the start node to the destination node.
# Use L for left child, R for right child, and U for parent.
#
# Trees below are shown in level order.
# root = [5, 1, 2, 3, None, 6, 4], start = 3, destination = 6 -> "UURL"
# root = [2, 1], start = 2, destination = 1 -> "L"


"""
Questions:
range of len(tree)? 2-100,000 (inclusive)
range of node.val? 1-n but max is 100,000
is it a binary search tree? no
each node value is unique? yes
is it balanced? no
the start and end are? integers
is there an explicit target? no
values will always be in tree? yes
can start and destination be the same node? no
root is node? yes
"""


"""
Appraoch (iterative bfs or dfs):
Time: O(n)
Space: O(n)
"""


class Solution:
  def __init__(self):
    pass
  def shortestPath(self, root, start, destination):
    parents = {root:None}
    
    stk = [root]
    
    while stk:
      node = stk.pop()
      
      if node.left:
        stk.append(node.left)
        parents[]
  










