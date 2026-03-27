# Problem: Number of Distinct Averages
# Language: python3
# Runtime: 39 ms
# Memory: 13.9 MB

class Solution:
    def distinctAverages(self, A: List[int]) -> int:
        ans = []
        while A:
            mn = min(A)
            ind = A.index(mn)
            A.remove(mn)
            
            mx = max(A)
            ind = A.index(mx)
            A.remove(mx)
            
            ans.append((mn + mx) / 2.0)
        return len(set(ans))
            