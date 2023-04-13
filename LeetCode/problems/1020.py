from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def check(land, H, W):
    y = land // W
    x = land % W
    for i in range(4):
        y_ = y + dy[i]
        x_ = x + dx[i]
        if not (0 <= y_ and y_ < H and 0 <= x_ and x_ < W):
            return False

    return True


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        H = len(grid)
        W = len(grid[0])
        N = H*W
        visited = [False for _ in range(N)]
        ans = 0
        for i in range(N):
            if visited[i] or grid[i // W][i % W] == 0:
                continue

            q = deque([i])
            lands = []
            while len(q) > 0:
                land = q.popleft()
                if visited[land]:
                    continue
                visited[land] = True
                lands.append(land)
                y = land // W
                x = land % W
                for i in range(4):
                    y_ = y + dy[i]
                    x_ = x + dx[i]
                    land_ = y_ * W + x_
                    if 0 <= y_ and y_ < H and 0 <= x_ and x_ < W and grid[y_][x_] == 1 and (not visited[land_]):
                        q.append(land_)

            flag = True
            for land in lands:
                if not check(land, H, W):
                    flag = False
                    break

            if flag:
                ans += len(lands)

        return ans
