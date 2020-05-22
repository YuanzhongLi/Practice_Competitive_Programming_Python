def Block(s):
  num = 1
  v1 = []
  v2 = []
  for i in range(len(s)):
    c = s[i]
    if i == 0:
      v1.append(c)
    elif c == s[i-1]:
      num += 1
    else:
      v2.append(num)
      v1.append(c)
      num = 1

    if i == len(s)-1:
      v2.append(num)
  return v1, v2
