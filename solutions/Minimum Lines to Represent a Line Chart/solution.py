# Problem: Minimum Lines to Represent a Line Chart
# Language: python3
# Runtime: 1586 ms
# Memory: 59.1 MB

class Solution:
    def minimumLines(self, A: List[List[int]]) -> int:
        A.sort()
        if len(A) == 1:
            return 0
        if len(A) <= 2:
            return 1
        B = []
        B.append(A[0])
        B.append(A[1])
        count = 1
        for x,y in A[2:]:
            dx = B[-1][0] - B[-2][0]
            dy = B[-1][1] - B[-2][1]
            
            ndx = x - B[-1][0]
            ndy = y - B[-1][1]
            
            if ndx * dy != ndy * dx:
                count += 1
                
            B.append([x,y])
        
        return count