dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # (y, x)
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ret = [[0 for _ in range(n)] for _ in range(n)]
        N = n*n
        idx_d = 0
        d = dirs[idx_d]
        cur = [0, 0]
        for i in range(1, N+1):
            y, x = cur[0], cur[1]
            ret[y][x] = i
            ny, nx = y+d[0], x+d[1]
            if 0 <= ny and ny < n and 0 <= nx and nx < n and ret[ny][nx] == 0:
                cur[0], cur[1] = ny, nx
            else:
                idx_d += 1
                idx_d %= 4
                d = dirs[idx_d]
                cur[0], cur[1] = y+d[0], x+d[1]
        return ret
