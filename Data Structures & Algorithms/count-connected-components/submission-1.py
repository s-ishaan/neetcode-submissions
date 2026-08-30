class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)

        visited = [False]*n

        def dfs(node):
            visited[node] = True

            for nei in g[node]:
                if not visited[nei]:
                    dfs(nei)

        components = 0
        for i in range(n):
            if not visited[i]:
                components += 1
                dfs(i)

        return components