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

LINF = int(1e18+7)
S = input().rstrip()
K = int(input().rstrip())

tmp = LINF
ch = '1'
for i in range(len(S)):
  if S[i] != '1':
    tmp = i
    ch = S[i]
    break

if tmp >= K:
  print(1)
else:
  print(ch)

