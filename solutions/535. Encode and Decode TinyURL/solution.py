# Problem: Encode and Decode TinyURL
# Language: python3
# Runtime: 32 ms
# Memory: 14.2 MB

class Codec:

    def __init__(self):
        self.id = 0
        self.hash = {}
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.hash[self.id] = longUrl
        self.id += 1
        return "http://tinyurl.com/" + str(self.id-1)
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.hash[int(shortUrl.lstrip("http://tinyurl.com/"))]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))