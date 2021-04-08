"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
INF = float('inf')
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = []
        for ary in schedule:
            for ele in ary:
                s,e = ele.start, ele.end
                intervals.append((s,e))
        intervals.sort()
        free_intervals = []
        cur = -INF
        for s, e in intervals:
            if cur < s:
                free_intervals.append((cur, s))
                cur = e
            else:
                cur = max(cur, e)
        ret = []
        for i in range(1, len(free_intervals)):
            ret.append(Interval(free_intervals[i][0], free_intervals[i][1]))
        return ret
