class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and len(trust) == 0:
            return 1

        mp = defaultdict(int)
        everybody = set([])
        for t in trust:
            a, b = t
            mp[b] += 1
            everybody.add(a)

        ans = -1
        for key in mp.keys():
            if mp[key] == n-1:
                if ans == -1:
                    ans = key
                else:
                    return -1

        if ans in everybody:
            return -1
        return ans
