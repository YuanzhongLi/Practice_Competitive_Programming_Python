from sys import stdin, setrecursionlimit

# 再帰の深さの上限を上げる
# これをしないと以下のエラーが生じる
# RecursionError: maximum recursion depth exceeded Command exited with non-zero status
setrecursionlimit(100005)
input = stdin.readline

N, E = map(int, input().rstrip().rsplit())
graph = [[] for _ in range(N)]

while E:
    s, t = map(int, input().rstrip().rsplit())
    graph[s].append(t)
    graph[t].append(s)
    E -= 1

# -1の場合は未探索としてvisitedの役割も兼ねる
order = [-1 for _ in range(N)]
global order_cnt
order_cnt = 0

lowest = [float("inf") for _ in range(N)]
aps = []


def dfs(u, p):
    ## order
    global order_cnt
    order[u] = order_cnt
    order_cnt += 1
    is_ap = False

    root_children_cnt = 0

    ## lowest
    lowest[u] = order[u]
    for v in graph[u]:
        if order[v] == -1:
            dfs(v, u)
            lowest[u] = min(lowest[u], lowest[v])

            if u == 0:
                root_children_cnt += 1
                if root_children_cnt >= 2:
                    is_ap = True
            elif order[u] <= lowest[v]:
                is_ap = True

        # 後退辺u->vが存在する（vには既に行っていてuの親ではない）
        elif v != p:
            lowest[u] = min(lowest[u], order[v])

    if is_ap:
        aps.append(u)


dfs(0, -1)
aps.sort()

for ap in aps:
    print(ap)
