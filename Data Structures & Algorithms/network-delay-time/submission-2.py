import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(list)
        for s,d,t in times:
            g[s].append((t,d))

        min_heap = [(0,k)] #distance from source to node, node
        min_times = {}

        while min_heap:
            time_to_k, node = heapq.heappop(min_heap)
            if node in min_times:
                continue
            
            min_times[node] = time_to_k
            for time_to_nei, nei in g[node]:
                if nei not in min_times:
                    heapq.heappush(min_heap, (time_to_k + time_to_nei, nei))
        
        if len(min_times) == n:
            return max(min_times.values())
        else:
            return -1
