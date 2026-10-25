# Personal notes (preserved)

# # k has to be larger or equal to the number of unique numbers
# # the list is not sorted
# # there has to be atleast 1 value in list
# # values are ints
# # the result order does not matter
#
# # brute force
# # [1, 1, 1, 2, 2, 3]
# # freqency = {1:3, 2:2 3:1} num :freq
# # Bottlneck: Sort
# #

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        # k has to be larger or equal to the number of unique numbers
        # the list is not sorted
        # there has to be atleast 1 value in list
        # values are ints
        # the result order does not matter

        # brute force
        # [1, 1, 1, 2, 2, 3]
        # freqency = {1:3, 2:2 3:1} num :freq
        res = []
        bucket = [[] for i in range(len(nums))]
        freq = Counter(nums)

        for num in freq:
            bucket[freq[num]-1].append(num)

        for i in range(len(nums)-1, -1, -1):
            for j in range(len(bucket[i])):
                res.append(bucket[i][j])
                if len(res) == k:
                    return res




        # Bottlneck: Sort
        #
