# Solution Link: https://leetcode.com/problems/fruits-into-baskets-ii/solutions/7045105/python-brute-force-solution-with-japanes-iilx/


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        N = len(fruits)

        ans = 0
        for num in fruits:
            is_placed = False
            for i in range(N):
                if baskets[i] >= num:
                    baskets[i] = 0
                    is_placed = True
                    break

            if not is_placed:
                ans += 1

        return ans
