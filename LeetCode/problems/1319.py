class Solution:
    def makeConnected(self, n: int, edges: List[List[int]]) -> int:
        if len(edges) < n-1:
            return -1
        uf = [i for i in range(n)]
        rank = [1 for _ in  range(n)]
        groups = n
        def root(a):
            if a == uf[a]:
                return a
            uf[a] = root(uf[a])
            return uf[a]

        def unite(a, b):
            a = root(a); b = root(b)
            if a == b: return

            nonlocal groups
            groups -= 1
            if rank[a] > rank[b]:
                uf[b] = a
            elif rank[a] < rank[b]:
                uf[a] = b
            else:
                rank[a] += 1
                uf[b] = a
            return

        for a, b in edges:
            unite(a, b)

        return groups - 1
