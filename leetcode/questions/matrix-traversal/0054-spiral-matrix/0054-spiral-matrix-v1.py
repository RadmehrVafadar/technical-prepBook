# Earlier screenshot draft

# Earlier revision (preserved)

# left = 0
# right = len(matrix[0])-1
# top = 0
# bottom = len(matrix)-1
# res = []
# while right <= left and top <= bottom:
#     for value in matrix[top]:
#         res.append(value)
#     top += 1
#     for row in range(top, bottom+1):
#         for value in matrix[right]:
#             res.append(right)
#     right -= 1
#     for value in matrix[bottom::-1]:

# Later partial draft

# Earlier revision (preserved)

# res = []
#         while right <= left and top <= bottom:
#
#             for value in matrix[top][left:right+1]:
#                 res.append(value)
#             top += 1
#
#             for row in range(top, bottom+1):
#                 for value in matrix[right]:
#                     res.append(right)
#             right -= 1
#
#             for value in matrix[bottom][right:left+1:-1]

# Complete user implementation before boundary fixes

# Earlier revision (preserved)

# class Solution:
#     def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
#         left = 0
#         right = len(matrix[0])-1
#         top = 0
#         bottom = len(matrix)-1
#         res = []
#         while left <= right and top <= bottom:
#             for row in range(left, right+1):
#                 res.append(matrix[top][row])
#             top += 1
#             for col in range(top, bottom+1):
#                 res.append(matrix[col][right])
#             right -= 1
#             for row in range(right, left-1, -1):
#                 res.append(matrix[bottom][row])
#             bottom -= 1
#             for col in range(bottom, top-1, -1):
#                 res.append(matrix[col][left])
#             left += 1
#         return res

# Final assisted solution, supplied after your full-solution request

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1
        res = []

        while left <= right and top <= bottom:
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1
            if top > bottom:
                break

            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1
            if right < left:
                break

            for col in range(right, left - 1, -1):
                res.append(matrix[bottom][col])
            bottom -= 1

            for row in range(bottom, top - 1, -1):
                res.append(matrix[row][left])
            left += 1

        return res
