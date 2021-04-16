ops = {"+": 0, "-": 1, "*": 2, "/": 3}
def getNum(ary):
    N = len(ary)
    d = 1
    ret = 0
    for i in range(N-1, -1, -1):
        ret += int(ary[i])*d
        d *= 10
    return ret

def f(op, a, b): # a op b
    if op == 0:
        return a+b
    elif op == 1:
        return a-b
    elif op == 2:
        return a*b
    else:
        return a//b

def calc_mul_div(s): # [2, "*", 2, "/", 3]
    N = len(s)
    ret = 1
    op = 2
    for i in range(N):
        if i%2 == 0: # number
            ret = f(op, ret, s[i])
        else:
            op = ops[s[i]]
    return ret # result: 1

def parse(s):
    A = []
    for ch in s: # remove space
        if ch != " ":
            A.append(ch)

    ret = []
    N = len(A)
    i = 0
    while i < N:
        if A[i].isdigit():
            tmp = []
            while i < N and A[i].isdigit():
                tmp.append(A[i])
                i+=1
            num = getNum(tmp)
            ret.append(num)
        else:
            ret.append(A[i])
            i+=1
    return ret

class Solution:
    def calculate(self, s: str) -> int:
        A = parse(s)
        N = len(A)
        i = 0
        ans = 0
        op = 0 # 0: +, 1: -, 2: *, 3: /
        while i < N:
          a = A[i]
          if i%2 == 0: # a is Number
            if i == N-1:
                ans = f(op, ans, a)
                break
            else:
                next_op = ops[A[i+1]]
                if next_op <= 1: # next op is + or -
                    ans = f(op, ans, a)
                    i+=1
                else: # next op is * or /
                    l = i; r = i+2
                    j = i+1
                    while j < N:
                        if ops[A[j]] >= 2: # op A[j] is * or /
                            r = j+1
                            j += 2
                        else:
                            break
                    num = calc_mul_div(A[l:r+1])
                    ans = f(op, ans, num)
                    i = r+1
          else:
              op = ops[A[i]]
              i += 1

        return ans
