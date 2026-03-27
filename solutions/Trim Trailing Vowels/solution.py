# Problem: Trim Trailing Vowels
# Language: python3
# Runtime: 0 ms
# Memory: 19.4 MB

class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        V = {'a', 'e', 'i', 'o', 'u'}

        A = list(s)

        while A and A[-1] in V:
            A.pop()

        return "".join(A)