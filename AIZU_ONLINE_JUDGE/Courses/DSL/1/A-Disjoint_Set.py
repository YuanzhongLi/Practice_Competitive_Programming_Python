from sys import stdin


class Unionfind:
    def __init__(self, N):
        self.roots = [i for i in range(N)]
        self.ranks = [1 for _ in range(N)]

    def root(self, u):
        roots = self.roots
        if roots[u] == u:
            return u
        # この時点でroots[u] != uなので途中状態を意味する
        # rootsを再帰的に更新しながら、根のノードを求める
        roots[u] = self.root(roots[u])
        return roots[u]

    def unite(self, u, v):
        root = self.root
        # ノードu, vの木を求めて置き換える
        # この２つをくっつけるので元のu, vはこれ以降必要ない
        u, v = root(u), root(v)
        if u == v:
            return

        ranks, roots = self.ranks, self.roots
        # ランクが高い方の木にもう一方の木をくっつける
        if ranks[u] >= ranks[v]:
            roots[v] = u
            # ランクが同じ場合はどちらでも良いがここではxの方にくっつける
            # ランクを+1する必要がある
            if ranks[u] == ranks[v]:
                ranks[u] += 1
        else:
            roots[u] = v

    def same(self, u, v):
        root = self.root
        return root(u) == root(v)


input = stdin.readline

n, q = map(int, input().rstrip().rsplit())
uf = Unionfind(n)

while q:
    com, u, v = map(int, input().rstrip().rsplit())
    if com == 0:
        uf.unite(u, v)
    else:
        if uf.same(u, v):
            print(1)
        else:
            print(0)

    q -= 1
