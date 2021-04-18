# n: left, m: right, n+m = k
# n, m=k-n
# sum[0:n] + sum[N-m:N]
# sum_array[i] = sum[:i]
# sum[i:j] = sum[j] - sum[i]
# O(N)
class Solution:
    def maxScore(self, A: List[int], k: int) -> int:
        N = len(A)
        for i in range(1, N):
            A[i] += A[i-1]

        ret = 0
        def sum(i, j): #[i, j]
            if i > j: return 0
            elif i == 0: return A[j]
            else: return A[j]-A[i-1]

        for n in range(k+1):
            m = k-n
            left = sum(0, n-1)
            right = sum(N-m, N-1)
            su = left + right
            ret = max(ret, su)
        return ret
