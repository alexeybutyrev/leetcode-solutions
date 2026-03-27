# Problem: Continuous Subarrays
# Language: python3
# Runtime: 875 ms
# Memory: 27.1 MB

class Solution:
    def continuousSubarrays(self, A: List[int]) -> int:
        N = len(A)
        nQ,xQ = deque(), deque()
        
        left = 0
        ans = 0
        
        for right in range(N):
            
            while xQ and A[xQ[-1]] < A[right]:
                xQ.pop()
            xQ.append(right)
            
            while nQ and A[nQ[-1]]>A[right]:
                nQ.pop()
            nQ.append(right)
            while A[xQ[0]] - A[nQ[0]] > 2:
                if xQ[0] <nQ[0]:
                    left = xQ.popleft() +1
                else:
                    left = nQ.popleft() +1
            ans += right - left +1
        
        return ans