class Unionfind:
    def __init__(self, N):
        self.N = N
        self.par = [i for i in range(N)]  # 節点
        self.rank = [0 for _ in range(N)]  # 木の高さ
        self.size = [1 for _ in range(N)]  # 節点が属する木の節点数
        self.treeNum = N  # 木の数

    def addNode(self, x):  # 節点(木)追加
        self.par[x] = x
        self.rank[x] = 0
        self.size[x] = 1
        self.treeNum += 1

    def root(self, x):  # 根を探すと同時に経路上にある節点の親が根になるように代入
        par = self.par
        if par[x] == x:
            return x
        else:
            par[x] = Unionfind.root(self, par[x])
            return par[x]

    def same(self, x, y):
        return Unionfind.root(self, x) == Unionfind.root(self, y)

    def unite(self, x, y):
        x = Unionfind.root(self, x)
        y = Unionfind.root(self, y)
        if x == y:
            return
        self.treeNum -= 1
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.size[y] += self.size[x]
        else:
            self.par[y] = x
            self.size[x] += self.size[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def group(self):
        N = self.N
        ret = [[]]
        table = [[] for _ in range(N)]
        for i in range(N):
            table[self.root(i)].append(i)
        for i in range(N):
            if len(table[i]) > 0:
                ret.append(table[i])

        return ret
