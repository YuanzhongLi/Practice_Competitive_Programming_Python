from collections import deque
dy = [-1, 0, 1, 0] # u, r, d, l
dx = [0, 1, 0, -1] # u, r, d, l

INF = 2147483647
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        q = deque([])
        H = len(rooms); W = len(rooms[0])
        for i in range(H):
            for j in range(W):
                if rooms[i][j] == 0:
                    q.append((i, j, 0))

        while q:
            uy,ux,d = q.popleft()
            for i in range(4):
                vy, vx = uy+dy[i], ux+dx[i]
                if 0 <= vy and vy < H and 0 <= vx and vx < W and rooms[vy][vx] > d+1:
                    q.append((vy, vx, d+1))
                    rooms[vy][vx] = d+1
