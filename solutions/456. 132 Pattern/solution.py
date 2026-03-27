# Problem: 132 Pattern
# Language: python3
# Runtime: 380 ms
# Memory: 36.3 MB

class Solution:
    def find132pattern(self, A: List[int]) -> bool:
        mn = inf
        mins = []
        for a in A:
            mn = min(mn, a)
            mins.append(mn)
        
        stack = []
        for j in range(len(A) - 1, -1, -1):
            if A[j] > mins[j]:
                while stack and stack[-1] <= mins[j]:
                    stack.pop()
            
                if stack and stack[-1] < A[j]:
                    return True
                
                stack.append(A[j])
            
        
        return False
        