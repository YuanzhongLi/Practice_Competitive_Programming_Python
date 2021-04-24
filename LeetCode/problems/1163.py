class Solution:
    def lastSubstring(self, s: str) -> str:
        N = len(s)
        i, j = 0, 1
        while j < N:
            if s[j] > s[i]:
                i = j
            elif s[j] == s[i]:
                p, q = i, j
                while p < j and q < N:
                    if s[p] > s[q]:
                        break
                    elif s[q] > s[p]:
                        i = j
                        break
                    else:
                        p += 1
                        q += 1
                j = q-1
            j = j+1
        return s[i:]
