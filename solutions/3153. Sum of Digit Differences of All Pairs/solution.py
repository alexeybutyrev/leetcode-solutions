# Problem: Sum of Digit Differences of All Pairs
# Language: python3
# Runtime: 1166 ms
# Memory: 31 MB

class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        N = len(nums)
        M = len(str(nums[0]))
        C = [Counter() for _ in range(M)]
        
        
        for i,x in enumerate(nums):
            S = str(x)
            for j in range(M):
                C[j][S[j]] += 1
        def count(A):
            if len(A) < 2: return 0
            ans = 0
            for i in range(len(A)):
                for j in range(i+1,len(A)):
                    ans += A[i] * A[j]
            return ans
        ans = 0
        for j in range(M):
            V = list(C[j].values())
            ans += count(V)
        return ans