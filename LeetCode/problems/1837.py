class Solution:
    def sumBase(self, n: int, k: int) -> int:
        ret = 0
        while n > 0:
            ret += n % k
            n //= k
        return ret
