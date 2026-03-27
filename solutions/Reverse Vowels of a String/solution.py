# Problem: Reverse Vowels of a String
# Language: python3
# Runtime: 382 ms
# Memory: 15.3 MB

class Solution:
    def reverseVowels(self, s: str) -> str:
        A = []
        for l in s:
            if l in ['a', 'e', 'i', 'o','u'] + list(map(lambda x: x.upper(), ['a', 'e', 'i', 'o','u'])):
                A.append(l)
        s = list(s)
        for i,l in enumerate(s):
            if l in ['a', 'e', 'i', 'o','u'] + list(map(lambda x: x.upper(), ['a', 'e', 'i', 'o','u'])):
                s[i] = A.pop()
        return "".join(s)