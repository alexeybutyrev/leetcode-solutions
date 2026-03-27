# Problem: Maximum Product of Three Elements After One Replacement
# Language: python3
# Runtime: 113 ms
# Memory: 32.6 MB

class Solution:
    def maxProduct(self, A: List[int]) -> int:
        A = [abs(x) for x in A]
        A.sort()
        a = A.pop()
        b = A.pop()
        c = A.pop()

        return a * b * 10**5

        
            

        