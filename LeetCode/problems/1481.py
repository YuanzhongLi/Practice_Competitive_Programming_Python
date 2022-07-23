from collections import defaultdict
class Solution:
    def findLeastNumOfUniqueInts(self, A: List[int], k: int) -> int:
        N = len(A)
        mp = defaultdict(int)
        for a in A:
            mp[a]+=1

        mem = [0 for _ in range(N+1)]
        for v in mp.values():
            mem[v] += 1

        for i in range(1, N+1):
            m = mem[i]
            if k >= i*m:
                mem[i] = 0
                k -= i*m
            else:
                q = k//i
                mem[i] -= q
                break

        ret = 0
        for i in range(1, N+1):
            ret += mem[i]
        return ret
