def add(A, B):  # 123 -> [3, 2, 1]
    N = len(A)
    M = len(B)

    carry = 0
    i = 0
    ret = []
    while i < N or i < M:
        alt = None
        if i < N and i < M:
            alt = A[i] + B[i] + carry
        elif i < N:
            alt = A[i] + carry
        elif i < M:
            alt = B[i] + carry


        carry = alt//10
        ret.append(alt%10)
        i += 1
    if carry > 0:
        ret.append(carry)
    return ret

def mul_1digit(A, x, d): # 0 <= x <= 9
    if x == 0: return None
    N = len(A)
    carry = 0
    ret = [0 for _ in range(d)]
    i = 0
    while i < N:
        alt = A[i] * x + carry
        carry = alt//10
        ret.append(alt%10)
        i += 1
    if carry > 0:
        ret.append(carry)
    return ret

# abc * def
# abc * f + abc * (e*10) + abc * (d*100)
class Solution:
    def multiply(self, s1: str, s2: str) -> str:
        if s1 == '0' or s2 == '0': return '0'
        A = list([int(ch) for ch in s1])[::-1]
        B = list([int(ch) for ch in s2])[::-1]
        ans = [0]
        for i in range(len(B)):
            alt =  mul_1digit(A, B[i], i)
            if alt == None: continue
            ans = add(ans, alt)

        return ''.join(str(num) for num in ans)[::-1]
