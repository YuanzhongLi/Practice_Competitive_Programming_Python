from sys import stdin

input = stdin.readline


def POW(x, n):
    ret = 1
    while n:
        if n & 1:
            ret *= x
        x *= x
        n >>= 1
    return ret


# 0-indexed
class SegTree:
    def __init__(self, nin, e=0, op=lambda x, y: None):
        n = 1
        while n < nin:
            n <<= 1
        self.n = n
        self.data = [e for _ in range(2 * n)]
        self.e = e
        self.op = op

    # a[k] = v
    def update(self, k, v):
        k += self.n - 1
        self.data[k] = v
        while k > 0:
            k = (k - 1) // 2
            self.data[k] = self.op(self.data[2 * k + 1], self.data[2 * k + 2])

    def querySub(self, a, b, k, l, r):
        if a >= b:  # case by case
            return self.e
        if r <= a or b <= l:
            return self.e
        if a <= l and r <= b:
            return self.data[k]
        vl = self.querySub(a, b, 2 * k + 1, l, (l + r) // 2)
        vr = self.querySub(a, b, 2 * k + 2, (l + r) // 2, r)
        return self.op(vl, vr)

    # [a, b)
    def query(self, a, b):
        return self.querySub(a, b, 0, 0, self.n)


N, Q = map(int, input().rstrip().rsplit())
A = list(map(int, input().rstrip().rsplit()))


def xor(a, b):
    return a ^ b


st = SegTree(N, 0, xor)
for i in range(N):
    st.update(i, A[i])

for i in range(Q):
    t, x, y = map(int, input().rstrip().rsplit())
    if t == 1:
        x -= 1
        ax = st.query(x, x + 1)
        st.update(x, xor(ax, y))
    else:
        x -= 1
        print(st.query(x, y))
