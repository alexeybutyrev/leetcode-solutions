# Problem: Median of Two Sorted Arrays
# Language: python3
# Runtime: 81 ms
# Memory: 16.6 MB

class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        
        def find(A,B,k):
            if not A:
                return B[k]
            if not B:
                return A[k]
            
            ia = len(A) // 2
            ib = len(B) // 2
            a = A[ia]
            b = B[ib]
            
            if ia + ib < k:
                if a > b:
                    return find(A,B[ib +1:], k - ib - 1)
                else:
                    return find(A[ia+1:],B, k - ia - 1)
            else:
                if a > b:
                    return find(A[:ia],B, k)
                else:
                    return find(A,B[:ib], k)
        
        
        l = len(A) + len(B)
        if l & 1:
            return find(A,B,l//2)
        return (find(A,B,l//2 - 1) + find(A,B,l//2)) / 2
        
        