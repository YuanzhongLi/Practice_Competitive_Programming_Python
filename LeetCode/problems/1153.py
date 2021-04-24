class Solution:
    def canConvert(self, s1, s2):
        if len(set(s2)) == 26:
            return s1 == s2

        mp = {}
        for i in range(len(s1)):
            ch1 = s1[i]; ch2 = s2[i]
            if ch1 in mp:
                if mp[ch1] != ch2:
                    return False
            else:
                mp[ch1] = ch2
        return True
