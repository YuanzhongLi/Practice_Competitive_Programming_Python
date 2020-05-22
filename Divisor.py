def Divisor(n):
  ret = []
  for i in range(1, n+1):
    if i*i > n:
      break
    else:
      if n % i == 0:
        ret.append(i)
        if i*i != n:
          ret.append(n//i)
  ret.sort()
  return ret
