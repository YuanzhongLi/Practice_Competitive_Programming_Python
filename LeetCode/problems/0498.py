# Solution Link: https://leetcode.com/problems/diagonal-traverse/solutions/7119000/python-enumerate-solution-with-japanese-tmrvh/


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        global H, W
        H, W = len(mat), len(mat[0])

        # asc: 進行方向が右上かどうか
        def get_next(i, j, asc):
            global H, W
            if asc:
                if j == W - 1:
                    return i + 1, j, False
                # j < W-1

                if i == 0:
                    return i, j + 1, False

                return i - 1, j + 1, True
            else:
                if i == H - 1:
                    return i, j + 1, True
                # i < H-1

                if j == 0:
                    return i + 1, j, True

                return i + 1, j - 1, False

        ans = []
        i, j, asc = 0, 0, True
        for _ in range(H * W):
            ans.append(mat[i][j])
            i, j, asc = get_next(i, j, asc)

        return ans
