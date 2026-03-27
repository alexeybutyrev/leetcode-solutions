# Problem: Max Number of K-Sum Pairs
# Language: python3
# Runtime: 883 ms
# Memory: 27.1 MB

class Solution:
    def maxOperations(self, A: List[int], k: int) -> int:
        
        pairs = set()
        
        ans = 0
        seen = Counter()
        for i,a in enumerate(A):
            if k - a in seen:
                ans += 1
                seen[k-a] -= 1
                if not seen[k-a]: del seen[k-a]
            else:
                seen[a] += 1
        return ans
            