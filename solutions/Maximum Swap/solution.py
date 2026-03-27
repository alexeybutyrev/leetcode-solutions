# Problem: Maximum Swap
# Language: python3
# Runtime: 34 ms
# Memory: 16.2 MB

class Solution:
    def maximumSwap(self, num: int) -> int:
        
        S = list(str(num))
        N = len(S)
        ans = str(num)
        for i in range(N):
            A = S[:]
            for j in range(i+1,N):
                A[i],A[j] = A[j], A[i]
                if "".join(A) > ans:
                    ans = "".join(A)
                A[i],A[j] = A[j], A[i]
        return int(ans)