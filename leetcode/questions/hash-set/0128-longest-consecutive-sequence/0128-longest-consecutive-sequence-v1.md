- Confidence: 3/5
- Result: can get with hint
- Workon: Justify total loop work precisely by separating successful removals from constant-cost repeated starts.

# 128. Longest Consecutive Sequence

## Users Own notes

## Code

```python
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        res = 0
        numSet = set()
        for num in nums:
            numSet.add(num)

        for num in nums:
            if num not in numSet:
                continue

            tempLen = 1

            l = num-1
            while l in numSet:
                tempLen += 1
                numSet.remove(l)
                l -= 1

            r = num+1
            while r in numSet:
                tempLen += 1
                numSet.remove(r)
                r += 1

            res = max(res, tempLen)
        return res
```

## Session summary

- Attempt started: October 20, 2026 at 7:05:26 PM EDT (America/Toronto).
- You shared the problem statement and an empty Python 3 method stub.
- You explained that the result is the length of the longest sequence of values increasing by one, with a list of integers as input and an integer as output. You identified empty input and negative values as cases to handle, and ruled out sorting because of the required O(n) time.
- You asked what [0, 0] returns; the coach clarified that duplicates do not extend a sequence and the result is 1.
- You proposed sorting as a baseline, scanning with a current count, skipping duplicate values, and resetting at gaps. You would compare the current count with the maximum before each reset and return the largest count.
- After the coach asked how a final sequence would be captured when no reset occurs, you revised the plan to compare against the stored maximum whenever you update the current count.
- You gave O(n log n) time and O(1) space for the baseline. The coach confirmed the time and explained that Python's list.sort() can require O(n) auxiliary space.
- When asked what sorting helps discover, you answered, "The order of consecutiveness."
- When asked what to check without sorting to see whether a sequence continues from x, you suggested checking whether there is a larger or smaller value.
- With a follow-up asking how much larger or smaller, you specified a difference of plus or minus 1.
- When asked which data structure supports O(1) average membership checks, you proposed a set or hash map.
- You proposed building a set of nums and using DFS to explore neighbors differing by 1, count each connected sequence, and retain the largest length. You described removing a value once exploration cannot continue in either direction, reasoning that its connected sequence cannot later belong to a longer one and that a set handles duplicates. You claimed O(n) time because values are traversed once and O(n) space for the set.
- After the coach questioned whether exploring both neighbors would revisit the parent, you clarified that you expand left and right from a starting value, with each branch continuing only in its own direction. You explained that starting anywhere within a sequence gives the same total length and proposed counting the recursive calls.
- You clarified that you would iterate over the original list, check whether each value remains in the set, and skip values that have already been removed.
- When asked about recursion on a sequence of 100,000 values, you recognized the risk of exceeding Python's recursion capacity and chose to implement the traversal iteratively for long sequences.
- You submitted an iterative implementation that expands left and right using numeric values and removes each neighbor it counts. You observed that this resembles a two-pointer approach rather than DFS. The starting value remains in the set in your submitted code.
- Asked to justify O(n) total work including duplicates, you explained that visited values are skipped and therefore each value is visited once. The coach asked you to reconcile that claim with the starting value remaining in the set.
- For the coach's example [2, 1, 3, 2], you explained that processing the repeated starting value cannot exceed the sequence length already recorded, so the result stays correct. You acknowledged leaving the start in the set and maintained that the extra processing still permits O(n) total time.
- You selected empty nums with expected result 0 and [1, 1, -1, 2] with expected result 2 as edge cases. These were predicted results, not reported execution results.

## Feedback

**Advance this person to the next round?**
Yes, narrowly, for an internship mock interview. You completed a correct solution and explained why counting and excluding a whole connected sequence is safe. Targeted questions helped you reach set membership and refine your complexity argument.

**Technical: 3 out of 4.**
You completed a working iterative solution with expected O(n) time and O(n) auxiliary space. No unresolved correctness defect was identified. Leaving the starting value in the set adds unnecessary constant-cost processing for duplicate starts, without changing correctness or asymptotic complexity. You predicted correct results for empty input and a case combining duplicates, a negative value, and a gap. You initially understated Python sorting space and recognized recursion limits after prompting.

**Problem solving: 3 out of 4.**
You established a sorting baseline and developed bidirectional expansion with removal. Questions guided you from sorting toward exact-neighbor membership and a suitable data structure. You justified excluding a counted sequence and correctly defended the implementation when a starting value remained. Your initial claim that every value is visited once was too broad; distinguish outer iterations from successful inner-loop removals.

**Communication: 3 out of 4.**
Your clarification of fixed-direction expansion resolved the coach's concern about revisiting a parent. You explained why a repeated starting value cannot improve the answer. Earlier descriptions of larger or smaller values and visiting once needed precision, but your revisions made the reasoning understandable.

**Things you did well:**

- You handled duplicates explicitly in both your baseline and set-based approach.
- You adapted recursion into iterative expansion and produced correct code.
- You defended correctness using the relationship between an isolated remaining start and its previously counted sequence.

**Areas of improvement:**

- Your first complexity justification did not match the implementation: starting values can be processed repeatedly. Bound each kind of work separately.
- Your baseline maximum update initially missed a sequence ending at the array boundary; a targeted question led you to update the maximum with the count.
- Your initial O(1) sorting-space claim overlooked Python's implementation costs.

**My advice:**

- Highest priority: before declaring linear time, identify what each successful inner iteration consumes and bound unsuccessful checks separately.
- On your next attempt, choose one boundary case before coding and trace the final update explicitly.
- Review Python sorting's auxiliary-space cost and recursion-depth limits.
