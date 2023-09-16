from sys import stdin
from collections import deque


input = stdin.readline

N = int(input().rstrip())
graph = [[] for _ in range(N)]

E = N - 1

while E:
    s, t, w = map(int, input().rstrip().rsplit())
    graph[s].append((t, w))
    graph[t].append((s, w))

    E -= 1

# (ノードu, ノード0からuまでの経路長, ノードuの親)
que = deque([(0, 0, -1)])
# ノード0から最も遠いノードまでの距離
dis_max_from0 = -1
# ノード0から最も遠いノード
x = -1

while que:
    u, u_dis, p = que.popleft()
    if u_dis > dis_max_from0:
        dis_max_from0 = u_dis
        x = u

    for v_pair in graph[u]:
        v, uv_dis = v_pair
        if v != p:
            que.append((v, u_dis + uv_dis, u))


# (ノードu, ノードxからuまでの経路長, ノードuの親)
que = deque([(x, 0, -1)])
# ノードxから最も遠いノードまでの距離
dis_max_from_x = -1
while que:
    u, u_dis, p = que.popleft()
    if u_dis > dis_max_from_x:
        dis_max_from_x = u_dis

    for v_pair in graph[u]:
        v, uv_dis = v_pair
        if v != p:
            que.append((v, u_dis + uv_dis, u))

print(dis_max_from_x)
