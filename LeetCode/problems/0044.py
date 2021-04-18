from collections import deque

def equal(s, p):
    for i in range(len(s)):
        if not (s[i] == p[i] or p[i] == '?'):
            return False
    return True

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 1. a … ?
        # 2. *a...a, a…*
        # 3. *a...a* -> remove * , ex) a*b*?c -> ab?c: if s has substring "ab?c"
        s = deque(list(s))
        p = deque(list(p))
        while s and p and p[0] != '*':
            if s[0] == p[0] or p[0] == '?':
                s.popleft(); p.popleft()
            else:
                return False

        while s and p and p[-1] != '*':
            if s[-1] == p[-1] or p[-1] == '?':
                s.pop(); p.pop()
            else:
                return False

        if (not s) and (not p): return True
        if s and (not p): return False
        if p[0] != '*' or p[-1] != '*': return False

        removed_p = deque([])
        tmp = ""
        for ch in p:
            if ch != '*':
                tmp += ch
            else:
                if tmp:
                    removed_p.append(tmp)
                tmp = ""

        s = ''.join(s)


        N = len(s)
        M = len(removed_p)
        ids = 0; idp = 0

        match_cnt = 0
        while ids < N and idp < M:
            cur_p = removed_p[idp]
            size = len(cur_p)
            if ids + size > N:
                return False
            else:
                if equal(s[ids:ids+size], cur_p):
                    match_cnt += 1
                    idp += 1; ids += size
                else:
                    ids += 1


        return match_cnt == M


# DP solution
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        N = len(s); M = len(p)
        dp = [[False for _ in range(N+1)] for _ in range(M+1)]
        dp[0][0] = True
        for p_idx in range(1, M+1):
            if p[p_idx-1] == '*':
                s_idx = 1
                while not dp[p_idx-1][s_idx-1] and s_idx < N+1:
                    s_idx += 1
                dp[p_idx][s_idx-1] = dp[p_idx-1][s_idx-1]
                while s_idx < N+1:
                    dp[p_idx][s_idx] = True
                    s_idx += 1
            elif p[p_idx-1] == '?':
                for s_idx in range(1, N+1):
                    dp[p_idx][s_idx] = dp[p_idx-1][s_idx-1]
            else:
                for s_idx in range(1, N+1):
                    dp[p_idx][s_idx] = dp[p_idx-1][s_idx-1] and p[p_idx-1] == s[s_idx-1]

        return dp[M][N]
