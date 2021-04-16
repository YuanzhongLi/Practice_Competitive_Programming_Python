from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        N = len(tickets)
        graph = defaultdict(list)
        for i, ticket in enumerate(tickets):
            fro, to = ticket
            graph[fro].append((to, i))

        for key in graph.keys():
            graph[key].sort()

        used = [False for _ in range(N)]
        ans = []
        def dfs(A):
            if len(A) == N:
                nonlocal ans
                alt = []
                for a in A:
                    ans.append(tickets[a][0])
                ans.append(tickets[A[-1]][1])
                return True

            cur = "JFK"
            if A:
                cur = tickets[A[-1]][1]
            n = len(A)
            for to, id in graph[cur]:
                if used[id]: continue
                used[id] = True
                A.append(id)
                if dfs(A):
                    return True
                A.pop()
                used[id] = False
            return False

        dfs([])
        return ans
