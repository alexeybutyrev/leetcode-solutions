# Problem: Minimum Number of Operations to Make Array Continuous
# Language: python3
# Runtime: 778 ms
# Memory: 38.7 MB

class Solution:
    def minOperations(self, A: List[int]) -> int:
        N = old_count = len(A)
        
        ctr = Counter(A)
        A.sort()
        
        
        A = sorted(set(A))
        j = 0
        ans = N
        for i in range(len(A)):
            new_bound = A[i] + N
            while j < len(A) and A[j] < new_bound:
                j += 1
            
            ans = min(ans, N - (j - i))
            
        return ans
        