# Solution Link: https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/solutions/6748654/python-dp-solution-with-japanese-explana-4k88/


class Solution:
    def getWordsInLongestSubsequence(
        self, words: List[str], groups: List[int]
    ) -> List[str]:
        def isHammingD1(idx1, idx2):
            if groups[idx1] == groups[idx2]:
                return False

            w1, w2 = words[idx1], words[idx2]
            if len(w1) != len(w2):
                return False

            N = len(w1)
            diff = 0
            for i in range(N):
                if w1[i] != w2[i]:
                    diff += 1
                if diff > 1:
                    return False

            return diff == 1

        N = len(words)

        # dp[i]: i番目のwordを末尾とする最長部分列について
        # [1つ前のwordのindex（なければwordと同じ）, 長さ]
        dp = [[i, 1] for i in range(N)]

        max_l = 0
        max_idx = -1
        for i, word in enumerate(words):
            # words[i]を末尾とする最長部分列
            i_l = 1
            for j in range(i):
                if isHammingD1(i, j):
                    j_l = dp[j][1]
                    if j_l + 1 > i_l:
                        i_l = j_l + 1
                        dp[i][0], dp[i][1] = j, i_l

            if i_l > max_l:
                max_l = i_l
                max_idx = i

        cur_idx = max_idx
        ans = []
        while True:
            ans.append(words[cur_idx])
            if dp[cur_idx][0] == cur_idx:
                break

            cur_idx = dp[cur_idx][0]

        ans.reverse()

        return ans
