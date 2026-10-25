# Personal notes (preserved)

# # [-1, -1, 2, 2, 0]
# # [-1, -1, 2]
#
# # [-1, -1, 0, 2, 2]
# #  |       l  r
# #target = 1
# # res= [-1, -1, r]

# Earlier revision (preserved)

# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         nums.sort()
#         res = []
#
#         for index in range(len(nums)):
#             if index > 0 and nums[index] == nums[index-1]:
#                 continue
#             target = -nums[index]
#
#             l, r = index+1, len(nums)-1
#
#             while l < r:
#                 while l > 0 and nums[l-1] == nums[l]:
#                     l += 1
#
#                 cur_sum = nums[l] + nums[r]
#                 if cur_sum > target:
#                     r -= 1
#                 elif cur_sum < target:
#                     l += 1
#                 else:
#                     res.append([nums[index], nums[l], nums[r]])
#                     l += 1
#                     r -= 1
#
#         return res

# ### Revised implementation

# Earlier revision (preserved)

# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         nums.sort()
#         res = []
#
#         for index in range(len(nums)):
#             if index > 0 and nums[index] == nums[index-1]:
#                 continue
#             target = -nums[index]
#
#             l, r = index+1, len(nums)-1
#
#             while l < r:
#                 while l > index+1 and l < r and nums[l-1] == nums[l]:
#                     l += 1
#
#                 cur_sum = nums[l] + nums[r]
#                 if cur_sum > target:
#                     r -= 1
#                 elif cur_sum < target:
#                     l += 1
#                 else:
#                     res.append([nums[index], nums[l], nums[r]])
#                     l += 1
#                     r -= 1
#
#         return res

# ### Latest implementation

# Earlier revision (preserved)

# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         nums.sort()
#         res = []
#
#         for index in range(len(nums)):
#             if index > 0 and nums[index] == nums[index-1]:
#                 continue
#             target = -nums[index]
#
#             l, r = index+1, len(nums)-1
#
#             while l < r:
#                 if l > index+1 and l < r and nums[l-1] == nums[l]:
#                     l += 1
#                     continue
#
#                 cur_sum = nums[l] + nums[r]
#                 if cur_sum > target:
#                     r -= 1
#                 elif cur_sum < target:
#                     l += 1
#                 else:
#                     res.append([nums[index], nums[l], nums[r]])
#                     l += 1
#                     r -= 1
#
#         return res

# ### Match-branch revision

# Earlier revision (preserved)

# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         nums.sort()
#         res = []
#
#         for index in range(len(nums)):
#             if index > 0 and nums[index] == nums[index-1]:
#                 continue
#             target = -nums[index]
#
#             l, r = index+1, len(nums)-1
#
#             while l < r:
#                 cur_sum = nums[l] + nums[r]
#                 if cur_sum > target:
#                     r -= 1
#                 elif cur_sum < target:
#                     l += 1
#                 else:
#                     res.append([nums[index], nums[l], nums[r]])
#                     l += 1
#
#                     while l < r and nums[l-1] == nums[l]:
#                         l += 1
#
#                     while l < r and nums[r-1] == nums[r]:
#                         r -= 1
#
#         return res

# ### Latest revision: skip left duplicates after a match

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        for index in range(len(nums)):
            if index > 0 and nums[index] == nums[index-1]:
                continue
            target = -nums[index]

            l, r = index+1, len(nums)-1

            # [-1, -1, 2, 2, 0]
            # [-1, -1, 2]

            # [-1, -1, 0, 2, 2]
            #  |       l  r
            #target = 1
            # res= [-1, -1, r]

            while l < r:
                cur_sum = nums[l] + nums[r]
                if cur_sum > target:
                    r -= 1
                elif cur_sum < target:
                    l += 1
                else:
                    res.append([nums[index], nums[l], nums[r]])
                    l += 1

                    while l < r and nums[l-1] == nums[l]:
                        l += 1

        return res
