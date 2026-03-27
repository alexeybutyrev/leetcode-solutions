# Problem: Number of Subarrays With LCM Equal to K
# Language: python3
# Runtime: 2921 ms
# Memory: 14 MB

class Solution:
    def subarrayLCM(self, A: List[int], k: int) -> int:
        
        
        l = lcm(A[0],1)
        N = len(A)
        ans = 0
        for i in range(N):
            l = A[i]
            for j in range(i,N):
                l = lcm(l, A[j])
                if l == k:
                    ans += 1
        return ans
            