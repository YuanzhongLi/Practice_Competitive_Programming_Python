# Solution Link: https://leetcode.com/problems/zero-array-transformation-iii/solutions/6768450/python-dynamic-imos-solution-with-japane-fabe/

from heapq import heappush, heappop


class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        N = len(nums)
        M = len(queries)
        imos = [0 for _ in range(N)]
        queries.sort()

        # queries index
        j = 0
        # 現在使用可能なクエリの最大右端rを保持するheap
        heap = []
        ans = M
        for i, num in enumerate(nums):
            if i > 0:
                imos[i] += imos[i - 1]

            while j < M:
                l, r = queries[j]
                if l <= i:
                    # 使用できるrを大きい順に取り出したいのでheapに入れていく
                    heappush(heap, -r)
                    j += 1
                else:
                    break

            while num + imos[i] > 0 and len(heap) > 0:
                r = -heappop(heap)
                if i > r:
                    # 現在使用可能な最大rのクエリを使用しても無理
                    return -1
                # 以降はi <= r

                # heapから取り出した最大rのクエリを使用して[i:r]の範囲を-1する
                imos[i] -= 1
                if r + 1 < N:
                    imos[r + 1] += 1

                ans -= 1

            if num + imos[i] > 0:
                return -1

        return ans
