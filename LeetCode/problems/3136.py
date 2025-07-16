# Solution Link: https://leetcode.com/problems/valid-word/solutions/6959580/python-enumerate-solution-with-japanese-wzy8p/


ord_0 = ord("0")
ord_9 = ord("9")

ord_a = ord("a")
ord_z = ord("z")

vowels = set(["a", "e", "i", "o", "u"])


class Solution:
    def isValid(self, word: str) -> bool:
        N = len(word)
        if N < 3:
            return False

        word = word.lower()

        def is_alphabet(ch):
            ord_ch = ord(ch)
            return ord_a <= ord_ch and ord_ch <= ord_z

        def is_vowel(ch):
            return ch in vowels

        def is_number(ch):
            ord_ch = ord(ch)
            return ord_0 <= ord_ch and ord_ch <= ord_9

        has_vowel = False
        has_consonant = False
        for ch in word:
            if is_number(ch):
                continue
            elif is_alphabet(ch):
                if is_vowel(ch):
                    has_vowel = True
                else:
                    has_consonant = True
            else:
                return False

        return has_vowel and has_consonant
