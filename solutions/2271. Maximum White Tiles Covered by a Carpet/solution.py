# Problem: Maximum White Tiles Covered by a Carpet
# Language: python3
# Runtime: 1177 ms
# Memory: 39.3 MB

class Solution:
    def maximumWhiteTiles(self, A: List[List[int]], L: int) -> int:
        A = [[l,r] for l,r in A]
        A.sort()
        
        N = len(A)
        
        S = [0]
        ans = -1
        
        for l,r in A:
            S.append(S[-1] + (r-l+1))
        
        #print(A)
        #print(S)
        j = 0
        for i in range(N):
            r = min(A[-1][1], A[i][0] + L-1)
            while j < N and A[j][1] < r:
                j += 1
            
            #if j == N:
            #    ans = max(ans, S[-1] - S[i])
            #    return ans
            
            if r >= A[j][0]:
                curr = S[j+1] - S[i] - (A[j][1] -r)
            else:
                curr = S[j] - S[i]
            ans = max(ans, curr)
        
        return ans
        