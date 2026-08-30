class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        g = defaultdict(list)
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)

        visited = set()

        def dfs(node, prev):
            if node in visited:
                return False

            visited.add(node)
            for nei in g[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node): 
                    return False
            
            return True

        return dfs(0,-1) and len(visited) == n