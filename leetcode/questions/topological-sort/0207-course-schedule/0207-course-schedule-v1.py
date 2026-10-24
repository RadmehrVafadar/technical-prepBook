# Personal notes (preserved)

# Revisit this problem and learn other approaches.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visited = set()
        def dfs(crs):
            if preMap[crs] == []:
                return True
            if crs in visited:
                return False

            visited.add(crs)
            for i in range(len(preMap[crs])):
                if not dfs(preMap[crs][i]): return False

            visited.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
