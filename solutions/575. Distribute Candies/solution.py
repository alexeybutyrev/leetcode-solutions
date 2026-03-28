# Problem: Distribute Candies
# Language: python3
# Runtime: 832 ms
# Memory: 16.7 MB

class Solution:
    def distributeCandies(self, A: List[int]) -> int:
        N = len(A)
        n = N // 2
        
        c = set(A)
        
        
        
        s = set()
        
        for k in c:
            s.add(k)
            n -= 1
            if n == 0:
                break
        
        return len(s)