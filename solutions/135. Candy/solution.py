# Problem: Candy
# Language: python3
# Runtime: 147 ms
# Memory: 19.6 MB

class Solution:
    def candy(self, A: List[int]) -> int:
        L = [1]
        N = len(A)
        for i in range(1,N):
            if A[i] > A[i-1]:
                L.append(L[-1] + 1)
            else:
                L.append(1)
        
        R = [1]
        
        for i in range(N-2,-1,-1):
            if A[i] > A[i+1]:
                R.append(R[-1] + 1)
            else:
                R.append(1)
        
        R = R[::-1]
        ans = 0
        for l,r in zip(L,R):
            ans += max(l,r)
        return ans
        