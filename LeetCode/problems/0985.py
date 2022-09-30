class Solution:
    def sumEvenAfterQueries(self, A: List[int], Q: List[List[int]]) -> List[int]:
        ret = []
        s = 0
        for a in A:
            if (a & 1) == 0:
                s += a

        for q in Q:
            v, i = q
            a = A[i]
            A[i] += v
            if (a & 1) == 0: # a is even
                if (v & 1) == 0: # v is even
                    s += v
                else: # v is odd
                    s -= a
            else: # a is odd
                if (v & 1) == 1: # v is odd
                    s += a + v

            ret.append(s)

        return ret
