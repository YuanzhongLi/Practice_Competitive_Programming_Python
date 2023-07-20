MOD = 10**9 + 7

def modplus(a, b):
    return (a + b) % MOD

def modminus(a, b):
    return (a + MOD - b) % MOD

def modmul(a, b):
    return (a * b) % MOD

# a^{-1}
def modinv(a):
    b, u, v = MOD, 1, 0
    while b:
        t = a // b
        a -= t * b; a, b = b, a
        u -= t * v; u, v = v, u

    u %= MOD
    if u < 0: u += MOD
    return u

def moddiv(a, b):
    return modmul(a, modinv(b))

# a^n
def modpow(a, n):
    ret = 1
    while n > 0:
        if n&1:
            ret = ret * a % MOD

        a = a * a %MOD
        n >>= 1

    return  ret

MAX = 510000

fac = [0 for _ in range(MAX)]
finv = [0 for _ in range(MAX)]
inv = [0 for _ in range(MAX)]

def com_init():
    fac[0], fac[1] = 1, 1
    finv[0], finv[1] = 1, 1
    inv[1] = 1
    for i in range(2, MAX):
        fac[i] = fac[i-1] * i % MOD
        inv[i] = MOD - inv[MOD%i] * (MOD//i) % MOD
        finv[i] = finv[i-1] * inv[i] % MOD

# nCk
def com(n, k):
    if n < k: return 0
    if n < 0 or k < 0: return 0
    return fac[n] * (finv[k] * finv[n-k] % MOD) % MOD

com_init()
