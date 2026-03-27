# Problem: Beautiful Array
# Language: python3
# Runtime: 40 ms
# Memory: 14.6 MB

class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        A = [1]
        
        while len(A) < n:
            A = [i * 2 - 1 for i in A] + [2 * i for i in A]
                    
        
        return [i for i in A if i <= n]
    