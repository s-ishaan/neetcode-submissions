from collections import Counter
import heapq
# import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        freq_heap = []
        heapq.heapify(freq_heap)

        for k,v in counter.items():
            heapq.heappush(freq_heap, -1*v)
        
        q = deque()
        time = 0

        while freq_heap or q:
            time += 1
            if freq_heap:
                cnt = 1+ heapq.heappop(freq_heap)
                if cnt:
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time:
                    heapq.heappush(freq_heap, q.popleft()[0])

        return time
                

            
        

