# Given the root of a binary tree with unique node values, a start value,
# and a destination value, return a string of directions along the shortest
# path from the start node to the destination node.
# Use L for left child, R for right child, and U for parent.
#
# Trees below are shown in level order.
# root = [5, 1, 2, 3, None, 6, 4], start = 3, destination = 6 -> "UURL"
# root = [2, 1], start = 1, destination = 2 -> "U"





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
  def shortestPath(self, root, start, destination):
      parents = self.dfs_createParentsHashmap(root)
      # root = [5, 1, 2, 3, None, 6, 4], start = 3, destination = 6 -> "UURL"
      # parents =  {5:(None,None), 1:(5,"L"), 2:(5,"R"), 6:(2, "L"), 4:(2, "R"), 3:(1, "L")}
      # start = None
      # destination = 5
      # dist = 3
      # path = {3:0, 1:1, 5:2}
      # directions = ["L", "R"]
      # return "UU" + "RL" = "UURL"



      # root = [2, 1], start = 1, destination = 2 -> "U"
      # parents = {2:(None, None), 1:(2,"L")}
      # start = 2
      # destination = 2
      # path = {1:0, 2:1}
      # dist = 1
      # directions = []
      # return "U"
      

      path = {}
      directions = []
      dist = 0
      
      while start:
        path[start] = dist
        if destination in path:
          return "U"*dist
        
        start = parents[start][0]
        dist += 1
      
      while destination:
        if destination in path:
          return "U"*path[destination] + "".join(directions[::-1])
        
        directions.append(parents[destination][1])
        destination = parents[destination][0]
      
  def dfs_createParentsHashmap(self, root):
    parents = {root.val:(None, None)}
    
    stk = [root]
    # root = [5, 1, 2, 3, None, 6, 4], start = 3, destination = 6 -> "UURL"
    # parent {5:(None,None), 1:(5,"L"), 2:(5,"R"), 6:(2, "L"), 4:(2, "R"), 3:(1, "L")}
    # stk = []
    while stk:
      node = stk.pop()
      
      if node.left:
        stk.append(node.left)
        parents[node.left.val] = (node.val, "L")
      
      if node.right:
        stk.append(node.right)
        parents[node.right.val] = (node.val, "R")
    
    return parents
      
     

        
        

        
      
      
  










