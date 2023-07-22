def gcd(a, b):
    if a == b:
        return a
    elif a < b:
        a, b = b, a

    a %= b
    if a == 0:
        return b
    else:
        return gcd(a, b)
