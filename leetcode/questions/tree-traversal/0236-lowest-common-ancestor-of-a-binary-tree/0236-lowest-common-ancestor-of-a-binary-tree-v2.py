# Given the root of a binary tree and two nodes in it, return the deepest
# node that appears on both paths from the root to the given nodes.
#
# Example (tree shown in level order):
#   root = [8, 3, 10, 1, 6], p = node with value 1, q = node with value 6
#   Output: node with value 3
"""
Questions:
is it a bst? no
could one of the chilren be itself? yes
are both nodes in tree? yes
range of len(tree)? 2-100,000 (inclusive)
time or spaece contraints? no
are values in our tree unique? yes
range of tree[i]? -10^9/+10^9 (inclusive)
are nodes reffernce or values? node
"""

"""
Approach: (iterative dfs)

Time: O(k)
Space: O(k)

"""

 # p
 #  \ 
 #   q
 
 
 # q   if root = q or root p
 #  \ 
 #   p
 
 
 #   2 p AND q if isleft isright
 #  /  \ 
 # q    p
 

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents = {root: None}
        stk = [root]


        while q not in parents or p not in parents:
            node = stk.pop()

            if node.left:
               parents[node.left] = node
               stk.append(node.left)

            if node.right:
                parents[node.right] = node
                stk.append(node.right) 
        
        ancestor = set()
        while q:
            ancestor.add(q)   
            q = parents[q]
        
        while p not in ancestor:
            p = parents[p]

        return p

            
            


        
     
 
 
 