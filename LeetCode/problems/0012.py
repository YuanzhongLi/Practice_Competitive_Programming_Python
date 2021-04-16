mp = [['I', 'V'], ['X', 'L'], ['C', 'D'], ['M']]

def getRoman(x, d):
    if x == 0: return ""
    elif x <= 4:
        if x == 4:
            return mp[d][0] + mp[d][1]
        else:
            return mp[d][0] * x
    else: # 5 <= x <= 9:
         if x == 9:
            return mp[d][0] + mp[d+1][0]
         else:
            return mp[d][1] + mp[d][0] * (x-5)

def I2A(x):
    ret  = []
    while x > 0:
        ret.append(x%10)
        x //= 10
    return ret

class Solution:
    def intToRoman(self, num: int) -> str:
        A = I2A(num)
        ret = []
        for d, a in enumerate(A):
            ret.append(getRoman(a, d))
        ret.reverse()
        return ''.join(ret)
