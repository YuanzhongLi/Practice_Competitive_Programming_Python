class Solution:
    def abbreviateProduct(self, L: int, R: int) -> str:
        two = 0
        five = 0
        ans = 1
        for i in range(L, R+1):
            num = i
            while num & 1 == 0:
                two += 1
                num >>= 1
            while num % 5 == 0:
                five += 1
                num //= 5
            ans *= num

        mi = min(two, five)
        for _ in range(two - mi):
            ans *= 2
        for _ in range(five - mi):
            ans *= 5

        S = str(ans)
        if len(S) > 10:
            pre = ""
            for i in range(5):
                pre += S[i]
            suf = ""
            for i in range(len(S)-5, len(S)):
                suf += S[i]
            S = pre + "..." + suf

        S += "e" + str(mi)
        return S
