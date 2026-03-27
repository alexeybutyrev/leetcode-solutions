# Problem: Trapping Rain Water
# Language: python3
# Runtime: 40 ms
# Memory: 14.9 MB

class Solution:
    def trap(self, A: List[int]) -> int:
        # find drop ind
        
        N = len(A)
        
        ml = 0
        mr = 0
        
        sl = 0
        sr = 0
        
        ans = 0
        
        l = 0
        r = N - 1
        while l < r:
            if A[l] <= A[r]:
                # move left to right
                if A[l] < ml:
                    sl += ml - A[l]
                else:
                    ans += sl
                    sl = 0
                    ml = A[l]
                l += 1
            else:
                # move right to left
                if A[r] < mr:
                    sr += mr - A[r]
                else:
                    ans += sr
                    sr = 0
                    mr = A[r]
                r -= 1
                
            
        return ans + sl + sr