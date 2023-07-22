INF = int(1e18)


def f(N, edges):
    graph = [[] for _ in range(N)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    order = [INF for _ in range(N)]
    low = [INF for _ in range(N)]
    visited = [False for _ in range(N)]
    id = 0
    ret = []
    aps = []

    def dfs(u, p):
        nonlocal id
        visited[u] = True
        order[u] = id
        low[u] = id
        id += 1
        child_count = 0
        is_aps = False
        for v in graph[u]:
            if not visited[v]:
                child_count += 1
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > order[u]:
                    ret.append([u, v])
                if p != -1 and low[v] >= order[u]:
                    is_aps = True
            elif v != p:
                low[u] = min(low[u], low[v])

        if p == -1 and child_count >= 2:
            is_aps = True
        if is_aps:
            aps.append(u)

    dfs(0, -1)
    return ret, aps
