class Solution:
    def sortString(self, s: str) -> str:
        N = len(s)
        mem = [0 for _ in range(26)]
        ord_a = ord('a')
        for ch in s:
            mem[ord(ch) - ord_a] += 1

        ret = ''
        state = 0
        while N > 0:
            if state == 0:
                for i in range(26):
                    if mem[i] > 0:
                        ret += chr(i + ord_a)
                        mem[i] -= 1
                        N -= 1

                state = 1
            else: # state = 1
                for i in range(25, -1, -1):
                    if mem[i] > 0:
                        ret += chr(i + ord_a)
                        mem[i] -= 1
                        N -= 1

                state = 0

        return ret
