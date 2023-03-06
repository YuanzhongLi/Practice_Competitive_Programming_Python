from collections import deque

def diff(s1, s2):
    ret = 0
    for i in range(8):
        if s1[i] != s2[i]:
            ret += 1
    return ret

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        q = deque([(start, 0)])
        visited = set([])
        while len(q) > 0:
            s, l = q.popleft()

            if s == end:
                return l

            if s in visited:
                continue

            visited.add(s)

            for s2 in bank:
                if s2 in visited or diff(s, s2) != 1:
                    continue
                q.append((s2, l+1))

        return -1
