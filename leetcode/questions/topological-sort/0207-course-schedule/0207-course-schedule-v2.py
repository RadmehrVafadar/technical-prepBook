# Personal notes (preserved)

# # adj dict

# Earlier revision (preserved)

# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
#         # adj dict
#         adj = {}
#
#         for course in range(numCourses):
#             adj[course] = []
#
#         for c, req in prerequisites:
#             adj[c].append(req)
#
#         def dfs(course, visited):
#             if course in visited:
#                 return False
#
#             if adj[course] == []:
#                 return True
#
#             visited.add(course)
#
#             while adj[course]:
#                 if dfs(adj[course][-1], visited):
#                     adj[course].pop()
#                 else:
#                     return False
#             return True
#         for course in adj:
#             if not dfs(course, set()):
#                 return False
#             else:
#                 adj[course].pop
#
#
#         return True

# ### Revised implementation

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # adj dict
        adj = {}

        for course in range(numCourses):
            adj[course] = []

        for c, req in prerequisites:
            adj[c].append(req)

        def dfs(course, visited):
            if course in visited:
                return False

            if adj[course] == []:
                return True

            visited.add(course)

            for val in adj[course]:
                if not dfs(val, visited):
                    return False

            visited.remove(course)
            adj[course] = []
            return True


        for course in adj:
            if not dfs(course, set()):
                return False
        return True
