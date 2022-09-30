class Solution:
    def maximum69Number (self, num: int) -> int:
        S = str(num)
        new_S = ""
        flag = True
        for ch in S:
            if ch == '6' and flag:
                new_S += '9'
                flag = False
            else:
                new_S += ch
        return int(new_S)
