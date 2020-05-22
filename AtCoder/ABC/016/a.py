from sys import stdin
input = stdin.readline

m, d = map(int, input().rstrip().split())

if m % d == 0:
  print("YES")
else:
  print("NO")
