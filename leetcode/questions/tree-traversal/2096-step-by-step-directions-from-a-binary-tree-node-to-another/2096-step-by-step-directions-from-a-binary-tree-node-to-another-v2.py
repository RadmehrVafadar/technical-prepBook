# Given a binary tree and the values of two nodes, return the directions
# along the shortest path from the start node to the destination node.
# Use U for parent, L for left child, and R for right child.
#
# root = [5,1,2,3,None,6,4], startValue = 3, destValue = 6 -> "UURL"
#      5
#     1  2
#   3 N  6 4

# root = [2,1], startValue = 2, destValue = 1 -> "L"
"""
Questions:
bst? no
balanced? no
range height(tree)? 2-100,000
range of node.val? 1-n inclusive
duplicates? no

start and dest the same? no

input: root (node), startValue (int), destvalue (int)
output: string

always in the tree? yes
always path? yes
target complexity? no
"""

class Solution:
  def __init__(self, root, startValue, destValue):
    self.root = root
    self.startValue = startValue
    self.destValue = destValue
    self.parent = {root.val:(None, None)}
    
    """
    root = [2, 1]
    startValue = 2, destValue = 1, #ouput: "L"
    parent = {2:(None, None), 1:(2, "L")}
    q = []
    cur = 1
    leftNode = None
    rightNode = None
    
    parent = {2:(None, None), 1:(2, "L")}
    
    path = {2:0}
    couter = 0
    node = 2
    
    dir = ["L"]
    """
  def shortestPath(self):
    parent = self.parent
    self.bfs()
    
    def makeString(num, dir): # 0, ["L"]
      # str = ["L"]
      str = ["U" * num]
      str.extend(dir[::-1])
      return "".join(str)
    
    
    path = {}
    node = self.startValue
    counter = 0
    while node:
      path[node] = counter
      counter += 1
      node = parent[node][0]
    
    dir = []
    
    node = self.destValue
    
    while node:
      if node in path:
        return makeString(path[node], dir)
      dir.append(parent[node][1])
      node = parent[node][0]

        
  
    
    
  def bfs(self):
    root = self.root
    parent = self.parent
    
    q = deque()
    q.append(root)
    while q:
      cur = q.popleft()
      leftNode = cur.left
      rightNode = cur.right
      
      if leftNode:
        q.append(leftNode)
        parent[leftNode.val] = (cur.val, "L")
      
      if rightNode:
        q.append(rightNode)
        parent[rightNode.val] = (cur.val, "R")
        
    
        
      