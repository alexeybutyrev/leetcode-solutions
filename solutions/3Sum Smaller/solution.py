# Problem: 3Sum Smaller
# Language: python3
# Runtime: 976 ms
# Memory: 14.3 MB

class Solution:
    def threeSumSmaller(self, A: List[int], target: int) -> int:
        N = len(A)
        A.sort()
        count = 0
        for i in range(2,N):
            j = 0
            k = i - 1
            while j < k:
                if A[i] + A[j] + A[k] < target:
                    count += k - j
                    j += 1
                else:
                    k -= 1
        return count
                    
        