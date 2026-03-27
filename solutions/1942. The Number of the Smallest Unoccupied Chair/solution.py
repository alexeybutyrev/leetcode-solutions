# Problem: The Number of the Smallest Unoccupied Chair
# Language: python3
# Runtime: 559 ms
# Memory: 22.9 MB

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        A = [(l,r,i) for i,(l,r) in enumerate(times)]
        A.sort()

        
        h = []
        chairs = []
        for i in range(len(A)):
            heappush(chairs, i)
        i = 0
        while i < len(A):
            l,r,t = A[i]
            while h and l >= h[0][0]:
                _,c = heappop(h)
                heappush(chairs, c)
             
            if t == targetFriend:
                return heappop(chairs)
            heappush(h, (r, heappop(chairs)) )
            
            
            
            i += 1
        
        return len(h)