# Personal notes (preserved)

# - Need to explain why going forward we dont need to worry about the intervals before the previous merged interval. (Also dont forget about sorting)

# Initial user implementation:

# Earlier revision (preserved)

# class Solution:
#     def merge(self, intervals: list[list[int]]) -> list[list[int]]:
#
#         # Non-negative starting from 0
#         # Overlap is includve ex [1,3] [3,4] overlap at 3
#         # Atleast one interval
#         # the numbers are int
#         # Can have douplicate invervals (an interval merge on itself)
#         # The list is not sorted
#         # may modify input list
#         res = []
#         intervals.sort()
#         prev_start = 0
#         prev_end = 0
#
#         # [1,4], [4,7]
#         #
#         for start, end in intervals:
#             if start < prev_end:
#                 res.append([prev_start, end])
#             else:
#                 res.append([start, end])
#
#             prev_start = start
#             prev_end = end
#
#         return res

# Final user-submitted implementation:

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
