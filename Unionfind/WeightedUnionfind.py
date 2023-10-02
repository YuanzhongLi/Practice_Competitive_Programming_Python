from sys import stdin

# VERIFICATIOIN: AIZU ONLINE JUDGE/DSL_1_B
# URL: https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/1/DSL_1_B


class WeightedUnionfind:
    def __init__(self, N):
        # ノードiの根ノードを記録（途中状態も含む）
        self.roots = [i for i in range(N)]
        self.ranks = [1 for _ in range(N)]
        # 根を基準としたときの重みを記録（途中状態も含む）
        self.weights = [0 for _ in range(N)]

    def root(self, u):
        roots = self.roots
        if roots[u] == u:
            return u

        # この時点でroots[u] != uなので途中状態を意味する
        root, weights = self.root, self.weights
        # rootsを再帰的に更新しながら、根のノードを求める
        r = root(roots[u])
        # 重みを累積していく
        weights[u] += weights[roots[u]]

        roots[u] = r
        return roots[u]

    # ノードuの所属する木の根を基準としたときのノードuの重み
    def weight(self, u):
        # これを実行することでノードuから根の経路上での途中状態をなくす
        self.root(u)
        return self.weights[u]

    # weight(y) - weight(x) = wとなる様にノードu, vをuniteする
    # u, vをuniteして矛盾するかを返す
    def unite(self, u, v, w):
        root, weight = self.root, self.weight

        root_u, root_v = root(u), root(v)
        if root_u == root_v:
            if weight(v) - weight(u) != w:
                # 既存の条件と矛盾
                return False
            return True

        # uとvそれぞれについて根との重み差分を補正
        w += weight(u)
        w -= weight(v)

        u, v = root_u, root_v

        ranks, roots, weights = self.ranks, self.roots, self.weights

        # uの方がランクが高くなる様にu, vをスワップする
        # これによってvをuにくっつける操作となる
        if ranks[u] < ranks[v]:
            u, v = v, u
            # u, vをスワップしたのでwを反転する必要がある
            w = -w
        elif ranks[u] == ranks[v]:
            ranks[u] += 1

        roots[v] = u
        weights[v] = w

        return True

    def diff(self, u, v):
        root, weight = self.root, self.weight
        return root(u) == root(v), weight(v) - weight(u)


n, q = map(int, input().rstrip().rsplit())
wuf = WeightedUnionfind(n)

while q:
    query = input().rstrip().rsplit()
    com, u, v = int(query[0]), int(query[1]), int(query[2])
    if com == 0:
        w = int(query[3])
        wuf.unite(u, v, w)
    else:
        is_same, d = wuf.diff(u, v)
        if is_same:
            print(d)
        else:
            print("?")

    q -= 1
