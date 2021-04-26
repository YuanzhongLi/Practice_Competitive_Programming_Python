def Block(s):
  num = 1
  v1 = []
  v2 = []
  for i in range(len(s)):
    c = s[i]
    if i == 0:
      v1.append(c)
    elif c == s[i-1]:
      num += 1
    else:
      v2.append(num)
      v1.append(c)
      num = 1

    if i == len(s)-1:
      v2.append(num)
  return v1, v2

A = ['a','e','i','o','u']

class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        v1, v2 = Block(word)
        ret = 0
        N = len(v1)
        for i in range(N-4):
            flag = True
            alt = 0
            for j in range(5):
                if v1[i+j] != A[j]:
                    flag = False
                    break
                else:
                    alt += v2[i+j]
            if flag:
                ret = max(ret, alt)
        return ret
