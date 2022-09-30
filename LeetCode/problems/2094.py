from collections import defaultdict

def f(n):
    a, b, c = n //100, n % 100 // 10, n % 10
    ret = defaultdict(int)
    ret[a] += 1
    ret[b] += 1
    ret[c] += 1
    return ret

class Solution:
    def findEvenNumbers(self, A: List[int]) -> List[int]:
        mem = defaultdict(int)
        for a in A:
            mem[a] += 1

        ans = []
        for i in range(100, 1000, 2):
            tmp = f(i)
            flag = True
            for key in tmp:
                if tmp[key] <= mem[key]:
                    continue
                flag = False
                break

            if flag:
                ans.append(i)
        return ans
