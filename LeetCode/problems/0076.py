def counter(s):
    mp = {}
    for i in range(26):
        mp[chr(i+ord('a'))] = 0
        mp[chr(i+ord('A'))] = 0
    for ch in s:
        mp[ch] += 1
    return mp

letters = []
for i in range(26):
    letters.append(chr(i+ord('A')))
for i in range(26):
    letters.append(chr(i+ord('a')))

def check(mem, mp_t):
    for letter in letters:
        if mem[letter] < mp_t[letter]:
            return False
    return True

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mp_s = counter(s)
        mp_t = counter(t)
        if not check(mp_s, mp_t):
            return ""

        N = len(s)
        l = 0
        r = 0
        ans = [0, N-1]
        mem = {}
        for i in range(26):
            mem[chr(i+ord('a'))] = 0
            mem[chr(i+ord('A'))] = 0

        while r < N:
            mem[s[r]] += 1
            if check(mem, mp_t):
                if r-l < ans[1] - ans[0]:
                    ans[0], ans[1] = l, r
                while l <= r:
                    mem[s[l]] -= 1
                    l += 1
                    if check(mem, mp_t):
                        if r - l < ans[1] - ans[0]:
                            ans[0], ans[1] = l, r
                    else:
                        break
            r += 1
            # print("l: {0}, r: {1}".format(l, r))
            # print('-----')

        ret = ""
        for i in range(ans[0], ans[1]+1):
            ret += s[i]
        return ret
