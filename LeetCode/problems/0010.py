class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        N = len(s)
        ps = []
        for ch in p:
            if ch == '*':
                ps[-1] += '*'
            else:
                ps.append(ch)
        p = ps
        M = len(p)
        dp = [[False for _ in range(M+1)] for _ in range(N+1)]
        dp[0][0] = True
        for i in range(0, N+1):
            idx = i-1
            for j in range(0, M+1):
                if i == 0 and j == 0: continue
                jdx = j-1

                j_is_ast = (jdx >= 0 and p[jdx][-1] == '*')
                j_ch = ''
                if jdx >= 0: j_ch = p[jdx][0]

                if dp[i-1][j-1]:
                    if j_is_ast:
                        if idx >= 0 and (j_ch == s[idx] or j_ch == '.'):
                            dp[i][j] = True; continue
                        if dp[i][j-1]:
                            dp[i][j] = True; continue
                    else:
                        if idx >= 0 and jdx >= 0 and (p[jdx][0] == s[idx] or p[jdx][0] == '.'):
                            dp[i][j] = True; continue

                if dp[i][j-1]:
                    if j_is_ast:
                        dp[i][j] = True; continue
                    else:
                        if idx >= 0 and dp[i-1][j-1] and (j_ch == s[idx] or j_ch == '.'):
                            dp[i][j] = True; continue

                if dp[i-1][j]:
                    if j_is_ast and (j_ch == s[idx] or j_ch == '.'):
                        dp[i][j] = True; continue
                    else: continue

        return dp[N][M]
