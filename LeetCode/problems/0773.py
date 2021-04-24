from collections import defaultdict, deque
from itertools import permutations

def stoa(state):
    ret = [[0 for _ in range(3)] for _ in range(2)]
    for i in range(6):
        ret[i//3][i%3] = state[i]

    return ret

def atos(A):
    return tuple(A[0])+tuple(A[1])

dy = [-1, 0, 1, 0] # u, r, d, l
dx = [0, 1, 0, -1] # u, r, d, l

INF = float('inf')
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        mp = defaultdict(int)
        tmp = [[0 for _ in range(3)] for _ in range(2)]
        for p in list(permutations([0,1,2,3,4,5])):
            for i in range(2):
                for j in range(3):
                    tmp[i][j] = p[i*3+j]

            mp[atos(tmp)] = INF

        y0 = x0 = None
        for i in range(2):
            for j in range(3):
                if board[i][j] == 0:
                    y0, x0 = i, j
                    break

        s = atos(board)
        e = atos([[1,2,3],[4,5,0]])
        q = deque([[s, y0, x0, 0]])
        visited = set([])
        while q:
            state, y1, x1, d = q.popleft()
            if state in visited: continue
            visited.add(state)
            if state == e:
                return d
            a = stoa(state)
            for i in range(4):
                y2, x2 = y1+dy[i], x1+dx[i]
                if 0 <= y2 and y2 < 2 and 0 <= x2 and x2 < 3:
                    a[y1][x1], a[y2][x2] = a[y2][x2], a[y1][x1]
                    next_state = atos(a)
                    a[y1][x1], a[y2][x2] = a[y2][x2], a[y1][x1]
                    if next_state in visited: continue
                    q.append([next_state, y2, x2, d+1])

        return -1
