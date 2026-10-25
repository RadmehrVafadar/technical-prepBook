# Personal notes (preserved)

# # atleast one pile
# # atleast as many hours as piles
# # piles are NOT sorted
# # you can modify the input
# # [3, 6, 7, 11] h = 8
# #           |
# # l = 3
# # r = 5
# # rate = 4
# # time = 1 + 2 + 2 + 3

# Earlier revision (preserved)

# class Solution:
#     def minEatingSpeed(self, piles: list[int], h: int) -> int:
#         # atleast one pile
#         # atleast as many hours as piles
#         # piles are NOT sorted
#         # you can modify the input
#
#         # [3, 6, 7, 11] h = 8
#         max_n = 0
#         for num in piles:
#             max_n = max(max_n, num)
#
#         l = 1
#         r = max_n
#
#         while l < r:
#             eating_rate = l + (r-l)
#             time = 0
#
#             for pile in piles:
#                 time += ceil(pile/eating_rate)
#
#                 if time > h:
#                     l += eating_rate + 1
#                 elif time <= h:
#                     r -= eating_rate - 1
#
#         return eating_rate

# Latest submitted version:

# Earlier revision (preserved)

# lass Solution:
#     def minEatingSpeed(self, piles: list[int], h: int) -> int:
#         # atleast one pile
#         # atleast as many hours as piles
#         # piles are NOT sorted
#         # you can modify the input
#
#         # [3, 6, 7, 11] h = 8
#         #           |
#         # l = 3
#         # r = 5
#         # rate = 4
#         # time = 1 + 2 + 2 + 3
#
#         max_n = 0
#         for num in piles:
#             max_n = max(max_n, num)
#
#         l = 1
#         r = max_n
#         res = max_n
#
#         while l < r:
#             eating_rate = l + ( (r-l) // 2 )
#             time = 0
#
#             for pile in piles:
#                 if time > h:
#                     break
#                 time += ceil(pile/eating_rate)
#
#             if time > h:
#                 l += eating_rate + 1
#             elif time <= h:
#                 res = min(eating_rate, res)
#                 r -= eating_rate - 1
#
#         return eating_rate

# Revised boundary assignments:

# Earlier revision (preserved)

# class Solution:
#     def minEatingSpeed(self, piles: list[int], h: int) -> int:
#         # atleast one pile
#         # atleast as many hours as piles
#         # piles are NOT sorted
#         # you can modify the input
#
#         # [3, 6, 7, 11] h = 8
#         #           |
#         # l = 3
#         # r = 5
#         # rate = 4
#         # time = 1 + 2 + 2 + 3
#
#         max_n = 0
#         for num in piles:
#             max_n = max(max_n, num)
#
#         l = 1
#         r = max_n
#         res = max_n
#
#         while l < r:
#             eating_rate = l + ( (r-l) // 2 )
#             time = 0
#
#             for pile in piles:
#                 if time > h:
#                     break
#                 time += ceil(pile/eating_rate)
#
#             if time > h:
#                 l = eating_rate + 1
#             elif time <= h:
#                 res = min(eating_rate, res)
#                 r = eating_rate - 1
#
#         return res

# Final revision after the boundary hint:

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # atleast one pile
        # atleast as many hours as piles
        # piles are NOT sorted
        # you can modify the input

        # [3, 6, 7, 11] h = 8
        #           |
        # l = 3
        # r = 5
        # rate = 4
        # time = 1 + 2 + 2 + 3

        max_n = 0
        for num in piles:
            max_n = max(max_n, num)

        l = 1
        r = max_n
        res = max_n

        while l <= r:
            eating_rate = l + ( (r-l) // 2 )
            time = 0

            for pile in piles:
                if time > h:
                    break
                time += ceil(pile/eating_rate)

            if time > h:
                l = eating_rate + 1
            elif time <= h:
                res = min(eating_rate, res)
                r = eating_rate - 1

        return res
