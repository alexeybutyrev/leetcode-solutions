# Problem: Valid Mountain Array
# Language: python3
# Runtime: 211 ms
# Memory: 15.6 MB

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3 or A[0] >= A[1]:
            return False
        
        for i in range(1,N:=len(A)):
            if A[i] == A[i-1]:
                return False
            if A[i] < A[i-1]:
                break
        else:
            return False
        
        for j in range(i+1,N):
            if A[j] >= A[j-1]:
                return False
        return True