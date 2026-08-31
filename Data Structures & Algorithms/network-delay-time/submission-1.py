import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(list)
        for s,d,t in times:
            g[s].append((d,t))

        min_times = {}
        min_heap = [(0,k)] #distance to source from node, node

        while min_heap:
            time, i = heapq.heappop(min_heap)
            if i in min_times:
                continue
            
            min_times[i] = time
            for nei, time_to_nei in g[i]:
                if nei not in min_times:
                    heapq.heappush(min_heap, (time+time_to_nei, nei))

        if len(min_times) == n:
            return max(min_times.values())
        else:
            return -1