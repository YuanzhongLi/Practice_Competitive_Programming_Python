def four(ary):
    two = True
    for i in range(1, 9):
        if ary[i]:
            two = False
            break

    if two:
        return 2

    one = True
    for i in range(3, 7):
        if ary[i]:
            one = False
            break

    if one:
        return 1

    one = True
    for i in range(1, 5):
        if ary[i]:
            one = False
            break

    if one:
        return 1

    one = True
    for i in range(5, 9):
        if ary[i]:
            one = False
            break

    if one:
        return 1

    return 0

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        mp = {}
        for seat in reservedSeats:
            row, col = seat
            if not (row in mp):
                mp[row] = [False for _ in range(10)]

            mp[row][col-1] = True

        ans = 0
        for ary in mp.values():
            ans += four(ary)
            n -= 1

        ans += 2 * n
        return ans
