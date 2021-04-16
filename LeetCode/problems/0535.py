class Codec:
    def __init__(self):
        self.cnt = 0
        self.l2s = {}
        self.s2l = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        shortUrl = str(self.cnt); self.cnt += 1
        self.l2s[longUrl] = shortUrl
        self.s2l[shortUrl] = longUrl
        return shortUrl


    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.s2l[shortUrl]
