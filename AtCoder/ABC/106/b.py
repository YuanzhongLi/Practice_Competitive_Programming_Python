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

def Divisor(n):
  ret = []
  for i in range(1, n+1):
    if i*i > n:
      break
    else:
      if n % i == 0:
        ret.append(i)
        if i*i != n:
          ret.append(n//i)
  ret.sort()
  return ret

N = int(input().rstrip())
ans = 0
for i in range(1, N+1):
  divs = Divisor(i)
  if (len(divs) == 8) and (i&1) :
    ans += 1

print(ans)
