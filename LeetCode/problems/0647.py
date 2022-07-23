from collections import deque
class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        q = deque([])
        for i in range(N):
            q.append((i,i))
            if i < N-1 and s[i] == s[i+1]:
                q.append((i,i+1))

        ans = 0
        while q:
            l, r = q.popleft()
            ans += 1
            ll, rr = l-1, r+1
            if 0 <= ll and rr < N and s[ll] == s[rr]:
                q.append((ll, rr))

        return ans
