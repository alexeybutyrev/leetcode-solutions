# Problem: Append K Integers With Minimal Sum
# Language: python3
# Runtime: 672 ms
# Memory: 29.4 MB

class Solution:
    def minimalKSum(self, A: List[int], k: int) -> int:
        A = list(set(A))
        A.sort()
        
        mn = A[0]
        ms = A[-1]
        
        
        if mn > k:
            return k * (k + 1) // 2
        
        k -= (mn-1)
        ans = mn * (mn - 1) // 2
        
        for i in range(1,len(A)):
            a = A[i-1]
            if A[i] == a + 1: continue
                
            if A[i] - a-1 >= k:
                return ans + a * k + k*(k + 1) // 2
            else:
                d = A[i] - a-1
                k -= d
                ans += a * d + d*(d + 1) // 2
        
        return ans + ms * k + k*(k + 1) // 2