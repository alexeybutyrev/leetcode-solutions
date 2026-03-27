# Problem: Check If It Is a Straight Line
# Language: python3
# Runtime: 64 ms
# Memory: 14.2 MB

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        p1,p2 = coordinates[0], coordinates[1]
        
        n = len(coordinates)
        if p1[0] == p2[0]:
            for i in range(n):
                if coordinates[i][0] != p1[0]:
                    return False
            return True
        
        if p1[1] == p2[1]:
            for i in range(n):
                if coordinates[i][1] != p1[1]:
                    return False
            return True
        
        
        dx, dy =  (p2[0] - p1[0]), (p2[1] - p1[1]) 
        
        eps = 1e-5
        for i in range(1,len(coordinates)):
            if abs((coordinates[i][1] - p1[1]) / dy - (coordinates[i][0] - p1[0]) / dx) > eps:
                return False
        
        return True