vowels = set(['a', 'e', 'i', 'o', 'u'])

def get_word_pattern(word):
    ret = ""
    for ch in word.lower():
        if  ch in vowels:
            ret += '*'
        else:
            ret += ch
    return ret

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        d1 = set(wordlist)
        d2 = {}
        d3 = {}
        for word in wordlist:
            word_lower = word.lower()
            if not (word_lower in d2):
                d2[word_lower] = word

            word_pattern = get_word_pattern(word)
            if not (word_pattern in d3):
                d3[word_pattern] = word

        ret = []
        for query in queries:
            if query in d1:
                ret.append(query)
                continue

            query_lower = query.lower()
            if query_lower in d2:
                ret.append(d2[query_lower])
                continue

            query_pattern = get_word_pattern(query)
            if query_pattern in d3:
                ret.append(d3[query_pattern])
                continue

            ret.append("")

        return ret
