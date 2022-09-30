from collections import defaultdict
from functools import cmp_to_key
def cmp(a, b):
    if a[1] < b[1]:
        return -1
    elif a[1] > b[1]:
        return 1
    elif a[0] > b[0]:
        return -1
    elif a[0] < b[0]:
        return 1
    else:
        return 0

class Solution:
    def frequencySort(self, A: List[int]) -> List[int]:
        mem = defaultdict(int)
        for a in A:
            mem[a] += 1
        tmp = []
        for key in mem:
            tmp.append([key, mem[key]])

        tmp.sort(key = cmp_to_key(cmp))
        ret = []
        for x in tmp:
            a, b = x
            for _ in range(b):
                ret.append(a)

        return ret
