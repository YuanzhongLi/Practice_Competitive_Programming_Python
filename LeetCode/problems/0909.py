from collections import deque

def idtocord(id, N):
    id -= 1
    h = id//(2*N)
    re = id-h*(2*N)
    if re >= N:
        h = (N-1)-(2*h+1)
        w = N-1-(re-N)
        return h, w
    else:
        w = re
        h = 2*h
        h = N-1-h
        return h, w

def cordtoid(y, x, N):
    y = N-1-y
    ret = 0
    if y&1 == 1:
        ret += (y+1)*N-x
    else:
        ret = 1+(y>>1)*(2*N)+x
    return ret

class Solution:
    def snakesAndLadders(self, grid: List[List[int]]) -> int:
        N = len(grid)
        graph = [[] for _ in range(N*N+1)]
        for i in range(N):
            for j in range(N):
                id = cordtoid(i,j, N)
                for k in range(1, 7):
                    next_id = id+k
                    if next_id > N*N: continue
                    next_y, next_x = idtocord(next_id, N)
                    if grid[next_y][next_x] != -1:
                        graph[id].append(grid[next_y][next_x])
                    else:
                        graph[id].append(next_id)

        q = deque([(1,0)])
        visited = [False for _ in range(N*N+1)]
        goal = N*N
        while q:
            u, d = q.popleft()
            if visited[u]: continue
            visited[u] = True
            if u == goal:
                return d
            for v in graph[u]:
                if visited[v]: continue
                q.append((v, d+1))
        return -1
