# Problem: Valid Square
# Language: python3
# Runtime: 60 ms
# Memory: 14.3 MB

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        A = [p1, p2, p3, p4]
        
        for i, a in enumerate(A):
            v = []
            for j, b in enumerate(A):
                if i != j:
                    if a == b:
                        return False
                    v.append( (A[i][0] - A[j][0],A[i][1] - A[j][1]) )
                                
            v1,v2,v3 = v
            d1 = (v1[0] * v1[0] + v1[1] * v1[1])
            d2 = (v2[0] * v2[0] + v2[1] * v2[1])
            d3 = (v3[0] * v3[0] + v3[1] * v3[1])
            if d1 != d2 and d2 != d3 and d1 != d3:
                return False
            
            a1 = (v1[0] * v2[0] + v1[1] * v2[1])
            a2 = (v1[0] * v3[0] + v1[1] * v3[1])
            a3 = (v3[0] * v2[0] + v3[1] * v2[1])
            
            if a1 != 0 and a2 != 0 and a3 != 0:
                return False
            
        
        return True