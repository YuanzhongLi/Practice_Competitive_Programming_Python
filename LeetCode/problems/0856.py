class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for ch in s:
            if ch == '(':
                stack.append(0)
            else:
                tmp = 0
                while stack and stack[-1] > 0:
                    tmp += stack.pop()

                if tmp == 0:
                    stack[-1] = 1
                else:
                    stack[-1] = tmp*2
        ret = 0
        for a in stack:
            ret += a
        return ret
