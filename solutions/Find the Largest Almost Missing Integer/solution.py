# Problem: Find the Largest Almost Missing Integer
# Language: python3
# Runtime: 3 ms
# Memory: 17.8 MB

class Solution:
    def largestInteger(self, A: List[int], k: int) -> int:
        ans = -1
        C = Counter()
        for i in range(len(A)):
            B = A[i:i+k]
            
            if len(B) == k:
                for x in set(B):
                    C[x] += 1

        for x in C:
            if C[x] == 1:
                ans = max(ans, x)
        return ans