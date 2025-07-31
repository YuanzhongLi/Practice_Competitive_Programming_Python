# Solution Link: https://leetcode.com/problems/bitwise-ors-of-subarrays/solutions/7026317/python-bit-manipulation-solution-with-ja-ukzz/


class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        bit_idx = [-1 for _ in range(32)]
        s = set()
        for i, num in enumerate(arr):
            if num == 0:
                s.add(0)
                continue

            b = 0
            while num > 0:
                if (num & 1) == 1:
                    bit_idx[b] = i
                b += 1
                num >>= 1

            cur = 0
            for idx in sorted(bit_idx, reverse=True):
                if idx == -1:
                    break
                cur |= arr[idx]
                s.add(cur)

        return len(s)
