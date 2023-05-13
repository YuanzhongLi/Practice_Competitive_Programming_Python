from copy import deepcopy as dc

def ary_id(ary):
    return str(ary)

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        se = set([i for i in range(N)])
        id_set = set([])
        ary = []
        ans = []
        def dfs():
            if len(ary) == N:
                id = ary_id(ary)
                if not id in id_set:
                    ans.append(dc(ary))
                    id_set.add(id)
                return
            l = list(se)
            for idx in l:
                se.remove(idx)
                ary.append(nums[idx])
                dfs()
                ary.pop()
                se.add(idx)

        dfs()
        return ans
