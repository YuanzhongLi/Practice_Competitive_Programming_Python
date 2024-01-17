### Knapsack
#### Intuition & Approach
- 品物がいくつでも選べるので、品物を順番に見て選ぶか選ばないかの二値を状態としたDPはできません。
- 実はこの問題は次の様に重さのみに着目すればうまくいきます。**「`dp[w]`: w以下の最大価値」**
- 重みを小さい順から確認して各アイテムを選んだときにどうなるかを考えれば良いです。

#### [Code](./C-Knapsack_Problem.py)
```python
from sys import stdin

input = stdin.readline

INF = float("inf")


def Knapsack(N: int, W: int, values: list[int], weights: list[int]) -> int:
    # dp[w]: 重みw以下での最大価値
    dp = [0 for _ in range(W + 1)]

    for w in range(1, W + 1):
        # 当然w-1以下での最大価値はw以下での最大価値の候補
        dp[w] = dp[w - 1]
        for i in range(N):
            vi, wi = values[i], weights[i]

            # 重さw-wi以下の最大価値はdp[w-wi]
            # これに対してi番目の品物を追加する場合を考える
            if w - wi >= 0:
                dp[w] = max(dp[w], dp[w - wi] + vi)

    return dp[W]


N, W = map(int, input().rstrip().rsplit())
values = [0 for _ in range(N)]
weights = [0 for _ in range(N)]

for i in range(N):
    vi, wi = map(int, input().rstrip().rsplit())
    values[i], weights[i] = vi, wi

print(Knapsack(N, W, values, weights))
```

#### 計算量
- Time complexity: $O(WN)$
- Space complexity: $O(W)$
