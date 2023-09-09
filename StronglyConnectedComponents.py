import sys

sys.setrecursionlimit(100005)

V, E = map(int, input().rstrip().rsplit())
graph = [[] for _ in range(V)]
r_graph = [[] for _ in range(V)]
for _ in range(E):
    s, t = map(int, input().rstrip().rsplit())
    graph[s].append(t)
    r_graph[t].append(s)

vs = []
used = [False for _ in range(V)]


def dfs(u):
    used[u] = True
    for v in graph[u]:
        if not used[v]:
            dfs(v)
    vs.append(u)


for i in range(V):
    if not used[i]:
        dfs(i)

# print(vs)

data = [-1 for _ in range(V)]
used = [False for _ in range(V)]


def rdfs(u, k):
    used[u] = True
    data[u] = k
    for v in r_graph[u]:
        if not used[v]:
            rdfs(v, k)


vs.reverse()
for v in vs:
    if not used[v]:
        rdfs(v, v)

# print(data)

Q = int(input())
ans = [0 for _ in range(Q)]
for i in range(Q):
    u, v = map(int, input().rstrip().rsplit())
    if data[u] == data[v]:
        ans[i] = 1

for a in ans:
    print(a)
