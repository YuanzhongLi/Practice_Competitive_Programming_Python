# VERIFICATIOIN: AIZU ONLINE JUDGE/GRL_3_A, AIZU ONLINE JUDGE/GRL_3_B
# URL: https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/3/GRL_3_A
# https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/3/GRL_3_B


from sys import stdin, setrecursionlimit

setrecursionlimit(100005)
input = stdin.readline

INF = int(1e18)

N, E = map(int, input().rstrip().rsplit())
graph = [[] for _ in range(N)]

while E:
    s, t = map(int, input().rstrip().rsplit())
    graph[s].append(t)
    graph[t].append(s)
    E -= 1


def f(N, graph):
    order = [INF for _ in range(N)]
    low = [INF for _ in range(N)]
    visited = [False for _ in range(N)]
    id = 0
    bridges = []
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
                    bridges.append([min(u, v), max(u, v)])
                if p != -1 and low[v] >= order[u]:
                    is_aps = True
            elif v != p:
                low[u] = min(low[u], order[v])

        if p == -1 and child_count >= 2:
            is_aps = True
        if is_aps:
            aps.append(u)

    dfs(0, -1)
    aps.sort()
    bridges.sort()
    return bridges, aps


bridges, aps = f(len(graph), graph)

for ap in aps:
    print(ap)

# for bridge in bridges:
#     print(bridge[0], bridge[1])
