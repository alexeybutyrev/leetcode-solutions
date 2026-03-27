# Problem: Maximum Score Of Spliced Array
# Language: python3
# Runtime: 1512 ms
# Memory: 32.4 MB

class Solution:
    def maximumsSplicedArray(self, A: List[int], B: List[int]) -> int:
        
        def gca(A,B):
            SA = sum(A)
            
            C = [y - x for x,y in zip(A,B)]
            
            ans = curr = 0
            for a in C:
                curr = max(curr + a, a)
                ans = max(ans, curr)
            
            return SA + ans
        
        return max(gca(A,B),gca(B,A))
        
        
            