# Problem: Previous Permutation With One Swap
# Language: python3
# Runtime: 228 ms
# Memory: 15.2 MB

class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        
        n = len(A)
        i = n - 1
        while i > 0 and A[i] >= A[i-1]:
            i-=1
        #print(i)
        if i <= 0:
            return A
        i -= 1
        #print(i)
        for j in range(n-1,-1,-1):
            if A[j] < A[i]:
                A[j], A[i] = A[i], A[j]
                return A
        return A