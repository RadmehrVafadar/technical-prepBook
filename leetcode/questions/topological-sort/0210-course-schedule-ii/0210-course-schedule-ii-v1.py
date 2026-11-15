# Given a course count and prerequisite pairs [a, b], course b must be
# completed before course a. Return a valid order for taking all courses.
#
# numCourses = 2, prerequisites = [[1, 0]] -> [0, 1]
# numCourses = 4, prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]] -> [0, 1, 2, 3]
"""
Questions:
input: 2D list of ints
output: list of ints


will be always valid? [] if impossible to finish
range of numCourses? 1-2,000 (inclusive)
range of prerequisites? 0-numCourses-1
target complexity? no
multiple prepreqs per course? yes
"""


"""
Approach ( adj list and result list adding to result when removing from adj):
Time: O(numCourses + prerequesites)
Space: O(numCourse + prerequisites)

"""


class Solution:
  def courseScheduleII(self, numCourses, prerequisites):
    
    #create adj hashmap
    dependants = {}
    edges = [0] * numCourses
    
    for crs, req in prerequisites:
      if req in dependants:
        dependants[req].append(crs)
        edges[crs] += 1
      else:
        dependants[req] = [crs]
        edges[crs] += 1
    
    q = deque()
    
    for crs in range(numCourses):
      if edges[crs] == 0:
        q.append(crs)
      
    res = []
    
    while q:
      course = q.popleft()
      res.appedn(course)
      
      if dependats[course]:
        for neighbor in dependants[course]:
          edges[neighbor] -= 1
        
          if edges[neighbor] == 0:
            q.append(neighbor)
    
    return res if len(res) == numCourses else []
      
# Time: O(V + E) numCourses + prerequisites
# Space:  O(V + E)numCourses + prerequisites
      
    
    
    
    