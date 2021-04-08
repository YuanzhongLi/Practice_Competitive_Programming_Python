dy = [-1, 0, 1, 0] # u, r, d, l
dx = [0, 1, 0, -1]
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        H = len(grid)
        W = len(grid[0])
        s = None; e = None
        tot = 0
        for i in range(H):
            for j in range(W):
                if grid[i][j] != -1:
                    tot += 1
                if grid[i][j] == 1:
                    s = i*W+j
                elif grid[i][j] == 2:
                    e = i*W+j

        used = [[False for _ in range(W)] for _ in range(H)]
        used[s//W][s%W] = True
        ans = 0
        def dfs(u, d):
            nonlocal ans
            if u == e and d == tot:
                ans += 1
                return
            uy,ux = u//W, u%W
            for i in range(4):
                vy,vx = uy+dy[i],ux+dx[i]
                if 0 <= vy and vy < H and 0 <= vx and vx < W and not used[vy][vx] and grid[vy][vx] != -1:
                    v = vy*W+vx
                    used[vy][vx] = True
                    dfs(v,d+1)
                    used[vy][vx] = False
        dfs(s, 1)
        return ans
