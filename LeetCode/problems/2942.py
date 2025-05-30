# Solution Link: https://leetcode.com/problems/find-words-containing-character/solutions/6774639/python-enumerate-solution-with-japanese-y66oj/


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        for i, word in enumerate(words):
            if x in word:
                ans.append(i)
        return ans
