# Problem: Alternating Groups II
# Language: python3
# Runtime: 755 ms
# Memory: 23.1 MB

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
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