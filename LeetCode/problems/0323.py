from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b); graph[b].append(a)
        visited = [False for _ in range(n)]
        ret = 0
        for i in range(n):
            if visited[i]: continue
            ret += 1
            q = deque([i])
            while q:
                u = q.popleft()
                if visited[u]: continue
                visited[u] = True
                for v in graph[u]:
                    if  visited[v]: continue
                    q.append(v)
        return ret
