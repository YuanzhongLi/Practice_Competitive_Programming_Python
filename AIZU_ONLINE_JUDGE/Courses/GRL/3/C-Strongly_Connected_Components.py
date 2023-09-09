from sys import stdin, setrecursionlimit

# 再帰の深さの上限を上げる
# これをしないと以下のエラーが生じる
# RecursionError: maximum recursion depth exceeded Command exited with non-zero status
setrecursionlimit(100005)
input = stdin.readline

N, E = map(int, input().rstrip().rsplit())
graph = [[] for _ in range(N)]
reverse_graph = [[] for _ in range(N)]

while E:
    s, t = map(int, input().rstrip().rsplit())
    graph[s].append(t)
    reverse_graph[t].append(s)
    E -= 1


# 1回目のDFSの帰り際で格納する配列
back_order = []
visited = [False for _ in range(N)]


def dfs(u):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(v)
    # 帰り際に格納
    back_order.append(u)


for u in range(N):
    if not visited[u]:
        dfs(u)

back_order.reverse()

# 各ノードのsccのidを記録する
scc_id = [-1 for _ in range(N)]
visited = [False for _ in range(N)]


# 2回目のDFSでsccを決定し、scc idを割り当てる
def reverse_dfs(u, id):
    visited[u] = True
    scc_id[u] = id
    for v in reverse_graph[u]:
        if not visited[v]:
            reverse_dfs(v, id)


# scc idのカウンター
scc_id_cnt = 0
for u in back_order:
    if not visited[u]:
        reverse_dfs(u, scc_id_cnt)
        scc_id_cnt += 1

Q = int(input().rstrip())
while Q:
    u, v = map(int, input().rstrip().rsplit())
    if scc_id[u] == scc_id[v]:
        print(1)
    else:
        print(0)
    Q -= 1
