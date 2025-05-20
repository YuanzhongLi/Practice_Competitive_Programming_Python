# Solution Link: https://leetcode.com/problems/type-of-triangle/solutions/6757496/python-math-solution-with-japanese-expla-iix6/


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        mi, mid, ma = nums
        if ma >= mid + mi:
            return "none"

        if ma == mid and mid == mi:
            return "equilateral"

        if ma == mid or mid == mi:
            return "isosceles"

        return "scalene"
