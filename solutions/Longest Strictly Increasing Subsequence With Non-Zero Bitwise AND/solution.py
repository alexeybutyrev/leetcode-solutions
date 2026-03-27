# Problem: Longest Strictly Increasing Subsequence With Non-Zero Bitwise AND
# Language: python3
# Runtime: 2818 ms
# Memory: 36 MB

def LIC( A: List[int]) -> int:
    B = [A[0]]
    
    for a in A[1:]:
        ind = bisect_left(B,a)
        if ind == len(B):
            B.append(a)
        else:
            B[ind] = a
    return len(B)
    
class Solution:
    def longestSubsequence(self, A: List[int]) -> int:
        N = len(A)
        ans = 0        
        for i in range(32):
            B = []
            for x in A:
                if x & (1 << i):
                    B.append(x)
            if B:
                ans = max(ans, LIC(B))
        
            
        return ans
        