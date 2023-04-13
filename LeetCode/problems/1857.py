from collections import deque, defaultdict

def has_cycle(graph): # O(N+M)
    N = len(graph)
    # 0: not visited
    # 1: visited in current dfs
    # 2: visited in the other dfs
    visited = [0 for _ in range(N)]
    def dfs(u):
        visited[u] = 1
        for v in graph[u]:
            if visited[v] == 2:
                continue
            elif visited[v] == 1:
                return True
            else:
                if dfs(v):
                    return True

        visited[u] = 2
        return False

    for i in range(N):
        if visited[i] == 2:
            continue
        if dfs(i):
            return True

    return False

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        N = len(colors)
        graph = [[] for _ in range(N)]
        in_degree = [0 for _ in range(N)]
        for edge in edges:
            fr, to = edge
            graph[fr].append(to)
            in_degree[to] += 1

        if has_cycle(graph):
            return -1

        q = deque([])
        for i, i_d in enumerate(in_degree):
            if i_d == 0:
                q.append(i)

        mp = [defaultdict(int) for _ in range(N)]
        while len(q) > 0:
            u = q.popleft()
            u_dict = mp[u]
            u_dict[colors[u]] += 1

            for v in graph[u]:
                v_dict = mp[v]
                for c in u_dict.keys():
                    v_dict[c] = max(v_dict[c], u_dict[c])

                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)

        ans = 0
        for i in range(N):
            ans = max(ans, max(mp[i].values()))

        return ans
