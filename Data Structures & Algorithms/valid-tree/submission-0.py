class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        g = defaultdict(list)

        for a,b in edges:
            g[a].append(b)
            g[b].append(a)

        def dfs(i, prev):
            if i in visited:
                return False

            visited.add(i)
            for nei in g[i]:
                if nei == prev:
                    continue
                if not dfs(nei, i):
                    return False
                
            return True

        return dfs(0,-1) and n==len(visited)
