class Solution:
    def maxFrequency(self, A: List[int], k: int) -> int:
        A.sort()
        ret = 1
        su = [0 for _ in range(len(A))]
        su[0] = A[0]
        for i in range(1, len(A)):
            a = A[i]
            su[i] = a+su[i-1]
            ok = i; ng = -1
            while (abs(ok-ng) > 1):
                mid = (ok+ng)//2
                tmp = 0
                if mid-1 >= 0:
                    tmp = su[mid-1]
                if k + (su[i]-tmp) >= a * (i-mid+1):
                    ok = mid
                else:
                    ng = mid
            ret = max(ret, i-ok+1)
        return ret
