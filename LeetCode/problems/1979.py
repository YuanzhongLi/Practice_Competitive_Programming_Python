class Solution:
    def findGCD(self, A: List[int]) -> int:
        ma = 0
        mi = 10000
        for a in A:
            ma = max(ma, a)
            mi = min(mi, a)

        a = ma
        b = mi
        while True:
            tmp = a % b
            if tmp == 0:
                return b
            a = b
            b = tmp
