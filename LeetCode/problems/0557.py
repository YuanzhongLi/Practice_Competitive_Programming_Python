class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        ret = ''
        for ch in s:
            if ch == ' ':
                while len(stack) > 0:
                    ret += stack.pop()
                ret += ' '
            else:
                stack.append(ch)

        while len(stack) > 0:
            ret += stack.pop()

        return ret
