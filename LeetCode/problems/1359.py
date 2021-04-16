mod = int(1e9)+7
def add(x, y):
    global mod
    return (x + y)%mod

class Solution:
    def countOrders(self, n: int) -> int:
        ret = 1
        for i in range(1, n+1):
            ret = mul(ret, i)
        for i in range(1, n+1):
            ret = mul(ret, 2*i-1)
        return ret
