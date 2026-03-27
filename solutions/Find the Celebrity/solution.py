# Problem: Find the Celebrity
# Language: python3
# Runtime: 2106 ms
# Memory: 14.6 MB

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        
        
        
        def is_cel(i):
            for j in range(n):
                if i != j:
                    if knows(i,j) or not knows(j,i):
                        return False
            return True
        
        
        for i in range(n):
            if is_cel(i):
                return i
        return -1