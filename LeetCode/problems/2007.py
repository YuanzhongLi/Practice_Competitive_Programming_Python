class Solution:
    def findOriginalArray(self, A: List[int]) -> List[int]:
        mem = [0 for _ in range(200010)]
        ret = []
        zero = 0
        for a in A:
            if a == 0:
                zero += 1
            else:
                mem[a] += 1

        if (zero & 1) == 1:
            return []

        for _ in range(zero >> 1):
            ret.append(0)

        for i in range(1, 100003):
            num = mem[i]
            if  num > 0:
                if mem[i * 2] >= num:
                    mem[i * 2] -= num
                    for _ in range(num):
                        ret.append(i)
                else:
                    return []

        return ret
