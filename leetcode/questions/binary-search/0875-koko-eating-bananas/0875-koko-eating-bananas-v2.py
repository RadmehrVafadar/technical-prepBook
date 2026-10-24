class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        max_pile = max(piles)

        l = 1
        r = max_pile

        res = -1

        """
        l = 1
        r = 5
        eating_rate = 3
        count = 4
        cur_pile = 8
        res = 0
        """
        while l < r:
            eating_rate = l + ((r-l)//2)
            count = 0

            for pile in piles:
                if count >= h:
                    l = eating_rate + 1
                    break

                cur_pile = pile
                while cur_pile > 0 and count < h:
                    count += 1
                    cur_pile -= eating_rate

            if count == h:
                res = max(res, eating_rate)

            if count <= h:
                r = eating_rate - 1

        return res
