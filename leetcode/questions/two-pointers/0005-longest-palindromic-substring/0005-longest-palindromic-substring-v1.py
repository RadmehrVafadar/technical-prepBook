# Personal notes (preserved)

# # At each index, check both center cases in sequence—odd and even—with separate while loops; no need to classify the whole string by parity.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        max_length = 0
        res = []
        n = len(s)
        for i in range(n):
            # odd
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                sublength = (r-l)+1
                if sublength > max_length:
                    max_length = sublength
                    res = s[l:r+1]
                l -= 1
                r += 1

            # even
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                sublength = (r-l)+1
                if sublength > max_length:
                    max_length = sublength
                    res = s[l:r+1]
                l -= 1
                r += 1
        return res
