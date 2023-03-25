from collections import deque

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for edge in edges:
            a, b = edge
            graph[a].append(b)
            graph[b].append(a)

        visited = [False for _ in range(n)]
        node_nums = []
        s = 0
        for i in range(n):
            if visited[i]:
                continue
            node_num = 0
            q = deque([i])
            while len(q) > 0:
                a = q.popleft()
                if visited[a]:
                    continue
                visited[a] = True
                node_num += 1

                for b in graph[a]:
                    if visited[b]:
                        continue
                    q.append(b)

            node_nums.append(node_num)
            s += node_num

        ans = s*s
        for node_num in node_nums:
            ans -= node_num*node_num

        return ans//2
