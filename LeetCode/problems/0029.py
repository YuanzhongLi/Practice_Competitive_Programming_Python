MAX = (1<<31)-1
def divide_pos(x, y): # x//y
    # y, 2*y, 4*y, 8*y …
    # 1,  0,    1 -> 5y
    if x == 0: return 0
    ys = []
    while y <= x:
        ys.append(y)
        y += y

    N = len(ys)
    bit = [0 for _ in range(N)]
    for i in range(N-1, -1, -1):
        if x >= ys[i]:
            bit[i] = 1
            x -= ys[i]
    ret = 0
    d = 1
    for i in range(N):
        ret += d * bit[i]
        d += d

    return ret

class Solution:
    def divide(self, x: int, y: int) -> int:
        if x == 0: return 0
        sign_x = sign_y = 1
        if x < 0: sign_x = -1
        if y < 0: sign_y = -1
        sign = sign_x * sign_y
        ret = sign * divide_pos(abs(x), abs(y))
        if ret > MAX:
            return MAX
        return ret
