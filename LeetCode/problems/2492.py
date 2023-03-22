INF = 10000000007
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [0 for _ in range(n)]
        scores = [INF for _ in range(n)]

        def root(x):
            if par[x] == x:
                return x
            else:
                par[x]= root(par[x])
                return par[x]


        def unite(x, y):
            x = root(x)
            y = root(y)
            if x == y:
                return

            if rank[x] < rank[y]:
                par[x] = y
            else:
                par[y] = x
                if rank[x] == rank[y]:
                    rank[x] += 1

        for road in roads:
            x, y, _ = road
            x -= 1
            y -= 1
            unite(x, y)

        for road in roads:
            x, y, d = road
            x -= 1
            y -= 1
            scores[root(x)] = min(scores[root(x)], d)

        return scores[root(n-1)]
