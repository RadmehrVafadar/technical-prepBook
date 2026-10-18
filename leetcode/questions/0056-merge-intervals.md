- Confidence: 3/5
- Result: can get with hint
- Workon: Explain why the stored interval remains correct after containment, extension, and separation, and distinguish output from auxiliary space.

# 56. Merge Intervals

## Users Own notes

- Need to explain why going forward we dont need to worry about the intervals before the previous merged interval. (Also dont forget about sorting)

## Code

Initial user implementation:

```python
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        # Non-negative starting from 0
        # Overlap is includve ex [1,3] [3,4] overlap at 3
        # Atleast one interval
        # the numbers are int
        # Can have douplicate invervals (an interval merge on itself)
        # The list is not sorted
        # may modify input list
        res = []
        intervals.sort()
        prev_start = 0 
        prev_end = 0

        # [1,4], [4,7]
        #  
        for start, end in intervals:
            if start < prev_end:
                res.append([prev_start, end])
            else:
                res.append([start, end])
            
            prev_start = start
            prev_end = end

        return res
```

Final user-submitted implementation:

```python
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        # Non-negative starting from 0
        # Overlap is includve ex [1,3] [3,4] overlap at 3
        # Atleast one interval
        # the numbers are int
        # Can have douplicate invervals (an interval merge on itself)
        # The list is not sorted
        # may modify input list
        res = []
        intervals.sort()
        prev_start = -1
        prev_end = -1

        # [0,2], [1,4], [3, 5]
        #    pe   s e 
        # res = [0,4],  
        # 
        # prev_start = 0
        # prev_end = 2

        for start, end in intervals:
            if start <= prev_end:
                if res:
                    res.pop()
                if prev_end > end:
                    res.append([prev_start, prev_end])

                else:
                    res.append([prev_start, end])
                    prev_end = end
            else:
                res.append([start, end])
                prev_start = start
                prev_end = end

        return res
```

## Session summary

1. In coaching, proposed comparing intervals while scanning. On [8,10], [1,3], recognized that this fails for unsorted input. The coach then supplied sorting by start as the fix.
2. Restarted as a mock interview. Clarified the list-of-lists input, integer endpoints, unsorted order, inclusive overlap, possible duplicates, nonnegative values, nonempty input, and permission to modify the list.
3. Proposed sorting by start and scanning. Initially described overlap using strict inequality, then changed to inclusive comparison in the submitted code.
4. The first implementation appended [1,3] prematurely. The user reported output [[1,3],[1,6],[8,10],[15,18]] instead of [[1,6],[8,10],[15,18]] and identified the extra interval during debugging.
5. In a dry run of [0,2], [1,4], [3,5], recognized that the stored end must update when a merge extends the interval. Submitted the final code above and reported that it passes.
6. Initially gave O(n) time for the scan; after a question about sorting, corrected the total to O(n log n). Gave O(n) space based on the worst-case output size without separating auxiliary sorting space.
7. Explained that the code detects an overlap, removes the previous result interval, and adds the merged one. The final explanation did not justify why sorted order makes comparison with only the most recent merged interval sufficient.
8. On the transfer question [1,10], [2,3], correctly said the stored end remains 10 because [2,3] lies inside [1,10]. Asked what a state variable means and confirmed that explaining the roles of `prev_start` and `prev_end` while coding would help.
9. After the write-up, tried to justify comparing only with the most recent merged interval using sorted starts, but did not yet explain why the new interval cannot overlap an earlier completed interval. Requested a clearer interview-ready phrasing.

## Feedback

**Advance this person to the next round?**

No. For an intern-level mock, you produced a plausible working solution and independently debugged the extra interval, but the sorting insight came from earlier coaching and the final correctness explanation remained incomplete. This is a mock recommendation, not a hiring prediction.

**Technical: 3 out of 4.**

You submitted a complete Python implementation and reported that it passed. You revised the overlap check to include touching endpoints and handled a contained interval by retaining the larger end. You initially omitted sorting from runtime, then corrected the total to O(n log n) after a question. Your O(n) space claim counts the output; sorting workspace was not discussed. No unresolved defect has been established for the submitted final code.

**Problem solving: 2 out of 4.**

You clarified input shape, sortedness, endpoint behavior, duplicates, and nonempty input. You noticed the unsorted-input problem after a counterexample, but the fix of sorting by start was supplied in earlier coaching. You independently diagnosed premature appending and later the stale previous-end state. The final explanation said all overlaps are merged, but did not justify why comparing only with the most recent merged interval finds every overlap.

**Communication: 2 out of 4.**

Your examples made the intended scan understandable, and you identified the extra [1,3] in the reported output. The description of previous start, previous end, and result changed while coding; your final correctness argument repeated the procedure instead of explaining why the procedure covers every case.

**Things you did well:**

- Asked precise questions about sortedness and touching endpoints before planning.
- Used the reported extra [1,3] to locate premature appending.
- Dry-ran [0,2], [1,4], [3,5] and recognized that previous end must change after extending a merge.

**Areas of improvement:**

- State what previous start and previous end represent after each iteration. This would have made the stale-state error easier to catch before running code.
- Explain why sorted starts let you compare the next interval only with the most recent merged interval. Saying that all overlaps are merged states the desired outcome without proving this step.
- Include preparation work when analyzing time and separate result storage from auxiliary workspace.

**My advice:**

- Highest priority: explain the sorted-scan invariant in two sentences, then use it to justify both the overlap and nonoverlap branches.
- Revisit the implementation without notes and walk through touching, containment, and a gap while stating the stored interval after each step.
