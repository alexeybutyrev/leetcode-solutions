# Problem: Search in Rotated Sorted Array
# Language: python3
# Runtime: 0 ms
# Memory: 18 MB

class Solution:
    def search(self, A: List[int], T: int) -> int:
        N = len(A)
        lo = 0
        hi = N-1

        while lo < hi:
            mid = lo + hi >> 1
            if A[mid] >= A[hi]:
                lo = mid + 1
            else:
                hi = mid
                
                
        MID = lo

        
        def search(A,T):
            lo = 0
            hi = len(A)-1
            while lo < hi:
                mid = lo + hi >> 1
                if A[mid] < T:
                    lo = mid + 1
                else:
                    hi = mid
            return lo
        
        x = search(A[0:MID], T)
        if x < MID and A[x] == T:
            return x
        x = search(A[MID:], T)

        if x < len(A[MID:]) and A[MID+x] == T:
            return x + MID 
        return -1


