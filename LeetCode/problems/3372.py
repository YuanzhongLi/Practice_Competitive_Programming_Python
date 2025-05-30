# Solution Link: https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/description/?envType=daily-question&envId=2025-05-28

from collections import deque

INF = 10**18


class Solution:
    def maxTargetNodes(
        self, edges1: List[List[int]], edges2: List[List[int]], k: int
    ) -> List[int]:
        N, M = len(edges1) + 1, len(edges2) + 1
        graph1 = [[] for _ in range(N)]
        graph2 = [[] for _ in range(M)]

        for a, b in edges1:
            graph1[a].append(b)
            graph1[b].append(a)

        for a, b in edges2:
            graph2[a].append(b)
            graph2[b].append(a)

        # less_k_1[i]: tree 1のi番目のノードからk以下の距離にある数
        less_k_1 = [0 for _ in range(N)]

        # less_k_1[i]: tree 1のi番目のノードからk-1以下の距離にある数
        less_k_2 = [0 for _ in range(M)]
        for i in range(N):
            q = deque([(i, -1, 0)])
            while q:
                u, p, d = q.popleft()
                if d > k:
                    break
                less_k_1[i] += 1
                for v in graph1[u]:
                    if v == p:
                        continue
                    q.append((v, u, d + 1))

        for i in range(M):
            q = deque([(i, -1, 0)])
            while q:
                u, p, d = q.popleft()
                if d > k - 1:
                    break
                less_k_2[i] += 1
                for v in graph2[u]:
                    if v == p:
                        continue
                    q.append((v, u, d + 1))

        ma = max(less_k_2)

        return [i + ma for i in less_k_1]
