from copy import deepcopy as dcopy

class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        dp = [set([]) for _ in range(target+1)]
        dp[0].add("")

        for num in nums:
            for i in range(target, num - 1, -1):
                for s in dp[i - num]:
                    t = dcopy(s)
                    if t == "":
                        t += str(num)
                    else:
                        t += "," + str(num)

                    dp[i].add(t)

        return [[int(t) for t in s.split(',')] for s in list(dp[target])]
