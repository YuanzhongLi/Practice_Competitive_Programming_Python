# Solution Link: https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/solutions/6778103/python-adhoc-solution-with-japanese-expl-v4ec/


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ord_a = ord("a")

        cnt = defaultdict(int)
        for word in words:
            cnt[word] += 1

        # centerに"xx"タイプをすでに置いたか
        center = False

        ans = 0
        for i in range(26):
            # "xx"タイプを考える
            # "xx"タイプのwordは一度だけ真ん中に使用可能
            ch_i = chr(ord_a + i)
            same_i = cnt[ch_i + ch_i]
            ans += 4 * (same_i // 2)
            if (not center) and (same_i % 2 == 1):
                center = True
                ans += 2

            # "xy","yx"のペアを考える
            for j in range(i + 1, 26):
                ch_j = chr(ord_a + j)
                xy = ch_i + ch_j
                yx = ch_j + ch_i
                ans += 4 * min(cnt[xy], cnt[yx])

        return ans
