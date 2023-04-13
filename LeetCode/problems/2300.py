class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        M = len(potions)
        p_first = potions[0]
        p_last = potions[M-1]
        ans = []
        for s in spells:
            if s * p_first >= success:
                ans.append(M)
                continue

            if s * p_last < success:
                ans.append(0)
                continue

            ok = M-1
            ng = -1
            while abs(ok - ng) > 1:
                mid = (ok + ng) // 2
                if s * potions[mid] >= success:
                    ok = mid
                else:
                    ng = mid
            ans.append(M - ok)

        return ans
