# Problem: Minimum Length of String After Deleting Similar Ends
# Language: python3
# Runtime: 124 ms
# Memory: 15 MB

class Solution:
    def minimumLength(self, s: str) -> int:
        N = len(s)
        i, j = 0, N - 1
        
        while i < j:

            if s[i] == s[j]:
                c = s[i]
                
                while i < N and s[i] == c:
                    i+=1
                
                while j > 0 and s[j] == c :
                    j-=1
            else:
                return 1 + j - i

        return 1 if i == j else 0