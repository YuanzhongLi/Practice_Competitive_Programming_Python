from collections import deque, defaultdict

class Solution:
    def minimumHammingDistance(self, S: List[int], T: List[int], A: List[List[int]]) -> int:
        n = len(S)
        graph = [[] for _ in range(n)]
        for a in A:
            x = a[0]
            y = a[1]
            graph[x].append(y)
            graph[y].append(x)

        used = [False for _ in range(n)]
        ans = 0
        for i in range(n):
            if used[i]:
                continue
            q = deque([i])
            sub_s = defaultdict(int)
            sub_t = []
            while len(q) > 0:
                x = q.popleft()
                if used[x]:
                    continue
                used[x] = True
                sub_s[S[x]] += 1
                sub_t.append(T[x])
                for y in graph[x]:
                    if used[y]:
                        continue
                    q.append(y)

            for t in sub_t:
                if sub_s[t] > 0:
                    sub_s[t] -= 1
                else:
                    ans += 1
        return ans
