# Problem: Construct Product Matrix
# Language: python3
# Runtime: 116 ms
# Memory: 44.6 MB

MOD = 12345
def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    l = [1] * n
    r = [1] * n
    pr = 1
    #1,2,3
    for i in range(1,n):
        l[i] = l[i-1] * nums[i-1]
        l[i] %= MOD

    for i in reversed(range(n)):

        l[i] = l[i] *pr
        l[i] %= MOD
        pr *= nums[i]
        pr %= MOD

    return l
    
class Solution:
    def constructProductMatrix(self, A: List[List[int]]) -> List[List[int]]:
        N,M = len(A), len(A[0])
        
        # flat matrix to list
        B = []
        for a in A:
            for x in a:
                B.append(x)
        
        B = productExceptSelf(B)
        ans = []
        for i in range(N):
            ans.append(B[i*M:(i+1) * M])        
        return ans
        