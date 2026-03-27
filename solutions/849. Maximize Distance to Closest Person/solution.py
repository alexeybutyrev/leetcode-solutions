# Problem: Maximize Distance to Closest Person
# Language: python3
# Runtime: 124 ms
# Memory: 14.6 MB

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        
        for i in range(n):
            if seats[i] == 1:
                break
        
        
        if i != 0:
            d = i
        else:
            d = 0 
        
        left, right = i, i
        while right < n:
            if seats[right] == 1:
                
                if (right - left) //2  > d:
                    d = (right - left) //2
                left = right
            right += 1
        
        if seats[n-1] == 0:
            if n - 1 - left > d:
                return n - 1 - left
        
        return d