# Problem: Convert 1D Array Into 2D Array
# Language: python3
# Runtime: 2105 ms
# Memory: 22.6 MB

class Solution:
    def construct2DArray(self, A: List[int], m: int, n: int) -> List[List[int]]:
        N = len(A)
        if m * n != N:
            return []
        
        ans = []
        i = 0
        for _ in range(m):
            r = []
            for j in range(n):
                r.append(A[i])
                i+=1
            ans.append(r)
        return ans