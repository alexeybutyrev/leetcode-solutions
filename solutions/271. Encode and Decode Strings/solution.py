# Problem: Encode and Decode Strings
# Language: python3
# Runtime: 60 ms
# Memory: 14.6 MB

class Codec:
    def __init__(self):
        self.s = ""
        self.d = defaultdict(list)
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        s = ""
        for w in strs:
            s += w
        self.s = hash(w)
        self.d[self.s] = strs
        
        return self.s

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        return self.d[self.s]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))