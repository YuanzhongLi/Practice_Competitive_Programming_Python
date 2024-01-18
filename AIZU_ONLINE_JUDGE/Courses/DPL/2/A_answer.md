### Traveling Salesman Problem
#### Intuition & Approach
- `dp[bitmask][i]`: 以下の`i`, `bitmask`における最短距離（遷移はコードのコメント参照）
    - `bitmask`: 始点0から通った頂点の集合（始点0は含まれない）
    - `i`: 今いる頂点（`bitmask`に含まれる）

`bitmask`をfor文で回すことについて説明します。(なぜfor文で回しても良いのかと疑問に思える方はDPで値が決定する順序をかなり意識できているので自信を持ってください。)　
- これは既知の状況から未知を求めるためです。
- `bitmask`は**小さい順に既知**となります。
- より正確に言うと立っているbitが増えて行く順に既知となっていきます。

以下の例は`bitmask`の部分は二進数で表しています。　　
例えば`dp[1111][0]`を求めたいとします。  
このときコードより
```python
dp[1111][0] = min(
    dp[1101][1] + graph[1][0],
    dp[1011][2] + graph[2][0],
    dp[0111][3] + graph[3][0]
)
```
です。これより1111は各bitが立っていないものに依存しています。　　
`bitmask`を小さい順い見ていくことでbitが立っていない順に決定していくことができてます。（実際に手を動かして0 ~ 1111でどうなるか試してみるとより理解が進むかと思います。）


#### [Code](./C-Knapsack_Problem.py)
```python
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
```

#### 計算量
- Time complexity: $O(2^NN^2)$
- Space complexity: $O(2^NN)$
