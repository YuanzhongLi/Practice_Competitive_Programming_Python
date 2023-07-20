# Intuition & Approach
<!-- Describe your first thoughts on how to solve this problem. -->
- Oが接し合う連結グラフとみなせる。
- 次にこの連結グラフが囲まれている条件を考える。
    - 実はこれはとてもシンプルで、連結グラフが４辺に接しないことと同値。
    これに気づけるかがこの問題のポイント。

# Complexity
H: ```board```の行
W: ```board```の列
N: H*W

- Time complexity: O(N)
<!-- Add your time complexity here, e.g. O(n) -->
全部のノードに対するBFSなのでO(N)。

- Space complexity: O(N)
<!-- Add your space complexity here, e.g. O(n) -->
BFSのための```que```と```visited```でそれぞれO(N)。後は定数メモリ。

# Code
```
from collections import deque

# 上下左右の4方向を見るため配列
dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]

INF = 1 << 30   

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        H, W = len(board), len(board[0])
        N = H*W
        visited = set([])
        for u in range(N):
            uy, ux = u // W, u % W
            if board[uy][ux] == 'X' or u in visited:
                continue

            # Oが互いに接する連結グループ
            connected_group = []

            # グループ内で4方向への最近値
            # 最初は極端な値で初期化
            min_y, max_y, min_x, max_x = INF, -1, INF, -1

            # BFSを行って連結しているグループを把握していく
            que = deque([u])    
            while que:          
                u = que.popleft()  
                if u in visited:
                    continue
                visited.add(u)
                connected_group.append(u)
                uy, ux = u // W, u % W
                min_y, max_y, min_x, max_x = min(min_y, uy), max(max_y, uy), min(min_x, ux), max(max_x, ux)

                for i in range(4):
                    vy, vx = uy + dy[i], ux + dx[i]
                    v = vy * W + vx
                    if 0 <= vy and vy < H and 0 <= vx and vx < W and board[vy][vx] == 'O' and not (v in visited):
                        que.append(v)

            # グループ内で４辺に接しているものがあるかを判定
            if 0 < min_y and max_y < H-1 and 0 < min_x and max_x < W-1:
                for u in connected_group:
                    uy, ux = u // W, u % W
                    board[uy][ux] = 'X'
        
```
