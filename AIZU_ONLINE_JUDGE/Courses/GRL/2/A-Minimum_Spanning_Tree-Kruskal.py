from sys import stdin


class Unionfind:
    def __init__(self, V):
        self.roots = [i for i in range(V)]
        self.ranks = [1 for _ in range(V)]

    def root(self, u):
        roots = self.roots
        if roots[u] == u:
            return u
        roots[u] = self.root(roots[u])
        return roots[u]

    def unite(self, u, v):
        root = self.root
        u, v = root(u), root(v)
        if u == v:
            return

        ranks, roots = self.ranks, self.roots
        if ranks[u] < ranks[v]:
            u, v = v, u
        elif ranks[u] == ranks[v]:
            ranks[u] += 1

        roots[v] = u
        return

    def same(self, u, v):
        root = self.root
        return root(u) == root(v)


input = stdin.readline
V, E = map(int, input().rstrip().rsplit())
uf = Unionfind(V)

edges = []

while E:
    edges.append([int(e) for e in list(input().rstrip().rsplit())])
    E -= 1


def Kruskal(N: int, edges: list[list[int]]):
    # 重みの小さい順でエッジをソート
    edges.sort(key=lambda x: x[2])

    uf = Unionfind(N)
    mst_cost = 0
    for edge in edges:
        u, v, w = edge
        if not uf.same(u, v):
            uf.unite(u, v)
            mst_cost += w

    return mst_cost


print(Kruskal(V, edges))
