- Confidence: 3/5
- Result: can get with hint
- Workon: State the retained-sum invariant and count total pointer movements before coding.

# 53. Maximum Subarray

## Users Own notes

## Code

```python
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # [-2, 1, -3, 4, 2, 1, -5, 4]
        max_sum = float('-inf')
        cur_sum = 0
        left = 0
        for right in range(len(nums)):
            cur_sum += nums[right]

            max_sum = max(max_sum, cur_sum)
            while cur_sum < 0:
                cur_sum -= nums[left]
                left += 1

        return max_sum
```

## Session summary

1. Restated the largest-subarray-sum task and identified negative values as the complication; later corrected the assumption that an empty subarray was allowed.
2. Independently compared cubic recomputation with quadratic running-sum enumeration, both using constant auxiliary space without constructing subarrays.
3. Noted that sorting changes contiguity and derived that a negative accumulated prefix cannot help future extensions.
4. Initially mixed resetting a negative sum with resetting below the global maximum; after questions, specified discarding a negative running sum.
5. Initialized the maximum to negative infinity and explained updating it before discarding negative values.
6. Verbally traced [-1,-4], tracking cur_sum = 0 after each iteration, max_sum = -1, and left advancing to 2.
7. Submitted code; initially called the nested loops quadratic, then concluded linear time after questions about total pointer movement.
8. Reported running the code successfully; specific executed inputs were not supplied.

## Feedback

**Advance this person to the next round?**

No. For an intern-level screen, you found a plausible linear approach and wrote a coherent implementation, but needed repeated interviewer prompts to establish the loop bound and later reported successful execution; specific test coverage was not supplied.

**Technical: 3 out of 4.**

You supplied a compact Python implementation with O(1) state, initialized the answer to negative infinity, correctly dry-ran [-1,-4], and later reported that you ran the code successfully. Your complexity analysis needed substantial prompting.

Correctness and complexity recorded:

User reasoned that a negative running prefix cannot improve any future subarray and should be discarded, and that max_sum must be updated before discarding it to preserve all-negative candidates. This was directionally sound, though the invariant was not stated precisely and took interviewer prompting.
Time complexity: O(n), because the right pointer and left pointer each advance at most n times total. User reached this conclusion after interviewer questions; initially misclassified nested loops as O(n^2).
Auxiliary-space complexity: O(1), using scalar state and indices.

**Problem solving: 2 out of 4.**

You independently moved from cubic to quadratic enumeration, identified the cost of recomputing sums, derived the negative-prefix discard idea, and recognized the all-negative initialization issue. The reset rule and O(n) aggregate analysis required multiple focused questions; the proof stayed informal.

**Communication: 2 out of 4.**

Your initial restatement and all-negative dry run were understandable. During approach selection, the explanation became repetitive and mixed competing reset rules; the complexity explanation treated loop nesting as multiplicative even after noting each pointer advances at most n times. You eventually corrected the conclusion.

**Things you did well:**

- You stated that the answer can be negative and corrected the maximum initialization to negative infinity.
- You noticed repeated work in the quadratic baseline and proposed retaining a running sum.
- You used a future large positive value to reason that a positive current sum should not be discarded merely because it is below the best sum so far.
- Your verbal dry run of [-1,-4] returned -1 and tracked left reaching 2.

**Areas of improvement:**

- Correctness: State the invariant before coding. Explain that the retained running sum is a useful suffix candidate and that a negative prefix cannot improve any extension. You initially described resetting based on comparison with the global maximum, which would not be the right criterion.
- Complexity: Do not infer O(n^2) from a loop nested inside another loop automatically. Count total pointer movements; here each pointer advances at most n times.
- Testing: You dry-ran one all-negative input and reported successful execution. Specific coverage of the visible example, a single element, and an all-positive case was not supplied.
- Communication: Reduce repeated restatement. Give the rule, one reason it is safe, then the complexity argument.

**My advice:**

Highest priority for your next attempt: before coding, state one sentence for the invariant and one sentence bounding total pointer movement. Then test one all-negative case and one mixed-sign case by hand. For this code, predict the return value on [-2,1,-3,4,2,1,-5,4] and explain why the inner while loop does not make the total runtime quadratic.
