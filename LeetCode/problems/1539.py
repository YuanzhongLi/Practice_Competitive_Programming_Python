class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        N = len(arr)
        s = set(arr)
        cnt = 0
        for i in range(1, N + k + 5):
            if not (i in s):
                cnt += 1
            if cnt == k:
                return i

        return 1
