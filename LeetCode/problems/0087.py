# from collections import deque
from collections import defaultdict


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        def possible(mp1, mp2):
            if len(mp1.keys()) != len(mp2.keys()):
                return False

            # 以降はkeyの数が同じ

            for key in mp1.keys():
                if mp1[key] != mp2[key]:
                    return False

            return True

        origin_s1_mp, origin_s2_mp = defaultdict(int), defaultdict(int)
        for i in range(len(s1)):
            origin_s1_mp[s1[i]] += 1
            origin_s2_mp[s2[i]] += 1

        if not possible(origin_s1_mp, origin_s2_mp):
            return False

        # 渡されるs1, s2において、各アルファベットの登場回数は同じ
        def rec(s1, s2):
            N = len(s1)
            if N <= 2:
                return True
            start_idx = 0
            for i in range(N):
                if s1[i] == s2[i]:
                    start_idx += 1
                else:
                    break

            if start_idx == N:
                return True

            end_idx = N
            for i in range(N):
                if s1[N - 1 - i] == s2[N - 1 - i]:
                    end_idx -= 1
                else:
                    break

            s1, s2 = s1[start_idx:end_idx], s2[start_idx:end_idx]
            N = len(s1)

            s1_mp, s2_mp, s2_r_mp = defaultdict(int), defaultdict(int), defaultdict(int)
            for i in range(N - 1):
                ch1, ch2, r_ch2 = s1[i], s2[i], s2[N - 1 - i]
                s1_mp[ch1] += 1
                s2_mp[ch2] += 1
                s2_r_mp[r_ch2] += 1
                print(s1_mp)
                print(s2_mp)
                print(s2_r_mp)
                print()
                if possible(s1_mp, s2_mp):
                    flag = False
                    if i <= N // 2:
                        flag = rec(s1[: i + 1], s2[: i + 1]) & rec(
                            s1[i + 1 :], s2[i + 1 :]
                        )
                    else:
                        flag = rec(s1[i + 1 :], s2[i + 1 :]) & rec(
                            s1[: i + 1], s2[: i + 1]
                        )
                    if flag:
                        return True

                if possible(s1_mp, s2_r_mp):
                    flag = False
                    if i <= N // 2:
                        flag = rec(s1[: i + 1], s2[N - 1 - i :]) & rec(
                            s1[i + 1 :], s2[: N - 1 - i]
                        )
                    else:
                        flag = rec(s1[i + 1 :], s2[: N - 1 - i]) & rec(
                            s1[: i + 1], s2[N - 1 - i :]
                        )
                    if flag:
                        return True

            # print(s1, s2, False)
            # print(s1_mp, s2_r_mp)
            return False

        return rec(s1, s2)


# Test
solution = Solution()
solution.isScramble("oatzzffqpnwcxhejzjsnpmkmzngne", "acegneonzmkmpnsjzjhxwnpqffzzt")
