# Solution Link: https://leetcode.com/problems/fruits-into-baskets-iii/solutions/7049334/python-segment-tree-solution-with-japane-yona/

INF = 10**9 + 7


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


def mi(x, y):
    return min(x, y)


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        N = len(fruits)
        st = SegTree(N, INF, mi)
        b_idxs = [i for i in range(N)]
        b_idxs.sort(key=lambda i: baskets[i])
        bi2i = [0 for _ in range(N)]
        baskets.sort()
        for i in range(N):
            st.update(i, b_idxs[i])
            bi2i[b_idxs[i]] = i

        ans = 0
        for num in fruits:
            if num > baskets[-1]:
                ans += 1
                continue

            ok, ng = N - 1, -1
            while abs(ok - ng) > 1:
                mid = (ok + ng) // 2
                if num <= baskets[mid]:
                    ok = mid
                else:
                    ng = mid

            min_idx = st.query(ok, N)
            if min_idx == INF:
                ans += 1
                continue

            st.update(bi2i[min_idx], INF)

        return ans
