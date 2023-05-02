class Solution:
    def kidsWithCandies(self, C: List[int], EX: int) -> List[bool]:
        ma = max(C)
        return [c+EX >= ma for c in C]
