# Problem: Squirrel Simulation
# Language: python3
# Runtime: 134 ms
# Memory: 17.4 MB

class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        dist = lambda x,y: abs(x[0] - y[0]) + abs(x[1] - y[1])
        
        S = 2 * sum( dist(tree, n) for n in nuts)
        
        return min([S - dist(tree, n) + dist(squirrel, n) for n in nuts])
            
                    
            