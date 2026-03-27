# Problem: Minimum Swaps to Group All 1's Together
# Language: python3
# Runtime: 923 ms
# Memory: 17.9 MB

class Solution:
    def minSwaps(self, A: List[int]) -> int:
        
        #c = Counter(A)
        
        no = sum(A)
        
        ans = no - sum(A[0:no])
        
        c = sum(A[0:no])
        for i in range(no, len(A)):
            c -= A[i-no]
            c += A[i]
            ans = min(ans, no - c)
        
        
        return ans