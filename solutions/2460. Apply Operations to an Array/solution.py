# Problem: Apply Operations to an Array
# Language: python3
# Runtime: 51 ms
# Memory: 14.1 MB

class Solution:
    def applyOperations(self, A: List[int]) -> List[int]:
        N = len(A)
        for i in range(N-1):
            if A[i] == A[i+1]:
                A[i]*=2
                A[i+1] = 0
        stack = []
        for a in A:
            if a:
                stack.append(a)
        return stack + (N - len(stack)) * [0]