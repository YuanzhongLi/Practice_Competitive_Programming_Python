from functools import cmp_to_key

ary = [3, 5, 1, 4, 10, 9, 6, 8, 7, 2]
ord = [i for i in range(10)]

def compare(a, b):
  if ary[a] == ary[b]:
    return 0
  elif ary[a] < ary[b]:
    return -1
  else:
    return 1

print(sorted(ord, key=cmp_to_key(compare)))
# result
# [2, 9, 0, 3, 1, 6, 8, 7, 5, 4]

ord.sort(key=cmp_to_key(compare))
print(ord)
# result
# [2, 9, 0, 3, 1, 6, 8, 7, 5, 4]
