### FLOW
#### Dinic.py
最大フロー（最小カット）を求める
マッチング問題等にも使用

### SEGMENT_TREE
#### LazySegmentTree.py
遅延評価セグメント木
ある範囲に対するクエリ操作と取得をO(logN)で行う（Nは全体の要素数）

### Block.py
s = aaabbbccd
v1, v2 = Block(s)
v1 = [a, b, c, d], v2 = [3, 3, 2, 1]

### Dijkstra.py
O(E+VlogV)で単一始点最短経路

### Divisor.py
O(sqrt(n))で nの約数を求める

### EratosthenesSieve
エラトステネスの篩

### Point.py
幾何的な座標問題の計算用

### PrimalDual.py
ある始点から終点へと流量Fを流す時の最小費用を求める
O(F*E*logV)

### PriorityQueue.py
優先度付きキュー
ただしc++と違って小さい方から取り出す

### Unionfind.py
unionforestを管理、生成する

### UseJson.py
pythonで*.jsonを扱う時のサンプルコード
