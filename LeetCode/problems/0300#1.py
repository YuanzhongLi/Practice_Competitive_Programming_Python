class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        A = [1000000]
        for x in nums:
            if x > A[-1]:
                A.append(x)
                continue

            n = len(A)
            ok = n-1
            ng = -1
            while (abs(ok - ng) > 1):
                mid = (ok + ng) // 2
                if A[mid] >= x:
                    ok = mid
                else:
                    ng = mid
            A[ok] = x

        return len(A)
