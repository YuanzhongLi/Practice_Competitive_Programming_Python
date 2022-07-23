class Trie:
    def __init__(self):
        self.tree = {}

    def insert(self, word: str) -> None:
        cur = self.tree
        for ch in word:
            if ch in cur:
                cur = cur[ch]
            else:
                cur[ch] = {}
                cur = cur[ch]
        cur['.'] = True


    def search(self, word: str) -> bool:
        cur = self.tree
        for ch in word:
            if ch in cur:
                cur = cur[ch]
            else:
                return False

        return '.' in cur

    def startsWith(self, prefix: str) -> bool:
        cur = self.tree
        for ch in prefix:
            if ch in cur:
                cur = cur[ch]
            else:
                return False

        return True
