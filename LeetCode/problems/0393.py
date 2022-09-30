def check0(x):
    return (x >> 7) == 0

def check1(x):
    return (x >> 5) == 6

def check2(x):
    return (x >> 4) == 14

def check3(x):
    return (x >> 3) == 30

def check4(x):
    return (x >> 6) == 2

def check(x):
    if check0(x):
        return 0
    elif check1(x):
        return 1
    elif check2(x):
        return 2
    elif check3(x):
        return 3
    elif check4(x): # 10xxxxxx
        return 4
    else:
        return -1


class Solution:
    def validUtf8(self, A: List[int]) -> bool:
        state = 0
        for a in A:
            c = check(a)
            if c == -1:
                return False

            if state == 0:
                if c == 4:
                    return False
                state = c # c = {0,1,2,3}
            elif state == 1:
                if c == 4:
                    state = 0
                else:
                    return False
            elif state == 2:
                if c == 4:
                    state = 1
                else:
                    return False
            elif state == 3:
                if c == 4:
                    state = 2
                else:
                    return False

        return state == 0
