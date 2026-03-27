# Problem: Minimum Costs Using the Train Line
# Language: python3
# Runtime: 1049 ms
# Memory: 44.3 MB

class Solution:
    def minimumCosts(self, A: List[int], X: List[int], EC: int) -> List[int]:
        T = [0]
        B = [EC]
        
        N = len(A)
        ans = []
        for i in range(N):
            
            
            t = min(T[-1] + A[i], B[-1] + A[i])
            b = min(B[-1] + X[i], t + EC)
            
            ans.append(min(t,B[-1] + X[i]))
            
            T.append(t)
            B.append(b)
            
        
        return ans
            
        
        