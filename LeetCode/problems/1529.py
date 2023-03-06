class Solution:
    def minFlips(self, target: str) -> int:
        n = len(target)
        pre = target[n-1]
        ret = 0
        if pre == '1':
            ret += 1
        for i in range(n-1, -1, -1):
            if target[i] == '1':
                if pre == 0:
                    ret += 2
                pre = 1
            else: # target[i] == '0'
                pre = 0

        return ret
