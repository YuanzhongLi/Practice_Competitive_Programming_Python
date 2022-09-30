INF = 1000000007
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = []
        for i, interval in enumerate(intervals):
            s, _ = interval
            starts.append((s, i))

        starts.append((INF, -1))
        starts.sort()
        N = len(starts)

        ret = []
        for interval in intervals:
            _, e = interval
            ok = N - 1
            ng = -1
            while abs(ok - ng) > 1:
                mid = (ok + ng) >> 1
                if starts[mid][0] >= e:
                    ok = mid
                else:
                    ng = mid
            ret.append(starts[ok][1])

        return ret
