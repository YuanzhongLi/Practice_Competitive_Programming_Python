class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)

        ans = [[], []]
        for n1 in s1:
            if not (n1 in s2):
                ans[0].append(n1)

        for n2 in s2:
            if not (n2 in s1):
                ans[1].append(n2)

        return ans
