import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        prox = []
        heapq.heapify(prox)
        for point in points:
            x,y = point
            dist = (x**2 + y**2)**0.5
            heapq.heappush(prox, (dist, point))


        ans = []

        for i in range(k):
            distance, point = heapq.heappop(prox)
            ans.append(point)

        return ans
