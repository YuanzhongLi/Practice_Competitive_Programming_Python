from random import randint
def partition(A, l, r, index=None):
  if index == None:
    index = r
  pivot = A[index]
  A[index], A[r] = A[r], A[index]
  i = l-1
  for j in range(l, r):
    if A[j] <= pivot:
      i += 1; A[i], A[j] = A[j], A[i]

  A[i+1], A[r] = A[r], A[i+1]
  return i+1

# average O(N), worst O(N^2), in place
def QuickSelect(A, l, r, k):
  if l == r:
    return A[l]

  pivot_index = randint(l, r)
  pivot_index = partition(A, l, r, pivot_index)
  if k == pivot_index:
    return A[k]
  elif k < pivot_index:
    return QuickSelect(A, l, pivot_index-1, k)
  else:
    return QuickSelect(A, pivot_index+1, r, k)
