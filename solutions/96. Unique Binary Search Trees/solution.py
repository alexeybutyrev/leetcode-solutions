# Problem: Unique Binary Search Trees
# Language: python3
# Runtime: 24 ms
# Memory: 14.1 MB

class Solution:
    def numTrees(self, n: int) -> int:
        
        @cache
        def count(n):
            if n <= 1:
                return 1
            s = 0
            for i in range(n):
                s += count(i) * count(n-i-1)

            
            return s
        
        return count(n)