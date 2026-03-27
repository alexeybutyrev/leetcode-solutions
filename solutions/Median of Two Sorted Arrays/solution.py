# Problem: Median of Two Sorted Arrays
# Language: python3
# Runtime: 4 ms
# Memory: 18.1 MB

class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        
        N = len(A)
        def median(A):
            i = len(A) // 2
            if len(A) & 1: return A[i]
            return (A[i] + A[i-1])  * 0.5
        
        if not N: return median(B)
        M = len(B)
        if not M: return median(A)

        i = j = 0

        C = []
        while len(C) < N + M:
            if i == N:
                C.append(B[j])
                j+=1
                continue
                
            if j == M:
                C.append(A[i])
                i+=1
                continue
                
            if A[i] <= B[j]:
                C.append(A[i])
                i += 1
            else:
                C.append(B[j])
                j += 1
        return median(C)

