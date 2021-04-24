class Solution:
    def majorityElement(self, A: List[int]) -> int:
        cnt = 0
        cur = -1
        for a in A:
            if cnt == 0:
                cur = a; cnt += 1
            else:
                if a == cur: cnt += 1
                else: cnt -= 1
        return cur
