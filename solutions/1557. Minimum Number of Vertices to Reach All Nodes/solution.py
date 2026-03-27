# Problem: Minimum Number of Vertices to Reach All Nodes
# Language: python3
# Runtime: 1165 ms
# Memory: 55 MB

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        seen = set([v for u,v in edges])        
        return [i for i in range(n) if i not in seen]