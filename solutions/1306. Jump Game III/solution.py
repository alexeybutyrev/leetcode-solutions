# Problem: Jump Game III
# Language: python3
# Runtime: 212 ms
# Memory: 20.9 MB

from collections import deque
class Solution:
    def canReach(self, A: List[int], start: int) -> bool:
        
        n = len(A)
        
        visited = set()
        visited.add(start)
        q = deque([start])
        
        while q:
            l = len(q)
            for _ in range(l):
                ind = q.popleft()
                if A[ind] == 0:
                    return True
                if ind + A[ind] < n and ind + A[ind] not in visited:
                    visited.add(ind + A[ind])
                    q.append(ind+A[ind])
                
                if ind - A[ind] >= 0 and ind - A[ind] not in visited:
                    visited.add(ind - A[ind])
                    q.append(ind-A[ind])
        
        return False
                
        
        