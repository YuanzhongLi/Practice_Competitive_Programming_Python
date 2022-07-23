INF = float("inf")
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        N = len(s)
        mem = [[] for i in range(26)]
        for i, ch in enumerate(s):
            mem[ord(ch)-ord("a")].append(i)
        for i in range(26):
            mem[i].append(INF)

        def check(word):
            cur = -1
            for ch in word:
                A = mem[ord(ch)-ord("a")]
                ng = -1
                ok = len(A)-1
                while abs(ok - ng) > 1:
                    mid = (ok + ng)//2
                    if A[mid] > cur:
                        ok = mid
                    else:
                        ng = mid
                cur = A[ok]
                if cur == INF:
                    return False
            return True

        ret = 0
        for word in words:
            if check(word):
                ret += 1
        return ret
