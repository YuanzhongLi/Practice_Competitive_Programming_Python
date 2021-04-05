from copy import deepcopy as cp
N = int(input())
A = []
for i in range(N):
  suit, num = input().rstrip().rsplit()
  num = int(num)
  A.append((suit, num))

B = cp(A); B.sort(key=lambda x: x[1])

def partition(A, l, r, index=None):
  if index == None:
    index = r
  pivot = A[index][1]
  i = l-1
  for j in range(l, r):
    if A[j][1] <= pivot:
      i += 1; A[i], A[j] = A[j], A[i]

  A[i+1], A[r] = A[r], A[i+1]
  return i+1

# average O(NlogN), worst O(N^2)
# in place sort
def QuickSort(A, l, r):
  if l < r:
    pivot_index = partition(A, l, r)
    QuickSort(A, l, pivot_index-1)
    QuickSort(A, pivot_index+1, r)

QuickSort(A, 0, N-1)

is_stable = True
for i in range(N):
  is_stable &= (A[i] == B[i])
  if not is_stable: break

if is_stable: print("Stable")
else: print("Not stable")

for i in range(N):
  print(A[i][0] + ' ' + str(A[i][1]))
