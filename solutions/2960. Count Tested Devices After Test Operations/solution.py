# Problem: Count Tested Devices After Test Operations
# Language: python3
# Runtime: 116 ms
# Memory: 16.2 MB

class Solution:
    def countTestedDevices(self, A: List[int]) -> int:
        ans = 0
        A = [x for x in A if x]
        
        ans = 0
        for i in range(len(A)):
            if A[i]:
                ans += 1
                for j in range(i+1,len(A)):
                    A[j] = max(0, A[j] - 1)
        
        return ans