# Solution Link: https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/solutions/6784730/python-math-solution-with-japanese-explanation/


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # 1, ..., nの合計
        n_sum = (n + 1) * n // 2

        # n以下のmの倍数の数
        divisible_num = n // m

        # n以下のmの倍数の合計
        divisible_sum = m * (divisible_num + 1) * divisible_num // 2

        return n_sum - 2 * divisible_sum
