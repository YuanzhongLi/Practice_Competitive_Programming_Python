from collections import deque
class Solution:
    def findOrder(self, N: int, edges: List[List[int]]) -> List[int]:
        inner = [0 for _ in range(N)]
        graph = [[] for _ in range(N)]
        for to, fro in edges:
            inner[to] += 1
            graph[fro].append(to)
        q = deque([])
        for i in range(N):
            if inner[i] == 0:
                q.append(i)

        ret = []
        taken = [False for _ in range(N)]
        while q:
            u = q.popleft()
            if taken[u]: continue
            taken[u] = True
            ret.append(u)
            for v in graph[u]:
                if taken[v]: return []
                inner[v] -= 1
                if inner[v] == 0:
                    q.append(v)

        if len(ret) != N: return []
        return ret

# DFS solution
class Solution:
    def findOrder(self, N: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(N)]
        for a, b in edges:
            graph[b].append(a)

        visited = [0 for _ in range(N)]
        A = []
        def dfs(u, p):
            visited[u] = 1
            for v in graph[u]:
                if v == u or visited[v] == 2:
                    continue
                elif visited[v] == 1:
                    return True
                else:
                    if dfs(v, u):
                        return True

            visited[u] = 2
            A.append(u)
            return False

        for i in range(N):
            if visited[i] == 2:
                continue
            has_cycle = dfs(i, -1)
            if has_cycle:
                return []
        A.reverse()
        return A
