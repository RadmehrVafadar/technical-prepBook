# Earlier revision (preserved)

# class Solution:
#     def coinChange(self, coins: list[int], amount: int) -> int:
#         dp = {}
#         for value in range(amount+1):
#             dp[value] = amount
#
#         dp = {0:0}
#
#         for target in range(amount+1):
#
#             for coin in coins:
#                 if (target-coin) < 0:
#                     continue
#                 dp[target] = min(dp[target], 1 + dp[target-coin])
#
#         return dp[amount] if dp[amount] < amount else -1

# ### Revised submission

# Earlier revision (preserved)

# class Solution:
#     def coinChange(self, coins: list[int], amount: int) -> int:
#         dp = {}
#         for value in range(amount+1):
#             dp[value] = amount
#
#         dp = {0:0}
#
#         for target in range(amount+1):
#             for coin in coins:
#                 if (target-coin) < 0:
#                     continue
#                 dp[target] = min(dp[target], 1 + dp[target-coin])
#
#         return dp[amount] if dp[amount] < amount+1 else -1

# ### Second revised submission

# Earlier revision (preserved)

# class Solution:
#     def coinChange(self, coins: list[int], amount: int) -> int:
#         dp = {}
#         for value in range(amount+1):
#             dp[value] = amount+1
#
#         dp = {0:0}
#
#         for target in range(amount+1):
#             for coin in coins:
#                 if (target-coin) < 0:
#                     continue
#                 dp[target] = min(dp[target], 1 + dp[target-coin])
#
#         return dp[amount] if dp[amount] < amount+1 else -1

# ### Correction reported by user
#
# Replaced `dp = {0:0}` in the second revised submission with `dp[0] = 0`.
#
# ### Final solution

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = {}
        for value in range(amount+1):
            dp[value] = amount+1

        dp[0] = 0

        for target in range(amount+1):
            for coin in coins:
                if (target-coin) < 0:
                    continue
                dp[target] = min(dp[target], 1 + dp[target-coin])

        return dp[amount] if dp[amount] < amount+1 else -1
