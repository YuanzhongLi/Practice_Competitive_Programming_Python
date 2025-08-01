# Solution Link: https://leetcode.com/problems/pascals-triangle/solutions/7030153/python-enumerate-solution-with-japanese-dxd39/


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for r in range(2, numRows + 1):
            prev_row = ans[-1]
            new_row = [0 for _ in range(r)]
            new_row[0] = new_row[-1] = 1
            for j in range(1, r - 1):
                new_row[j] = prev_row[j - 1] + prev_row[j]
            ans.append(new_row)

        return ans
