# Problem: Best Sightseeing Pair
# Language: python3
# Runtime: 468 ms
# Memory: 19.9 MB

class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        B = [i + a for i,a in enumerate(A)]
        
        ans = 0 
        mx = B[0]
        N = len(A)
        for j in range(1,N):
            ans = max(ans, mx + A[j]-j)
            if B[j] > mx:
                mx = B[j]
        
        return ans