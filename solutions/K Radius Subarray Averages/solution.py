# Problem: K Radius Subarray Averages
# Language: python3
# Runtime: 1613 ms
# Memory: 35.4 MB

class Solution:
    def getAverages(self, A: List[int], k: int) -> List[int]:
        if not k:
            return A
        ans = []
        s = 0
        N = len(A)
        for i in range(k):
            if i == N: return ans
            s += A[i]
            ans.append(-1)
        j = i

        for l in range(i+1, 2 * k + 1):
            if l == N: return [-1] * N
            s += A[l]
        
        ans.append(s//(2*k+1))

        for l in range(2 * k + 1, N):
            s -= A[l - 2 * k - 1]
            s += A[l]
            ans.append(floor(s/(2*k+1)))
        return ans + [-1] * (j + 1)
            
        