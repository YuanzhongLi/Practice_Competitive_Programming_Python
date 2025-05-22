# Solution Link: https://leetcode.com/problems/set-matrix-zeroes/solutions/6764760/python-in-place-solution-with-japanese-explanation/


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        H, W = len(matrix), len(matrix[0])
        top_edge_0, left_edge_0 = False, False
        for i in range(H):
            for j in range(W):
                if matrix[i][j] == 0:
                    if i == 0:
                        top_edge_0 = True
                    if j == 0:
                        left_edge_0 = True

                    if 0 < i and 0 < j:
                        matrix[i][0] = matrix[0][j] = 0

        for i in range(1, H):
            if matrix[i][0] == 0:
                for j in range(W):
                    matrix[i][j] = 0

        for j in range(1, W):
            if matrix[0][j] == 0:
                for i in range(H):
                    matrix[i][j] = 0

        if top_edge_0:
            for i in range(W):
                matrix[0][i] = 0

        if left_edge_0:
            for i in range(H):
                matrix[i][0] = 0

        return None
