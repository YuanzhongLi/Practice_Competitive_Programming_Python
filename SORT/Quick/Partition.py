N = int(input())
nums = list(map(int, input().rstrip().rsplit()))
# O(N)
# [l, r]
def partition(l, r, base_index=None): # return pivot index
  if base_index == None: base_index = r
  pivot = nums[base_index]
  nums[base_index], nums[r] = nums[r], nums[base_index]

  i = l-1
  for j in range(l, r):
    if nums[j] <= pivot:
      i+=1
      nums[i], nums[j] = nums[j], nums[i]
  nums[i+1], nums[r] = nums[r], nums[i+1]
  return i+1

pivot_index = partition(0, N-1)
str_nums = []
for i, num in enumerate(nums):
  if i == pivot_index:
    str_nums.append('['+str(num)+']')
  else:
    str_nums.append(str(num))

print(' '.join(str_nums))
