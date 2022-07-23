class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        s2id = {}
        s = set([])
        for eq in equations:
            fr, to = eq
            if fr not in s:
                s2id[fr] = len(s)
                s.add(fr)
            if to not in s:
                s2id[to] = len(s)
                s.add(to)

        graph = [[] for _ in range(len(s))]
        for i, eq in enumerate(equations):
            fr, to = eq
            graph[s2id[fr]].append((s2id[to], values[i]))
            graph[s2id[to]].append((s2id[fr], 1.0/values[i]))

        def solve(start, end):
            visited = set([])
            ret = -1.0
            def dfs(val, cur, end):
                nonlocal ret
                if cur == end:
                    ret = val
                    return True

                visited.add(cur)
                for to, v in graph[cur]:
                    if to in visited: continue
                    if dfs(val*v, to, end): return True

                return False

            dfs(1.0, start, end)
            return ret

        ans = []
        for start_s, end_s in queries:
            if start_s in s2id and end_s in s2id:
                start, end = s2id[start_s], s2id[end_s]
                ans.append(solve(start, end))
            else: ans.append(-1.0)
        return ans
