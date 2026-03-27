# Problem: Largest Rectangle in Histogram
# Language: python3
# Runtime: 776 ms
# Memory: 27.7 MB

class Solution:
    def largestRectangleArea(self, A: List[int]) -> int:
        stack = [-1]
        
        ans = 0
        for i,a in enumerate(A):
            while stack[-1] >= 0 and a <= A[stack[-1]]:
                    cur_height = A[stack.pop()]
                    cur_width = i - stack[-1] -1
                    ans = max(ans, cur_height * cur_width)
            
            stack.append(i)
             
        while stack[-1] >= 0:
            cur_height = A[stack.pop()]
            cur_width = len(A) - stack[-1] -1
            ans = max(ans, cur_height * cur_width)
        
        return ans