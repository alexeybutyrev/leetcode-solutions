# Problem: K Items With the Maximum Sum
# Language: python3
# Runtime: 43 ms
# Memory: 13.8 MB

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k == 0:
            return 0
        s = 0
        for i in range(numOnes):
            s += 1
            k -= 1
            if k == 0:
                return s
        
        for i in range(numZeros):
            s += 0
            k -= 1
            if k == 0:
                return s
        
        for i in range(numNegOnes):
            s -= 1
            k -= 1
            if k == 0:
                return s
        return s
        