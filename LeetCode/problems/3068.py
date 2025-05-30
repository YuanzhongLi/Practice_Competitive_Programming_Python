# Solution Link: https://leetcode.com/problems/find-the-maximum-sum-of-node-values/solutions/6771735/python-tree-dp-solution-with-japanese-explanation/


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        N = len(nums)
        tree = [[] for _ in range(N)]
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)

        # uがxorされてる場合の最大値, uがxorされてない場合の最大値を返す
        def dfs(u, p):
            val_u, val_u_xor = nums[u], nums[u] ^ k

            diffs = []

            # uから子へ出るedgeを全てxorにした場合の合計
            xor_sum = 0

            # uから子へ出るedgeを全てxorにしない場合の合計
            not_sum = 0
            for v in tree[u]:
                if v == p:
                    continue
                val_v = nums[v]
                val_v_xor = nums[v] ^ k
                v_not, v_xor, is_v_leaf = dfs(v, u)

                # u - v edgeをxorしない場合の最大値
                uv_not = max(v_xor, v_not)
                if is_v_leaf:
                    uv_not = v_not
                # u - v edgeをxorする場合の最大値
                uv_xor = max(v_xor + val_v - val_v_xor, v_not - val_v + val_v_xor)
                if is_v_leaf:
                    uv_xor = v_xor

                not_sum += uv_not
                xor_sum += uv_xor
                diffs.append((uv_xor - uv_not, uv_not, uv_xor))

            M = len(diffs)
            is_u_leaf = M == 0
            # print(u, val_u, val_u_xor, is_u_leaf)

            # u_xorを最大化する場合、uv_xor - uv_not > 0となるu-v edgeを奇数個できるだけ選び、
            # それらのedgeをxorさせることで最大化する
            # 逆にu_notを最大化する場合は、uv_xor - uv_not > 0となるu-v edgeを偶数個できるだけ選び、
            # それらのedgeをxorさせることで最大化する
            # uv_xor - uv_not を大きい順にソートして以下の様に範囲和を使用して順番に見るのが楽
            diffs.sort(reverse=True)
            u_not = not_sum
            u_xor = 0
            tmp_not_sum = 0
            tmp_xor_sum = 0
            for i in range(M):
                tmp_not_sum += diffs[i][1]
                tmp_xor_sum += diffs[i][2]
                if i % 2 == 1:
                    u_not = max(u_not, tmp_xor_sum + not_sum - tmp_not_sum)
                else:
                    u_xor = max(u_xor, tmp_xor_sum + not_sum - tmp_not_sum)

            u_xor += val_u_xor
            u_not += val_u

            return u_not, u_xor, is_u_leaf

        ans = max(dfs(0, -1))

        return ans
