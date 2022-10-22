class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i,n in enumerate(nums):
            if n in d:
                if i - d[n][-1] <= k:
                    return True
                d[n].append(i)
            else:
                d[n] = [i]

        return False
