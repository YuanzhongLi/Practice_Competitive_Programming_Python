s = list(input().rstrip())
alpha = [[] for _ in range(26)]
for i, ch in enumerate(s):
  alpha[ord(ch)-ord('a')].append(i)

l = -1
r = -1
for li in alpha:
  n = len(li)
  for j in range(1, n):
    if li[j]-li[j-1] <= 2:
     l = li[j-1]+1
     r = li[j]+1

print("{0} {1}".format(l, r))
