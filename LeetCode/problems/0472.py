class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            cur = trie
            for ch in word:
                if ch in cur:
                    cur = cur[ch]
                else:
                    cur[ch] = {}
                    cur = cur[ch]
            cur['E'] = True # 'E' means the end of the word

	      # recursion function for checking if a word prefix is in words
		    # check if the word is consist of more or equal than 2 words
		    # nums is a counter which counts how many words it is consist of
        def check(word, nums):
            N = len(word)
            cur = trie
            for i, ch in enumerate(word):
                if ch in cur:
                    cur = cur[ch]
                    if 'E' in cur:
                        if i == N-1:
                            if nums+1 >= 2:
                                return True
                            else:
                                return False
                        else:
                            if check(word[i+1:], nums+1):
                                return True
                else:
                    return False

        ret = []
        for word in words:
            if check(word, 0):
                ret.append(word)

        return ret
