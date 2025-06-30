# Solution Link: https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/solutions/6870491/python-enumerate-solution-with-japanese-8d9wk/


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        N = len(s)
        ans = []
        for i in range(0, N, k):
            tmp = ""
            for j in range(i, k + i):
                if j >= N:
                    tmp += fill
                else:
                    tmp += s[j]
            ans.append(tmp)

        return ans
