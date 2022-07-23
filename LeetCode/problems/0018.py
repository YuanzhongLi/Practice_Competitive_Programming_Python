from collections import defaultdict
class Solution:
    def fourSum(self, A: List[int], target: int) -> List[List[int]]:
        A.sort()
        N = len(A)
        mp = defaultdict(int)
        for a in A: mp[a] += 1

        s = set([])
        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1, N-1):
                    a, b, c = A[i], A[j], A[k]
                    su = a+b+c
                    d = target-su
                    if d < c:
                        break
                    else:
                        if mp[d] > 0:
                            s.add((a, b, c, d))

        ret = []
        for a, b, c, d in list(s):
            tmp = defaultdict(int)
            tmp[a] += 1
            tmp[b] += 1
            tmp[c] += 1
            tmp[d] += 1
            ok = True
            for key in tmp.keys():
                if mp[key] < tmp[key]:
                    ok = False
                    break
            if ok:
                ret.append([a, b, c, d])

        return ret
