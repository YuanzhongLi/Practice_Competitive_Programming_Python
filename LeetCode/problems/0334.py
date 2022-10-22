from heapq import heappush

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        N = len(nums)
        small = [False for _ in range(N)] # small[i]: There is a num in {nums[0], ... , nums[i-1]} < nums[i]
        large = [False for _ in range(N)] # large[i]: There is a num in {nums[i+1], ... , nums[N-1]} > nums[i]
        h = [nums[0]]
        for i in range(1, N-1):
            if h[0] < nums[i]:
                small[i] = True
            heappush(h, nums[i])

        h = [-nums[N-1]]
        for i in range(N-2, -1, -1):
            if -h[0] > nums[i]:
                large[i] = True
            heappush(h, -nums[i])

        for i in range(N):
            if small[i] and large[i]:
                return True

        return False
