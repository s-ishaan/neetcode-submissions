
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        A = []
        ans = []
        heapq.heapify(A)
        for point in points:
            x,y = point
            dist = (x**2 + y**2)**0.5
            dist_tup = (dist, point)
            heapq.heappush(A, dist_tup)
            
        for i in range(k):
            p = heapq.heappop(A)
            a,point = p
            ans.append(point)

        return ans