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

N, M = map(int, input().rstrip().split())

A = VI(N)
B = VI(N)
C = VI(M)
D = VI(M)

for i in range(N):
  A[i], B[i] = map(int, input().rstrip().split())

for i in range(M):
  C[i], D[i] = map(int, input().rstrip().split())

INF = int(1e18)

ans = VI(N)
for i in range(N):
  a = A[i]
  b = B[i]
  ddist = INF
  for j in range(M):
    c = C[j]
    d = D[j]
    dist = abs(a-c)+abs(b-d)
    if (dist < ddist):
      ans[i] = j+1
      ddist = dist

for i in range(N):
  print(ans[i])
