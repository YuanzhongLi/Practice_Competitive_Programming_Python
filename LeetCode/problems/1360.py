def f1(y): # calc date from 0000
    return y * 365 + (y // 4) - (y // 100) + (y // 400)

MD = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def f2(y, m, d): # calc date from y-01-01
    ret = d
    if m >= 3:
        if y % 400 == 0:
            ret += 31 + 29
        elif y % 100 == 0:
            ret += 31 + 28
        elif y % 4 == 0:
            ret += 31 + 29
        else:
            ret += 31 + 28

        for i in range(2, m-1):
            ret += MD[i]
    else:
        for i in range(m-1):
            ret += MD[i]

    return ret

def f(y1, m1, d1, y2, m2, d2):
    tmp1 = f1(y1-1) + f2(y1, m1, d1)
    tmp2 = f1(y2-1) + f2(y2, m2, d2)
    return abs(tmp1 - tmp2)


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        y1, m1, d1 = date1.split('-')
        y2, m2, d2 = date2.split('-')
        return f(int(y1), int(m1), int(d1), int(y2), int(m2), int(d2))
