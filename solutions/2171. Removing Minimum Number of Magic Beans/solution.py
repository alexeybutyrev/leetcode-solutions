# Problem: Removing Minimum Number of Magic Beans
# Language: python3
# Runtime: 2005 ms
# Memory: 28.4 MB

from statistics import median
class Solution:
    def minimumRemoval(self, A: List[int]) -> int:
        A.sort()
        ans = S = sum(A)
        N = len(A)
        
        for i,a in enumerate(A):
            ans = min(ans, S - (N-i)*a)
        return ans