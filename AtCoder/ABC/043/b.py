s = list(input().rstrip())
ans = []
for ch in s:
  if ch =='0':
    ans.append('0')
  elif ch == '1':
    ans.append('1')
  elif ch == 'B' and len(ans) > 0:
    ans.pop(-1)
print(''.join(ans))
