def get_primes():
    A = [False for _ in range(201)]
    primes = []
    for i in range(2, 201):
        if not A[i]:
            primes.append(i)
            for j in range(i, 201, i):
                A[j] = True
        else:
            continue
    return primes

def count_prime(x, primes):
    pn = len(primes)
    ret = [0 for _ in range(pn)]
    for i, p in enumerate(primes):
        while x > 1 and x % p == 0:
            ret[i] += 1
            x //= p
        if x == 1:
            break
    return ret

def count_prime_factorial(x, primes):
    pn = len(primes)
    ret = [0 for _ in range(pn)]
    for i in range(2,x+1):
        i_p_cnt = count_prime(i, primes)
        for j in range(pn):
            ret[j] += i_p_cnt[j]
    return ret

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # (m+n)Cm = (m+n)!/m!/n!
        m-=1; n-=1
        if m > n:
            m,n = n,m

        primes = get_primes()
        pn = len(primes)
        N = m+n
        N_f = count_prime_factorial(N, primes)
        m_f = count_prime_factorial(m, primes)
        n_f = count_prime_factorial(n, primes)
        ret = 1
        for i,p in enumerate(primes):
            ret *= p**(N_f[i]-m_f[i]-n_f[i])

        return ret
