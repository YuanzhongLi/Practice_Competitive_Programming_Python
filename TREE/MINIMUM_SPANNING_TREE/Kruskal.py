class Unionfind:
    def __init__(self, N):
        self.N = N
        self.par = [i for i in range(N)] # 節点
        self.rank = [0 for _ in range(N)] # 木の高さ
        self.size = [1 for _ in range(N)] # 節点が属する木の節点数
        self.treeNum = N # 木の数

    def addNode(self, x): # 節点(木)追加
        self.par[x] = x
        self.rank[x] = 0
        self.size[x] = 1
        self.treeNum += 1

    def root(self, x): # 根を探すと同時に経路上にある節点の親が根になるように代入
        if self.par[x] == x:
            return x
        else:
            self.par[x] = Unionfind.root(self, self.par[x])
            return self.par[x]

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

# VERIFICATIOIN: typical90 049
# URL: https://atcoder.jp/contests/typical90/submissions/22938876

def Kruskal(N, edges):
    edges.sort()
    uf = Unionfind(N)

    ret = 0
    for cost, u, v in edges:
        if not uf.same(u, v):
            ret += cost
            uf.unite(u, v)

    if uf.treeNum > 1: # can not build connected tree
        return -1

    return ret

N, M = map(int, input().rstrip().rsplit())
edges = []
for i in range(M):
  c, l, r = map(int, input().rstrip().rsplit())
  edges.append((c, l-1, r))

ans = Kruskal(N+1, edges)

print(ans)
