# Given the root of a binary tree, return the number of edges in its longest path.
#
# Examples show tree nodes in level order.
# Input: root = [1, 2, 3, 4, 5]
# Output: 3
#
# Input: root = [1, 2]
# Output: 1
"""
is it a node class and we are given the root? Yes
is it a full binary tree? no, 0,1 or 2
range of len(root)? 1-10,000 (inclusive)
is there an inherit time or space compleity? no
modify? yes
are we allowed to use deque? yes
"""

"""
Approach: (iterative bfs) X
1. make a queue
2. load up the queue wit the root
3. for each time we go though all of the layers we incease the count by one
4. do this for each layer of children untill the end of the tree
5. return the count

Time: O(n)
Space: O(n)

Invariance:
- we count how deep we can go in the layers of our tree and return that value
Example:
root = 1
[1,2,3,4]
# output: 3

q = []
count = 3


Approach (iterative dfs and dp): 
1. Each entry could hold a node and a flag saying weather its children have been scheduled, in the stack
Time: O(n)
Space: O(n)
"""

class Solution:
  def longestPath(root):
    
    stk = [(root, False)]
    heights = {}
    maxpath = 0
    
    while stk:
      node, isVisited = stk.pop()
      
      
      if not node:
        continue
  
      if isVisited:
        left = heights.get(node.left, 0)
        right = heights.get(node.right, 0)
        
        maxpath = max(maxpath , left + right)
        heights[node] = max(left, right) + 1
      else:
        stk.append((node, True))
        stk.append((node.left, False))
        stk.append((node.right, False))
    return maxpath
      
    
    

