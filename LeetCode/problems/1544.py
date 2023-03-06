class Solution:
    def makeGood(self, s: str) -> str:
        ret = ""
        n = len(s)
        stack = []
        for ch in s:
            if len(stack) == 0:
                stack.append(ch)
            else:
                if stack[-1] != ch and stack[-1].upper() == ch.upper():
                    stack.pop()
                else:
                    stack.append(ch)

        return ''.join(stack)
