class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        """
        temperatures = [73,74,75,71,69,72,76,73]
        stk = [73:0, 74:1, 75, 76]


        tempatures = [10, 5,6,7,8,9]
        stk = [10]

        """
        n = len(temperatures)
        stk = []
        res = [0] * n

        for i in range(n):
            while stk and temperatures[i] > (stk[-1][0]):
                temp, index = stk.pop()
                res[index] = (i - index)

            stk.append([temperatures[i], i])

        return res
