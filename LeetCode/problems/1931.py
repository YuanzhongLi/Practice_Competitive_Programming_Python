# Solution Link: https://leetcode.com/problems/painting-a-grid-with-three-different-colors/solutions/6754864/python-matrix-and-dp-solution-with-japan-jz72/

MOD = 10**9 + 7


class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        # 状態数
        N = 3 << (m - 1)

        # id2state[id] -> (状態)
        id2state = [None for _ in range(N)]

        # state2id[(状態)] -> id
        state2id = {}

        global id_cnt
        id_cnt = 0

        tmp = []

        def dfs():
            if len(tmp) == m:
                global id_cnt
                id2state[id_cnt] = tuple(tmp)
                state2id[id2state[id_cnt]] = id_cnt

                id_cnt += 1
                return

            if len(tmp) == 0:
                for i in range(3):
                    tmp.append(i)
                    dfs()
                    tmp.pop()
            else:
                tmp.append((tmp[-1] + 1) % 3)
                dfs()
                tmp.pop()

                tmp.append((tmp[-1] + 2) % 3)
                dfs()
                tmp.pop()

        dfs()

        # 状態s1 -> 状態s2へと行けるか
        def canTransit(s1, s2):
            N = len(s1)
            for i in range(N):
                if s1[i] == s2[i]:
                    return False
            return True

        mat = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N):
            state_i = id2state[i]
            for j in range(N):
                state_j = id2state[j]
                if canTransit(state_i, state_j):
                    mat[i][j] = 1

        MAX = 1
        tmp = n - 1
        while tmp > 0:
            MAX += 1
            tmp >>= 1

        def mul_mat(mat1, mat2):
            N = len(mat1)
            ret = [[0 for _ in range(N)] for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    for k in range(N):
                        ret[i][j] += (mat1[i][k] * mat2[k][j]) % MOD
                    ret[i][j] %= MOD

            return ret

        # mats[i] = mat^(2^i)
        mats = [None for _ in range(MAX)]
        mats[0] = mat
        for i in range(1, MAX):
            mats[i] = mul_mat(mats[i - 1], mats[i - 1])

        # mat^(n-1)
        mat_n = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N):
            mat_n[i][i] = 1

        tmp = n - 1
        i = 0
        while tmp > 0:
            if tmp & 1 == 1:
                mat_n = mul_mat(mats[i], mat_n)
            tmp >>= 1
            i += 1

        ans = 0
        for i in range(N):
            ans += sum(mat_n[i])
            ans %= MOD

        return ans
