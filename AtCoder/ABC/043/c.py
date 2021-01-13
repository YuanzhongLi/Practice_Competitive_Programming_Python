N = int(input().rstrip())
A = list(map(int, input().rstrip().rsplit()))
INF = 100200300400500
cost = INF
for n in  range(-100, 101):
  c = 0
  for a in A:
    c += (a-n)**2
  if c < cost:
    cost = c

print(cost)
