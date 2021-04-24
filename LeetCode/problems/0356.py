INF = float('inf')
class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        s = set([])
        ma_x = -INF; mi_x = INF
        for x, y in points:
            ma_x = max(ma_x, x); mi_x = min(mi_x, x)
            s.add((x, y))

        points = list(s)
        N = len(points)
        axis2 = ma_x + mi_x
        for x, y in points:
            x2 = axis2-x
            if not ((x2, y) in s):
                return False
        return True
