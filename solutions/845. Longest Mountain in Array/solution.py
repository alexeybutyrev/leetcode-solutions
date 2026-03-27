# Problem: Longest Mountain in Array
# Language: python3
# Runtime: 160 ms
# Memory: 15.1 MB

class Solution:
    def longestMountain(self, A: List[int]) -> int:
        n = len(A)
        if n == 0 or n == 1:
            return 0
        
        
        max_count = 0
        count_up = 1
        count_down = 0
        up = False
        for j in range(1,n):
            if A[j] > A[j-1]:
                count_up +=1
                count_down = count_up
                up = True
            
            if A[j] == A[j-1]:
                up = False
                count_up = 1
            if A[j] < A[j-1] and up:
                
                count_down += 1
                max_count = max(max_count, count_down)
                count_up = 1
            
                
        return max_count
    