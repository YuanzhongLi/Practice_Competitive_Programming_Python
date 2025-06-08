# Solution Link: https://leetcode.com/problems/lexicographical-numbers/solutions/6821677/python-iterate-solution-with-japanese-ex-kiiv/


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def next(x):
            # x -> x0の様に0を増やせるなら増やす
            if x * 10 <= n:
                return x * 10

            # 以降は0を増やせないので値を増やす(+1)

            # 上の様に0は増やせる時に増やしている
            # つまり0が後につくものは0を減らす必要がある
            cur = x + 1
            # 0を減らしたかどうか
            flag = False
            while cur % 10 == 0:
                cur //= 10
                flag = True
            if flag:
                return cur

            if x + 1 <= n:
                return x + 1

            # x+1が範囲外なので桁を1つ落として増やす(+1)
            cur = x // 10 + 1

            # 同様に後に0があるなら減らしておく
            while cur % 10 == 0:
                cur //= 10
            return cur

        ans = [1]
        for _ in range(n - 1):
            ans.append(next(ans[-1]))

        return ans
