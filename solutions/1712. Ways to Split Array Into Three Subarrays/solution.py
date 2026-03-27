# Problem: Ways to Split Array Into Three Subarrays
# Language: python3
# Runtime: 1847 ms
# Memory: 27.1 MB

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        
        A = list(accumulate(nums))
        N = len(A)
        MOD = 10 ** 9 + 7
        
        def search(x,lo):
            return A[lo] <= (A[x] - A[lo]) and 2 * A[x] <= A[lo] + A[-1]
        
        #print(A)
        #return 2
        ans = 0
        j = k = 0
        for i in range(len(A) - 2):
            while j <= i or (j < N -1 and A[j] < A[i] * 2):
                j += 1
            
            while k < j or (k < N -1 and 2 * A[k] <= A[-1] + A[i]):
                k += 1
            
            ans += (k - j)
            ans %= MOD
             
        return ans