from collections import defaultdict
class Solution:
    def minSetSize(self, A: List[int]) -> int:
        mem = defaultdict(int)
        for a in A:
            mem[a] += 1

        cnts = []
        for num in mem:
            cnts.append(mem[num])
        cnts.sort()
        cnts.reverse()

        tmp = 0
        ans = 0
        for c in cnts:
            ans += 1
            tmp += c
            if tmp * 2 >= len(A):
                return ans
