# Problem: Contains Duplicate II
# Language: python3
# Runtime: 1385 ms
# Memory: 27.6 MB

class Solution:
    def containsNearbyDuplicate(self, A: List[int], k: int) -> bool:
        k+=1
        N = len(A)
        c = Counter(A[:k])
        if max(c.values()) > 1:
            return True
        
        for i in range(k,N):
            c[A[i-k]] -= 1
            c[A[i]] += 1
            if c[A[i]] > 1:
                return True