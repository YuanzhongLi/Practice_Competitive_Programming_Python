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
