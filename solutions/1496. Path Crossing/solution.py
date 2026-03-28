# Problem: Path Crossing
# Language: python3
# Runtime: 44 ms
# Memory: 13.9 MB

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x,y = 0,0
        visited = set()
        visited.add((0,0))
        for s in path:
            
            if s == "N":
                y+=1
            if s == "S":
                y-=1
            if s == "E":
                x+=1
            if s == "W":
                x-=1

            if (x,y) in visited:
                return True
            else:
                visited.add((x,y))
        
        return False