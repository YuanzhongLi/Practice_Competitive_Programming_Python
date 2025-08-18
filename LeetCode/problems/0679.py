# Solution Link: https://leetcode.com/problems/24-game/solutions/7093886/python-dp-gcd-and-fraction-number-soluti-91ii/

from itertools import permutations


def gcd(a, b):
    a, b = abs(a), abs(b)
    if a > b:
        a, b = b, a
    return _gcd(a, b)


def _gcd(a, b):
    if a % b == 0:
        return b
    return _gcd(b, a % b)


def frac_plus(x, y):
    x_son, x_mom = x
    y_son, y_mom = y

    son = x_son * y_mom + y_son * x_mom
    if son == 0:
        return (0, 1)
    mom = x_mom * y_mom
    g = gcd(son, mom)

    return (son // g, mom // g)


def frac_minus(x, y):
    x_son, x_mom = x
    y_son, y_mom = y

    son = x_son * y_mom - y_son * x_mom
    if son == 0:
        return (0, 1)
    mom = x_mom * y_mom
    g = gcd(son, mom)

    return (son // g, mom // g)


def frac_mul(x, y):
    x_son, x_mom = x
    y_son, y_mom = y

    son = x_son * y_son
    if son == 0:
        return (0, 1)
    mom = x_mom * y_mom
    g = gcd(son, mom)

    return (son // g, mom // g)


def frac_div(x, y):
    x_son, x_mom = x
    y_son, y_mom = y
    if y_son == 0:
        return None

    son = x_son * y_mom
    if son == 0:
        return (0, 1)
    mom = x_mom * y_son
    g = gcd(son, mom)

    return (son // g, mom // g)


frac_functions = [frac_plus, frac_minus, frac_mul]

# a b cは1 ~ 9の数
# memo[abc]: a b cで作れる分数
memo = [None for _ in range(1000)]


def dp(n):
    if memo[n] != None:
        return memo[n]

    memo[n] = set()
    tmp = n
    if n < 10:
        memo[n].add((n, 1))
    elif n < 100:
        a, b = tmp // 10, tmp % 10
        frac_a = (a, 1)
        frac_b = (b, 1)
        for frac_func in frac_functions:
            memo[n].add(frac_func(frac_a, frac_b))
            div_frac = frac_div(frac_a, frac_b)
        if div_frac != None:
            memo[n].add(div_frac)
    elif n < 1000:
        c = tmp % 10
        tmp //= 10
        a, b = tmp // 10, tmp % 10

        ab = a * 10 + b
        ab_set = dp(ab)
        c_set = dp(c)
        for frac_ab in ab_set:
            for frac_c in c_set:
                for frac_func in frac_functions:
                    memo[n].add(frac_func(frac_ab, frac_c))
                div_frac = frac_div(frac_ab, frac_c)
                if div_frac != None:
                    memo[n].add(div_frac)

        bc = b * 10 + c
        a_set = dp(a)
        bc_set = dp(bc)
        for frac_a in a_set:
            for frac_bc in bc_set:
                for frac_func in frac_functions:
                    memo[n].add(frac_func(frac_a, frac_bc))
                div_frac = frac_div(frac_a, frac_bc)
                if div_frac != None:
                    memo[n].add(div_frac)

    return memo[n]


for i in range(1, 10):
    memo[i] = dp(i)

for i in range(10, 100):
    a, b = i // 10, i % 10
    if a == 0 or b == 0:
        continue
    memo[i] = dp(i)

for i in range(100, 1000):
    tmp = i
    c = tmp % 10
    tmp //= 10
    a, b = tmp // 10, tmp % 10
    if a == 0 or b == 0 or c == 0:
        continue
    memo[i] = dp(i)


def toNum(a, b, c):
    return a * 100 + b * 10 + c


goal = (24, 1)


class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        for p_cards in permutations(cards):
            for i in range(3):
                first = 0
                cur = 1
                for j in range(i, -1, -1):
                    first += p_cards[j] * cur
                    cur *= 10

                second = 0
                cur = 1
                for j in range(3, i, -1):
                    second += p_cards[j] * cur
                    cur *= 10

                first_set, second_set = memo[first], memo[second]
                for frac_f in first_set:
                    # first + second = 24
                    target = frac_minus(goal, frac_f)
                    if target in second_set:
                        return True

                    # first - second = 24
                    target = frac_minus(frac_f, goal)
                    if target in second_set:
                        return True

                    if frac_f == (0, 1):
                        continue

                    # first * second = 24
                    target = frac_div(goal, frac_f)
                    if target in second_set:
                        return True

                    # first / second = 24
                    target = frac_div(frac_f, goal)
                    if target in second_set:
                        return True

        return False
