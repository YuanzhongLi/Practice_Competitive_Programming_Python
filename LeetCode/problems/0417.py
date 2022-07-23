# BFS solution
dy = [-1, 0, 1, 0] # u, r, d, l
dx = [0, 1, 0, -1] # u, r, d, l
from collections import deque
class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        H = len(grid); W = len(grid[0]); N = H*W
        po = deque([]); ao = deque([])
        graph = [[] for _ in range(N)]

        for i in range(H):
            for j in range(W):
                u = i*W+j
                u_num = grid[i][j]
                if i == 0 or j == 0: po.append(u)
                if i == H-1 or j == W-1: ao.append(u)
                for k in range(4):
                    vy, vx = i+dy[k], j+dx[k]; v = vy*W+vx
                    if 0 <= vy and vy < H and 0 <= vx and vx < W:
                        v_num = grid[vy][vx]
                        if u_num <= v_num:
                            graph[u].append(v)

        po_set = set([]); ao_set = set([])
        while po:
            u = po.popleft()
            if u in po_set: continue
            po_set.add(u)
            for v in graph[u]:
                if v in po_set: continue
                po.append(v)
        ret = []
        while ao:
            u = ao.popleft()
            if u in ao_set: continue
            ao_set.add(u)
            if u in po_set: ret.append([u//W, u%W])
            for v in graph[u]:
                if v in ao_set: continue
                ao.append(v)

        return ret
