class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        vs = ""
        for ch in s:
            if ch in vowels:
                vs += ch

        n = len(vs)
        i = n-1
        ret = ""
        for ch in s:
            if ch in vowels:
                ret += vs[i]
                i -= 1
            else:
                ret += ch

        return ret
