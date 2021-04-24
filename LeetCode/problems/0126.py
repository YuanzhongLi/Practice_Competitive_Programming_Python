from collections import defaultdict, deque
from copy import deepcopy as cp

INF = float('inf')

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = [beginWord] + wordList
        combodict = defaultdict(list)
        wtoid = defaultdict(int)
        idtow = {}
        w_set = set([])
        for w in wordList:
            if w in w_set: continue
            wtoid[w] = len(w_set)
            idtow[len(w_set)] = w
            w_set.add(w)
            for i in range(len(w)):
                combodict[w[:i]+'*'+w[i+1:]].append(w)

        if endWord not in w_set: return []
        N = len(w_set)
        graph = [[] for _ in range(N)]
        for w in wordList:
            w_id = wtoid[w]
            if len(graph[w_id]) == 0:
                for i in range(len(w)):
                    w_ = w[:i]+'*'+w[i+1:]
                    for to_w in combodict[w_]:
                        if to_w == w: continue
                        to_w_id = wtoid[to_w]
                        graph[w_id].append(to_w_id)

        s, e = wtoid[beginWord], wtoid[endWord]
        q = deque([(s, 0)])
        visited = [False for _ in range(N)]
        dist = [INF for _ in range(N)]
        while q:
            u, d = q.popleft()
            if d > dist[e]:
                break
            if visited[u]: continue
            visited[u] = True
            dist[u] = d
            for v in graph[u]:
                if visited[v]: continue
                q.append((v, d+1))

        stoe_dist = dist[e]
        ret = []
        def dfs(A):
            u = A[-1]
            if u == s:
                ret.append(cp(A))
                return
            for v in graph[u]:
                if dist[v] == stoe_dist - len(A):
                    A.append(v)
                    dfs(A)
                    A.pop()
        dfs([e])

        for i in range(len(ret)):
            ret[i].reverse()
            ret[i] = [idtow[id] for id in ret[i]]

        return ret
