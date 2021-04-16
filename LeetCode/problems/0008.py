def is_digit(ch):
    return ord('0') <= ord(ch) and ord(ch) <= ord('9')

def parse(s):
    N = len(s)
    flag = False
    ret = ""
    for i in range(N):
        ch = s[i]
        if flag:
            if is_digit(ch):
                ret += ch
            else:
                flag = False; break
        else:
            if ch == ' ': continue
            elif ch == '+':
                flag = True
            elif ch == '-':
                ret += ch
                flag = True
            elif is_digit(ch):
                ret += ch
                flag = True
            else:
                flag = False; break
    return ret

def check(s):
    if s[0] == '-':
        for i in range(1, len(s)):
            if not is_digit(s[i]): return False
        return -1, True
    else:
        for i in range(len(s)):
            if not is_digit(s[i]): return False
        return 1, True

def remove_leading0(s):
    ret = ""
    flag = False
    for ch in s:
        if not flag:
            if ch == '0':
                continue
            else:
                flag = True
                ret += ch
        else:
            ret += ch
    return ret

MAX = (1<<31)+7
FMAX = float(MAX)
def overflow(s):
    d = 1.0
    d2 = 1
    cur = 0.0
    ret = 0
    for ch in s[::-1]:
        cur += d*float(ch)
        if cur >= FMAX: return MAX
        ret += d2*int(ch)
        d *= 10.0
        d2 *= 10

    if ret > (1<<31): return MAX
    return ret


def getNumber(s):
    s = parse(s)
    if s == "": return '0'
    sign, ok = check(s)
    if not ok:
        return '0'
    if sign == -1:
        s = s[1:]
    s = remove_leading0(s)
    if s == "": return 0
    num = overflow(s)
    ans = 0
    if sign == 1:
        if num == MAX or num == (1<<31):
            ans = (1<<31)-1
        else: ans = num
    else:
        if num == MAX:
            ans = -(1<<31)
        else: ans = -num
    return str(ans)

class Solution:
    def myAtoi(self, s: str) -> int:
        return getNumber(s)
