class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        def check(r, c):
            if grid[r][c] == 1:
                if c == n-1:
                    return -1, -1
                if grid[r][c+1] == -1:
                    return -1, -1
                return r+1, c+1
            else: # grid[r][c] == -1:
                if c == 0:
                    return -1, -1
                if grid[r][c-1] == 1:
                    return -1, -1
                return r+1, c-1

        ret= [-1 for _ in range(n)]
        for i in range(n):
            r = 0
            c = i
            while r < m and r != -1:
                r, c = check(r, c)

            if r != -1:
                ret[i] = c

        return ret
