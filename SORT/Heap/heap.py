# 0-indexed
def Left(i):
  return ((i+1)<<1)-1

def Right(i):
  return ((i+1)<<1)

def Parent(i):
  return (i-1)>>1

# H: size of Heap (Array)
def maxHeapify(A, i, H):
  if i >= H:
    return
  l = Left(i); r = Right(i)
  largest = None
  if l < H and A[l] > A[i]: largest = l
  else: largest = i
  if r < H and A[r] > A[largest]: largest = r

  if largest != i:
    A[i], A[largest] = A[largest], A[i]
    maxHeapify(A, largest, H)

# O(N) Note: not NlogN
def Heapify(A):
  H = len(A)
  for i in range((H-1)>>1, -1, -1):
    maxHeapify(A, i, H)

# O(logN)
def Heappush(A, num):
  i = len(A)
  A.append(num)
  while i > 0:
    p = Parent(i)
    if A[p] < A[i]:
      A[p], A[i] = A[i], A[p]
      i = p
    else: break

# O(logN)
def Heappop(A, sort=False, H=None):
  ret = A[0]
  if not sort:
    A[0] = A[-1]
    A.pop()
    maxHeapify(A,0,len(A))
    return ret
  else:
    A[0] = A[H-1]
    A[H-1] = ret
    maxHeapify(A, 0, H-1)
    return ret

# O(N + NlogN)
def HeapSort(A):
  Heapify(A)
  for H in range(len(A), 0, -1):
    Heappop(A, True, H)

from random import randint
from copy import deepcopy as cp
H = 1000
A = [0 for _ in range(H)]
for _ in range(1000):
  for i in range(H):
    A[i] = randint(-H, H)
  B = cp(A)
  HeapSort(A)
  B.sort()

  if A != B:
    print("no")
