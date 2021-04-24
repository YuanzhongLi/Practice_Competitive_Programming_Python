class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], d: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        N = len(slots1); M = len(slots2)
        i = j = 0
        while i < N and j < M:
            s1,e1 = slots1[i]
            s2,e2 = slots2[j]
            if e1 < s2:
                i += 1
            elif e2 < s1:
                j += 1
            else:
                s = max(s1, s2)
                e = min(e1, e2)
                if s + d <= e:
                    return [s, s+d]
                else:
                    if e1 <= e2:
                        i += 1
                    else:
                        j += 1
        return []
