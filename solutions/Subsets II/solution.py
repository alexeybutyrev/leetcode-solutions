# Problem: Subsets II
# Language: python3
# Runtime: 32 ms
# Memory: 14.5 MB

class Solution:
    def subsetsWithDup(self, A: List[int]) -> List[List[int]]:
        ans = set()
        N = len(A)
        def backtrack(c,i):
            nonlocal ans
            ans.add(tuple(sorted(c)))
            for j in range(i+1, N):
                backtrack(c + [A[j]],j)
        
        backtrack([],-1)
        return ans