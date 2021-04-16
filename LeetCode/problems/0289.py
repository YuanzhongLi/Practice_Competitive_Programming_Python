class Solution:
    def gameOfLife(self, grid: List[List[int]]) -> None:
        H = len(grid); W = len(grid[0])
        def get_live_neighbors(uy, ux):
            nonlocal H, W
            ret = 0
            for vy in range(uy-1, uy+2):
                for vx in range(ux-1, ux+2):
                    if vy == uy and vx == ux: continue
                    if 0 <= vy and vy < H and 0 <= vx and vx < W:
                        val = grid[vy][vx]
                        if val == 1 or val == 2:
                            ret += 1
            return ret

        for i in range(H):
            for j in range(W):
                neighbors = get_live_neighbors(i, j)
                if grid[i][j] == 0:
                    if neighbors == 3:
                        grid[i][j] = 3
                else:
                    if 2 <= neighbors and neighbors <= 3:
                        continue
                    else:
                        grid[i][j] = 2

        for i in range(H):
            for j in range(W):
                if grid[i][j] == 2:
                    grid[i][j] = 0
                elif grid[i][j] == 3:
                    grid[i][j] = 1
