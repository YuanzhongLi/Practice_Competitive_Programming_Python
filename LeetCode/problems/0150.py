def isop(s):
    return s == '+' or s == '-' or s == '*' or s == '/'

def calc(op, a, b):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    else:
        a_sign = 1 if a >= 0 else -1
        b_sign = 1 if b >= 0 else -1
        sign = a_sign * b_sign
        return sign * (abs(a)//abs(b))

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if isop(token):
                b = stack.pop()
                a = stack.pop()
                stack.append(calc(token, a, b))
            else:
                stack.append(int(token))
        return stack[0]
