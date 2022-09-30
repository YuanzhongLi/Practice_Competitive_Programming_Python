class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        ret = []
        odds = []
        evens = []
        for i,n in enumerate(nums):
            if i & 1:
                odds.append(n)
                ret.append(1)
            else:
                evens.append(n)
                ret.append(0)

        odds.sort()
        evens.sort()
        evens.reverse()

        for i in range(len(ret)):
            if ret[i] == 1:
                ret[i] = odds.pop()
            else:
                ret[i] = evens.pop()

        return ret
