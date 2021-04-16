from collections import deque
class HitCounter:
    def __init__(self):
        self.q = deque([])
        self.hits = 0

    def hit(self, t: int) -> None:
        q = self.q
        while q and q[0][0] <= t-300:
            self.hits -= q.popleft()[1]

        if q and q[-1][0] == t:
            q[-1][1] += 1
        else:
            q.append([t, 1])
        self.hits += 1


    def getHits(self, t: int) -> int:
        q = self.q
        while q and q[0][0] <= t-300:
            self.hits -= q.popleft()[1]
        return self.hits
