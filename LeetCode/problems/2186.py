class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_cnt = [0 for _ in range(26)]
        t_cnt = [0 for _ in range(26)]
        for ch in s:
            s_cnt[ord(ch)-ord("a")] += 1
        for ch in t:
            t_cnt[ord(ch)-ord("a")] += 1

        ret = 0
        for i in range(26):
            ret += abs(s_cnt[i] - t_cnt[i])

        return ret
