# Problem: Uncommon Words from Two Sentences
# Language: python3
# Runtime: 37 ms
# Memory: 16.6 MB

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        return (set(s1.split(" ")) - set(s2.split(" ")) - {k for k,v in Counter(s1.split(" ")).items() if v > 1}) | (set(s2.split(" ")) - set(s1.split(" ")) - {k for k,v in Counter(s2.split(" ")).items() if v > 1})