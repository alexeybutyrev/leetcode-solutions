# Problem: Minimum Deletions to Make String Balanced
# Language: python3
# Runtime: 500 ms
# Memory: 25.5 MB

class Solution:
    def minimumDeletions(self, s: str) -> int:
        curr = 0
        B = []
        for x in s:
            if x == 'b':
                curr += 1
            B.append(curr)
        
        A = []
        curr = 0
        for x in s[::-1]:
            
            if x == 'a':
                curr += 1
            A.append(curr)
        A = A[::-1]
        ans = len(s)
        for i in range(len(s)):
            ans = min(ans, B[i] + A[i]-1)
        return ans
                
            
            