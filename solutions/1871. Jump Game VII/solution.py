# Problem: Jump Game VII
# Language: python3
# Runtime: 268 ms
# Memory: 18.3 MB

from itertools import groupby
class Solution:
    def canReach(self, A: str, minJump: int, maxJump: int) -> bool:
        q = deque([0])
        N = len(A)
        
        for i in range(1,N):
            if A[i] == "0":
                while q and q[0] < i - maxJump:
                    q.popleft()
                if q and q[0] <= i - minJump:
                    q.append(i)
        
        return q and q[-1] == N-1
        

            
            