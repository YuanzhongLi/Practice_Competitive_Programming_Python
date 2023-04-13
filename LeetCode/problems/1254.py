from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def check(id, H, W):
    h = id // W
    w = id % W
    for i in range(4):
        dh = h + dy[i]
        dw = w + dx[i]
        if dh < 0 or dw < 0 or dh >= H or dw >= W:
            return False

    return True


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        H = len(grid)
        W = len(grid[0])
        N = H*W
        visited = [False for _ in range(N)]
        ans = 0
        for i in range(N):
            h = i // W
            w = i % W
            if grid[h][w] == 1 or visited[i]:
                continue

            q = deque([i])
            ids = []
            while len(q) > 0:
                id = q.popleft()
                if visited[id]:
                    continue
                visited[id] = True
                ids.append(id)

                y = id // W
                x = id % W
                for j in range(4):
                    y_ = y + dy[j]
                    x_ = x + dx[j]
                    id_ = y_ * W + x_
                    if 0<=y_ and y_<H and 0<=x_ and x_< W and grid[y_][x_]==0 and (not visited[id_]):
                        q.append(id_)

            flag = True
            for id in ids:
                if not check(id, H, W):
                    flag = False
                    break

            if flag:
                ans += 1

        return ans
