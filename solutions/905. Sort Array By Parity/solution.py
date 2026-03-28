# Problem: Sort Array By Parity
# Language: python3
# Runtime: 120 ms
# Memory: 14.4 MB

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        n = len(A)
        if 1 == n:
            return A
        i = 0
        count = 0
        while count < n:
            if A[i] % 2 != 0:
                v = A.pop(i)
                A.append(v)
                count +=1
            else:
                i+=1
                count +=1
                
        return A