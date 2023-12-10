from sys import stdin
from copy import deepcopy as cp

input = stdin.readline


def Knapsack(N: int, W: int, values: list[int], weights: list[int]) -> int:
    dp_prev = [0 for _ in range(W + 1)]

    for i in range(1, N + 1):
        vi, wi = values[i - 1], weights[i - 1]
        dp_cur = cp(dp_prev)
        for w in range(1, W + 1):
            if w - wi >= 0:
                dp_cur[w] = max(dp_cur[w], dp_prev[w - wi] + vi)

        dp_prev = dp_cur

    return dp_prev[W]


N, W = map(int, input().rstrip().rsplit())
values = [0 for _ in range(N)]
weights = [0 for _ in range(N)]

for i in range(N):
    vi, wi = map(int, input().rstrip().rsplit())
    values[i], weights[i] = vi, wi

print(Knapsack(N, W, values, weights))
