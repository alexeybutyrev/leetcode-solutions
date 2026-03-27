# Problem: Minimum Operations to Maximize Last Elements in Arrays
# Language: python3
# Runtime: 159 ms
# Memory: 16.6 MB

class Solution:
    def minOperations(self, A: List[int], B: List[int]) -> int:
        
        N = len(A)
        if N == 1: return 0
        
        def count(A,B):
            ca = A[-1]
            cb = B[-1]
            ans = 0
            for i in range(N-2,-1,-1):
                if A[i] <= ca and B[i] <= cb:
                    continue
                if A[i] > ca and B[i] <= ca and A[i] <= cb:
                    ans += 1
                    continue
                
                if B[i] > cb and A[i] <= cb and B[i] <= ca:
                    ans += 1
                    continue
                return inf
            return ans
        
        ans = count(A,B)
        A[-1],B[-1] = B[-1], A[-1]
        c2 = 1 + count(A,B)
        ans = min(ans,c2)
        return -1 if ans == inf else ans
                
        