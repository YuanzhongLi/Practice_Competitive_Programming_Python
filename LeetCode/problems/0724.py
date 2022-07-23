class Solution:
    def pivotIndex(self, A: List[int]) -> int:
        N = len(A)
        su = [0 for _ in range(N)]
        su[0] = A[0]
        for i in range(1, N):
            su[i] = A[i] + su[i-1]

        for i in range(N):
            if i == 0:
                if su[N-1] - su[i] == 0:
                    return i
            else:
                if su[N-1] - su[i] == su[i-1]:
                    return i
        return -1
