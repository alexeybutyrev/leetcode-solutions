# Problem: Minimum Average Difference
# Language: python3
# Runtime: 1070 ms
# Memory: 31.5 MB

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        L = list(accumulate(nums))
        R = list(accumulate(nums[::-1]))[::-1]
        N = len(L)
        ind = N - 1
        ans = floor(R[0]/N)
        for i in range(len(L)-1):
            
            l = floor(L[i]/(i+1))
            r = floor(R[i+1]/(N-i-1))
            if ans > abs(l-r) or (ind ==N-1 and ans == abs(l-r)):
                ans = abs(l-r)
                ind = i
                
        return ind