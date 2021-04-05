class Solution:
    def largestSubmatrix(self, mat: List[List[int]]) -> int:
        H = len(mat); W = len(mat[0])
        for i in range(1, H):
            for j in range(W):
                if mat[i][j] != 0:
                    mat[i][j] += mat[i-1][j]
        ans = 0
        for i in range(H):
            mat[i].sort(reverse=True)
            A = mat[i]
            for j in range(W):
                ans = max(ans, A[j]*(j+1))
        return ans
