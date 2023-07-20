from collections import deque

dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]

INF = 1 << 30

def debug(board):
    for b in board:
        print(b)
    print()

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # debug(board)
        H, W = len(board), len(board[0])
        N = H*W
        visited = set([])
        for u in range(N):
            uy, ux = u // W, u % W
            if board[uy][ux] == 'X' or u in visited:
                continue

            connected_group = []
            min_y, max_y, min_x, max_x = INF, -1, INF, -1
            que = deque([u])
            while que:
                u = que.popleft()
                if u in visited:
                    continue
                visited.add(u)
                connected_group.append(u)
                uy, ux = u // W, u % W
                min_y, max_y, min_x, max_x = min(min_y, uy), max(max_y, uy), min(min_x, ux), max(max_x, ux)

                for i in range(4):
                    vy, vx = uy + dy[i], ux + dx[i]
                    v = vy * W + vx
                    if 0 <= vy and vy < H and 0 <= vx and vx < W and board[vy][vx] == 'O' and not (v in visited):
                        que.append(v)


            if 0 < min_y and max_y < H-1 and 0 < min_x and max_x < W-1:
                for u in connected_group:
                    uy, ux = u // W, u % W
                    board[uy][ux] = 'X'

        # debug(board)
