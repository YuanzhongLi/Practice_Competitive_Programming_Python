class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        chs = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        s = set([])
        for w in words:
            tmp = []
            for ch in w:
                tmp.append(chs[ord(ch)-ord('a')])
            s.add(''.join(tmp))
        return len(s)
