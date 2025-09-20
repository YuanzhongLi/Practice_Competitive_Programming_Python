# Solution Link: https://leetcode.com/problems/maximum-average-pass-ratio/solutions/7143100/python-heap-and-greedy-solution-with-japanese-explanation/

from heapq import heappush, heappop


class Class:
    def __init__(self, p, t):
        self.p = p
        self.t = t
        # som / mom: extraを1人追加した時の増加幅(= (p+1/t+1) - p/t)
        self.son = t - p
        self.mom = t * (t + 1)

    def __lt__(self, c):
        # heapでson / mom が大きい順に取り出せる様に
        return self.son * c.mom > self.mom * c.son


class Solution:
    def maxAverageRatio(self, A: List[List[int]], ex: int) -> float:
        N = len(A)
        hq = []
        for (
            a,
            b,
        ) in A:
            heappush(hq, Class(a, b))

        while ex:
            ex -= 1
            top = heappop(hq)
            heappush(hq, Class(top.p + 1, top.t + 1))

        ans = 0.0
        for obj in hq:
            ans += obj.p / obj.t

        return ans / N
