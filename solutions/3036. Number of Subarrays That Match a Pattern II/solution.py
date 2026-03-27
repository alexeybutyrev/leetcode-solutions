# Problem: Number of Subarrays That Match a Pattern II
# Language: python3
# Runtime: 1504 ms
# Memory: 114.1 MB

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

class Solution:
    def countMatchingSubarrays(self, A: List[int], P: List[int]) -> int:
        B = []
        for i in range(1,len(A)):
            if A[i] > A[i-1]:
                B.append(1)
            elif A[i] == A[i-1]:
                B.append(0)
            else:
                B.append(-1)
        A = P + [215] + B
        
        dp = kmp(A)
        return dp.count(len(P))