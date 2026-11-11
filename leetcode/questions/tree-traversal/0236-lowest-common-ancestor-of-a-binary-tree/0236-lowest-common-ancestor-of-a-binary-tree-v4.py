# Given the root of a binary tree and two nodes in it, return the deepest
# node that lies on both paths from the root to the given nodes.
#
# Example (tree shown in level order):
# root = [8, 3, 10, 1, 6], p = node 1, q = node 6
# Output: node 3
"""
Questions:
range of nodes in tree? 2-100,000 (inclusive)
is it a binary search tree? no
is each value in the node unique? yes
is it balanced or not? could be unbalanced
is p and q in tree always? yes both always in
if one node is ancestor does that count? yes
is the root the node? yes
return by refference? yes
ordred? no
is there a time or space target? no
"""

"""
Approach: (iterative dfs)
1. create a list of node: parents (dfs)
2. start at node p and trace a path to the root
3. start at q go to root if q's node is in the path that p had to take, return that node
Time: O(n)
Space: O(n)
"""



class Solution:
# root = [8, 3, 10, 1, 6], p = node 1, q = node 6
# Output: node 3
# stk = []
# node = 8
# parent = {8:None, 3:8, 10:8, 1:3, 6:3}
# path = (1, 3, 8)
# p = 8
# q = 3
  def lowestCommonAncestor(self, root, p, q):
    parent = {root: None}
    
    stk = [root]
    
    while stk:
      node = stk.pop()
      
      if node.left:
        stk.append(node.left)
        parent[node.left] = node
      
      if node.right:
        stk.append(node.right)
        parent[node.right] = node
    
    path = set()
    while p:
      path.add(p)
      p = parent[p]
    
    while q:
      if q in path:
        return q
    
      q = parent[q]
      

    
    