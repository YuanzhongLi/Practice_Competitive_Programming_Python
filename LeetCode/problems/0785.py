class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        N = len(graph)

        color = [0 for _ in range(N)]
        used = set([])
        def dfs(u, p, c):
            used.add(u)
            color[u] = c
            for v in graph[u]:
                if v in used: continue
                dfs(v, u, c^1)

        for u in range(N):
            if u in used: continue
            dfs(u, -1, 0)

        for u in range(N):
            for v in graph[u]:
                if color[u] == color[v]:
                    return False

        return True
