# Personal notes (preserved)

# # 2
# # adj = [1:[0], 0:[]]
# # dfs(1, set()) -> dfs(1, ())

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        adj = {value:[] for value in range(numCourses)}


        for c, req in prerequisites:
            adj[c].append(req)


        # 2
        # adj = [1:[0], 0:[]]
        # dfs(1, set()) -> dfs(1, ())
        def dfs(course, visited):
            if adj[course] == []:
                return True
            if course in visited:
                return False

            visited.add(course)

            for c in adj[course]:
                if not dfs(c, visited):
                    return False

            visited.remove(course)
            adj[course] = []
            return True



        for value in adj:
            if not dfs(value, set()):
                return False
        return True
