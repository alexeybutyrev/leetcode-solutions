# Problem: Special Array II
# Language: python3
# Runtime: 1024 ms
# Memory: 55.9 MB

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        A = [ 1 if x % 2  else 0 for x in nums]
        
        I = [0]
        N = len(A)
        if N == 1: return [True] * len(queries)
        
        for i in range(1,N):
            if not (A[i] ^ A[i-1]):
                I.append(i)
        if not I: return [True] * len(queries)

        ans = []
        for a,b in queries:
            l = bisect_right(I,a)
            r = bisect_right(I,b)
            if r != l:
                ans.append(False)
            else:
                ans.append(True)
        return ans