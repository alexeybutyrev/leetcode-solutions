# Problem: Shortest Palindrome
# Language: python3
# Runtime: 44 ms
# Memory: 17.1 MB

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        N = len(s)
        r = s[::-1]
        s = s + "#" + r
        def kmp(s):
            """
            Knuth-Morris-Pratt Algorythm of finding the longest common prefix that is also suffix
            """
            
            N = len(s)
            dp = [0] * N
            k = 0
            for i in range(1,N):
                while s[i] != s[k] and k > 0:
                    k = dp[k-1]
                
                if s[i] == s[k]:
                    k+=1
                
                dp[i] = k
            
            return dp
        
        dp = kmp(s)
        return  r[0:N-dp[-1]] + s[0:N]
        