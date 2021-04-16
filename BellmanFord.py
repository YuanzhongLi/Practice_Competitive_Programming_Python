# VERIFICATIOIN: ABC 61_D
# URL: https://atcoder.jp/contests/abc061/submissions/21783179

# 単一始点全点間最短路を求めるアルゴリズム。単一始点全点間最短路を求めるアルゴリズム。負辺があっても動作する。また負閉路も検出する。
# 計算量 O(V * E)

class BellmanFord:
  def __init__(self, V, INF=float('inf')):
    self.INF = INF
    self.V = V
    self.dist = [INF for _ in range(V)]
    self.edges = []

  def add_edge(self, a, b, cost):
    self.edges.append((a, b, cost))

  def run(self, s=0):
    dist = self.dist; INF = self.INF; edges = self.edges; V = self.V
    for i in range(V): dist[i] = INF
    dist[s] = 0
    for _ in range(V-1):
      for a, b, cost in edges:
        if dist[a] == INF: continue
        dist[b] = min(dist[b], dist[a]+cost)

    neg = [False for _ in range(V)]
    has_negative_loop = False
    for a, b, cost in edges:
      if dist[a] == INF: continue
      if dist[a]+cost < dist[b]:
        dist[b] = dist[a]+cost
        neg[b] = True
        has_negative_loop = True

      if neg[a]: neg[b] = True

    return dist, neg, has_negative_loop


N, M = map(int, input().rstrip().rsplit())
bf = BellmanFord(N)
for _ in range(M):
  a, b, c = map(int, input().rstrip().rsplit())
  a -= 1; b -= 1; c = -c
  bf.add_edge(a, b, c)

dist, neg, _ = bf.run()
if neg[N-1]:
  print('inf')
else:
  print(-dist[N-1])
