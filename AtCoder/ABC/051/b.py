K, S = map(int, input().rstrip().rsplit())
ans = 0
for x in range(K+1):
    for y in range(K+1):
        z = S-(x+y)
        if z <= K and 0 <= z:
            ans+=1
print(ans)
