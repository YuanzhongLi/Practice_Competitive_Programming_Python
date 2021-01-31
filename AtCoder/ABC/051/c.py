sx, sy, tx, ty = map(int, input().rstrip().rsplit())
a = tx-sx
b = ty-sy
ans = ""
for i in range(a):
    ans += 'R'
for i in range(b):
    ans += 'U'
for i in range(a):
    ans += 'L'
for i in range(b):
    ans += 'D'

ans += 'D'
for i in range(a+1):
    ans += 'R'
for i in range(b+1):
    ans += 'U'
ans += 'L'
ans += 'U'
for i in range(a+1):
    ans += 'L'
for i in range(b+1):
    ans += 'D'
ans += 'R'

print(ans)
