# Problem: Find K Closest Elements
# Language: python3
# Runtime: 913 ms
# Memory: 15.9 MB

class Solution:
    def findClosestElements(self, A: List[int], k: int, x: int) -> List[int]:
        h = []
        for i in range(k):
            heappush(h,(-abs(x-A[i]),A[i]))
        
        for y in A[k:]:
            if abs(y-x) < -h[0][0]:
                heappop(h)
                heappush(h,(-abs(y-x),y))
        A =[]
        while h:
            _,x = heappop(h)
            A.append(x)
        return sorted(A)

        
