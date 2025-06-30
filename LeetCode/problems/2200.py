# Solution Link: https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/solutions/6878205/python-2-pointer-solution-for-memory-o1-9nvu9/


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        N = len(nums)
        ans = []
        for i in range(N):
            if nums[i] == key:
                last_idx = -1 if len(ans) == 0 else ans[-1]
                for j in range(max(i - k, last_idx + 1), min(i + k + 1, N)):
                    ans.append(j)

        return ans
