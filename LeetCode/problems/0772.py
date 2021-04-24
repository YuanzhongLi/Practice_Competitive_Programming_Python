class C:
    def __init__(self, outer = None, inner = None):
        self.stack = [0]
        self.outer = outer
        self.inner = inner

def is_mul_div(ch):
    return ch == '*' or ch == '/'

def isop(ch):
    return ch == '+' or ch == '-' or ch == '*' or ch == '/'

def check(stack):
    return len(stack) == 1 and type(stack[0]) == type(0)

def calc(op, a, b):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    else:
        sign_a = 1 if a >= 0 else -1
        sign_b = 1 if b >= 0 else -1
        sign = sign_a*sign_b
        return sign * (abs(a)//abs(b))

def calc_stack(stack):
    ret = 0
    sign = 1
    for ele in stack:
        if isop(ele):
            if ele == '-': sign = -1
            else: sign = 1
        else:
            ret += sign * int(ele)
    return ret

def getNumber(s, i):
    N = len(s)
    ret = ""
    while i < N:
        if s[i].isdigit():
            ret += s[i]
        else:
            break
        i += 1
    return int(ret), i-1


class Solution:
    def calculate(self, s: str) -> int:
        cur = C()
        N = len(s)
        i = 0
        while i < N:
            ch = s[i]
            if ch == '(':
                cur.inner = C(outer = cur)
                cur = cur.inner
            elif ch == ')':
                b = calc_stack(cur.stack)
                cur = cur.outer
                stack = cur.stack
                if check(stack):
                    stack[0] += b
                elif cur.stack and is_mul_div(stack[-1]) :
                    op = stack.pop()
                    a = stack.pop()
                    stack.append(calc(op, a, b))
                else:
                    stack.append(b)
            elif isop(ch):
                stack = cur.stack
                stack.append(ch)
            else: # number
                b, i = getNumber(s, i)
                stack = cur.stack
                if check(stack):
                    stack[0] += b
                elif cur.stack and is_mul_div(stack[-1]):
                    op = stack.pop()
                    a = stack.pop()
                    stack.append(calc(op,a,b))
                else:
                    stack.append(b)

            i+=1

        return calc_stack(cur.stack)
