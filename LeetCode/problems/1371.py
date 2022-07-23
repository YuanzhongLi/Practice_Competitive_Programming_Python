INF = float('inf')

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        D = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        mp = [INF for _ in range(32)]; mp[0] = -1
        state = 0
        ret = 0
        for i,ch in enumerate(s):
            if ch in D:
                state ^= (1<<D[ch])

            ret = max(ret, i-mp[state])
            mp[state] = min(mp[state], i)

        return ret
