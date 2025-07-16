# Solution Link: https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/solutions/6964675/python-bit-solution-with-japanese-explan-rx9a/


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # 4パターンのみ
        # 0, 0, 0, 0, ...
        # 0, 1, 0, 1, ...
        # 1, 0, 1, 0, ...
        # 1, 1, 1, 1, ...

        odds, evens = 0, 0
        prev = -1
        # 0, 1または1, 0と交互のパターン
        cross = 0
        for num in nums:
            bi = num & 1
            if bi == 1:
                odds += 1
            else:
                evens += 1

            if prev == -1:
                cross = 1
                prev = bi
            elif prev != bi:
                cross += 1
                prev = bi

        return max(odds, evens, cross)
