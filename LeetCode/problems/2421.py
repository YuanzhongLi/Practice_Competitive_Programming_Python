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



class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        ma = max(vals)
        N = len(vals)

        uf = Unionfind(N)

        val_nodes = [[] for _ in range(ma+1)]
        for node, val in enumerate(vals):
            val_nodes[val].append(node)

        adj_list = [[] for _ in range(N)]
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])

        ans = 0
        for val in range(ma+1):
            for from_node in val_nodes[val]:
                for to_node in adj_list[from_node]:
                    if vals[to_node] <= val:
                        uf.unite(from_node, to_node)

            mp = defaultdict(int)
            for node in val_nodes[val]:
                root = uf.root(node)

                mp[root] += 1

            for num in mp.values():
                ans += num * (num + 1) // 2

        return ans
