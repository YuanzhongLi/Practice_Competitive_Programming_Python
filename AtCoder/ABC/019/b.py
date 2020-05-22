from sys import stdin
input = stdin.readline

# map(int, input().rstrip().split())

def VI(N, init=0):
  return [init for _ in range(N)]
def VVI(N, M, init=0):
  return [[init for _ in range(M)] for _ in range(N)]

def VD(N, init=0.0):
  return [init for _ in range(N)]
def VVD(N, M, init=0.0):
  return [[init for _ in range(M)] for _ in range(N)]

def Block(s):
  num = 1
  v1 = [] # ch
  v2 = [] # num
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

s = input().rstrip()
chs, num = Block(s)

ans = ""
for i in range(len(chs)):
  ans += chs[i]
  ans += str(num[i])

print(ans)
