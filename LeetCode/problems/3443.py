# Solution Link: https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/solutions/6863667/python-enumerate-solution-with-japanese-fhedz/


class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        cnt = defaultdict(int)
        ans = 0
        for ch in s:
            cnt[ch] += 1
            NE = cnt["N"] + cnt["E"]
            NW = cnt["N"] + cnt["W"]
            SE = cnt["S"] + cnt["E"]
            SW = cnt["S"] + cnt["W"]

            # 北東, 北西, 南東, 南西へのmax距離をそれぞれ求める
            NE_max = NE - max(0, SW - k) + min(k, SW)
            NW_max = NW - max(0, SE - k) + min(k, SE)
            SE_max = SE - max(0, NW - k) + min(k, NW)
            SW_max = SW - max(0, NE - k) + min(k, NE)

            ans = max(ans, NE_max, NW_max, SE_max, SW_max)

        return ans
