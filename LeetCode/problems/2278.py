class Solution:
    def percentageLetter(self, s: str, c: str) -> int:
        N = len(s)
        cnt = 0
        for ch in s:
            if ch == c:
                cnt += 1

        return cnt * 100 // N
