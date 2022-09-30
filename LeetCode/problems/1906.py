MAX = 101

def getMin(ary):
    tmp = []
    for i in range(MAX):
        if ary[i] > 0:
            tmp.append(i)

    if len(tmp) == 1:
        return -1

    ret = MAX
    for i in range(len(tmp) - 1):
        ret = min(ret, tmp[i+1] - tmp[i])
    return ret


class Solution:
    def minDifference(self, A: List[int], Q: List[List[int]]) -> List[int]:
        N = len(A)
        mem = [[0 for _ in range(MAX)] for _ in range(N+1)]
        for i in range(N):
            a = A[i]
            for j in range(MAX):
                mem[i+1][j] = mem[i][j]
            mem[i+1][a] += 1

        # print(mem)

        ret = []
        for q in Q:
            l, r = q
            ary = [0 for _ in range(MAX)]
            for i in range(MAX):
                ary[i] = mem[r+1][i] - mem[l][i]
            ret.append(getMin(ary))

        return ret
