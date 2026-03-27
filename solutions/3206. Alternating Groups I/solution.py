# Problem: Alternating Groups I
# Language: python3
# Runtime: 42 ms
# Memory: 16.6 MB

class Solution:
    def numberOfAlternatingGroups(self, A: List[int]) -> int:
        
        def f(colors, k):
            N = len(colors)
            A = colors + colors
            q = deque()
            ans = 0
            for i,x in enumerate(A):
                if q and A[q[-1]] != x:
                    q.append(i)
                else:
                    q=deque()
                    q.append(i)
                
                if q[0] >= N:
                    return ans
                
                if len(q) == k:
                    ans += 1
                    q.popleft()
            return ans
        
        return f(A,3)
            