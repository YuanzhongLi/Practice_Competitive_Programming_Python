# Solution Link: https://leetcode.com/problems/maximum-score-from-removing-substrings/solutions/6992729/python-greedy-and-stack-solution-with-ja-10o0/


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def get_max_score(s, x, y):
            first = "a"
            second = "b"
            if x < y:
                first = "b"
                second = "a"
            ma = max(x, y)
            mi = min(x, y)

            ret = 0

            # x, yのうち大きい方maを貪欲にとっていく
            stack = []
            for ch in s:
                if len(stack) > 0:
                    if stack[-1] == first and ch == second:
                        ret += ma
                        stack.pop()
                    else:
                        stack.append(ch)
                else:
                    stack.append(ch)

            # 残ったものから小さい方miを貪欲にとっていく
            stack2 = []
            for ch in stack:
                if len(stack2) > 0:
                    if stack2[-1] == second and ch == first:
                        ret += mi
                        stack2.pop()
                    else:
                        stack2.append(ch)
                else:
                    stack2.append(ch)

            return ret

        N = len(s)
        ans = 0
        is_ab = False
        cur = ""
        for i in range(N):
            if s[i] == "a" or s[i] == "b":
                is_ab = True
                cur += s[i]
            else:
                if is_ab:
                    ans += get_max_score(cur, x, y)
                    is_ab = False
                cur = ""
        if is_ab:
            ans += get_max_score(cur, x, y)
        return ans
