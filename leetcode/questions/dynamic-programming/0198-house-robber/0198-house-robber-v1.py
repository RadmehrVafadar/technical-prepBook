# Personal notes (preserved)

# # [1, 2, 3, 1]
# #  |

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
