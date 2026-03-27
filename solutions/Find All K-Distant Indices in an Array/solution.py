# Problem: Find All K-Distant Indices in an Array
# Language: python3
# Runtime: 612 ms
# Memory: 14.2 MB

class Solution:
    def findKDistantIndices(self, A: List[int], key: int, k: int) -> List[int]:
        N = len(A)
        ans = []
        for i in range(N):
            for j in range(N):
                if abs(i-j) <= k and A[j] == key:
                    ans.append(i)
                    break
        
        return ans