from collections import deque, defaultdict
from functools import cmp_to_key

class Solution:
    def watchedVideosByFriends(self, WV: List[List[str]], F: List[List[int]], id: int, k: int) -> List[str]:
        N = len(WV)
        q = deque([(0, id)])
        used = [False for _ in range(N)]
        mem = defaultdict(int)
        while len(q) > 0:
            level, i = q.popleft()
            if used[i]:
                continue
            used[i] = True

            if level == k:
                for v in WV[i]:
                    mem[v] += 1
                continue

            for j in F[i]:
                if used[j]:
                    continue
                q.append((level + 1, j))

        ret = list(mem.keys())

        def comp(a, b):
            if mem[a] < mem[b]:
                return -1
            elif mem[a] > mem[b]:
                return 1
            else:
                if a <= b:
                    return -1
                else:
                    return 1

        ret.sort(key=cmp_to_key(comp))

        return ret
