import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        
        
        stones = [-1*stone for stone in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            s1 = -1*heapq.heappop(stones)
            s2 = -1*heapq.heappop(stones)
            diff = s2-s1
            if diff != 0:
                heapq.heappush(stones, diff)

        return -stones[0] if stones else 0
