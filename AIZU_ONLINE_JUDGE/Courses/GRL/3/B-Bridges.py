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
global order_id, root_children_cnt
order_cnt = 0
root_children_cnt = 0

parent = [-1 for _ in range(N)]
lowest = [float("inf") for _ in range(N)]


def dfs(u, p):
    ## order
    global order_cnt
    order[u] = order_cnt
    order_cnt += 1

    ## parent
    parent[u] = p

    ## lowest
    lowest[u] = order[u]
    for v in graph[u]:
        if order[v] == -1:
            dfs(v, u)
            lowest[u] = min(lowest[u], lowest[v])

            if p == -1:
                global root_children_cnt
                root_children_cnt += 1

        # 後退辺u->vが存在する（vには既に行っていてuの親ではない）
        elif v != p:
            lowest[u] = min(lowest[u], order[v])


# order, parent, lowestを計算
dfs(0, -1)

is_aps = [False for _ in range(N)]
if root_children_cnt >= 2:
    is_aps[0] = True

bridges = []

# 根を除いて関節点の条件を確認
for u in range(N):
    p = parent[u]

    # どの様にしてもuはpを経由せずにpより上のorderのノードには辿り着けない、つまりpは関節点
    # p == -1 と p == 0を除く
    if p != -1 and order[p] < lowest[u]:
        bridges.append([min(p, u), max(p, u)])

bridges.sort()
for bridge in bridges:
    print(bridge[0], bridge[1])
