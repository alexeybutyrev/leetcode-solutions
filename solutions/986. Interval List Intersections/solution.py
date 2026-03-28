# Problem: Interval List Intersections
# Language: python3
# Runtime: 152 ms
# Memory: 14.5 MB

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        
        n, m = len(A), len(B)
        if 0 == n or 0 == m:
            return []
        i = j = 0
        C = []
        while i<n and j<m:
            L = max(A[i][0], B[j][0])
            R = min(A[i][1], B[j][1])
            
            if B[j][1] > A[i][1]:
                i+=1
            else:
                j+=1
    
            if L <= R:
                C.append([L,R])
    
        return C