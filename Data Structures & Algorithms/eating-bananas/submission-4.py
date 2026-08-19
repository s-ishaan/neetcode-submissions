class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_piles = max(piles)
        l = 1
        r = max_piles

        while (l<=r):
            k = l + ((r-l)//2)
            time = 0
            for pile in piles:
                time += (pile+k-1)//k

            if time > h:
                l = k+1
            else:
                r = k-1
            
        return l