- Confidence: 1/5
- Result: incorrect
- Workon: Check that the initial best sum allows an all-negative input to return its best valid range.

# Maximum subarray sum with equal endpoints

## Code

[Python working file](maximum-subarray-sum-with-equal-endpoints-v1.py)

## Session summary

1. Tracking began November 20, 2026 at 8:39 AM EST (America/Toronto).
   The interview start was not captured.
2. In Google Round 2, clarified that the input is a nonempty, unsorted integer list that may contain duplicates and negative values, and that a singleton counts once.
3. Considered an `O(n^3)` baseline, then wrote an `O(n^2)` time and `O(n)` space solution using prefix sums and a scan over matching endpoint pairs.
4. Sketched grouping indices by value in a hash map.

## Feedback
