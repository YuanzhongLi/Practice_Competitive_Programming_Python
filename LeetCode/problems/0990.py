class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        par = [i for i in range(26)]
        size = [1 for _ in range(26)]

        def root(x):
            if par[x] == x:
                return par[x]
            else:
                par[x] = root(par[x])
                return par[x]

        def unite(x, y):
            x = root(x)
            y = root(y)
            if size[x] == size[y]:
                par[y] = x
                size[x] += 1
            elif size[x] > size[y]:
                par[y] = x
            else:
                par[x] = y

        def same(x, y):
            return root(x) == root(y)

        ord_a = ord('a')
        for eq in equations:
            x = ord(eq[0]) - ord_a
            y = ord(eq[3]) - ord_a
            if eq[1] == '=':
                unite(x, y)

        for eq in equations:
            x = ord(eq[0]) - ord_a
            y = ord(eq[3]) - ord_a
            if eq[1] == '!':
                if same(x, y):
                    return False

        return True
