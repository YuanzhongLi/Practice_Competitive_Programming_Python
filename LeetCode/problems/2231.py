class Solution:
    def largestInteger(self, num: int) -> int:
        ps = []
        odds = []
        evens = []

        d = 0
        while num > 0:
            a = num % 10
            if a % 2 == 0: # even
                ps.append(0)
                evens.append(a)
            else: # odd
                ps.append(1)
                odds.append(a)
            num //= 10

        odds.sort()
        odds.reverse()
        evens.sort()
        evens.reverse()

        ans = 0
        d = 1
        for p in ps:
            if p == 0:
                ans += d * evens.pop()
            else:
                ans += d * odds.pop()
            d *= 10

        return ans
