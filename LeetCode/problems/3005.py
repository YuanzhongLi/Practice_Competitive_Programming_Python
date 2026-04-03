# Solution Link: https://leetcode.com/problems/count-elements-with-maximum-frequency/solutions/7212165/python-dict-solution-with-japanese-expla-m8m7/


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        max_cnt = 0
        for num in nums:
            counter[num] += 1
            max_cnt = max(max_cnt, counter[num])

        ans = 0
        for num in counter:
            if counter[num] == max_cnt:
                ans += counter[num]

        return ans
