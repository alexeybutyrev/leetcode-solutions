# Problem: Shortest Palindrome
# Language: python3
# Runtime: 411 ms
# Memory: 17 MB

class Solution:
    def shortestPalindrome(self, S: str) -> str:
        is_pali = lambda x:  x == x[::-1]
        N = len(S)
        for i in range(N,-1,-1):
            if is_pali(S[:i]):
                return S[i:][::-1] + S
            