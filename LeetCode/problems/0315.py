# BIT solution

# 0, 1, 2, 3, 4, 5, 6, 7...
# [0, 1, 1, 0, 0, 1, 1, 0 ….]

# 0-indexed
class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0 for _ in range(n)]
    # sum [0, i]
    def sum(self, i):
        ret = 0
        while i >= 0:
            ret += self.data[i]
            i = (i&(i+1)) -1
        return ret

    # sum[i, j]
    def sum_between(self, i, j):
        if i > j: return 0
        return self.sum(j) - self.sum(i-1)

    def add(self, i, x):
        while i < self.n:
            self.data[i] += x
            i |= (i+1)
        return

base = 10000
class Solution:
    def countSmaller(self, A: List[int]) -> List[int]:
        N = len(A)
        bit = BIT(20005)
        for a in A:
            bit.add(a+base, 1)
        ret = []
        for a in A:
            ret.append(bit.sum(a+base-1))
            bit.add(a+base, -1)

        return ret

# merge sort solution
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        N = len(nums)
        nums = [(num, i) for i,num in enumerate(nums)]
        ans = [0 for _ in range(N)]
        def merge(A, B): # [(2,1), (5, 0)], [(1, 3), (6, 2)]
            na = len(A); nb = len(B)
            i = j = 0
            cnt = 0
            ret = []
            while i < na or j < nb:
                if i < na and j < nb:
                    a, aid = A[i]; b, bid = B[j]
                    if a > b:
                        ret.append(B[j]); cnt += 1; j += 1
                    else:
                        ret.append(A[i]);
                        ans[aid] += cnt
                        i += 1

                elif i < na:
                    a, aid = A[i]
                    ret.append(A[i])
                    ans[aid] += cnt
                    i+=1
                elif j < nb:
                    ret.append(B[j]); j += 1
            return ret

        def mergeSort(A):
            M = len(A)
            if M <= 1:
                return A
            ret = merge(mergeSort(A[:M//2]), mergeSort(A[M//2:]))
            return ret

        nums = mergeSort(nums)
        return ans
