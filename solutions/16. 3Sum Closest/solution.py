# Problem: 3Sum Closest
# Language: python3
# Runtime: 420 ms
# Memory: 14.4 MB

class Solution:
    def threeSumClosest(self, A: List[int], t: int) -> int:
        N = len(A)
        A.sort()

        d = inf
        ans = -1
        for i in range(N):
            lo = i + 1
            hi = N - 1
            while lo < hi:
                s = A[i] + A[lo] + A[hi]
                #print(s,i,lo,hi)
                if d > abs(s - t):
                    d = abs(s - t)
                    ans = s
                
                if s < t:
                    lo += 1
                else:
                    hi -= 1
        
        return ans