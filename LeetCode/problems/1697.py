from functools import cmp_to_key

class UnionFind:
    def __init__(self, N):
        self.N = N
        self.par = [i for i in range(N)]
        self.rank = [0 for _ in range(N)]

    def root(self, x):
        if self.par[x] == x:
            return x
        self.par[x] = UnionFind.root(self, self.par[x])
        return self.par[x]

    def same(self, x, y):
        return UnionFind.root(self, x) == UnionFind.root(self, y)

    def unite(self, x, y):
        x = UnionFind.root(self, x)
        y = UnionFind.root(self, y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1


class Solution:
    def distanceLimitedPathsExist(self, N: int, edges: List[List[int]], queries: List[List[int]]) -> List[bool]:
        M = len(edges)
        Q = len(queries)
        query_idxs = [i for i in range(Q)]

        def compare_query(q1, q2):
            if q1[2] == q2[2]: # limit
                if q1[1] == q2[1]:
                    return q1[0] - q2[0]
                return q1[1] - q2[1]
            return q1[2] - q2[2]

        def compare_query_idx(idx1, idx2):
            q1 = queries[idx1]
            q2 = queries[idx2]
            return compare_query(q1, q2)

        query_idxs.sort(key=cmp_to_key(compare_query_idx))
        queries.sort(key=cmp_to_key(compare_query))

        def compare_edge(e1, e2): # compare distance
            return e1[2] - e2[2]

        edges.sort(key=cmp_to_key(compare_edge))

        uf = UnionFind(N)

        edge_idx = 0
        ans = [False for _ in range(Q)]
        for i, query in enumerate(queries):
            p, q, limit = query
            while edge_idx < M and edges[edge_idx][2] < limit:
                u, v, _ = edges[edge_idx]
                uf.unite(u, v)
                edge_idx += 1

            query_idx = query_idxs[i]
            ans[query_idx] = uf.same(p, q)

        return ans
