class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        N = len(word1)
        cnt1 = [0 for _ in range(26)]
        cnt2 = [0 for _ in range(26)]
        ord_a = ord('a')
        for i in range(N):
            ch1 = word1[i]
            ch2 = word2[i]
            cnt1[ord(ch1)-ord_a] += 1
            cnt2[ord(ch2)-ord_a] += 1

        for i in range(26):
            if abs(cnt1[i] - cnt2[i]) > 3:
                return False

        return True
