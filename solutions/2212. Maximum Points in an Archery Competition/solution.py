# Problem: Maximum Points in an Archery Competition
# Language: python3
# Runtime: 580 ms
# Memory: 13.9 MB

class Solution:
    def maximumBobPoints(self, NA: int, A: List[int]) -> List[int]:
        N = len(A)
        def dp(i,na,l):
            if not na:
                return (0,l)
            if i == N:
                lt = l[:]
                lt[0] += na
                return (0,lt)
            
            s1,l1 = dp(i+1,na,l)
            s2,l2 = 0,None
            if A[i] == 0: 
                lt = l[:]
                lt[i] = 1
                s2,l2 = dp(i+1,na-1,lt)
                s2 += i
            elif A[i] < na:
                lt = l[:]
                lt[i] = A[i] + 1
                s2,l2 = dp(i+1,na-A[i]-1,lt)
                s2 += i
            if s1 >= s2:
                return s1,l1
            return s2,l2
        
        score, ans = dp(0,NA,[0] * N)
        return ans