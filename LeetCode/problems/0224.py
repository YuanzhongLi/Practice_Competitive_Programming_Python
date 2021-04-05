def getNum(i, s):
    N = len(s)
    ret = ""
    while i < N and s[i].isdigit():
        ret += s[i]
        i += 1
    return int(ret[::-1]), i

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        s = s[::-1]
        N = len(s)
        i = 0
        while i < N:
            ch = s[i]
            if ch == ' ':
                i+=1
            elif ch == '-':
                stack.append('-')
                i+=1
            elif ch == '+':
                stack.append('+')
                i+=1
            elif ch == ')':
                stack.append(')')
                i+=1
            elif ch == '(':
                sign = 1
                tmp = 0
                while stack[-1] != ')':
                    if stack[-1] == '-':
                        sign = -1
                    elif stack[-1] == '+':
                        sign = 1
                    else:
                        tmp += sign * stack[-1]
                    stack.pop()
                if stack: # pop ')'
                    stack.pop()
                stack.append(tmp)
                i += 1
            else: # number
                num, i = getNum(i, s)
                stack.append(num)
        ans = 0
        sign = 1
        while stack:
            if stack[-1] == '-':
                sign = -1
            elif stack[-1] == '+':
                sign = 1
            else:
                ans += sign * stack[-1]
            stack.pop()

        return ans
