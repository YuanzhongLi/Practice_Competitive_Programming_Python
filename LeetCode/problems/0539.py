def parse(s):
    HH, MM =  s.split(':')
    h = int(HH)
    m = int(MM)
    return h, m

def getMinute(h, m):
    return h *60 + m

class Solution:
    def findMinDifference(self, A: List[str]) -> int:
        B = []
        for i, s in enumerate(A):
            h, m = parse(s)
            minute = getMinute(h, m)
            B.append(minute)
            B.append(minute+24*60)
        B.sort()
        ret = float('inf')
        for i in range(len(B)-1):
            ret = min(ret, B[i+1]-B[i])
        return ret
