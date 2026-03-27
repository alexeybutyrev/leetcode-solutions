# Problem: Longest Palindrome After Substring Concatenation I
# Language: python3
# Runtime: 1523 ms
# Memory: 17.7 MB

class Solution:
    def longestPalindrome(self, S: str, T: str) -> int:
        NS, NT = len(S), len(T)
        ans = 0
        is_pali = lambda x:  x == x[::-1]
        for i in range(NS):
            for j in range(i,NS+1):
                s = S[i:j]
                for i1 in range(NT):
                    for j1 in range(i1,NT+1):
                        t = T[i1:j1]
                        if is_pali(s + t):
                            ans = max(ans, len(s+t))
                        
        return ans