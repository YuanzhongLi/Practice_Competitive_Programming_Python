# Solution Link: https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/solutions/6745067/python-enumerate-solution-with-japanese-explanation/


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans = []
        pre = -1
        for i, bi in enumerate(groups):
            if bi != pre:
                ans.append(words[i])
            pre = bi

        return ans
