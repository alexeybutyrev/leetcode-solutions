# Problem: Missing Number In Arithmetic Progression
# Language: python3
# Runtime: 48 ms
# Memory: 14.6 MB

class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        
        
        N = len(arr)
        
        delta = (arr[N-1] - arr[0]) // N
        
        
        c = arr[0]
        for i in range(1, N):
            c += delta
            if arr[i] != c:
                return c
        return arr[0]