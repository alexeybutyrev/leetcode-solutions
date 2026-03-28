# Problem: Closest Divisors
# Language: python3
# Runtime: 176 ms
# Memory: 14.1 MB

class Solution:
    def closestDivisors(self, N: int) -> List[int]:
        
        for i in range(int(math.sqrt(N+2)), 0, -1):
            if (N + 1) % i ==0 :
                return [i, (N+ 1)//i]
            if (N + 2) % i ==0:
                return [i, (N+ 2)//i]
        
        return [1,N+1]
                    
            
                    
            