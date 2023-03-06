from math import inf
from heapq import heapify, heappush, heappop

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        evens = []
        minimum = 1000000000000
        for num in nums:
            if num % 2 == 0:
                evens.append(-num)
                minimum = min(minimum, num)
            else:
                evens.append(-num*2)
                minimum = min(minimum, num * 2)

        heapify(evens)
        min_deviation = 1000000000000
        while evens:
            current_value = -heappop(evens)
            min_deviation = min(min_deviation, current_value - minimum)
            if current_value % 2 == 0:
                minimum = min(minimum, current_value//2)
                heappush(evens, -current_value//2)
            else:
                break


        return min_deviation
