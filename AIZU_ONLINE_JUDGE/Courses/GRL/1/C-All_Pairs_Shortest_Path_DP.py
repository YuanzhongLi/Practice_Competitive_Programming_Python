from sys import stdin


input = stdin.readline


def WarshallFloyd(N: int, edges: list[list[int]]) -> list[list[int]]:
    # (1)
    # d[k][u][v] = ノード0 ~ kのみを経由するu -> vの最短距離
    # 最初は到達不可能ということでfloat('inf')で初期化
    dp = [[[float("inf") for _ in range(N)] for _ in range(N)] for _ in range(N)]

    for k in range(N):
        # d[k][u][u] = 0で初期化(自分自身へは距離0で到達可能)
        for u in range(N):
            dp[k][u][u] = 0

        # d[k][u][v] = wで初期化
        for edge in edges:
            u, v, w = edge
            dp[k][u][v] = w

    for k in range(N):
        for u in range(N):
            for v in range(N):
                # (2)
                # dp[k-1][u][v]: ノード0 ~ k-1のみを経由するu -> vの最短距離
                # dp[k-1][u][k]: ノード0 ~ k-1のみを経由するu -> kの最短距離
                # dp[k-1][k][v]: ノード0 ~ k-1のみを経由するk -> vの最短距離
                dp[k][u][v] = min(dp[k - 1][u][v], dp[k - 1][u][k] + dp[k - 1][k][v])

    for u in range(N):
        # 自分自身への最短距離が負ということは負閉路が存在することを意味する
        # （自分自身を経由していくらでも小さくできる閉路が存在）
        if dp[N - 1][u][u] < 0:
            return None

    return dp[N - 1]


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
