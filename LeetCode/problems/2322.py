# Solution Link: https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/solutions/6996978/python-brute-force-and-dfs-solution-with-12ne/


class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        N = len(nums)
        total_xor = 0
        for num in nums:
            total_xor ^= num

        def get_edge_id(a, b):
            if a > b:
                a, b = b, a
            return a * 10000 + b

        graph = [[] for _ in range(N)]
        # edge_xor[edge_id][a]: edgeの端点aをrootとした木のxor(b側を含めない)
        edge_xor = {}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            edge_xor[get_edge_id(a, b)] = {a: None, b: None}

        def dfs(edge_id, u, p):
            if edge_xor[edge_id][u] != None:
                return edge_xor[edge_id][u]

            u_xor = nums[u]
            for v in graph[u]:
                if v == p:
                    continue
                next_edge_id = get_edge_id(u, v)
                u_xor ^= dfs(next_edge_id, v, u)

            edge_xor[edge_id][u] = u_xor
            return edge_xor[edge_id][u]

        for edge_id in edge_xor.keys():
            a, b = edge_id // 10000, edge_id % 10000
            edge_id = get_edge_id(a, b)
            edge_xor[edge_id][a] = dfs(edge_id, a, b)
            edge_xor[edge_id][b] = dfs(edge_id, b, a)

        # edge_side[edge_id][u]: ノードuがedge1の端点のどちら側にあるか
        edge_side = {}
        for edge_id in edge_xor.keys():
            edge_side[edge_id] = [None for _ in range(N)]

        def dfs2(u, p, root):
            for v in graph[u]:
                if v == p:
                    continue
                edge_id = get_edge_id(u, v)
                edge_side[edge_id][root] = u
                dfs2(v, u, root)

        for u in range(N):
            dfs2(u, -1, u)

        ans = float("inf")
        for edge1_id in edge_xor.keys():
            a, b = edge1_id // 10000, edge1_id % 10000
            for edge2_id in edge_xor.keys():
                if edge1_id == edge2_id:
                    continue

                c, d = edge2_id // 10000, edge2_id % 10000
                comp1, comp2, comp3 = None, None, None

                # edge2がa側にある
                if edge_side[edge1_id][c] == a:
                    comp1 = edge_xor[edge1_id][b]
                    rest = total_xor ^ comp1

                    # d - c - a - bの並び
                    if edge_side[edge2_id][a] == c:
                        comp2 = edge_xor[edge2_id][d]
                    else:  # c - d - a - b
                        comp2 = edge_xor[edge2_id][c]
                    comp3 = rest ^ comp2
                else:  # edge2がb側にある
                    comp1 = edge_xor[edge1_id][a]
                    rest = total_xor ^ comp1

                    # a - b - c - d
                    if edge_side[edge2_id][b] == c:
                        comp2 = edge_xor[edge2_id][d]
                    else:  # a - b - d - c
                        comp2 = edge_xor[edge2_id][c]
                    comp3 = rest ^ comp2

                ans = min(ans, max(comp1, comp2, comp3) - min(comp1, comp2, comp3))

        return ans
