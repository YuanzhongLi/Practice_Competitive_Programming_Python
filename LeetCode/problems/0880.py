class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        if k == 0:
            for i in range(len(s)-1, -1, -1):
                if not s[i].isdigit(): return s[i]

        ch_num = 0
        for i,ch in enumerate(s):
            if ch.isdigit():
                if ch_num * int(ch) >= k:
                    return self.decodeAtIndex(s[:i], k%ch_num)
                ch_num *= int(ch)
            else:
                ch_num += 1
                if ch_num == k:
                    return ch
