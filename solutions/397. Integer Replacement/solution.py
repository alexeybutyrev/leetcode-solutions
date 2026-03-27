# Problem: Integer Replacement
# Language: python3
# Runtime: 40 ms
# Memory: 16.1 MB

class Solution:
    def integerReplacement(self, n: int) -> int:
        h = []
        
        count = 0
        q = deque([n])
        
        ans = 0
        seen = set()
        while q:
            L = len(q)
            for _ in range(L):
                n = q.popleft()
                if n == 1: return ans
                if n & 1:
                    if n - 1 not in seen:
                        seen.add(n-1)
                        q.append(n-1)
                    if n + 1 not in seen:
                        seen.add(n+1)
                        q.append(n+1)
                else:
                    if n >> 1 not in seen:
                        seen.add(n>>1)
                        q.append(n >> 1)
            ans+=1
        
        
                 