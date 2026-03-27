# Problem: Count Collisions on a Road
# Language: python3
# Runtime: 14 ms
# Memory: 18.2 MB

class Solution:
    def countCollisions(self, A: str) -> int:   
        return len(A.lstrip("L").rstrip("R").replace("S",""))
        