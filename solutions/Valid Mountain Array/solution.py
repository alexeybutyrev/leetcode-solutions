# Problem: Valid Mountain Array
# Language: python3
# Runtime: 192 ms
# Memory: 15.7 MB

class Solution:
    def validMountainArray(self, a: List[int]) -> bool:
        n = len(a)
        if n == 1:
            return False
        
        if a[1] <= a[0]:
            return False
        
        for i in range(1,n):
            if a[i] <= a[i-1]:
                break
            
        
        if a[i] == a[i-1]:
            return False
        
        for j in range(i,n):
            if a[j] >= a[j-1]:
                return False
        return True