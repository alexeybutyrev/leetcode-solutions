# Problem: Maximum Score of a Good Subarray
# Language: python3
# Runtime: 1064 ms
# Memory: 27.2 MB

class Solution:
    def maximumScore(self, A: List[int], k: int) -> int:
        
    
        N = len(A)
        i = j = k
        ans = m = A[k]
        while i >= 0 and j < N:

            m = min(A[i], A[j], m)
            ans = max(ans, m * (j - i + 1))
            
            if i == 0 and j == N-1:
                break
                
            if i == 0:
                j +=1
                continue
            
            if j == N-1:
                i -= 1
                continue
            
            if A[j+1] > A[i-1]:
                j += 1
            else:
                i -= 1
                
        return ans