# Problem: Longest Fibonacci Subarray
# Language: python3
# Runtime: 126 ms
# Memory: 33.5 MB

class Solution:
    def longestSubarray(self, A: List[int]) -> int:
        N = len(A)
        q = []
        ans = 2
        for x in A:
            if len(q) < 2:
                q.append(x)
                
            else:
                if q[-1] + q[-2] == x:
                    q.append(x)
                else:
                    q = [q[-1], x]
                    
            
            ans = max(ans, len(q))
        return ans