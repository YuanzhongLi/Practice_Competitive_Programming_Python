# Solution Link: https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/solutions/6791162/python-bfs-solution-with-japanese-explan-fo08/

from collections import deque


class Solution:
    def maxTargetNodes(
        self, edges1: List[List[int]], edges2: List[List[int]]
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

        # graph1のノードがノード0と同じグループかどうか
        group = [False for _ in range(N)]

        q = deque([(0, -1, 0)])
        graph1_group0_num = 0
        while q:
            u, p, l = q.popleft()
            if l % 2 == 0:
                graph1_group0_num += 1
                group[u] = True
            for v in graph1[u]:
                if v == p:
                    continue
                q.append((v, u, l + 1))

        # graph1のノード0と異なるグループ
        graph1_rest = N - graph1_group0_num

        q = deque([(0, -1, 0)])
        graph2_group0_num = 0
        while q:
            u, p, l = q.popleft()
            if l % 2 == 0:
                graph2_group0_num += 1

            for v in graph2[u]:
                if v == p:
                    continue
                q.append((v, u, l + 1))

        # graph2においての最大target数
        max_graph2 = max(graph2_group0_num, M - graph2_group0_num)

        ans = []
        for i, isGroup0 in enumerate(group):
            if isGroup0:
                ans.append(graph1_group0_num + max_graph2)
            else:
                ans.append(graph1_rest + max_graph2)

        return ans
