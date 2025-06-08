# Solution Link: https://leetcode.com/problems/candy/solutions/6695346/python-enumerate-solution-with-japanese-explanation


class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 1 + 2 + ... + x
        def getSum(x):
            return x * (x + 1) // 2

        # llast_bottom <-> last_top <-> last_bottom 間の最小キャンディ数を求める
        def get_ll_top_l(llast_bottom, last_top, last_bottom):
            if llast_bottom != -1:
                # llast_bottom <-> last_top <-> last_bottom 間を求める
                l_diff = last_top - llast_bottom
                r_diff = last_bottom - last_top
                max_d = max(l_diff, r_diff)
                min_d = min(l_diff, r_diff)
                return getSum(max_d + 1) + getSum(min_d)
            else:
                # last_top <-> last_bottom 間を求める
                return getSum(last_bottom - last_top + 1)

        # [l, r)間で全て異なる場合を解く
        def solve_unique_pattern(l, r):
            N = r - l
            if N <= 2:
                return getSum(N)

            first_is_bottom = ratings[l] < ratings[l + 1]
            last_is_bottom = ratings[r - 1] < ratings[r - 2]

            llast_bottom, last_bottom = -1, -1
            last_top = -1
            if first_is_bottom:
                last_bottom = l
            else:
                last_top = l

            ret = 0
            for i in range(l + 1, r - 1):
                # i is bottom
                if ratings[i - 1] > ratings[i] and ratings[i] < ratings[i + 1]:
                    llast_bottom, last_bottom = last_bottom, i
                    # last_bottom自身を除く
                    ret += get_ll_top_l(llast_bottom, last_top, last_bottom) - 1

                # i is top
                if ratings[i - 1] < ratings[i] and ratings[i] > ratings[i + 1]:
                    last_top = i

            if last_is_bottom:
                llast_bottom, last_bottom = last_bottom, r - 1
                # 最後なのでlast_bottom自身も含める
                ret += get_ll_top_l(llast_bottom, last_top, last_bottom)
            else:  # last is top
                ret += getSum(r - last_bottom)

            return ret

        N = len(ratings)
        pre_r = ratings[0]
        s_idx = 0

        ans = 0
        for i in range(1, N):
            cur_r = ratings[i]
            if cur_r == pre_r:
                ans += solve_unique_pattern(s_idx, i)
                s_idx = i
            pre_r = cur_r

        ans += solve_unique_pattern(s_idx, N)

        return ans
