MP = {'a':0, 'e':1, 'i':2, 'o':3, 'u':4}

def countVowelSubString(s):
    N = len(s)
    sums = [[0 for _ in range(N+1)] for _ in range(5)]
    for i, ch in enumerate(s):
        for j in range(5):
            sums[j][i+1] = sums[j][i]

        if ch in MP:
            sums[MP[ch]][i+1] = sums[MP[ch]][i] + 1

    ans = 0
    for i in range(1, N+1):
        for j in range(i, N+1):
            flag = True
            for k in range(5):
                flag &= (sums[k][j] - sums[k][i-1] > 0)
                if not flag:
                    break
            if flag:
                ans += 1

    return ans

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        ans = 0
        tmp = ""
        for ch in word:
            if ch in MP:
                tmp += ch
            else:
                if len(tmp) >= 5:
                    ans += countVowelSubString(tmp)
                tmp = ""

        if len(tmp) >= 5:
            ans += countVowelSubString(tmp)

        return ans
