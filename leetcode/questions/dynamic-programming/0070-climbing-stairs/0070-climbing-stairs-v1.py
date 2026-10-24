# Personal notes (preserved)

# # n = 4
# # memoization = {2: 2}
# # [1, 1, 1, 1]

# ### Initial attempt

# Earlier revision (preserved)

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         memoization = {}
#         def numWays(n):
#             if n == 1:
#                 return 1
#             elif n == 2:
#                 return 2
#
#             if (n-1) in memoization:
#                 stepBefore = memoization[n-1]
#             else:
#                 stepBefore = numWays(n-1)
#
#             if (n-2) in memoization:
#                 twoBefore = memoization[n-2]
#             else:
#                 twoBefore = numWays(n-2)
#
#
#             return stepBefore + twoBefore
#
#         return numWays(n)

# ### Revised attempt

# Earlier revision (preserved)

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         memoization = {}
#         def numWays(n):
#             if n == 1:
#                 return 1
#             elif n == 2:
#                 return 2
#
#             if (n-1) in memoization:
#                 stepBefore = memoization[n-1]
#             else:
#                 stepBefore = numWays(n-1)
#                 memoization[n-1] = stepBefore
#
#             if (n-2) in memoization:
#                 twoBefore = memoization[n-2]
#             else:
#                 twoBefore = numWays(n-2)
#                 memoization[n-2] = twoBefore
#
#
#             return stepBefore + twoBefore
#
#         return numWays(n)

# ### Bottom-up attempt

class Solution:
    def climbStairs(self, n: int) -> int:
        # n = 4
        # memoization = {2: 2}
        # [1, 1, 1, 1]

        def numWays(n):
            if n == 1:
                return 1
            elif n == 2:
                return 2

            ways = [0] * (n + 1)
            ways[1] = 1
            ways[2] = 2
            for i in range(3, n+1):
                ways[i] = ways[i - 1] + ways[i - 2]

            return ways[n]
        return numWays(n)
