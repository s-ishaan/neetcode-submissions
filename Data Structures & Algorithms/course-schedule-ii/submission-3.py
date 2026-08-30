from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        courses = prerequisites

        for a,b in courses:
            g[a].append(b)

        VISITED = 2
        VISITING = 1
        UNVISITED = 0
        states = [UNVISITED]*numCourses
        path = []

        def dfs(node):
            state = states[node]
            if state == VISITING: return False
            elif state == VISITED: return True

            states[node] = VISITING
            for nei in g[node]:
                if not dfs(nei): return False
            states[node] = VISITED
            path.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return path
        