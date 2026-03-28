# Problem: Array Nesting
# Language: python3
# Runtime: 104 ms
# Memory: 19.3 MB

class Solution:
    def arrayNesting(self, A: List[int]) -> int:
        i = 0
        seen = set()
        N = len(A)
        ans = 0
        seen = set(range(N))
        
        while seen:
            
            s = set()
            ind = seen.pop()
            while ind not in s:
                s.add(ind)
                ind = A[ind]
            
            seen -= s
            ans = max(len(s),ans)
            
            if len(seen) <= ans:
                return ans
        return ans