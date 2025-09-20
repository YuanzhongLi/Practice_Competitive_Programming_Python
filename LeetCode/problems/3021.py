# Solution Link: https://leetcode.com/problems/alice-and-bob-playing-flower-game/solutions/7133348/python-math-solution-with-japanese-expla-7vpk/


class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        return ((n + 1) // 2) * (m // 2) + (n // 2) * ((m + 1) // 2)
