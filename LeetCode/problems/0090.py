def convert(A):
    if A[0] == '':
        return []
    return [int(a) for a in A]

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        s = set([])
        for i in range((1<<N)):
            tmp = ''
            for j in range(N):
                if ((i >> j) & 1) == 1:
                    if len(tmp) > 0:
                        tmp += ',' + str(nums[j])
                    else:
                        tmp += str(nums[j])
            s.add(tmp)

        ret = []
        for st in s:
            ret.append(convert(st.split(',')))

        return ret
