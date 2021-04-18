from collections import defaultdict
INF = float('inf')
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.word_idx = defaultdict(list)
        for i,word in enumerate(wordsDict):
            self.word_idx[word].append(i)
        self.mp = {}

    def shortest(self, word1: str, word2: str) -> int:
        if word1 > word2:
            word1, word2 = word2, word1

        if self.mp.get((word1, word2), None) == None:
            A = self.word_idx[word1]; N = len(A)
            B = self.word_idx[word2]; M = len(B)
            ai = 0; bi = 0
            ret = INF
            while ai < N and bi < M:
                ret = min(ret, abs(A[ai]-B[bi]))
                if A[ai] > B[bi]:
                    bi += 1
                else:
                    ai += 1
            self.mp[(word1, word2)] = ret
            return ret
        else:
            return self.mp[(word1, word2)]
