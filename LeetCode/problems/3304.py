# Solution Link: https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/solutions/6913018/python-bit-solution-with-japanese-explan-t43q/


class Solution:
    def kthCharacter(self, k: int) -> str:
        # bitで考える

        ord_ch = -1
        # 最初の0が続いてるか
        is_seq0 = True
        while k > 0:
            if (k & 1) == 1:
                is_seq0 = False
                ord_ch += 1
            elif is_seq0:
                ord_ch += 1

            k >>= 1

        ord_ch %= 26
        return chr(ord_ch + ord("a"))
