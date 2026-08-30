class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)

        visited = [False] * n
        components = 0

        def dfs(i):
            visited[i] = True

            for nei in g[i]:
                if not visited[nei]:
                    dfs(nei)
            
        for node in range(n):
            if not visited[node]:
                components += 1
                dfs(node)

        return components
