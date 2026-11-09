# You are given a tree with n nodes labeled 0 through n - 1 and a list
# of its undirected edges. Return all node labels that, when chosen as
# the root, give the tree the smallest height.
# Height is the longest distance in edges from the root to a leaf.
#
# n = 4, edges = [[1, 0], [1, 2], [1, 3]] -> [1]
# n = 6, edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]] -> [3, 4]
"""
Questions:
- what is the range of the number n? 1-20,000 (inclusive)
- what is the range of len(edges)? 0-19,999
- what is the maximum number of edges one node may have? atle
- does each node have to have one edge? every node in n > 1 has to have alteast one edge
"""

"""
Approach: (brute force bfs iterative)
How about we go though each edge once?
- for each node we would assume it is the root and do bfs do see how deep it goes and keep track of the of the number of how deep it went
- if we find a smaller tree we would update the track with a new list of the nodes and appen to that list
- otherwise if it euqls the current smallest one we would add to that array

Time: O(n^2)
Space: O(n)


"""