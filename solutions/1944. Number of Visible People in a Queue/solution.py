# Problem: Number of Visible People in a Queue
# Language: python3
# Runtime: 1180 ms
# Memory: 29.8 MB

class Solution:
    def canSeePersonsCount(self, H: List[int]) -> List[int]:
        
        N = len(H)
        ans = [0] * N
        stack = []
        
        for i,h in enumerate(H):
            while stack and H[stack[-1]] < h:
                ans[stack.pop()] += 1
            
            if stack:
                ans[stack[-1]] += 1
            stack.append(i)
        
        return ans