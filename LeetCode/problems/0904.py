# Solution Link: https://leetcode.com/problems/fruit-into-baskets/solutions/7041221/python-sliding-window-solution-with-japa-2lek/


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        N = len(fruits)

        ans = 1
        f1, f2 = fruits[0], None
        f1_cnt, f2_cnt = 1, 0
        l, r = 0, 0
        while True:
            if r == N - 1:
                break
            f = fruits[r + 1]
            if f == f1 or f == f2 or f1 == None or f2 == None:
                if f == f1:
                    f1_cnt += 1
                elif f == f2:
                    f2_cnt += 1
                elif f1 == None:
                    f1 = f
                    f1_cnt = 1
                else:  # f2 == None
                    f2 = f
                    f2_cnt = 1
                ans = max(ans, f1_cnt + f2_cnt)
                r += 1
            else:
                l_f = fruits[l]
                if l_f == f1:
                    f1_cnt -= 1
                    if f1_cnt == 0:
                        f1 = None
                else:  # l_f == f2
                    f2_cnt -= 1
                    if f2_cnt == 0:
                        f2 = None
                l += 1

        return ans
