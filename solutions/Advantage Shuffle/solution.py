# Problem: Advantage Shuffle
# Language: python3
# Runtime: 352 ms
# Memory: 17 MB

from math import inf
class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        
        if not A:
            return A
        
        n = len(A)
        B = [(num,i) for i,num in enumerate(B)]
        A.sort()
        B.sort()
        res = [-1] * n
        
        j = 0
        left = []

        for num,i in B:            
            while j < n and A[j] <= num:
                left.append(A[j])
                j+=1               
            
            if j >= n:
                break
                
            if A[j] > num:
                res[i] = A[j]
                j+=1
                
                    
        i = 0
        while left and i < n:
            
            if res[i] < 0:
                res[i] = left.pop()
            i+=1
            
        return res
                    