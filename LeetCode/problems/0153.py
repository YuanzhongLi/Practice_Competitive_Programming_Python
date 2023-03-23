class Solution:
    def findMin(self, A: List[int]) -> int:
        def rec(l, r):
            if A[l] <= A[r-1]:
                return A[l]
            mid = (l+r)//2
            return min(rec(l, mid), rec(mid, r))

        return rec(0, len(A))
