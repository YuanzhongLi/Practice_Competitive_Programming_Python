# Solution Link: https://leetcode.com/problems/lexicographically-smallest-equivalent-string/solutions/6812037/python-unionforest-solution-with-japanes-026k/


class UnionForest:
    def __init__(self, N):
        self.N = N
        self.par = [i for i in range(N)]
        self.rank = [0 for _ in range(N)]
        self.group_min = {}

    def root(self, x):
        if x == self.par[x]:
            return x
        x = self.root(self.par[x])
        return x

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        rank = self.rank
        par = self.par
        if rank[x] >= rank[y]:
            par[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1
        else:
            par[x] = y

    # 各グループの中の最小文字を求めておく
    def cal_group_min(self):
        N = self.N
        group_min = self.group_min
        for i in range(N):
            pi = self.root(i)
            if pi in group_min:
                group_min[pi] = min(group_min[pi], i)
            else:
                group_min[pi] = min(pi, i)


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        N = len(s1)
        ord_a = ord("a")

        uf = UnionForest(26)

        for i in range(N):
            ch1, ch2 = s1[i], s2[i]
            uf.unite(ord(ch1) - ord_a, ord(ch2) - ord_a)

        uf.cal_group_min()

        M = len(baseStr)
        ans = ""
        for i in range(M):
            mi = uf.group_min[uf.root(ord(baseStr[i]) - ord_a)]
            mi_ch = chr(mi + ord_a)
            ans += mi_ch

        return ans
