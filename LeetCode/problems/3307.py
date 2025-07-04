# Solution Link: https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/solutions/6917252/python-bit-solution-with-japanese-explan-97vd/


class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        k -= 1
        ord_ch = 0
        i = 0
        while k > 0:
            if (k & 1) == 1 and operations[i] == 1:
                ord_ch += 1
            k >>= 1
            i += 1

        ord_ch %= 26
        return chr(ord_ch + ord("a"))
