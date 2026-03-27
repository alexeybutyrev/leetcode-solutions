# Problem: Minimum Number of Operations to Reinitialize a Permutation
# Language: python3
# Runtime: 496 ms
# Memory: 14.3 MB

class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm = list(range(n))
        copy = list(range(n))
        
        arr = [0] * n
        count = 0
        def equal(a,b):
            for x,y in zip(a,b):
                if x != y:
                    return False
            return True
        
        while True:
            for i in range(n):
                if i % 2 == 0:
                    arr[i] = perm[i//2]
                else:
                    arr[i] = perm[n // 2 + (i - 1) // 2]
            
            count += 1
            if equal(copy,arr):
                return count
            else:
                perm = arr[:]
        
                