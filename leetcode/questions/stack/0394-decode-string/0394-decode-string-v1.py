# Earlier revision (preserved)

# class Solution:
#     def decodeString(self, s: str) -> str:
#         stk = []
#
#         for c in s:
#             if c == ']':
#                 inBracket = ''
#                 while stk[-1] != '[':
#                     inBracket = stk.pop() + inBracket
#                 stk.pop()
#
#                 k = ''
#                 while stk and stk[-1].isdigit():
#                     k = stk.pop() + k
#
#                 stk.append( int(k) * inBracket)
#             else:
#                 stk.append(c)
#
#         return ''.join(stk)

# Revised implementation:

class Solution:
    def decodeString(self, s: str) -> str:
        stk = []

        for c in s:
            if c == ']':
                inBracket = []
                while stk[-1] != '[':
                    inBracket.append(stk.pop())

                inBracket = ''.join(inBracket[::-1])
                stk.pop()

                k = []
                while stk and stk[-1].isdigit():
                    k.append(stk.pop())
                k = ''.join(k[::-1])

                stk.append( int(k) * inBracket)
            else:
                stk.append(c)

        return ''.join(stk)
