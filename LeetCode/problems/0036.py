class Solution:
    def isValidSudoku(self, B: List[List[str]]) -> bool:
        for i in range(3):
            for j in range(3):
                top_r = i * 3
                top_c = j * 3
                s = set([])
                for x in range(3):
                    for y in range(3):
                        c = B[top_r + x][top_c + y]
                        if c == '.':
                            continue
                        else:
                            if c in s:
                                return False
                            s.add(c)

        for x in range(9):
            s = set([])
            for y in range(9):
                c = B[x][y]
                if c == '.':
                    continue
                else:
                    if c in s:
                        return False
                    s.add(c)

        for y in range(9):
            s = set([])
            for x in range(9):
                c = B[x][y]
                if c == '.':
                    continue
                else:
                    if c in s:
                        return False
                    s.add(c)

        return True
