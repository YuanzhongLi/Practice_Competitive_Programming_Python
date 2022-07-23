INF = float('inf')
def parse(s):
    tmp = []
    for ch in s:
        if ch == ')':
            find = False
            for i in range(len(tmp)-1, -1, -1):
                if tmp[i] == '(':
                    tmp[i] = ''
                    find = True
                    break
            if not find:
                tmp.append(ch)
        else:
            tmp.append(ch)
    ret = []
    for ch in tmp:
        if ch != '':
            ret.append(ch)
    return ret

class Solution:
    def checkValidString(self, s: str) -> bool:
        A = parse(s)
        r_last, l_first = -1, INF
        for i,ch in enumerate(A):
            if ch == ')': r_last = max(r_last, i)
            elif ch == '(': l_first = min(l_first, i)

        if r_last != -1:
            cnt = 0
            for i in range(r_last+1):
                ch = A[i]
                if ch == '*':
                    cnt += 1
                elif ch == ')':
                    if cnt == 0:
                        return False
                    else:
                        cnt -= 1

        if l_first != INF:
            cnt = 0
            for i in range(l_first, len(A)):
                ch = A[i]
                if ch == '*':
                    cnt -= 1; cnt = max(cnt, 0)
                elif ch == '(':
                    cnt += 1
            if cnt > 0:
                return False

        return True
