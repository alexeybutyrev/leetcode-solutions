# Problem: Next Greater Element II
# Language: python3
# Runtime: 584 ms
# Memory: 15.6 MB

class Solution:
    def nextGreaterElements(self, A: List[int]) -> List[int]:
        stack = []
        ans = [-1] * (N:=len(A))
        for i in list(range(N)) * 2:
            while stack and A[stack[-1]] < A[i]:
                ans[stack.pop()] = A[i]
            stack.append(i)
        return ans
        