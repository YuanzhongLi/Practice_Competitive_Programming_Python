class Solution:
    def maxLength(self, arr: List[str]) -> int:
        N = len(arr)
        ret = 0
        for i in range((1 << N)):
            s = set([])
            flag = True
            for j in range(N):
                if ((i >> j) & 1) == 1:
                    for ch in arr[j]:
                        if ch in s:
                            flag = False
                            break
                        s.add(ch)
                    if flag == False:
                        break
            if flag:
                ret = max(ret, len(s))

        return ret
