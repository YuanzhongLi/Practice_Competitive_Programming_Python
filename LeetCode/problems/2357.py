class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        s = set([])
        for n in nums:
            if n > 0:
                s.add(n)

        return len(s)
