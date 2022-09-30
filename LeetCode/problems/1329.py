class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        H = len(mat)
        W = len(mat[0])
        for r in range(H):
            i = r
            j = 0
            tmp = []
            while i < H and j < W:
                tmp.append(mat[i][j])
                i += 1
                j += 1
            tmp.sort()

            i = r
            j = 0
            idx = 0
            while i < H and j < W:
                mat[i][j] = tmp[idx]
                i += 1
                j += 1
                idx += 1

        for c in range(W):
            i = 0
            j = c
            tmp = []
            while i < H and j < W:
                tmp.append(mat[i][j])
                i += 1
                j += 1
            tmp.sort()

            i = 0
            j = c
            idx = 0
            while i < H and j < W:
                mat[i][j] = tmp[idx]
                i += 1
                j += 1
                idx += 1

        return mat
