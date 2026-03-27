# Problem: Reverse Words in a String III
# Language: python3
# Runtime: 24 ms
# Memory: 14.6 MB

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([w[::-1] for w in s.split(" ")])