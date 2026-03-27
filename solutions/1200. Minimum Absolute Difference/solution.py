# Problem: Minimum Absolute Difference
# Language: python3
# Runtime: 60 ms
# Memory: 31.5 MB

class Solution:
    def minimumAbsDifference(self, A: List[int]) -> List[List[int]]:
        A.sort()
        d = inf
        for i in range(1,len(A)):
            d = min(d,A[i] - A[i-1])
        
        ans = []
        for i in range(1,len(A)):
            if A[i] - A[i-1] == d:
                ans.append([A[i-1],A[i]])
        return sorted(ans)
            
        
