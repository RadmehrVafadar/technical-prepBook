# Personal notes (preserved)

# # upper and lower case
# # spaces, acci symbols
# # upper and lower are diffirent
# # can only contrain one space or symbols
#
# # input = "awdada dawod ao91"
# # output: length of substring (int)
#
# # set = (b)
# # "abcabcbb"
# #         ||
# # res = max((r-l)+1, res)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # upper and lower case
        # spaces, acci symbols
        # upper and lower are diffirent
        # can only contrain one space or symbols

        # input = "awdada dawod ao91"
        # output: length of substring (int)

        # set = (b)
        # "abcabcbb"
        #         ||
        # res = max((r-l)+1, res)
        res = 0
        if not s:
            return res

        detector = set()
        l = 0
        for r in range(len(s)):
            while s[r] in detector:
                detector.remove(s[l])
                l += 1
            detector.add(s[r])
            res = max(res, (r-l)+1)


        return res
