### FLOW
#### Dinic.py
最大フロー（最小カット）を求める
マッチング問題等にも使用

[link](./FLOW/Dinic.py)


#### PrimalDual.py
ある始点から終点へと流量Fを流す時の最小費用を求める
O(F*E*logV)

[link](./FLOW/PrimalDual.py)

### SEGMENT_TREE
#### LazySegmentTree.py
遅延評価セグメント木
ある範囲に対するクエリ操作と取得をO(logN)で行う（Nは全体の要素数）

[link](./SEGMENT_TREE/LazySegmentTree.py)

### Block.py
s = aaabbbccd
v1, v2 = Block(s)
v1 = [a, b, c, d], v2 = [3, 3, 2, 1]

[link](./Block.py)

### Dijkstra.py
O(E+VlogV)で単一始点最短経路

[link](./Dijkstra.py)

### Divisor.py
O(sqrt(n))で nの約数を求める

[link](./Divisor.py)

### EratosthenesSieve
エラトステネスの篩

[link](./EratosthenesSieve.py)

### Point.py
幾何的な座標問題の計算用

[link](./Point.py)

### PriorityQueue.py
優先度付きキュー
ただしc++と違って小さい方から取り出す

[link](./PriorityQueue.py)

### Unionfind.py
unionforestを管理、生成する

[link](./Unionfind.py)

### UseJson.py
pythonで*.jsonを扱う時のサンプルコード

[link](./UseJson.py)

### ModInt.py
modintを管理、生成する

[link](./ModInt.py)
