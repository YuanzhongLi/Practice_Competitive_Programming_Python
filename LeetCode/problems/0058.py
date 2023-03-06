class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ret = 0
        N = len(s)
        start_flag = False
        for i in range(N-1, -1, -1):
            if s[i] == ' ':
                if start_flag:
                    return ret
            else:
                if start_flag:
                    ret += 1
                else:
                    ret = 1
                    start_flag = True

        return ret
