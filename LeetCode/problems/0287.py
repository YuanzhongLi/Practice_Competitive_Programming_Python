# mid
class Solution:
    def findDuplicate(self, A: List[int]) -> int:
        to = ha = A[0]
        while True:
            to = A[to]
            ha = A[A[ha]]
            if to == ha:
                break

        to = A[0]
        while to != ha:
            to = A[to]
            ha = A[ha]
        return to
