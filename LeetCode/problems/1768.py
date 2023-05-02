from collections import deque
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        N1 = len(word1)
        N2 = len(word2)
        i1 = 0
        i2 = 0
        ret = ""
        while i1 < N1 or i2 < N2:
            if i1 < N1 and i2 < N2:
                if len(ret) % 2 == 0:
                    ret += word1[i1]
                    i1 += 1
                else:
                    ret += word2[i2]
                    i2 += 1

            elif i1 < N1:
                ret += word1[i1]
                i1 += 1
            elif i2 < N2:
                ret += word2[i2]
                i2 += 1
        return ret
