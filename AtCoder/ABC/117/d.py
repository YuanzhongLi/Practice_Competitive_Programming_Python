from sys import stdin
input = stdin.readline
import copy as cp
from collections import deque, OrderedDict

INF = 1001002003004005006

def VI(N, init=0):
  return [init for _ in range(N)]
def VVI(N, M, init=0):
  return [[init for _ in range(M)] for _ in range(N)]

def VD(N, init=0.0):
  return [init for _ in range(N)]
def VVD(N, M, init=0.0):
  return [[init for _ in range(M)] for _ in range(N)]

def Decimal(x):
  print("{0:.10f}".format(x))

class Pair:
  def __init__(self, x=0, y=0):
    self.first = x
    self.second = y

  def __repr__(self):
    return '{0} {1}'.format(self.first, self.second)

  def __lt__(self, pi):
    return self.first < pi.first

def POW(x, n):
  ret = 1
  while n:
    if n&1:
      ret *= x
    x *= x
    n >>= 1
  return ret

N, K = map(int, input().rstrip().rsplit())

A = list(map(int, input().rstrip().rsplit()))
bit_cnt = VI(50)

for a in A:
  for i in range(50):
    if (a >> i)&1 == 1:
      bit_cnt[i] += 1

# 左づめでの10進数xをdigits桁のN進数vectorにしてを返す
def baseNumber(N, digits, x):
  ret = [0 for _ in range(digits)]
  # 商
  q = x
  cnt = 0
  while q > 0:
    # 余り
    re = q % N
    q //= N
    ret[cnt] = re
    cnt += 1

  return ret

bit_k = baseNumber(2, 50, K+1)

ans = 0
for i in range(50): # 区切り
  if bit_k[i] == 0:
    continue

  # bit_k[i] == 1, bit_x[i] == 0
  tmp = 0
  for j in range(i):
    tmp += max(bit_cnt[j], N-bit_cnt[j]) * (1 << j)

  tmp += (bit_cnt[i]) * (1 << i)

  for j in range(i+1, 50):
    if bit_k[j]:
      tmp += (N-bit_cnt[j]) * (1 << j)
    else:
      tmp += bit_cnt[j] * (1 << j)
  ans = max(ans, tmp)


print(ans)
