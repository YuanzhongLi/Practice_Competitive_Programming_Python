class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        H = len(mat); W = len(mat[0])
        N = H*W
        if target < mat[0][0] or target > mat[H-1][W-1]: return False
        ok = 0; ng = N
        while abs(ok-ng) > 1:
            mid = (ok+ng)//2
            if mat[mid//W][mid%W] <= target:
                ok = mid
            else:
                ng = mid
        return mat[ok//W][ok%W] == target
