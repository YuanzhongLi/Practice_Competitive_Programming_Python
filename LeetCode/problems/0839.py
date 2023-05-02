from collections import deque

def compare(s1, s2):
    N = len(s1)
    idx1 = -1
    idx2 = -1
    for i in range(N):
        ch1, ch2 = s1[i], s2[i]
        if ch1 != ch2:
            if idx1 == -1:
                idx1 = i
            elif idx2 == -1:
                idx2 = i
            else:
                return False

    if idx1 == -1:
        return True

    if idx2 == -1:
        return False

    return s1[idx1] == s2[idx2] and s1[idx2] == s2[idx1]

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        N = len(strs)
        graph = [[] for _ in range(N)]
        for i in range(N):
            for j in range(i+1, N):
                if compare(strs[i], strs[j]):
                    graph[i].append(j)
                    graph[j].append(i)

        visited = [False for _ in range(N)]
        ans = 0
        for i in range(N):
            if visited[i]:
                continue
            ans += 1
            q = deque([i])
            while len(q) > 0:
                u = q.popleft()
                if visited[u]:
                    continue
                visited[u] = True
                for v in graph[u]:
                    if visited[v]:
                        continue
                    q.append(v)

        return ans
