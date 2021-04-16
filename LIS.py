from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, A: List[int]) -> int:
        ans  = []
        for a in A:
            if ans:
                if a > ans[-1]: # 注意: 以上、以下の場合 <= , >=となる
                    ans.append(a)
                elif a == ans[-1]:
                    continue
                else:
                    id = bisect_left(ans, a) # 注意: 以上、以下の場合upper_boundとなる
                    ans[id] = a
            else:
                ans.append(a)

        return len(ans)
