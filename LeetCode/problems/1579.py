from collections import deque

def is_connected_graph(graph):
    N = len(graph)
    visited = [False for _ in range(N)]
    q = deque([0])
    while len(q) > 0:
        u = q.popleft()
        if visited[u]:
            continue
        visited[u] = True
        for v in graph[u]:
            if visited[v]:
                continue
            q.append(v)

    for ok in visited:
        if not ok:
            return False

    return True

class Solution:
    def maxNumEdgesToRemove(self, N: int, edges: List[List[int]]) -> int:
        ans = 0

        c_graph = [[] for _ in range(N)]
        for edge in edges:
            t, u, v = edge
            u -= 1
            v -= 1
            if t == 3:
                c_graph[u].append(v)
                c_graph[v].append(u)

        c_groups = []
        visited = [False for _ in range(N)]
        node_to_group = [-1 for _ in range(N)]
        for i in range(N):
            if visited[i]:
                continue

            c_group = []
            q = deque([i])
            while len(q) > 0:
                u = q.popleft()
                if visited[u]:
                    continue
                visited[u] = True
                c_group.append(u)
                for v in c_graph[u]:
                    if visited[v]:
                        continue
                    q.append(v)

            c_groups.append(c_group)
            group_id = len(c_groups) - 1
            group_edge_num = 0
            for u in c_group:
                node_to_group[u] = group_id
                for v in c_graph[u]:
                    group_edge_num += 1
            group_edge_num //= 2
            ans += group_edge_num - (len(c_group) - 1)

        M = len(c_groups)
        # based on c_group id
        a_graph = [[] for _ in range(M)]
        b_graph = [[] for _ in range(M)]
        a_edge_num = 0
        b_edge_num = 0
        for edge in edges:
            t, u, v = edge
            u -= 1
            v -= 1
            c_u = node_to_group[u]
            c_v = node_to_group[v]
            if t == 1: # Alice
                a_graph[c_u].append(c_v)
                a_graph[c_v].append(c_u)
                a_edge_num += 1
            elif t == 2: # Bob
                b_graph[c_u].append(c_v)
                b_graph[c_v].append(c_u)
                b_edge_num += 1

        if  is_connected_graph(a_graph) and is_connected_graph(b_graph):
            ans += a_edge_num - (M-1)
            ans += b_edge_num - (M-1)
            return ans

        return -1
