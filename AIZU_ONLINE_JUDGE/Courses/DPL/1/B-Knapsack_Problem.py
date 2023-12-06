from sys import stdin

input = stdin.readline


def Knapsack(N: int, W: int, values: list[int], weights: list[int]) -> int:
    dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]

    for i in range(1, N + 1):
        vi, wi = values[i - 1], weights[i - 1]
        for w in range(1, W + 1):
            dp[i][w] = max(dp[i][w], dp[i - 1][w], dp[i][w - 1])
            if w - wi >= 0:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - wi] + vi)

    return dp[N][W]


N, W = map(int, input().rstrip().rsplit())
values = [0 for _ in range(N)]
weights = [0 for _ in range(N)]

for i in range(N):
    vi, wi = map(int, input().rstrip().rsplit())
    values[i], weights[i] = vi, wi

print(Knapsack(N, W, values, weights))
