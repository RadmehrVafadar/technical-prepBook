class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        res = 0
        numSet = set()
        for num in nums:
            numSet.add(num)

        for num in nums:
            if num not in numSet:
                continue

            tempLen = 1

            l = num-1
            while l in numSet:
                tempLen += 1
                numSet.remove(l)
                l -= 1

            r = num+1
            while r in numSet:
                tempLen += 1
                numSet.remove(r)
                r += 1

            res = max(res, tempLen)
        return res
