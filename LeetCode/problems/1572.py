class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        ans = 0
        for r in range(n):
            c1 = r
            c2 = n-1-r
            ans += mat[r][c1]
            if c1 != c2:
                ans += mat[r][c2]

        return ans
