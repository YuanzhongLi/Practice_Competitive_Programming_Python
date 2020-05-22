from sys import stdin
input = stdin.readline

# map(int, input().rstrip().split())

a, b, c = map(int, input().rstrip().split())

if (a+b==c) and (a-b==c):
  print("?")
elif (a+b==c):
  print("+")
elif (a-b==c):
  print("-")
else:
  print("!")
