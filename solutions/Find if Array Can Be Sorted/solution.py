# Problem: Find if Array Can Be Sorted
# Language: python3
# Runtime: 12 ms
# Memory: 16.7 MB

class Solution:
    def canSortArray(self, A: List[int]) -> bool:
        B = []
        for x in A:
            B.append(bin(x)[2:].count("1"))
        
        N = len(A)
        C = [A[0]]
        ANS = []
        for i in range(1, N):
            if B[i] == B[i-1]:
                C.append(A[i])
            else:
                C.sort()
                ANS += C[:]
                C = [A[i]]
        C.sort()
        ANS += C[:]
        
        return ANS == sorted(A)
            