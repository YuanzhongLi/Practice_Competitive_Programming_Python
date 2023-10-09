from sys import stdin


input = stdin.readline


def WarshallFloyd(N: int, edges: list[list[int]]) -> list[list[int]]:
    # d[u][v] = u -> vの最短経路の長さ
    # 最初は到達不可能ということでfloat('inf')で初期化
    d = [[float("inf") for _ in range(N)] for _ in range(N)]
    # d[u][u] = 0で初期化(自分自身へは距離0で到達可能)
    for u in range(N):
        d[u][u] = 0

    # d[u][v] = wで初期化
    for edge in edges:
        u, v, w = edge
        d[u][v] = w

    for k in range(N):
        for u in range(N):
            for v in range(N):
                # kを経由した最短距離で更新
                d[u][v] = min(d[u][v], d[u][k] + d[k][v])

    for u in range(N):
        # 自分自身への最短距離が負ということは負閉路が存在することを意味する
        # （自分自身を経由していくらでも小さくできる閉路が存在）
        if d[u][u] < 0:
            return None

    return d


V, E = map(int, input().rstrip().rsplit())
edges = []

while E:
    edges.append([int(e) for e in list(input().rstrip().rsplit())])
    E -= 1

d = WarshallFloyd(V, edges)

if d:
    for row in d:
        print(" ".join([str(e) if e != float("inf") else "INF" for e in row]))

else:
    print("NEGATIVE CYCLE")
