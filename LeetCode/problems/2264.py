# Solution Link: https://leetcode.com/problems/largest-3-same-digit-number-in-string/solutions/7078449/python-enumerate-solution-with-japnese-e-124p/


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        N = len(num)
        pp, p = num[0], num[1]

        ma = -1
        for i in range(2, N):
            c = num[i]
            if c == p and c == pp:
                ma = max(ma, int(c))

            pp, p = p, c

        if ma == -1:
            return ""

        return str(ma) * 3
