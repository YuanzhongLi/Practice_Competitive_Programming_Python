from collections import defaultdict
class Solution:
    def canConstruct(self, A: str, B: str) -> bool:
        mem = defaultdict(int)
        for ch in B:
            mem[ch] += 1

        for ch in A:
            if mem[ch] > 0:
                mem[ch] -= 1
            else:
                return False

        return True
