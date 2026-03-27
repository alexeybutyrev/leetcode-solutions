# Problem: Frequency of the Most Frequent Element
# Language: python3
# Runtime: 1076 ms
# Memory: 28.2 MB

class Solution:
    def maxFrequency(self, A: List[int], k: int) -> int:
        N = len(A)
        
        A.sort()
        
        
        i = 0
        j = 1
        s = 0
        ans = 1
        while i < N and j < N:
            s += (A[j] - A[j-1]) * (j - i)
            if s <= k:
                ans = max(ans, j - i+1)
            else:
                s -= A[j] - A[i] 
                i+=1
            j += 1
        
        return ans