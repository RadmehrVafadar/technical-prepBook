class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = l + ((r-l)//2)
            sum_hours = 0

            for p in piles:
                sum_hours += math.ceil(p/k)


            if sum_hours > h:
                l = k + 1
            else:
                r = k - 1
                res = min(res, k)

        return res
