class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans = []
        pre = -1
        for i, bi in enumerate(groups):
            if bi != pre:
                ans.append(words[i])
            pre = bi

        return ans
