# Solution Link: https://leetcode.com/problems/find-the-original-typed-string-i/solutions/6904554/python-enumerate-solution-with-japanese-boen9/


class Solution:
    def possibleStringCount(self, word: str) -> int:
        N = len(word)
        cur_num = 1
        cur_ch = word[0]

        # 全部をうつときのパターンとして1で初期化
        ans = 1
        for i in range(1, N):
            ch = word[i]
            if ch == cur_ch:
                cur_num += 1
            else:
                # 全部をうつときのパターンが重複としてあるのでそれを排除
                ans += cur_num - 1

                cur_ch = ch
                cur_num = 1

        ans += cur_num - 1
        return ans
