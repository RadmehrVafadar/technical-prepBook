- Confidence: 4/5
- Result: can get with hint
- Workon: Give a concise correctness argument using a precise definition of the stored best total.

# 198. House Robber

## Users Own notes

```python
# [1, 2, 3, 1]
#  | 
```

## Code

```python
class Solution:
    def rob(self, nums: list[int]) -> int:
        # [1, 2, 3, 1]
        #  | 



        n = len(nums)
        
        if n == 1:
            return nums[0]

        dp = [0] * (n)

        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if (i-2) < 0:
                dp[i] = max(nums[i], dp[i-1])
            else:
                dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[-1]
```

## Session summary

- Attempt started October 12, 2026 at 1:42:48 PM EDT (America/Toronto).
- You shared the problem screenshot with Python 3 selected and no implementation yet.
- You described the input as cash amounts indexed by house and the output as the maximum total from nonadjacent houses. You noted that the array is not sorted and does not need to be modified.
- You said you would choose "every other section"; the coach asked whether this meant exactly alternating houses or allowing larger gaps.
- You clarified that larger gaps are allowed and that only adjacent houses cannot both be chosen on the same night.
- You independently proposed scanning left to right, storing the maximum obtainable total through each position, and comparing the previous position's maximum with the current value plus the maximum from two positions earlier. You walked through the first positions of the screenshot's example.
- You estimated O(n) time from computing and storing each position once and O(n) space for storing all position results. You called this memoization and asked whether to proceed to coding.
- Asked why the comparison covers all valid possibilities, you described two choices: taking the current house or discarding it and using the previous maximum. Your wording sometimes equated the previous maximum with taking the adjacent house; the coach asked you to distinguish these meanings.
- You initially said the previous best must include that house, then immediately corrected yourself: it can come from a selection that skips that house if skipping gives the maximum.
- You submitted a Python implementation with a single-house return, an array of stored totals, separate handling for the second house, and the proposed comparison for later positions.
- You verbally dry-ran [2, 1, 1, 2], obtaining stored totals [2, 2, 3, 4] and a final answer of 4. You explained the comparisons and second-house boundary, and reported that the dry run worked. You did not explicitly identify the selected houses.
- You correctly explained O(n) time for visiting each position once and O(n) auxiliary space for the stored totals. Your explanation of correctness emphasized keeping the maximum through each position, but remained lengthy and sometimes called a stored total a house's value.
- For the space-reduction variation, you proposed replacing processed input values with their best totals. You explained that a house's original value is no longer needed after its comparison and identified dependence on the previous two results. You correctly claimed O(n) time and O(1) auxiliary space for this input-mutating approach; no variation code was submitted.
- When asked to preserve the input, you proposed variables for the previous two best totals and the new result, then shifting the previous best into the two-positions-back role and the new result into the previous-best role. The coach asked how to avoid losing the old previous best while updating.
- You proposed preserving a needed value in a temporary variable, completing the calculations, and then shifting the stored totals before continuing. This addressed the update-order concern conceptually; no optimized code was submitted.

## Feedback

**Advance this person to the next round?**
Yes.

For an internship mock interview, you demonstrated a working solution, independently derived the main comparison, and correctly dry-ran it. Your state definition needed clarification. This is a mock recommendation, not a prediction of a company's hiring decision.

**Technical: 3 out of 4.**
You completed a working solution for nonempty inputs, with no unresolved defect identified in that domain. Your initialization and second-house handling are correct. You accurately explained O(n) time and O(n) auxiliary space. Your reported dry run was correct; broader boundary testing was not demonstrated.

**Problem solving: 3 out of 4.**
You independently derived the comparison between skipping the current house and taking it with the best total from two positions earlier. You correctly allowed larger gaps. A targeted question helped you distinguish the best total through a position from a selection that must include that house. Your take-or-skip justification was sound, but the precise state meaning needed prompting.

**Communication: 3 out of 4.**
Your approach and dry run were understandable, and you explained both complexity costs. Calling stored totals a house's value sometimes obscured the meaning; you clarified it when questioned. Use a precise state definition to make the same explanation shorter.

**Things you did well:**

- You derived the main comparison before coding, which gave your implementation a clear plan.
- You corrected your claim about whether the previous best must include the previous house.
- You traced the boundary and later comparisons accurately in your verbal dry run.

**Areas of improvement:**

- State meaning: distinguish a house's cash from the best total using houses through that position.
- Correctness: explain why every valid selection either takes or skips the current house, and why each branch uses the best compatible earlier total.
- Testing: demonstrate a smallest-input check and a case where skipping is optimal, rather than relying on one walkthrough.

**My advice:**

- Highest priority: define the stored quantity in one sentence before explaining the comparison.
- On your next attempt, give the two-case justification without referring to a stored total as a single house.
- Before declaring completion, predict and dry-run a smallest input and one case where the current house is skipped.

