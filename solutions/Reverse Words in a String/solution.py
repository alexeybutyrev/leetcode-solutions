# Problem: Reverse Words in a String
# Language: python3
# Runtime: 24 ms
# Memory: 14.7 MB

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(list(reversed(list(filter(lambda x: len(x) > 0, s.split(" "))))))
        