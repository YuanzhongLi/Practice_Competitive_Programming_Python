# Solution Link: https://leetcode.com/problems/replace-non-coprime-numbers-in-array/solutions/7194506/python-gcd-and-stack-solution-with-japan-lyel/


class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            cur = num
            while len(ans) > 0:
                g = gcd(ans[-1], cur)
                if g == 1:
                    break
                else:
                    cur = (cur // g) * ans[-1]
                    ans.pop()

            ans.append(cur)

        return ans
