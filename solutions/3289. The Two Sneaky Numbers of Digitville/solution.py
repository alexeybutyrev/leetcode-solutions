# Problem: The Two Sneaky Numbers of Digitville
# Language: python3
# Runtime: 3 ms
# Memory: 17.7 MB

class Solution:
    def getSneakyNumbers(self, A: List[int]) -> List[int]:
        y = 0
        for x in A:
            y ^= x
        n = len(A)-2
        for i in range(n):
            y ^= i
        
        lb = y & (-y)

        x1 = x2 = 0
        for x in A:
            if x & lb:
                x1 ^= x
            else:
                x2 ^= x
        
        for x in range(n):
            if x & lb:
                x1 ^= x
            else:
                x2 ^= x
        return [x1,x2]



        