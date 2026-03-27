# Problem: Combinations
# Language: python3
# Runtime: 305 ms
# Memory: 18.3 MB

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []
        def backtrack(A):
            if len(A) == k:
                self.ans.append(A)
            else:
                for i in range(A[-1]+1,n+1):
                    backtrack(A + [i])
        for i in range(1,n+1):
            backtrack([i])
        return self.ans