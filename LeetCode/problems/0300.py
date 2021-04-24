from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, A: List[int]) -> int:
        ret = []
        for a in A:
            if ret:
                if ret[-1] < a:
                    ret.append(a)
                else:
                    idx = bisect_left(ret, a)
                    ret[idx] = a
            else:
                ret.append(a)

        return len(ret)
