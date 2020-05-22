from sys import stdin
input = stdin.readline

# map(int, input().rstrip().split())

def VI(N, init=0):
  return [init for _ in range(N)]
def VVI(N, M, init=0):
  return [[init for _ in range(M)] for _ in range(N)]

INF = int(1e9+7)

N, M = map(int, input().rstrip().split())

dist = VVI(N, N, INF)
for i in range(N):
  dist[i][i] = 0

for i in range(M):
  a, b = map(int, input().rstrip().split())
  a -= 1
  b -= 1
  dist[a][b] = dist[b][a] = 1

for k in range(N):
  for i in range(N):
    for j in range(N):
      dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

for i in range(N):
  ans = 0
  for j in range(N):
    if dist[i][j] == 2:
      ans += 1
  print(ans)



