class Solution:
    def updateBoard(self, grid: List[List[str]], click: List[int]) -> List[List[str]]:
        H = len(grid); W = len(grid[0])
        def rec(y, x):
            nonlocal H, W
            if grid[y][x] == 'M':
                grid[y][x] = 'X'
                return
            elif grid[y][x] == 'E':
                cnt = 0
                for y_ in range(y-1, y+2):
                    for x_ in range(x-1, x+2):
                        if 0 <= y_ and y_ < H and 0 <= x_ and x_ < W:
                            if grid[y_][x_] == 'M':
                                cnt += 1
                if cnt == 0:
                    grid[y][x] = 'B'
                    for y_ in range(y-1, y+2):
                        for x_ in range(x-1, x+2):
                            if 0 <= y_ and y_ < H and 0 <= x_ and x_ < W:
                                if grid[y_][x_] == 'E':
                                    rec(y_, x_)
                else:
                    grid[y][x] = str(cnt)
            return

        rec(click[0], click[1])
        return grid
