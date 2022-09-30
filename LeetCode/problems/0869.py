def cnt(n):
    ret = [0 for _ in range(10)]
    while n > 0:
        ret[n % 10] += 1
        n //= 10
    return ret

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        n_cnt = cnt(n)
        b = 1
        for _ in range(40):
            b_cnt = cnt(b)
            flag = True
            for i in range(10):
                flag &= (n_cnt[i] == b_cnt[i])
                if not flag:
                    break

            if flag:
                return True
            b *= 2

        return False
