import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(list)
        for source, target, time in times:
            g[source].append((target, time))

        min_times = {}
        min_heap = [(0,k)] #distance from source to node, node

        while min_heap:
            time_k_to_i, i = heapq.heappop(min_heap)
            if i in min_times:
                continue

            min_times[i] = time_k_to_i
            for nei, time_to_nei in g[i]:
                if nei not in min_times:
                    heapq.heappush(min_heap, (time_k_to_i + time_to_nei,nei))

        if len(min_times)==n:
            return max(min_times.values())
        else:
            return -1
                