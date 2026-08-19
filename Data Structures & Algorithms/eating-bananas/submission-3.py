class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)
        l = 1
        r = max_pile

        while (l<=r):
            m = l + ((r-l)//2)
            time = 0
            for pile in piles:
                time += (pile + m - 1)//m

            if time > h:
                l = m+1
            else:
                r = m - 1

        return l


    