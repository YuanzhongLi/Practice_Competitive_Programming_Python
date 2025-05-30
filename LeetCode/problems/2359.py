# Solution Link: https://leetcode.com/problems/find-closest-node-to-given-two-nodes/solutions/6794142/python-bfs-solution-with-japanese-explan-jxbf/

INF = 10**18


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        N = len(edges)
        # node1からの距離
        dist1 = [INF for _ in range(N)]
        # node2からの距離
        dist2 = [INF for _ in range(N)]

        cur = node1
        d = 0
        while cur != -1 and d < dist1[cur]:
            dist1[cur] = d
            d += 1
            cur = edges[cur]

        cur = node2
        d = 0
        while cur != -1 and d < dist2[cur]:
            dist2[cur] = d
            d += 1
            cur = edges[cur]

        ans = -1
        min_d = INF
        for i in range(N):
            max_d = max(dist1[i], dist2[i])
            if max_d < min_d:
                ans = i
                min_d = max_d

        return ans
