# Problem: Maximal Rectangle
# Language: python3
# Runtime: 200 ms
# Memory: 15.5 MB

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        A = []
        for l in matrix:
            r = [+(l[0] == '1')]
            for i in range(1,len(l)):
                if l[i] != '1':
                    r.append(0)
                else:
                    r.append(r[-1] + 1)
                    
            A.append(r)
        
        
        def area_under_hist(A) -> int:
            stack = [-1]
            ans = 0
            for i,a in enumerate(A):
                while stack[-1] >= 0 and a <= A[stack[-1]]:
                    H = A[stack.pop()]
                    W = i - stack[-1] - 1
                    ans = max(ans, H * W)
                stack.append(i)

            while stack[-1] >= 0:
                H = A[stack.pop()]
                W = len(A) - stack[-1] - 1
                ans = max(ans, H * W)

            return ans
        
        ans = 0
        for r in zip(*A):
            ans = max(ans, area_under_hist(r))
        
        return ans
            