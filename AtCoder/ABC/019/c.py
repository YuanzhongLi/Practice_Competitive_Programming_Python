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

N = int(input().rstrip())

A = list(map(int, input().rstrip().split()))
A.sort()

INF = int(1e9+7)
s = set()
ans = 0
for i in range(N):
  a = A[i]
  if a in s:
    continue

  ans += 1
  while a < INF:
    s.add(a)
    a *= 2

print(ans)

