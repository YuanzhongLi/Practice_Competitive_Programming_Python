# BFS
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        H = len(grid); W = len(grid[0])
        graph = [[] for _ in range(H*W)]
        for i in range(H):
            for j in range(W):
                if grid[i][j] != 0: continue
                for y in range(i-1, i+2):
                    for x in range(j-1, j+2):
                        if y == i and x == j: continue
                        if 0 <= y and y < H and 0 <= x and x < W and grid[y][x] == 0:
                            graph[i*W+j].append(y*W+x)
        visited = [False for _ in range(H*W)]
        q = deque([[0,1]])
        while q:
            u,d = q.popleft()
            if visited[u]:
                continue

            visited[u] = True
            if u == H*W-1:
                return d

            for v in graph[u]:
                if visited[v]: continue
                q.append([v, d+1])

        return -1

# A *
from heapq import *
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        H = len(grid); W = len(grid[0])
        graph = [[] for _ in range(H*W)]
        for i in range(H):
            for j in range(W):
                if grid[i][j] != 0: continue
                for y in range(i-1, i+2):
                    for x in range(j-1, j+2):
                        if y == i and x == j: continue
                        if 0 <= y and y < H and 0 <= x and x < W and grid[y][x] == 0:
                            graph[i*W+j].append(y*W+x)
        visited = [False for _ in range(H*W)]
        def shortest(y, x):
            nonlocal H, W
            return max(H-y, W-x)

        hq = [(1+shortest(0, 0,), 1, 0)]
        while hq:
            _, d, u = heappop(hq)
            if visited[u]:
                continue

            visited[u] = True
            if u == H*W-1:
                return d

            for v in graph[u]:
                if visited[v]: continue
                vy, vx = v//W, v%W
                heappush(hq, (1+shortest(vy, vx)+d, d+1, v))

        return -1
