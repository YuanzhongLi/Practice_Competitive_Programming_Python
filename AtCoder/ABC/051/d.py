from heapq import heapify, heappush, heappop
INF = 10**18
N, M = map(int, input().rstrip().rsplit())
dist = [[INF for _ in range(N)] for _ in range(N)]
for i in range(N):
    dist[i][i] = 0

edges = []
for i in range(M):
    a, b, c = map(int, input().rstrip().rsplit())
    a -= 1
    b -= 1
    dist[a][b] = c
    dist[b][a] = c
    edges.append((a, b, c))

for i in range(N):
    for j in range(N):
        for k in range(N):
            dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])

ans = 0
for edge in edges:
  if dist[edge[0]][edge[1]] < edge[2]:
    ans += 1

print(ans)
