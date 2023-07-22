from sys import stdin

input = stdin.readline
import copy as cp
from collections import deque, OrderedDict

LINF = 1001002003004005006
INF = 1001001001


def VI(N, init=0):
    return [init for _ in range(N)]


def VVI(N, M, init=0):
    return [[init for _ in range(M)] for _ in range(N)]


def VD(N, init=0.0):
    return [init for _ in range(N)]


def VVD(N, M, init=0.0):
    return [[init for _ in range(M)] for _ in range(N)]


def Decimal(x):
    print("{0:.10f}".format(x))


class Pair:
    def __init__(self, x=0, y=0):
        self.first = x
        self.second = y

    def __repr__(self):
        return "{0} {1}".format(self.first, self.second)

    def __lt__(self, pi):
        return self.first < pi.first


def POW(x, n):
    ret = 1
    while n:
        if n & 1:
            ret *= x
        x *= x
        n >>= 1
    return ret


# 小さい順にpopすることに注意！
from heapq import heapify, heappop, heappush, heappushpop


class PriorityQueue:
    def __init__(self, heap):
        """
        heap ... list
        """
        self.heap = heap
        heapify(self.heap)

    def push(self, item):
        heappush(self.heap, item)

    def pop(self):
        return heappop(self.heap)

    def pushpop(self, item):
        return heappushpop(self.heap, item)

    def __call__(self):
        return self.heap

    def __len__(self):
        return len(self.heap)

    def __repr__(self):
        return str(self.heap)


# VERIFICATION: ABC 35_D
# URL: https://atcoder.jp/contests/abc035/submissions/13632716


class Dijkstra:
    def __init__(self, V):
        self.V = V
        self.graph = [[] for _ in range(V)]
        self.color = VI(V)
        self.dist = VI(V)
        self.parent = VI(V)
        self.WHITE = 0  # 未到達
        self.GRAY = 1  # 到達
        self.BLACK = 2  # 探索済み

    def add_edge(self, ffrom, to, cost):
        self.graph[ffrom].append(Pair(to, cost))

    def min_path(self, s):
        PQ = PriorityQueue([])

        # initialize
        for i in range(self.V):
            self.dist[i] = LINF
            self.color[i] = self.WHITE

        self.dist[s] = 0
        PQ.push(Pair(0, s))
        self.color[s] = self.GRAY

        while len(PQ) > 0:
            f = PQ.pop()
            u = f.second
            self.color[u] = self.BLACK

            for j in range(len(self.graph[u])):
                v = self.graph[u][j].first
                if self.color[v] == self.BLACK:
                    continue
                if self.dist[v] > self.dist[u] + self.graph[u][j].second:
                    self.dist[v] = self.dist[u] + self.graph[u][j].second
                    self.parent[v] = u
                    PQ.push(Pair(self.dist[v], v))
                    self.color[v] = self.GRAY
