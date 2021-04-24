def f(A, B):
    N = len(A)
    M = len(B)
    ret = 0
    for i in range(N):
        alt = 0
        tmp = 0
        for j in range(M):
            a_idx = j+i
            if a_idx == N: break
            b_idx = j
            if A[a_idx] == B[b_idx]:
                tmp += 1
                ret = max(ret, tmp)
            else: tmp = 0
    return ret

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        return max(f(A, B), f(B, A))
