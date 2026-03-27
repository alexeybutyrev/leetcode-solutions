# Problem: Beautiful Arrangement II
# Language: python3
# Runtime: 52 ms
# Memory: 15.2 MB

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        A = list(range(1,n+1))
        ans = list(range(1, n - k+1))

        B = deque(A[n-k:])

        C = []
        while B:
            if B:
                C.append(B.pop())
            if B:
                C.append(B.popleft())
        
        return ans + C
        
        