# Problem: Find The Original Array of Prefix Xor
# Language: python3
# Runtime: 2103 ms
# Memory: 32.7 MB

class Solution:
    def findArray(self, A: List[int]) -> List[int]:
        x = A[0]
        ans = [x]
        N = len(A)
        for i in range(1,N):
            ans.append(A[i] ^ A[i-1])
        return ans