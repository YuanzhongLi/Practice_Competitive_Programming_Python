# DP solution
def check(w1, w2): # chain: w1->w2 bool
    n1 = len(w1); n2 = len(w2)
    if n1 + 1 == n2:
        i1 = 0; i2 = 0
        skip = False
        while i1 < n1:
            if w1[i1] == w2[i2]:
                i1 += 1; i2 += 1
            else:
                if not skip:
                    i2 += 1
                    skip = True
                else:
                    return False
        return True
    else: return False

INF = float('inf')
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        mem = [[INF, -INF] for _ in range(1005)]
        N = len(words)
        dp = [1 for _ in range(N)]
        ans = 1
        for i in range(N):
            n = len(words[i])
            ma = 0
            for j in range(mem[n-1][0], mem[n-1][1]+1):
                if check(words[j], words[i]):
                    ma = max(ma, dp[j])
            dp[i] += ma
            ans = max(ans,dp[i])
            mem[n][0] = min(mem[n][0], i)
            mem[n][1] = max(mem[n][1], i)
        return ans

# DFS solution
from collections import defaultdict
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        mp1 = defaultdict(list)
        mp2 = defaultdict(list)
        s = set([])
        for word in words:
            if word in s: continue
            s.add(word)
            N = len(word)
            if N == 1:
                mp1[word].append(word+'*')
                mp1[word].append('*'+word)
            else:
                for i in range(N):
                    mp2[word[:i]+'*'+word[i+1:]].append(word)
                for i in range(N):
                    mp1[word].append(word[:i]+'*'+word[i:])
                mp1[word].append(word+'*')

        graph = defaultdict(list)
        s.clear()
        for word in words:
            if word in s: continue
            s.add(word)
            for to in mp1[word]:
                for to_word in mp2[to]:
                    graph[word].append(to_word)

        mem = defaultdict(int)
        def dfs(word):
            if mem[word] > 0:
                return mem[word]
            alt = 1
            ma = 0
            for to_word in graph[word]:
                ma = max(ma, dfs(to_word))

            mem[word] = alt + ma
            return mem[word]

        ret = 0
        for word in words:
            ret = max(ret, dfs(word))
        return ret
