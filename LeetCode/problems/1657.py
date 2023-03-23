from collections import defaultdict

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        mp1 = defaultdict(int)
        mp2 = defaultdict(int)
        for ch in word1:
            mp1[ch] += 1
        for ch in word2:
            mp2[ch] += 1

        for ch in mp1.keys():
            if not (ch in mp2):
                return False

        for ch in mp2.keys():
            if not (ch in mp1):
                return False

        ar1 = []
        ar2 = []
        for cnt in mp1.values():
            ar1.append(cnt)
        ar1.sort()
        for cnt in mp2.values():
            ar2.append(cnt)
        ar2.sort()

        if len(ar1) == len(ar2):
            for i in range(len(ar1)):
                if ar1[i] != ar2[i]:
                    return False
            return True
        else:
            return False
