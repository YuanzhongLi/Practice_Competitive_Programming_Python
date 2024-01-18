from sys import stdin

input = stdin.readline

INF = float("inf")


def TSP(graph: list[list[int]]) -> int:
    N = len(graph)

    # dp[bitmask][i]: 以下のi, bitmaskにおける最短距離
    # bitmask: 始点0から通った頂点の集合（始点0は含まれない）
    # i: 今いる頂点（bitmaskに含まれる）
    dp = [[INF for _ in range(N)] for _ in range(1 << N)]
    dp[0][0] = 0

    # bitmaskでfor文を回す
    for bitmask in range(1, 1 << N):
        for i in range(N):
            # dp[bimask][i]を考える
            for x in range(N):
                # 1つ前はxにいて、x -> iと通ってきてdp[bimask][i]となる状況を考える
                if x != i and ((bitmask >> i) & 1) and graph[x][i] != INF:
                    dp[bitmask][i] = min(
                        dp[bitmask][i], dp[bitmask ^ (1 << i)][x] + graph[x][i]
                    )
    return dp[(1 << N) - 1][0]


N, E = map(int, input().rstrip().rsplit())
graph = [[INF for _ in range(N)] for _ in range(N)]
for i in range(N):
    graph[i][i] = 0

for _ in range(E):
    s, t, d = map(int, input().rstrip().rsplit())
    graph[s][t] = d


ans = TSP(graph)
if ans == INF:
    print(-1)
else:
    print(ans)
