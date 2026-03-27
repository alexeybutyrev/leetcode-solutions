# Problem: Number of Beautiful Pairs
# Language: python3
# Runtime: 281 ms
# Memory: 16.4 MB

class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        A = [(int(str(x)[0]),int(str(x)[-1])) for x in nums]
        N = len(A)
        ans = 0
        for i in range(N):
            for j in range(i+1,N):
                if gcd(A[i][0], A[j][1])==1:
                    ans+=1
        return ans