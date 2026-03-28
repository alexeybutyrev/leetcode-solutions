# Problem: Single-Threaded CPU
# Language: python3
# Runtime: 1872 ms
# Memory: 62.4 MB

from heapq import *
class Solution:
    def getOrder(self, A: List[List[int]]) -> List[int]:
        A = [ (st,et,i) for i, (st,et) in enumerate(A)]
        A.sort()
        
        A = deque(A)
        
        
        h = []
        ans = []
        P = 0
        i = A[0][0]
        while A or h:
            
            while A and A[0][0] <= i:
                _, d, ind = A.popleft()
                heappush(h, (d,ind))
            
            if P <= 0:
                if h:
                    d, ind = heappop(h)
                    P = d
                    ans.append(ind)
                else:
                    i = A[0][0]
                    continue
            
            
            if not A:
                while h:
                    d, ind = heappop(h)
                    ans.append(ind)
                return ans
            else:
                if A[0][0] - i >= P:
                    i += P
                    P = 0
                else:
                    P -= A[0][0] - i 
                    i = A[0][0]
                    
        
        return ans