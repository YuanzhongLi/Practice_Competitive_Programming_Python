class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        ans = 0
        for i in range(k):
            if s[i] in vowels:
                ans += 1

        tmp = ans
        for i in range(k, n):
            if s[i] in vowels:
                tmp += 1
            if s[i - k] in vowels:
                tmp -= 1

            ans = max(ans, tmp)

        return ans
