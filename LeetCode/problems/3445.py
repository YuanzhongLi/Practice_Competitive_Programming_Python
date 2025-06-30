# Solution Link: https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/solutions/6831227/python-range-sum-and-2-pointer-solution-oxs6g/

INF = 10**18


class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        def pattern(a_cnt, b_cnt):
            return (a_cnt & 1) * 2 + (b_cnt & 1)

        def calc(a, b):
            N = len(s)

            # 現在の個数
            a_cnt, b_cnt = 0, 0
            last_a_idx, last_b_idx = -1, -1
            for i in range(k):
                ch = s[i]
                if ch == a:
                    a_cnt += 1
                    last_a_idx = i
                elif ch == b:
                    b_cnt += 1
                    last_b_idx = i

            ret = -INF
            if pattern(a_cnt, b_cnt) == 2 and b_cnt > 0:
                ret = a_cnt - b_cnt

            # i-k+1,last_a_idx,last_b_idxより前のパターンでの最小値を記録する
            #        :    a,   b
            # memo[0]: even, even
            # memo[1]: even, odd
            # memo[2]: odd , even
            # memo[3]: odd , odd
            memo = [INF for _ in range(4)]

            # even, evenのパターンだけどちらの文字も含まれないのは空文字列で成立するので0で初期化
            memo[0] = 0

            # jはi-k+1,last_a_idx,last_b_idxを超えない様にするためのインデックス
            # これは少なくともk個前かつ文字a,bどちらも含むようにするため
            j = 0
            a_cnt2 = 0
            b_cnt2 = 0
            for i in range(k, N):
                ch = s[i]
                if ch == a:
                    a_cnt += 1
                    last_a_idx = i
                elif ch == b:
                    b_cnt += 1
                    last_b_idx = i

                while j < min(i - k + 1, last_a_idx, last_b_idx):
                    ch2 = s[j]
                    if ch2 == a:
                        a_cnt2 += 1
                    elif ch2 == b:
                        b_cnt2 += 1
                    # i-k+1,last_a_idx,last_b_idxより前のパターンの最小値を更新
                    before_pattern = pattern(a_cnt2, b_cnt2)
                    memo[before_pattern] = min(memo[before_pattern], a_cnt2 - b_cnt2)
                    j += 1

                # 現在のa_cntとb_cntの偶奇のパターン
                cur_pattern = pattern(a_cnt, b_cnt)

                # 最大化するための対応する偶奇のパターン
                target_pattern = pattern((a_cnt & 1) ^ 1, b_cnt)

                if a_cnt > 0 and b_cnt > 0 and memo[target_pattern] != INF:
                    ret = max(ret, a_cnt - b_cnt - memo[target_pattern])
            return ret

        ans = -INF
        for i in range(5):
            for j in range(5):
                if i == j:
                    continue
                ans = max(ans, calc(str(i), str(j)))

        return ans
