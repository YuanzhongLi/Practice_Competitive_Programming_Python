class Solution:
    def validPalindrome(self, s: str) -> bool:
        N = len(s)
        l = 0
        r = N-1
        erase = False
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else: # you have to erase
                # erase left
                l_ = l+1
                r_ = r
                l_flag, r_flag = True, True
                while l_ < r_:
                    if s[l_] == s[r_]:
                        l_ += 1
                        r_ -= 1
                    else:
                        l_flag = False
                        break

                # erase right
                l_ = l
                r_ = r-1
                while l_ < r_:
                    if s[l_] == s[r_]:
                        l_ += 1
                        r_ -= 1
                    else:
                        r_flag = False
                        break
                return l_flag or r_flag

        return True
