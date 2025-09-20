# Solution Link: https://leetcode.com/problems/find-closest-person/solutions/7152993/python-abs-solution-with-japanese-explan-3sia/


class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        d1 = abs(x - z)
        d2 = abs(y - z)
        if d1 < d2:
            return 1
        if d2 < d1:
            return 2

        return 0
