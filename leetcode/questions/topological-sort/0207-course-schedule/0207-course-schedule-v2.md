- Confidence: 3/5
- Result: need review
- Workon: Trace shared mutable state and early returns precisely, then justify complexity by counting total work.

# 207. Course Schedule

## Users Own notes

```python
# adj dict
```

## Code

```python
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

            while adj[course]:
                if dfs(adj[course][-1], visited):
                    adj[course].pop()
                else:
                    return False
            return True
        for course in adj:
            if not dfs(course, set()):
                return False
            else:
                adj[course].pop
        
        
        return True
```

### Revised implementation

```python
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
```

## Session summary


- Attempt started: October 19, 2026 at 5:07:36 PM EDT (America/Toronto).
- Shared the Course Schedule problem with an empty Python 3 method stub.
- Requested interview mode before beginning the explanation or solution work.
- Explained that each pair contains a course followed by its prerequisite, and that the result indicates whether all courses can be completed.
- Independently identified a cycle anywhere in the prerequisites as preventing completion, using two mutually dependent courses as an example.
- Said that "the numCourses number itself will never be larger then course numbers"; the intended meaning of this statement has not yet been clarified.
- Interviewer clarified that numCourses is the total count and valid labels range from 0 to numCourses - 1.
- Proposed traversing courses and detecting when a course requires itself somewhere in the search; traversal state and the precise detection condition have not yet been specified.
- Described starting at course 0, following its prerequisite 1 and further prerequisites, and returning False if course 0 is encountered again.
- Proposed an adjacency dictionary, saying the course would be the value and its prerequisite list the key; the intended mapping needs clarification.
- Proposed removing a prerequisite from the original course's requirements when that prerequisite reaches an empty requirement list, then processing remaining prerequisites.
- Proposed adding the course being searched to a visited set and returning False if a requirement is already in that set. Has not yet specified when courses leave the set.
- Clarified that visited means a course has been seen during the current starting course's prerequisite search. Would keep entries throughout that search and reset the set for each new starting course in the adjacency dictionary.
- Submitted a Python implementation using course-to-prerequisite lists, recursive searches, destructive removal of completed prerequisites, and a fresh visited set per starting course.
- Proposed cases with numCourses = 1 and prerequisites written as [[0:1][1:0]] and [[0:1]]. Both refer to course 1, outside the valid label range for that count; no predicted results or dry runs provided yet.
- Corrected the intended numCourses to 2 for both proposed cases after the interviewer pointed out the label range.
- Submitted a revision that iterates over prerequisites, removes the current course from visited after successful exploration, and clears its prerequisite list. No explanation of the revision or test results supplied yet.
- Explained that leaving a completed prerequisite in visited could cause a later prerequisite branch to be mistaken for a cycle when the original course depends on both. Removes completed courses to avoid that false detection.
- Explained that after all prerequisites succeed, the course can be taken; clearing its list represents that established result and is safe when other courses depend on it.
- Shared a LeetCode screenshot showing the submitted solution was accepted, with 54/54 test cases passed.
- Estimated space as O(numCourses^2), reasoning that each dictionary entry could hold up to numCourses prerequisites. Estimated time as O(numCourses * log req) for adjacency construction and traversing prerequisites; has not justified the logarithmic factor or accounted explicitly for recursion space.
- Initially attributed the logarithmic factor to DFS. When asked to justify it by counting prerequisite processing, revised "log req" to "req"; the total-work bound still needs clarification.
- Said each prerequisite list is counted "atleast once" when asked for its total exploration count; has not established an upper bound yet.
- Proposed numCourses as the maximum number of full explorations of a course's prerequisite list, without justification yet.
- Offered numCourses = 3 with pairs [0, 1], [0, 2], and [0, 0], discussed the number of adjacent courses, and revised the claim to "linear." Has not yet distinguished list length from repeated full exploration or specified what input quantity the linear bound uses.
- Said course 0's prerequisite list would be explored twice for that example. Wrote the call sequence as d(0, set()) -> d(1, (0)) -> d(2, (0,1)).
- When asked about dfs(1, {0}) with an empty prerequisite list, correctly said it returns True but said visited would then contain nothing. Tracking shared set contents and early returns remains unresolved.
- Pointed to line 26 when asked where 0 would be removed. Acknowledged that dfs(1, {0}) returns before the removal line, but still answered [] for visited afterward.
- Finally stated O(V + E) time and O(V + E) space. Explained that clearing completed prerequisite lists prevents repeated exploration and that the adjacency dictionary stores courses and prerequisite edges. Did not explicitly account for recursion or visited-set space despite being asked.

## Feedback

**Advance this person to the next round?**
No.

For this intern mock interview, you completed a working solution, but your dry run and complexity reasoning were not reliable enough to support advancing on this session. This is a mock-interview recommendation, not a prediction of a company's hiring decision.

**Technical: 2 out of 4.**
Your revised Python solution works, and you reported an accepted submission. No unresolved defect is apparent in that revision. Your first implementation could falsely detect a cycle after revisiting a completed shared prerequisite; you independently revised it to remove completed courses from visited. However, you could not accurately trace the shared set through an early return. Your final O(V + E) bounds are correct, but required repeated questioning; you omitted the O(V) recursion stack and visited set from your explanation. Your proposed testing covered a cycle and a simple dependency, but you did not complete an accurate dry run.

**Problem solving: 3 out of 4.**
You independently reduced the problem to cycle detection and developed the recursive approach. You explained why completed branches leave visited and why clearing a successfully explored prerequisite list is safe. No algorithmic solution was supplied. Your main gap was connecting those explanations to exact execution and an upper bound on total work.

**Communication: 2 out of 4.**
Your explanations of shared prerequisites and completed-course caching were understandable. Earlier, you reversed dictionary keys and values verbally, gave an invalid course count, and used "at least once" when asked for an upper bound. Several short answers did not include the requested justification, making your reasoning difficult to verify.

**Things you did well:**

- Identified that a cycle anywhere prevents finishing all courses.
- Revised the implementation without receiving replacement code or an algorithmic hint.
- Explained why a course proven completable remains safe for later dependents.

**Areas of improvement:**

- Trace actual execution rather than expected behavior. dfs(1, {0}) returns immediately on its empty list, so visited remains {0}; it neither adds 1 nor removes 0.
- Derive bounds from total operations. A DFS is not inherently logarithmic, and calling it from every course does not imply fully exploring every list repeatedly.
- Include all auxiliary storage: adjacency O(V + E), active-search set O(V), and recursion stack O(V).

**My advice:**

- Highest priority: trace one branching graph using columns for current call, visited, adjacency changes, and return value. Predict each change before moving to the next statement.
- For your next three graph attempts, justify complexity by separately counting expanded vertices, processed edges, and maximum call depth.
- Choose tests for no prerequisites, a self-cycle, disconnected components, and shared prerequisites; state expected results before tracing.
