class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        N = len(A)
        A.sort()
        A.reverse()
        for i, a in enumerate(A):
            if i+2 < N:
                b, c = A[i+1], A[i+2]
                if b + c > a:
                    return a + b + c

        return 0
