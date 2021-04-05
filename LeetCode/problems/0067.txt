class Solution:
    def addBinary(self, A: str, B: str) -> str:
        na = len(A)
        nb = len(B)
        ai = na-1
        bi = nb-1
        carry = 0
        ret = []
        while ai >= 0 or bi >= 0:
            a, b = 0, 0
            if ai >= 0:
                a = int(A[ai])
            if bi >= 0:
                b = int(B[bi])
            su = a + b + carry
            carry = su//2
            ret.append(su%2)
            ai -= 1
            bi -= 1

        if carry > 0:
            ret.append(1)

        ret.reverse()
        return ''.join([str(i) for i in ret])
