import sys
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

v = 0
dist = 0
for i in range(N):
  if i+1 == 1:
    continue
  print("? {0} {1}".format(1, i+1))
  sys.stdout.flush()
  tmp = int(input().rstrip())
  if (tmp > dist):
    v = i+1
    dist = tmp

ans = 0
for i in range(N):
  if i+1 == v:
    continue
  print("? {0} {1}".format(v, i+1))
  sys.stdout.flush()
  tmp = int(input().rstrip())
  if (tmp > ans):
    ans = tmp

print("! {0}".format(ans))

