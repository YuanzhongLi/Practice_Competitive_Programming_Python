# Solution Link: https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/solutions/7122656/python-enumerate-solution-with-japanese-tldmv/


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        cur_max = 0
        ans = 0
        for l, w in dimensions:
            d2 = l * l + w * w
            area = l * w
            if d2 > cur_max:
                cur_max = d2
                ans = area
            elif d2 == cur_max:
                ans = max(ans, area)

        return ans
