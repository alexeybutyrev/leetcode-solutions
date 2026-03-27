# Problem: Brick Wall
# Language: python3
# Runtime: 188 ms
# Memory: 19.2 MB

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
        c = Counter()
        for w in wall:
            
            c[w[0]] += 1
            for i in range(1, len(w)):
                w[i] += w[i-1]
                
                c[w[i]] += 1
        
        del c[wall[0][-1]]

        return len(wall) - max(c.values()) if c else len(wall)
                
        
        
        
        
                
        
        