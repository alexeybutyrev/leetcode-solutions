# Problem: Count Negative Numbers in a Sorted Matrix
# Language: python3
# Runtime: 130 ms
# Memory: 15.1 MB

class Solution:
    def countNegatives(self, A: List[List[int]]) -> int:
        M = len(A[0])
        def search(A):
            lo=0
            hi=len(A)
            while lo<hi:
                mid=lo+hi>>1
                if A[mid]>=0:
                    lo = mid +1
                else:
                    hi = mid
            return M -lo
        
        ans=0
        for r in A:
            ans+=search(r)
        return ans