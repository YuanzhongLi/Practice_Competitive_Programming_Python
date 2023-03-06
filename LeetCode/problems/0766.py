class Solution:
    def isToeplitzMatrix(self, mat: List[List[int]]) -> bool:
        n = len(mat)
        m = len(mat[0])
        for i in range(n):
            num = mat[i][0]
            r = i
            for c in range(m):
                if r >= n:
                    break
                if mat[r][c] != num:
                    return False
                r += 1

        for i in range(m):
            num = mat[0][i]
            c = i
            for r in range(n):
                if c >= m:
                    break
                if mat[r][c] != num:
                    return False
                c += 1

        return True
